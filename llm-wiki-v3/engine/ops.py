"""Operations: ingest, query, lint, decay, review."""

from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import config, evals, extract, graph, index, nlp, readers, render, sources, state


def _store() -> state.StateStore:
    return state.StateStore(config.load_schema()).load()


def _register(store: state.StateStore, source: readers.Source) -> None:
    store.sources[source.source_id] = source.record()


def _question_rows(results: list[extract.ExtractionResult]) -> list[dict[str, Any]]:
    """One row per distinct prompt: the same question often appears in several sources."""
    def rank(question: dict[str, Any]) -> tuple[int, int, str]:
        return (
            1 if config.is_private_sensitivity(question.get("privacy", "internal")) else 0,
            1 if "gitdiff" in question["locator"] else 0,
            question["locator"],
        )

    rows: dict[str, dict[str, Any]] = {}
    for result in results:
        for question in result.questions:
            key = " ".join(question["text"].lower().split())
            existing = rows.get(key)
            if existing is None:
                rows[key] = question
            elif rank(question) < rank(existing):
                question.setdefault("also_seen_in", []).extend(
                    [existing["locator"]] + existing.get("also_seen_in", [])
                )
                rows[key] = question
            else:
                existing.setdefault("also_seen_in", []).append(question["locator"])
    return [rows[key] for key in sorted(rows, key=lambda item: (rank(rows[item]), item))]


def _write_extraction(observations: list[dict[str, Any]], results: list[extract.ExtractionResult]) -> None:
    def is_private(row: dict[str, Any]) -> bool:
        return config.is_private_sensitivity(row.get("privacy", "internal"))

    ordered = sorted(observations, key=lambda o: (o["source_id"], o["locator"], o["observation_id"]))
    config.write_jsonl(config.OBS_DIR / "accepted" / "observations.jsonl",
                       [row for row in ordered if not is_private(row)])
    config.write_jsonl(config.PRIVATE_OBS_DIR / "observations.jsonl",
                       [row for row in ordered if is_private(row)])
    rejected = [
        row for result in results for row in result.rejected
    ]
    config.write_jsonl(config.OBS_DIR / "rejected" / "rejected.jsonl",
                       sorted(rejected, key=lambda r: (r["source_id"], r["locator"], r["reason"])))
    config.write_jsonl(config.OBS_DIR / "pending" / "pending.jsonl", [])


@dataclass
class IngestReport:
    sources: int = 0
    changed_sources: list[str] = field(default_factory=list)
    observations: int = 0
    questions: int = 0
    rejected: int = 0
    new_claims: int = 0
    support_updates: int = 0
    contradiction_updates: int = 0
    supersessions: int = 0
    duplicates: int = 0
    pages: int = 0
    rebuilt: bool = False


GENERATED_DIRS = ("state", "transitions", "graph", "wiki", "retrieval", "reports")


def wipe_state(keep_raw: bool = True) -> None:
    """Delete only this build's generated directories, never the repository or raw/."""
    for name in GENERATED_DIRS:
        directory = config.WIKI_ROOT / name
        if directory.parent != config.WIKI_ROOT:
            raise SystemExit(f"refusing to wipe unexpected path: {directory}")
        if directory.exists():
            shutil.rmtree(directory)
    if not keep_raw and config.RAW_DIR.exists():
        shutil.rmtree(config.RAW_DIR)
    for sub in ("accepted", "rejected", "pending", "archived"):
        (config.OBS_DIR / sub).mkdir(parents=True, exist_ok=True)
    for name in ("accepted/observations.jsonl", "rejected/rejected.jsonl", "private/observations.jsonl"):
        path = config.OBS_DIR / name
        if path.exists():
            path.unlink()
    config.ensure_dirs()


