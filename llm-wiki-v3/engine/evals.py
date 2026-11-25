"""Evals: retrieval quality, state-update behaviour, rendering faithfulness, governance."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import config, index, render, state
from .readers import Source


@dataclass
class EvalResult:
    retrieval: dict[str, float] = field(default_factory=dict)
    state_cases: list[tuple[str, bool, str]] = field(default_factory=list)
    faithfulness: dict[str, Any] = field(default_factory=dict)
    governance: list[tuple[str, bool, str]] = field(default_factory=list)


def _fixture_source(source_id: str, authority: float = 0.9, created_at: str | None = None) -> Source:
    return Source(
        source_id=source_id,
        rel_path=f"fixtures/{source_id}.md",
        abs_path=Path(f"/nonexistent/{source_id}.md"),
        type="exam",
        authority=authority,
        created_at=created_at or config.now_iso(),
        author="fixture",
        scope="shared",
        sensitivity="internal",
        title=source_id,
        content_hash="0" * 64,
    )


def _observation(key: str, text: str, source_id: str, stance: str = "supports",
                 confidence: float = 0.8, locator: str | None = None, entities: list[str] | None = None) -> dict[str, Any]:
    return {
        "observation_id": "obs_" + config.short_hash(f"{key}|{text}|{source_id}", 10),
        "source_id": source_id,
        "source_path": f"{source_id}.md",
        "source_type": "exam",
        "extracted_at": config.now_iso(),
        "extractor": {"model": "fixture", "prompt_version": "fixture", "version": "1", "quality": 0.9},
        "claim_key": key,
        "claim_text": text,
        "stance": stance,
        "confidence": confidence,
        "evidence_span": text,
        "locator": locator or f"{source_id}.md:1",
        "entities": entities or [],
        "relationships": [],
        "conditions": [],
        "valid_from": None,
        "valid_until": None,
        "privacy": "internal",
        "topic": "kafka.log",
        "topic_score": 3.0,
        "topic_runner_up": None,
        "block": "paragraph",
        "heading": "fixture",
        "labels": [],
    }


def state_cases() -> list[tuple[str, bool, str]]:
    schema = config.load_schema()
    results: list[tuple[str, bool, str]] = []

    # 1. support raises probability
    store = state.StateStore(schema)
    source = _fixture_source("src_a")
    store.apply_observations([_observation("kafka.log.topic", "A topic is split into partitions.", "src_a")], {"src_a": source})
    claim = next(iter(store.claims.values()))
    results.append(("support raises a new claim above the prior", claim["probability"] > 0.5,
                    f"probability={claim['probability']}"))

    # 2. a second independent source raises it further
    before = claim["probability"]
    store.apply_observations([_observation("kafka.log.topic", "A topic is split into partitions.", "src_b")], {"src_b": _fixture_source("src_b")})
    after = next(iter(store.claims.values()))["probability"]
    results.append(("independent support accumulates", after > before, f"{before:.2f} -> {after:.2f}"))

    # 3. same source does not double count
    store.apply_observations([_observation("kafka.log.topic", "A topic is split into partitions.", "src_a", locator="a.md:9")], {"src_a": source})
    same = next(iter(store.claims.values()))["probability"]
    results.append(("same-source evidence does not double count", abs(same - after) < 0.001, f"{after:.2f} -> {same:.2f}"))

    # 4. contradiction lowers probability and opens a conflict
    store.apply_observations([_observation("kafka.log.topic", "A topic is not split into partitions.", "src_c")], {"src_c": _fixture_source("src_c")})
    contradicted = next(iter(store.claims.values()))
    results.append(("contradiction lowers probability", contradicted["probability"] < same,
                    f"{same:.2f} -> {contradicted['probability']:.2f}"))
    results.append(("contradiction opens a conflict", len(store.conflicts) == 1,
                    f"conflicts={len(store.conflicts)}"))
    results.append(("contradicted claim is disputed", contradicted["status"] in {"disputed", "candidate"},
                    f"status={contradicted['status']}"))

    # 5. supersession keeps history and lowers the old claim
    store = state.StateStore(schema)
    store.apply_observations([
        _observation("retrieval.primary_store", "Cosmos DB is the primary retrieval store.", "src_old"),
    ], {"src_old": _fixture_source("src_old")})
    old = next(iter(store.claims.values()))
    store.apply_observations([
        _observation("retrieval.primary_store", "Azure AI Search replaces Cosmos DB as the primary retrieval store.", "src_new", stance="supersedes"),
    ], {"src_new": _fixture_source("src_new")})
    superseded = [claim for claim in store.claims.values() if claim["status"] == "superseded"]
    replacement = [claim for claim in store.claims.values() if claim["status"] != "superseded"]
    results.append(("supersession keeps the old claim", len(superseded) == 1, f"superseded={len(superseded)}"))
    results.append(("supersession links old and new",
                    bool(superseded and superseded[0]["superseded_by"] == replacement[0]["claim_id"]),
                    "superseded_by set"))
    results.append(("superseded claim loses probability",
                    bool(superseded and superseded[0]["probability"] <= schema["thresholds"]["supersede_probability"]),
                    f"p={superseded[0]['probability'] if superseded else 'n/a'}"))

    # 6. decay lowers certainty of an old confirmation
    store = state.StateStore(schema)
    store.apply_observations([_observation("kafka.log.topic", "A topic is split into partitions.", "src_decay_1")],
                             {"src_decay_1": _fixture_source("src_decay_1")})
    store.apply_observations([_observation("kafka.log.topic", "A topic is split into partitions.", "src_decay_2")],
                             {"src_decay_2": _fixture_source("src_decay_2")})
    claim = next(iter(store.claims.values()))
    claim["last_confirmed_at"] = "2024-01-01T00:00:00Z"
    before = claim["probability"]
    store.decay_all()
    results.append(("decay lowers an unconfirmed claim", claim["probability"] < before,
                    f"{before:.2f} -> {claim['probability']:.2f}, freshness {claim.get('freshness')}"))

    # 7. every update leaves a transition
    results.append(("transitions are written", len(store.transitions) >= 1,
                    f"transitions={len(store.transitions)}"))
    return results


def retrieval_eval(store: state.StateStore, schema: dict[str, Any], sample: int = 80) -> dict[str, float]:
    hybrid = index.HybridIndex(schema).build(list(store.claims.values()), store.entities)
    claims = [claim for claim in store.claims.values() if claim["evidence"]]
    claims.sort(key=lambda claim: claim["claim_id"])
    step = max(1, len(claims) // sample)
    selected = claims[::step][:sample]
    hits_at_1 = hits_at_5 = hits_at_10 = 0
    reciprocal = 0.0
    used = 0
    for claim in selected:
        query = claim["evidence"][0]["span"]
        results = hybrid.search(query, limit=10)
        ranked = [item["claim_id"] for item in results]
        used += 1
        if claim["claim_id"] in ranked[:1]:
            hits_at_1 += 1
        if claim["claim_id"] in ranked[:5]:
            hits_at_5 += 1
        if claim["claim_id"] in ranked[:10]:
            hits_at_10 += 1
        if claim["claim_id"] in ranked:
            reciprocal += 1.0 / (ranked.index(claim["claim_id"]) + 1)
    return {
        "queries": used,
        "recall_at_1": round(hits_at_1 / used, 3) if used else 0.0,
        "recall_at_5": round(hits_at_5 / used, 3) if used else 0.0,
        "recall_at_10": round(hits_at_10 / used, 3) if used else 0.0,
        "mrr": round(reciprocal / used, 3) if used else 0.0,
    }


def faithfulness_eval(store: state.StateStore) -> tuple[dict[str, Any], list[tuple[str, bool, str]]]:
    checks: list[tuple[str, bool, str]] = []
    pages = sorted((config.WIKI_DIR).rglob("*.md"))
    missing_text: list[str] = []
    unknown_claim: list[str] = []
    unsupported_evidence = 0
    superseded_as_current = 0
    claims_checked = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if "\nclaim_ids:" not in text:
            continue
        block = text.split("---", 2)[1]
        claim_ids = [
            line.strip().lstrip("- ").strip()
            for line in block.splitlines()
            if line.strip().startswith("- claim_")
        ]
        normalised_page = " ".join(text.split()).lower()
        for claim_id in claim_ids:
            claim = store.claims.get(claim_id)
            if claim is None:
                unknown_claim.append(claim_id)
                continue
            claims_checked += 1
            excerpt = " ".join(claim["current_text"].split()[:12]).lower()
            if excerpt and excerpt not in normalised_page:
                missing_text.append(f"{page.name}:{claim_id}")
            if claim["status"] == "superseded":
                heading_index = normalised_page.find("## superseded")
                text_index = normalised_page.find(excerpt)
                if heading_index == -1 or (text_index != -1 and text_index < heading_index):
                    superseded_as_current += 1
            for entry in claim["evidence"]:
                if entry["observation_id"] not in claim["supporting_observations"] + claim["contradicting_observations"]:
                    unsupported_evidence += 1
    checks.append(("every claim id on a page exists in state", not unknown_claim,
                   f"unknown={len(unknown_claim)} {unknown_claim[:3]}"))
    checks.append(("rendered claims contain their text", not missing_text,
                   f"mismatch={len(missing_text)} {missing_text[:3]}"))
    checks.append(("evidence entries are attached to their claim", unsupported_evidence == 0,
                   f"orphan evidence={unsupported_evidence}"))
    checks.append(("superseded claims are not presented as current", superseded_as_current == 0,
                   f"violations={superseded_as_current}"))
    return {"pages": len(pages), "claims_checked": claims_checked,
            "missing_text": len(missing_text), "unknown_claims": len(unknown_claim),
            "superseded_as_current": superseded_as_current}, checks


def _normalise(text: str) -> str:
    """Letters and digits only: markdown formatting must not mask a match."""
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def privacy_leaks(
    store: state.StateStore, probe_chars: int = 80, wiki_dir: Path | None = None
) -> list[str]:
    """Private claim text that reached wiki/ without already existing in public material.

    A teacher answer that restates a public sentence is not a leak; the same words are
    already on the page from their own public source. Only text unique to the private
    tier counts.
    """
    private = [claim for claim in store.claims.values()
               if config.is_private_sensitivity(claim.get("privacy", "internal"))]
    if not private:
        return []
    public: list[str] = []
    for claim in store.claims.values():
        if config.is_private_sensitivity(claim.get("privacy", "internal")):
            continue
        public.append(_normalise(claim["current_text"]))
        public.extend(_normalise(entry["span"]) for entry in claim.get("evidence", []))
    for question in config.read_jsonl(config.STATE_DIR / "questions.jsonl"):
        public.append(_normalise(question.get("text", "")))
    corpus = " ".join(public)
    pages = " ".join(
        _normalise(page.read_text(encoding="utf-8"))
        for page in (wiki_dir or config.WIKI_DIR).rglob("*.md")
    )
    leaks: list[str] = []
    for claim in private:
        probe = _normalise(claim["current_text"])[:probe_chars]
        if len(probe) < 24 or probe in corpus:
            continue
        if probe in pages:
            leaks.append(claim["claim_id"])
    return leaks


def governance_eval(store: state.StateStore) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    checks.append(("audit log is written", bool(store.audit) or bool(config.read_jsonl(config.TRANS_DIR / "audit_log.jsonl")),
                   f"events={len(store.audit)}"))
    missing_actor = [t for t in store.transitions if not t.get("actor") or not t.get("operation")]
    checks.append(("every transition has an actor and an operation", not missing_actor,
                   f"invalid={len(missing_actor)}"))
    without_source = [c for c in store.claims.values() if not c["source_ids"]]
    checks.append(("every claim has provenance", not without_source, f"claims without source={len(without_source)}"))
    raw_missing = 0
    for record in store.sources.values():
        raw_path = config.WIKI_ROOT / record.get("raw_path", "")
        if not raw_path.exists():
            raw_missing += 1
            continue
        if config.sha256_file(raw_path) != record["hash"].replace("sha256:", ""):
            raw_missing += 1
    checks.append(("raw copies match their recorded hash", raw_missing == 0, f"mismatches={raw_missing}"))
    private_claims = [c for c in store.claims.values()
                      if config.is_private_sensitivity(c.get("privacy", "internal"))]
    leaks = privacy_leaks(store)
    checks.append(("no private-only text appears in a rendered page", not leaks,
                   f"private claims={len(private_claims)} leaks={len(leaks)}"))
    public_ids = {row["claim_id"] for row in config.read_jsonl(config.STATE_DIR / "claims.jsonl")}
    mixed = [claim["claim_id"] for claim in private_claims if claim["claim_id"] in public_ids]
    checks.append(("private claims are stored apart from public claims", not mixed,
                   f"mixed={len(mixed)}"))
    return checks


def run_all(write: bool = False) -> str:
    schema = config.load_schema()
    store = state.StateStore(schema).load()
    if not store.claims:
        return "No state yet. Run `python3 -m engine ingest` first."
    result = EvalResult()
    result.retrieval = retrieval_eval(store, schema)
    result.state_cases = state_cases()
    result.faithfulness, faithfulness_checks = faithfulness_eval(store)
    result.governance = governance_eval(store)

    lines = ["# Eval report", "", f"Generated {config.now_iso()}", ""]
    lines.append("## Retrieval (evidence span -> claim)")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    for key, value in result.retrieval.items():
        lines.append(f"| {key} | {value} |")
    lines.append("")
    lines.append("## State update cases")
    lines.append("")
    lines.append("| Case | Pass | Detail |")
    lines.append("|---|---|---|")
    for name, passed, detail in result.state_cases:
        lines.append(f"| {name} | {'pass' if passed else 'FAIL'} | {detail} |")
    lines.append("")
    lines.append("## Faithfulness")
    lines.append("")
    for name, passed, detail in faithfulness_checks:
        lines.append(f"- {'pass' if passed else 'FAIL'} — {name} ({detail})")
    lines.append("")
    lines.append(f"Pages checked: {result.faithfulness.get('pages')} · claims checked: {result.faithfulness.get('claims_checked')}")
    lines.append("")
    lines.append("## Governance")
    lines.append("")
    for name, passed, detail in result.governance:
        lines.append(f"- {'pass' if passed else 'FAIL'} — {name} ({detail})")
    lines.append("")
    failed = (
        sum(1 for _, passed, _ in result.state_cases if not passed)
        + sum(1 for _, passed, _ in result.governance if not passed)
        + sum(1 for _, passed, _ in faithfulness_checks if not passed)
    )
    lines.append(f"Failures: {failed}")
    report = "\n".join(lines)

    config.EVALS_DIR.mkdir(parents=True, exist_ok=True)
    cases = [
        {
            "case_id": "regression_001",
            "input": "Same claim restated by a second source",
            "expected_transition": "support_update",
            "not_expected": "new_claim",
        },
        {
            "case_id": "regression_002",
            "input": "Negated restatement of an active claim",
            "expected_transition": "contradiction_update",
            "not_expected": "support_update",
        },
        {
            "case_id": "regression_003",
            "input": "Newer exam file renames a station and rewrites its questions",
            "expected_transition": "supersession",
            "not_expected": "contradiction_update",
        },
        {
            "case_id": "regression_004",
            "input": "Same source repeats its own claim",
            "expected_transition": "evidence_attached",
            "not_expected": "support_update",
        },
    ]
    config.write_jsonl(config.EVALS_DIR / "regression_cases.jsonl", cases)
    config.write_json(config.EVALS_DIR / "results.json", {
        "generated_at": config.now_iso(),
        "retrieval": result.retrieval,
        "state_cases": [{"case": name, "pass": passed, "detail": detail} for name, passed, detail in result.state_cases],
        "faithfulness": result.faithfulness,
        "governance": [{"check": name, "pass": passed, "detail": detail} for name, passed, detail in result.governance],
    })
    if write:
        (config.EVALS_DIR / "report.md").write_text(report + "\n", encoding="utf-8")
    return report
