"""LLM extraction boundary: export chunks, validate and apply contract 13.1 output.

The engine never calls a model itself. It ships the prompt, checks the response
against the schema, verifies every evidence span, and then feeds the observations
into the same state updater the deterministic sensor uses.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from . import config, graph, index, nlp, readers, render, state

VALID_STANCES = {"supports", "contradicts", "supersedes", "modifies", "creates_exception", "defines", "new_claim"}
REQUIRED_FIELDS = ("claim_key", "claim_text", "stance", "confidence", "evidence_span")


def _segment_text(source_id: str, sources: dict[str, dict[str, Any]]) -> str:
    record = sources.get(source_id)
    if not record:
        return ""
    path = config.REPO_ROOT / record["path"]
    if not path.exists():
        raw = config.WIKI_ROOT / record.get("raw_path", "")
        path = raw if raw.exists() else path
    if not path.exists():
        return ""
    source = readers.Source(
        source_id=source_id, rel_path=record["path"], abs_path=path, type=record.get("type", "readme"),
        authority=record.get("source_authority", 0.8), created_at=record.get("created_at", ""),
        author=record.get("author", ""), scope="shared", sensitivity=record.get("sensitivity", "internal"),
        title=record.get("title", ""), content_hash=record.get("hash", "").replace("sha256:", ""),
    )
    return "\n".join(segment.raw for segment in readers.read_source(source))


def export_batch(size: int = 6000, limit: int = 0) -> Path:
    store = state.StateStore(config.load_schema()).load()
    out_dir = config.EXPORTS_DIR / "llm"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for source_id, record in sorted(store.sources.items()):
        text = _segment_text(source_id, store.sources)
        if not text.strip():
            continue
        buffer: list[str] = []
        length = 0
        chunk_index = 0
        for paragraph in text.split("\n"):
            if length + len(paragraph) > size and buffer:
                rows.append({
                    "chunk_id": f"{source_id}_c{chunk_index}",
                    "source_id": source_id,
                    "path": record["path"],
                    "text": "\n".join(buffer),
                })
                chunk_index += 1
                buffer, length = [], 0
            buffer.append(paragraph)
            length += len(paragraph) + 1
        if buffer:
            rows.append({
                "chunk_id": f"{source_id}_c{chunk_index}",
                "source_id": source_id,
                "path": record["path"],
                "text": "\n".join(buffer),
            })
    if limit:
        rows = rows[:limit]
    path = out_dir / "chunks.jsonl"
    config.write_jsonl(path, rows)
    prompt = (config.PROMPTS_DIR / "extract_claims_v1.md")
    if prompt.exists():
        (out_dir / "prompt.md").write_text(prompt.read_text(encoding="utf-8"), encoding="utf-8")
    (out_dir / "README.md").write_text(
        "# LLM extraction batch\n\n"
        "1. Give each line of `chunks.jsonl` to a model together with `prompt.md`.\n"
        "2. Write the model's answers to `answers.jsonl`, one JSON object per line:\n"
        '   `{"source_id": "...", "observations": [ ... ]}`\n'
        "3. Run `python3 -m engine llm-apply exports/llm/answers.jsonl`.\n\n"
        "Every observation is validated against `schema.json`; an evidence span that does not occur\n"
        "in the source text is rejected. Accepted observations go through the same belief updater.\n",
        encoding="utf-8",
    )
    return path


def _normalise(text: str) -> str:
    return " ".join(text.split()).lower()


def validate(observation: dict[str, Any], source_text: str) -> list[str]:
    errors = [field for field in REQUIRED_FIELDS if not observation.get(field)]
    if errors:
        return [f"missing field: {', '.join(errors)}"]
    if observation["stance"] not in VALID_STANCES:
        return [f"invalid stance: {observation['stance']}"]
    try:
        confidence = float(observation["confidence"])
    except (TypeError, ValueError):
        return ["confidence is not a number"]
    if not 0.0 <= confidence <= 1.0:
        return ["confidence outside 0..1"]
    span = _normalise(str(observation["evidence_span"]))
    if span and span not in _normalise(source_text):
        return ["evidence span does not occur in the source text"]
    if len(str(observation["claim_text"])) < 15:
        return ["claim text too short"]
    return []


def apply_file(path: str) -> str:
    schema = config.load_schema()
    store = state.StateStore(schema).load()
    answers = config.read_jsonl(Path(path))
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, str]] = []
    sources: dict[str, readers.Source] = {}
    for source_id, record in store.sources.items():
        file_path = config.REPO_ROOT / record["path"]
        sources[source_id] = readers.Source(
            source_id=source_id, rel_path=record["path"], abs_path=file_path,
            type=record.get("type", "readme"), authority=record.get("source_authority", 0.8),
            created_at=record.get("created_at", ""), author=record.get("author", ""),
            scope="shared", sensitivity=record.get("sensitivity", "internal"),
            title=record.get("title", ""), content_hash=record.get("hash", "").replace("sha256:", ""),
        )
    cache: dict[str, str] = {}
    for line in answers:
        source_id = line.get("source_id", "")
        batch = line.get("observations", [line] if "claim_key" in line else [])
        if source_id not in cache:
            cache[source_id] = _segment_text(source_id, store.sources)
        for observation in batch:
            errors = validate(observation, cache[source_id])
            if errors:
                rejected.append({"source_id": source_id, "claim_text": str(observation.get("claim_text"))[:80],
                                 "reason": "; ".join(errors)})
                continue
            text = str(observation["claim_text"]).strip()
            evidence = str(observation["evidence_span"]).strip()
            topic, _, runner_up = nlp.best_topic(
                text, store.sources.get(source_id, {}).get("path", ""), schema
            )
            accepted.append({
                "observation_id": "obs_" + config.short_hash(f"llm|{source_id}|{text}|{evidence}", 10),
                "source_id": source_id,
                "source_path": store.sources.get(source_id, {}).get("path", ""),
                "source_type": store.sources.get(source_id, {}).get("type", "readme"),
                "extracted_at": config.now_iso(),
                "extractor": {
                    "model": observation.get("model", "external-llm"),
                    "prompt_version": observation.get("prompt_version", "extract_claims_v1"),
                    "version": str(observation.get("extractor_version", "external")),
                    "quality": float(observation.get("extraction_quality", 0.9)),
                },
                "claim_key": str(observation["claim_key"]),
                "claim_text": text if text.endswith(".") else text + ".",
                "stance": observation["stance"],
                "confidence": float(observation["confidence"]),
                "evidence_span": evidence,
                "locator": str(observation.get("locator") or store.sources.get(source_id, {}).get("path", "")),
                "entities": [str(item) for item in observation.get("entities", [])][:10],
                "relationships": observation.get("relationships", [])[:4],
                "conditions": [str(item) for item in observation.get("conditions", [])][:3],
                "valid_from": observation.get("valid_from") or (store.sources.get(source_id, {}).get("created_at") or "")[:10],
                "valid_until": observation.get("valid_until"),
                "privacy": observation.get("privacy", "internal"),
                "topic": topic,
                "topic_score": 0.0,
                "topic_runner_up": runner_up,
                "block": "llm",
                "heading": observation.get("heading", ""),
                "labels": ["llm"],
            })
    store.apply_observations(accepted, sources)
    store.link_claim_entities()
    store.audit.append({
        "audit_id": "aud_" + config.short_hash(f"llm-apply|{path}", 10),
        "timestamp": config.now_iso(),
        "action": "llm_apply",
        "actor": "external-llm",
        "details": {"accepted": len(accepted), "rejected": len(rejected), "file": str(path)},
    })
    store.save()
    index.HybridIndex(schema).build(list(store.claims.values()), store.entities).save()
    graph.export(store)
    render.render_all(store, config.read_jsonl(config.STATE_DIR / "questions.jsonl"))
    lines = [f"accepted {len(accepted)} observations, rejected {len(rejected)}"]
    for row in rejected[:10]:
        lines.append(f"  rejected: {row['reason']} — {row['claim_text']}")
    return "\n".join(lines)