def ingest(include_inbox: bool = True, force_rebuild: bool = False, quiet: bool = False) -> IngestReport:
    config.ensure_dirs()
    schema = config.load_schema()
    report = IngestReport()
    store = _store()

    paths = list(sources.discover())
    dropzone: set[Path] = set()
    if include_inbox:
        dropzone = set(sources.discover_dropzone(schema))
        paths.extend(sorted(dropzone))
    inbox_paths = {path for path in paths if config.INBOX_DIR in path.parents}
    source_objects = [
        sources.make_source(
            path, schema,
            raw_dir=config.INBOX_DIR if path in inbox_paths else None,
            dropzone=path in dropzone,
        )
        for path in paths
    ]

    changed = [
        source.rel_path for source in source_objects
        if source.source_id in store.sources
        and store.sources[source.source_id]["hash"] != f"sha256:{source.content_hash}"
    ]
    if changed and not force_rebuild:
        if not quiet:
            print(f"{len(changed)} source(s) changed since the last ingest; rebuilding derived state.")
        rebuilt = rebuild(inner=True)
        rebuilt.changed_sources = changed
        return rebuilt

    observations: list[dict[str, Any]] = []
    results: list[extract.ExtractionResult] = []
    for source in source_objects:
        sources.register_raw(source, config.RAW_DIR)
        _register(store, source)
        segments = readers.read_source(source)
        result = extract.extract_source(source, segments, schema)
        results.append(result)
        observations.extend(result.observations)
        report.sources += 1
        report.observations += len(result.observations)
        report.rejected += len(result.rejected)
        report.questions += len(result.questions)
        if not quiet:
            print(f"  {source.type:12s} {len(result.observations):4d} obs  {len(result.questions):3d} q  {source.rel_path}")

    _write_extraction(observations, results)
    transitions_before = len(store.transitions)
    store.apply_observations(observations, {source.source_id: source for source in source_objects})
    counts: dict[str, int] = {}
    for transition in store.transitions[transitions_before:]:
        counts[transition["operation"]] = counts.get(transition["operation"], 0) + 1
    report.new_claims = counts.get("new_claim", 0)
    report.support_updates = counts.get("support_update", 0)
    report.contradiction_updates = counts.get("contradiction_update", 0)
    report.supersessions = counts.get("supersession", 0)
    report.duplicates = counts.get("evidence_attached", 0)

    store.link_claim_entities()
    questions = _question_rows(results)
    public_questions = [
        question for question in questions
        if not config.is_private_sensitivity(question.get("privacy", "internal"))
    ]
    config.write_jsonl(config.STATE_DIR / "questions.jsonl", public_questions)
    config.write_jsonl(config.PRIVATE_QUESTIONS_PATH, [
        question for question in questions
        if config.is_private_sensitivity(question.get("privacy", "internal"))
    ])
    report.questions = len(questions)

    store.audit.append({
        "audit_id": "aud_" + config.short_hash(f"ingest|{report.sources}|{len(observations)}", 10),
        "timestamp": config.now_iso(),
        "action": "ingest",
        "actor": "engine",
        "details": {
            "sources": report.sources,
            "observations": len(observations),
            "questions": len(questions),
            "claims": len(store.claims),
            "new_claims": report.new_claims,
        },
    })
    store.save()

    index.HybridIndex(schema).build(list(store.claims.values()), store.entities).save()
    graph.export(store)
    rendered = render.render_all(store, questions)
    store.save()
    report.pages = len(rendered.pages)
    return report


def rebuild(inner: bool = False) -> IngestReport:
    wipe_state(keep_raw=True)
    report = ingest(include_inbox=True, force_rebuild=True, quiet=inner)
    report.rebuilt = True
    return report


# ------------------------------------------------------------------- query


def query(text: str, limit: int = 8, as_json: bool = False, include_private: bool = False) -> str:
    schema = config.load_schema()
    store = _store()
    hybrid = index.HybridIndex(schema).build(list(store.claims.values()), store.entities)
    results = hybrid.search(text, limit=limit * 3 if include_private else limit)
    if not include_private:
        results = [
            item for item in results
            if not config.is_private_sensitivity(item["claim"].get("privacy", "internal"))
        ][:limit]
    else:
        results = results[:limit]
        # The same sentence may exist in both tiers; the public claim already answers it.
        public_texts = {
            nlp.normalize_text(item["claim"]["current_text"]).lower()
            for item in results
            if not config.is_private_sensitivity(item["claim"].get("privacy", "internal"))
        }
        results = [
            item for item in results
            if not config.is_private_sensitivity(item["claim"].get("privacy", "internal"))
            or nlp.normalize_text(item["claim"]["current_text"]).lower() not in public_texts
        ]
    if as_json:
        return json.dumps({
            "query": text,
            "results": [
                {
                    "claim_id": item["claim_id"],
                    "score": item["score"],
                    "streams": item["streams"],
                    "probability": item["claim"]["probability"],
                    "status": item["claim"]["status"],
                    "text": item["claim"]["current_text"],
                    "topic": item["claim"]["topic"],
                    "evidence": item["claim"]["evidence"][:2],
                }
                for item in results
            ],
        }, ensure_ascii=False, indent=2)
    if not results:
        return (
            f"# {text}\n\nNo claim in the current state matches this query. "
            "The knowledge base only answers from claims that a source supports.\n"
        )
    lines = [f"# {text}", ""]
    lines.append("Reconstructed from current claim state, not from a nearest chunk.")
    lines.append("")
    lines.append("## Answer")
    lines.append("")
    substantive = [item for item in results if len(nlp.content_tokens(item["claim"]["current_text"])) >= 7]
    comparison = bool(index.COMPARISON_INTENT_RE.search(text))
    procedural_intent = bool(index.PROCEDURAL_INTENT_RE.search(text))
    pool = substantive or results
    preferred = [
        item for item in pool
        if (procedural_intent or not index.PROCEDURE_RE.match(item["claim"]["current_text"]))
        and (comparison or item["claim"].get("block") != "table_row")
    ]
    preferred_ids = {item["claim_id"] for item in preferred}
    answer_items = (preferred + [item for item in pool if item["claim_id"] not in preferred_ids])[:4]
    for index_, item in enumerate(answer_items):
        claim = item["claim"]
        caveat = ""
        if claim["status"] == "disputed":
            caveat = " **Disputed:** evidence pulls both ways."
        elif claim["status"] == "superseded":
            caveat = " **Superseded:** no longer current belief."
        if index_ == 1:
            lines.append("")
            lines.append("Also retrieved:")
            lines.append("")
        if config.is_private_sensitivity(claim.get("privacy", "internal")):
            caveat += " **Teacher-only:** not in the wiki."
        lines.append(
            f"- {claim['current_text']} (confidence {claim['probability']:.2f}, {claim['status']}).{caveat}"
        )
    lines.append("")
    dominant_topic = results[0]["claim"]["topic"]
    topic_spec = next((topic for topic in schema["topics"] if topic["id"] == dominant_topic), None)
    if topic_spec:
        topic_claims = sum(1 for claim in store.claims.values() if claim["topic"] == dominant_topic)
        lines.append(
            f"Topic page: [[{render.topic_slug(dominant_topic)}|{topic_spec['title']}]] "
            f"({topic_claims} claims)."
        )
        lines.append("")
    lines.append("## Evidence")
    lines.append("")
    for item in results[:5]:
        claim = item["claim"]
        for entry in claim["evidence"][:2]:
            lines.append(f"- `{entry['locator']}` — “{render.truncate(entry['span'], 200)}”")
    lines.append("")
    contested = [item for item in results if item["claim"]["contradicting_observations"]]
    if contested:
        lines.append("## Contradictions and Caveats")
        lines.append("")
        for item in contested[:4]:
            claim = item["claim"]
            lines.append(f"- “{render.truncate(claim['current_text'], 120)}” is contested ({claim['probability']:.2f}).")
            for entry in claim["evidence"]:
                if entry["stance"] == "contradicts":
                    lines.append(f"  - against: `{entry['locator']}` — “{render.truncate(entry['span'], 140)}”")
        lines.append("")
    lines.append("## Retrieved Claims")
    lines.append("")
    lines.append("| Claim | Topic | Confidence | Status | Streams |")
    lines.append("|---|---|---|---|---|")
    for item in results:
        claim = item["claim"]
        lines.append(
            f"| `{claim['claim_id']}` | {claim['topic']} | {claim['probability']:.2f} | "
            f"{claim['status']} | {', '.join(item['streams'])} |"
        )
    lines.append("")
    return "\n".join(lines)


# -------------------------------------------------------------------- lint


@dataclass
class LintFinding:
    check: str
    severity: str
    message: str
    ref: str = ""


def lint() -> tuple[list[LintFinding], str]:
    schema = config.load_schema()
    store = _store()
    findings: list[LintFinding] = []
    questions = config.read_jsonl(config.STATE_DIR / "questions.jsonl")

    wiki_files = sorted(p for p in config.WIKI_DIR.rglob("*.md"))
    slugs = {p.stem: p for p in wiki_files}

    for page in wiki_files:
        text = page.read_text(encoding="utf-8")
        for match in re.finditer(r"\[\[([^\]|]+)", text):
            target = match.group(1).strip()
            if target.endswith("index"):
                continue
            candidate = target.split("/")[-1]
            if candidate not in slugs:
                findings.append(LintFinding("broken_link", "error",
                                            f"Link target '{target}' does not exist.", str(page.relative_to(config.WIKI_ROOT))))

    private_claims: list[dict[str, Any]] = []
    for claim in store.claims.values():
        if config.is_private_sensitivity(claim.get("privacy", "internal")):
            private_claims.append(claim)
            for entry in claim["evidence"]:
                path = entry["locator"].split("#")[0].rsplit(":", 1)[0]
                if path and not config.resolve_source_path(path).exists():
                    findings.append(LintFinding("dangling_evidence", "error",
                                                f"Evidence locator points at a missing file: {entry['locator']}",
                                                claim["claim_id"]))
            continue
        if claim["status"] == "superseded":
            continue
        if not claim["supporting_observations"]:
            findings.append(LintFinding("claim_without_evidence", "error",
                                        f"{claim['claim_id']} has no supporting observation.", claim["claim_key"]))
        if not claim.get("source_ids"):
            findings.append(LintFinding("claim_without_source", "error",
                                        f"{claim['claim_id']} has no source.", claim["claim_key"]))
        for entry in claim["evidence"]:
            path = entry["locator"].split("#")[0].rsplit(":", 1)[0]
            if path and not config.resolve_source_path(path).exists() and not path.startswith("inbox/"):
                findings.append(LintFinding("dangling_evidence", "error",
                                            f"Evidence locator points at a missing file: {entry['locator']}",
                                            claim["claim_id"]))
        if claim.get("freshness", 1.0) < 0.3 and claim["status"] in {"active", "candidate"}:
            findings.append(LintFinding("stale_claim", "warning",
                                        f"{claim['claim_id']} is stale (freshness {claim['freshness']:.2f}).",
                                        claim["claim_key"]))
        if claim["topic"] == "unfiled":
            findings.append(LintFinding("unfiled_claim", "warning",
                                        f"{claim['claim_id']} could not be assigned to a topic.",
                                        claim["current_text"][:80]))

    for conflict in store.conflicts:
        if conflict.get("status") == "open":
            findings.append(LintFinding("unresolved_conflict", "warning",
                                        f"{conflict['type']}: {render.truncate(conflict.get('incoming_text', ''), 90)}",
                                        conflict.get("claim_id", "")))

    if private_claims:
        for claim_id in evals.privacy_leaks(store):
            claim = store.claims[claim_id]
            findings.append(LintFinding("privacy_leak", "error",
                                        f"{claim_id} is {claim.get('privacy')} but its text appears in wiki/.",
                                        claim_id))
        public_ids = {
            row["claim_id"] for row in config.read_jsonl(config.STATE_DIR / "claims.jsonl")
        }
        leaked = [claim["claim_id"] for claim in private_claims if claim["claim_id"] in public_ids]
        if leaked:
            findings.append(LintFinding("privacy_split", "error",
                                        f"{len(leaked)} private claim(s) are stored in state/claims.jsonl.",
                                        ", ".join(leaked[:5])))
        public_questions = config.read_jsonl(config.STATE_DIR / "questions.jsonl")
        if any(config.is_private_sensitivity(q.get("privacy", "internal")) for q in public_questions):
            findings.append(LintFinding("privacy_split", "error",
                                        "Private questions are still in the public question file.", "questions.jsonl"))

    seen_entities: dict[str, str] = {}
    for entity in store.entities.values():
        key = entity["name"].lower().replace("-", " ").strip()
        if key in seen_entities:
            findings.append(LintFinding("duplicate_entity", "warning",
                                        f"'{entity['name']}' duplicates '{seen_entities[key]}'.", entity["entity_id"]))
        else:
            seen_entities[key] = entity["entity_id"]

    by_key: dict[str, list[str]] = {}
    for claim in store.claims.values():
        by_key.setdefault(claim["claim_key"], []).append(claim["claim_id"])
    for key, ids in by_key.items():
        if len(ids) > 1:
            findings.append(LintFinding("same_key_multiple_claims", "info",
                                        f"{len(ids)} claims share key '{key}'; check for scope splits.", key))

    manifest_path = config.RETRIEVAL_DIR / "render_manifest.json"
    manifest = config.read_json(manifest_path, {}) or {}
    for relative, digest in manifest.get("pages", {}).items():
        path = config.WIKI_ROOT / relative
        if not path.exists():
            findings.append(LintFinding("missing_page", "error", f"{relative} is in the manifest but missing.", relative))
        elif config.short_hash(path.read_text(encoding="utf-8"), 12) != digest:
            findings.append(LintFinding("outdated_render", "warning",
                                        f"{relative} changed after the last render; re-run render.", relative))

    for question in questions:
        if question.get("kind") == "exam_prompt" and not question.get("topic"):
            findings.append(LintFinding("question_without_topic", "warning",
                                        f"Question from {question['locator']} has no topic.", question["locator"]))

    stats = store.stats()
    lines = ["# Lint report", "", f"Generated {config.now_iso()}", ""]
    lines.append(f"Claims: {stats['claims']} · Sources: {stats['sources']} · Open conflicts: {stats['open_conflicts']}")
    lines.append("")
    lines.append("| Severity | Check | Reference | Message |")
    lines.append("|---|---|---|---|")
    order = {"error": 0, "warning": 1, "info": 2}
    for finding in sorted(findings, key=lambda f: (order.get(f.severity, 3), f.check, f.ref)):
        lines.append(f"| {finding.severity} | {finding.check} | `{finding.ref}` | {finding.message.replace('|', '/')} |")
    lines.append("")
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.severity] = counts.get(finding.severity, 0) + 1
    lines.append(f"Totals: {counts}")
    report_text = "\n".join(lines)
    config.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (config.REPORTS_DIR / "lint_latest.md").write_text(report_text + "\n", encoding="utf-8")
    return findings, report_text


# ------------------------------------------------------------------- decay


def decay() -> int:
    store = _store()
    changed = store.decay_all()
    store.audit.append({
        "audit_id": "aud_" + config.short_hash(f"decay|{config.now_iso()}", 10),
        "timestamp": config.now_iso(),
        "action": "decay",
        "actor": "decay_scheduler",
        "details": {"claims_changed": changed},
    })
    store.save()
    questions = config.read_jsonl(config.STATE_DIR / "questions.jsonl")
    index.HybridIndex(store.schema).build(list(store.claims.values()), store.entities).save()
    graph.export(store)
    render.render_all(store, questions)
    return changed


# ------------------------------------------------------------------ review


def review(action: str, claim_id: str, second: str = "", note: str = "") -> str:
    store = _store()
    claim = store.claims.get(claim_id)
    if claim is None:
        raise SystemExit(f"unknown claim: {claim_id}")
    before = {"probability": claim["probability"], "status": claim["status"]}
    if action == "approve":
        claim["probability"] = max(claim["probability"], 0.9)
        claim["probability_basis"] = claim["probability"]
        claim["status"] = "active"
        claim["needs_review"] = False
    elif action == "reject":
        claim["probability"] = min(claim["probability"], 0.15)
        claim["probability_basis"] = claim["probability"]
        claim["status"] = "archived"
        claim["needs_review"] = False
    elif action == "obsolete":
        claim["status"] = "archived"
        claim["probability"] = min(claim["probability"], 0.2)
        claim["probability_basis"] = claim["probability"]
    elif action == "restore":
        claim["status"] = "active"
        claim["probability"] = max(claim["probability"], 0.7)
        claim["probability_basis"] = claim["probability"]
    elif action == "merge" and second:
        target = store.claims.get(second)
        if target is None:
            raise SystemExit(f"unknown merge target: {second}")
        for observation_id in claim["supporting_observations"]:
            if observation_id not in target["supporting_observations"]:
                target["supporting_observations"].append(observation_id)
        target["evidence"].extend(claim["evidence"])
        target["source_ids"] = sorted(set(target["source_ids"]) | set(claim["source_ids"]))
        target["entities"] = sorted(set(target["entities"]) | set(claim["entities"]))
        claim["status"] = "superseded"
        claim["superseded_by"] = second
        claim["probability"] = 0.0
    elif action == "resolve":
        for conflict in store.conflicts:
            if conflict.get("claim_id") == claim_id and conflict.get("status") == "open":
                conflict["status"] = "resolved"
                conflict["resolved_at"] = config.now_iso()
                conflict["resolution"] = note or "resolved by human review"
    else:
        raise SystemExit(f"unknown action: {action}")
    store.transitions.append({
        "transition_id": "tr_" + config.short_hash(f"human|{action}|{claim_id}|{len(store.transitions)}", 10),
        "timestamp": config.now_iso(),
        "operation": "human_override" if action != "merge" else "human_merge",
        "claim_id": claim_id,
        "observation_id": None,
        "before": before,
        "after": {"probability": claim["probability"], "status": claim["status"]},
        "reason": note or f"human review: {action}",
        "actor": "human",
        "review_required": False,
    })
    store.save()
    questions = config.read_jsonl(config.STATE_DIR / "questions.jsonl")
    index.HybridIndex(store.schema).build(list(store.claims.values()), store.entities).save()
    graph.export(store)
    render.render_all(store, questions)
    return f"{action}: {claim_id} {before['probability']:.2f} → {claim['probability']:.2f} ({claim['status']})"
