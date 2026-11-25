"""Render markdown wiki pages from the current belief state.

Rendering never reads a raw source: every sentence comes from a claim, and every
load-bearing statement keeps its claim id and evidence locator.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Iterable

from . import config, nlp, readers

@dataclass
class RenderReport:
    pages: list[str] = field(default_factory=list)
    claims_rendered: int = 0
    entities_rendered: int = 0
    questions_rendered: int = 0
    skipped_unchanged: int = 0
    private_withheld: int = 0


def topic_slug(topic_id: str) -> str:
    return topic_id.replace(".", "-")


def page_path(schema: dict[str, Any], topic_id: str) -> str:
    topic = next(t for t in schema["topics"] if t["id"] == topic_id)
    return f"wiki/{topic['page_type']}/{topic_slug(topic_id)}.md"


def humanise(text: str) -> str:
    words = text.replace("-", " ").replace("_", " ").replace(".", " ").split()
    if not words:
        return text
    return " ".join(words).capitalize()


def truncate(text: str, limit: int = 190) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0] + "…"


def median(values: Iterable[float]) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def frontmatter(data: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif value is None:
            lines.append(f"{key}: null")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def claim_block(claim: dict[str, Any], sources: dict[str, dict[str, Any]]) -> list[str]:
    text = claim["current_text"].rstrip(".")
    status = claim["status"]
    sources_n = len(claim.get("source_ids", []))
    meta = [
        f"Confidence {claim['probability']:.2f}",
        status,
        f"{sources_n} source{'s' if sources_n != 1 else ''}",
    ]
    if claim.get("conditions"):
        meta.append("when: " + "; ".join(claim["conditions"][:2]))
    if claim.get("needs_review"):
        meta.append("needs review")
    lines = [f"**{text}.**", " · ".join(meta)]
    supports = [entry for entry in claim["evidence"] if entry["stance"] == "supports"]
    if supports:
        best = supports[0]
        span = readers.clean_inline(best["span"])
        lines.append(f"Evidence: `{best['locator']}` — “{truncate(span)}”")
    return lines


def group_by_aspect(claims: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for claim in claims:
        prefix = claim["topic"] + "."
        aspect = claim["claim_key"][len(prefix):] if claim["claim_key"].startswith(prefix) else claim["claim_key"]
        grouped.setdefault(aspect, []).append(claim)
    for items in grouped.values():
        items.sort(key=lambda c: (-c["probability"], c["claim_id"]))
    return dict(sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])))


def render_topic(
    schema: dict[str, Any],
    topic_id: str,
    claims: list[dict[str, Any]],
    questions: list[dict[str, Any]],
    sources: dict[str, dict[str, Any]],
    entities: dict[str, dict[str, Any]],
    transitions: list[dict[str, Any]],
    now: str,
) -> str:
    topic = next(t for t in schema["topics"] if t["id"] == topic_id)
    title = topic["title"]
    claim_ids = [claim["claim_id"] for claim in claims]
    entity_counts: dict[str, int] = {}
    for claim in claims:
        for name in claim.get("entities", []):
            entity_counts["ent_" + nlp.slug(name, max_words=4)] = entity_counts.get(
                "ent_" + nlp.slug(name, max_words=4), 0
            ) + 1
    entity_ids = [entity_id for entity_id, _ in sorted(entity_counts.items(), key=lambda item: (-item[1], item[0]))[:12]]
    source_ids = sorted({source_id for claim in claims for source_id in claim.get("source_ids", [])})
    probabilities = [claim["probability"] for claim in claims]
    confidence = round(median(probabilities), 3)
    status = "disputed" if any(claim["status"] == "disputed" for claim in claims) else "active"
    review_required = any(claim.get("needs_review") for claim in claims)

    body: list[str] = []
    body.append(frontmatter({
        "title": title,
        "type": topic["page_type"],
        "topic": topic_id,
        "entity_ids": entity_ids,
        "claim_ids": claim_ids,
        "confidence": confidence,
        "status": status,
        "last_rendered": now,
        "sources": source_ids,
        "review_required": review_required,
    }))
    body.append("")
    body.append(f"# {title}")
    body.append("")
    active = sum(1 for claim in claims if claim["status"] == "active")
    summary = (
        f"Rendered from {len(claims)} claims and {len(source_ids)} sources. "
        f"Median confidence {confidence:.2f}; {active} active, "
        f"{sum(1 for c in claims if c['status'] == 'disputed')} disputed, "
        f"{sum(1 for c in claims if c['status'] == 'superseded')} superseded."
    )
    body.append(summary)
    body.append("")

    body.append("## Current Understanding")
    body.append("")
    grouped = group_by_aspect([claim for claim in claims if claim["status"] != "superseded"])
    if not grouped:
        body.append("_No current claims on this topic._")
        body.append("")
    for aspect, items in grouped.items():
        body.append(f"### {humanise(aspect)}")
        body.append("")
        for claim in items:
            body.extend(claim_block(claim, sources))
            body.append("")

    contested = [claim for claim in claims if claim["status"] == "disputed" or claim["contradicting_observations"]]
    if contested:
        body.append("## Contested")
        body.append("")
        body.append("These claims received observations that pull in the opposite direction. They are not settled.")
        body.append("")
        for claim in contested:
            body.append(f"- **{claim['current_text'].rstrip('.')}.** Confidence {claim['probability']:.2f}, status {claim['status']}.")
            for entry in claim["evidence"]:
                if entry["stance"] == "contradicts":
                    body.append(f"  - against: `{entry['locator']}` — “{truncate(entry['span'], 150)}”")
        body.append("")

    superseded = [claim for claim in claims if claim["status"] == "superseded"]
    if superseded:
        body.append("## Superseded")
        body.append("")
        body.append("Kept for history. These are no longer current belief.")
        body.append("")
        for claim in superseded:
            replacement = claim.get("superseded_by")
            body.append(
                f"- ~~{claim['current_text'].rstrip('.')}~~ (probability now {claim['probability']:.2f}) "
                f"— replaced by `{replacement}`"
            )
        body.append("")

    body.append("## Sources")
    body.append("")
    body.append("| Source | Type | Authority | Claims | Date |")
    body.append("|---|---|---|---|---|")
    for source_id in source_ids:
        source = sources.get(source_id, {})
        count = sum(1 for claim in claims if source_id in claim.get("source_ids", []))
        path = source.get("path", source_id)
        body.append(
            f"| `{path}` | {source.get('type', '?')} | {source.get('source_authority', 0):.2f} | {count} | "
            f"{(source.get('created_at') or '')[:10]} |"
        )
    body.append("")

    related: dict[str, int] = {}
    for claim in claims:
        for name in claim.get("entities", []):
            entity_id = "ent_" + nlp.slug(name, max_words=4)
            entity = entities.get(entity_id)
            if not entity:
                continue
            for other in entity.get("topics", []):
                if other != topic_id:
                    related[other] = related.get(other, 0) + 1
    related_topics = [item for item in sorted(related.items(), key=lambda item: (-item[1], item[0]))[:6]]
    body.append("## Related Pages")
    body.append("")
    if related_topics:
        for other, weight in related_topics:
            other_topic = next((t for t in schema["topics"] if t["id"] == other), None)
            if other_topic:
                body.append(f"- [[{topic_slug(other)}|{other_topic['title']}]] ({weight} shared entities)")
    else:
        body.append("_No related topic pages yet._")
    body.append("")

    topic_questions = [question for question in questions if question.get("topic") == topic_id]
    body.append("## Open Questions")
    body.append("")
    if topic_questions:
        body.append(f"{len(topic_questions)} prompts from the material are collected in [[questions/{topic_slug(topic_id)}|Questions: {title}]].")
        for question in topic_questions[:3]:
            body.append(f"- {truncate(question['text'], 140)}")
    else:
        body.append("_No open questions recorded for this topic._")
    body.append("")

    recent = [
        transition for transition in transitions
        if transition.get("claim_id") in set(claim_ids)
    ][-8:]
    if recent:
        body.append("## Timeline")
        body.append("")
        for transition in recent:
            before = transition["before"]["probability"]
            after = transition["after"]["probability"]
            change = "" if before is None else f" ({before:.2f} → {after:.2f})"
            body.append(
                f"- {transition['timestamp'][:10]}: {transition['operation']} on `{transition['claim_id']}`{change}"
            )
        body.append("")
    return "\n".join(body).rstrip() + "\n"


def render_entity(
    entity: dict[str, Any],
    claims: list[dict[str, Any]],
    entities: dict[str, dict[str, Any]],
    schema: dict[str, Any],
    now: str,
    linkable: set[str] | None = None,
) -> str:
    name = entity["name"]
    probabilities = [claim["probability"] for claim in claims]
    confidence = round(median(probabilities), 3) if probabilities else entity.get("confidence", 0.5)
    body = [frontmatter({
        "title": name,
        "type": "entity",
        "entity_id": entity["entity_id"],
        "entity_type": entity["type"],
        "claim_ids": [claim["claim_id"] for claim in claims],
        "confidence": confidence,
        "last_rendered": now,
        "sources": sorted({sid for claim in claims for sid in claim.get("source_ids", [])}),
    }), ""]
    body.append(f"# {name}")
    body.append("")
    body.append(f"Type: {entity['type']}. Mentioned in {len(claims)} claims across {len(entity.get('topics', []))} topics.")
    if entity.get("aliases"):
        body.append(f"Aliases: {', '.join(entity['aliases'][:6])}.")
    body.append("")
    body.append("## Claims")
    body.append("")
    for claim in sorted(claims, key=lambda c: (-c["probability"], c["claim_id"])):
        topic = claim["topic"]
        body.append(
            f"- **{claim['current_text'].rstrip('.')}.** "
            f"Confidence {claim['probability']:.2f} · [[{topic_slug(topic)}|{next((t['title'] for t in schema['topics'] if t['id'] == topic), topic)}]]"
        )
    body.append("")
    neighbours: dict[str, int] = {}
    for claim in claims:
        for other in claim.get("entities", []):
            if other == name:
                continue
            other_entity = entities.get("ent_" + nlp.slug(other, max_words=4))
            if other_entity:
                neighbours[other] = neighbours.get(other, 0) + 1
    if neighbours:
        body.append("## Related Entities")
        body.append("")
        for other, weight in sorted(neighbours.items(), key=lambda item: (-item[1], item[0]))[:10]:
            other_id = "ent_" + nlp.slug(other, max_words=4)
            if linkable is None or other_id in linkable:
                body.append(f"- [[{nlp.slug(other, max_words=4)}|{other}]] ({weight})")
            else:
                body.append(f"- {other} ({weight})")
        body.append("")
    return "\n".join(body).rstrip() + "\n"


def render_questions(
    schema: dict[str, Any],
    topic_id: str,
    questions: list[dict[str, Any]],
    now: str,
) -> str:
    topic = next(t for t in schema["topics"] if t["id"] == topic_id)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for question in questions:
        grouped.setdefault(question.get("heading") or "General", []).append(question)
    body = [frontmatter({
        "title": f"Questions: {topic['title']}",
        "type": "questions",
        "topic": topic_id,
        "question_count": len(questions),
        "last_rendered": now,
    }), ""]
    body.append(f"# Questions: {topic['title']}")
    body.append("")
    body.append(
        "Prompts extracted from the material. No answers are stored: the state holds claims, "
        "not solutions, so these stay open until someone writes a claim with evidence."
    )
    body.append("")
    for heading, items in grouped.items():
        body.append(f"## {heading}")
        body.append("")
        for question in items:
            body.append(f"- {question['text']}")
            body.append(f"  - `{question['locator']}` · {question.get('kind', 'open_question')}")
        body.append("")
    return "\n".join(body).rstrip() + "\n"


def render_index(
    schema: dict[str, Any],
    claims: list[dict[str, Any]],
    questions: list[dict[str, Any]],
    sources: dict[str, dict[str, Any]],
    stats: dict[str, Any],
    now: str,
) -> str:
    by_topic: dict[str, list[dict[str, Any]]] = {}
    for claim in claims:
        by_topic.setdefault(claim["topic"], []).append(claim)
    body = [frontmatter({
        "title": "Knowledge Index",
        "type": "index",
        "last_rendered": now,
        "claims": len(claims),
        "sources": len(sources),
    }), ""]
    body.append("# Big Data Processing — Knowledge Index")
    body.append("")
    body.append(
        f"Rendered from {len(sources)} sources into {len(claims)} claims. "
        f"{stats.get('open_conflicts', 0)} open conflicts, {stats.get('needs_review', 0)} claims flagged for review."
    )
    body.append("")
    body.append(
        f"Graph: {stats.get('entities', 0)} entities and {stats.get('relationships', 0)} typed relationships. "
        f"{len(questions)} prompts are collected in the question pages."
    )
    body.append("")
    if stats.get("withheld_private"):
        body.append(
            f"{stats['withheld_private']} claims come from teacher-only sources and are withheld from this wiki. "
            "They stay queryable with `python3 -m engine query --include-private`."
        )
        body.append("")
    body.append("The wiki is a view. The source of truth is `raw/`, `observations/`, `state/` and `transitions/`.")
    body.append("")
    body.append("## Topics")
    body.append("")
    body.append("| Topic | Claims | Active | Disputed | Sources | Median confidence |")
    body.append("|---|---|---|---|---|---|")
    for topic in schema["topics"]:
        topic_claims = by_topic.get(topic["id"], [])
        if not topic_claims:
            continue
        confidence = median([claim["probability"] for claim in topic_claims])
        body.append(
            f"| [[{topic_slug(topic['id'])}|{topic['title']}]] | {len(topic_claims)} | "
            f"{sum(1 for c in topic_claims if c['status'] == 'active')} | "
            f"{sum(1 for c in topic_claims if c['status'] == 'disputed')} | "
            f"{len({sid for c in topic_claims for sid in c['source_ids']})} | {confidence:.2f} |"
        )
    body.append("")

    contested = [claim for claim in claims if claim["status"] == "disputed"][:8]
    if contested:
        body.append("## Contested Claims")
        body.append("")
        for claim in contested:
            body.append(f"- {truncate(claim['current_text'], 150)} — {claim['probability']:.2f} (`{claim['claim_id']}`)")
        body.append("")

    superseded = [claim for claim in claims if claim["status"] == "superseded"][:8]
    if superseded:
        body.append("## Superseded Claims")
        body.append("")
        for claim in superseded:
            body.append(f"- {truncate(claim['current_text'], 150)} → `{claim.get('superseded_by')}`")
        body.append("")

    body.append("## Sources")
    body.append("")
    body.append("| Source | Type | Authority | Claims | Date |")
    body.append("|---|---|---|---|---|")
    source_claim_counts: dict[str, int] = {}
    for claim in claims:
        for source_id in claim.get("source_ids", []):
            source_claim_counts[source_id] = source_claim_counts.get(source_id, 0) + 1
    for source_id, source in sorted(sources.items(), key=lambda item: item[1].get("path", "")):
        body.append(
            f"| `{source.get('path')}` | {source.get('type')} | {source.get('source_authority', 0):.2f} | "
            f"{source_claim_counts.get(source_id, 0)} | {(source.get('created_at') or '')[:10]} |"
        )
    body.append("")
    if questions:
        body.append(f"## Questions")
        body.append("")
        body.append(f"{len(questions)} prompts are collected under [[questions/index|Questions]].")
        body.append("")
    body.append("## Using This System")
    body.append("")
    body.append("```bash")
    body.append("cd llm-wiki-v3")
    body.append("python3 -m engine query \"why is parquet faster than csv\"")
    body.append("python3 -m engine lint")
    body.append("python3 -m engine ingest            # after adding PDFs to raw/inbox/")
    body.append("python3 -m engine rebuild           # full re-derivation from raw sources")
    body.append("```")
    body.append("")
    return "\n".join(body).rstrip() + "\n"


def write_page(relative_path: str, content: str) -> bool:
    """Write only when the body changed, ignoring the last_rendered timestamp."""
    path = config.WIKI_ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        strip = lambda text: re.sub(r"last_rendered: .*\n", "", text)
        if strip(existing) == strip(content):
            return False
    path.write_text(content, encoding="utf-8")
    return True


def render_all(store, questions: list[dict[str, Any]], now: str | None = None) -> RenderReport:
    now = now or config.now_iso()
    report = RenderReport()
    private = sum(1 for claim in store.claims.values()
                  if config.is_private_sensitivity(claim.get("privacy", "internal")))
    report.private_withheld += private
    claims = [
        claim for claim in store.claims.values()
        if not config.is_private_sensitivity(claim.get("privacy", "internal"))
    ]
    questions = [
        question for question in questions
        if not config.is_private_sensitivity(question.get("privacy", "internal"))
    ]
    by_topic: dict[str, list[dict[str, Any]]] = {}
    for claim in claims:
        by_topic.setdefault(claim["topic"], []).append(claim)

    for topic in store.schema["topics"]:
        topic_id = topic["id"]
        topic_claims = by_topic.get(topic_id, [])
        if not topic_claims:
            continue
        relative = page_path(store.schema, topic_id)
        content = render_topic(
            store.schema, topic_id, topic_claims, questions, store.sources,
            store.entities, store.transitions, now,
        )
        if write_page(relative, content):
            report.pages.append(relative)
        else:
            report.skipped_unchanged += 1
        report.claims_rendered += len(topic_claims)

    for topic in store.schema["topics"]:
        topic_id = topic["id"]
        topic_questions = [question for question in questions if question.get("topic") == topic_id]
        if not topic_questions:
            continue
        question_path = f"wiki/questions/{topic_slug(topic_id)}.md"
        if write_page(question_path, render_questions(store.schema, topic_id, topic_questions, now)):
            report.pages.append(question_path)
            report.questions_rendered += len(topic_questions)

    linkable = {
        entity["entity_id"] for entity in store.entities.values()
        if len(entity.get("claim_ids", [])) >= 2
    }
    for entity in store.entities.values():
        entity_claims = [claim for claim in claims if claim["claim_id"] in entity.get("claim_ids", [])]
        if len(entity_claims) < 2:
            continue
        relative = f"wiki/entities/{nlp.slug(entity['name'], max_words=4)}.md"
        if write_page(relative, render_entity(entity, entity_claims, store.entities, store.schema, now, linkable)):
            report.pages.append(relative)
            report.entities_rendered += 1

    if questions:
        question_topics = {question.get("topic") for question in questions}
        lines = [frontmatter({
            "title": "Questions",
            "type": "index",
            "question_count": len(questions),
            "last_rendered": now,
        }), "", "# Questions", "",
            "Every prompt found in the material, grouped by topic. No answers are stored.", ""]
        for topic in store.schema["topics"]:
            if topic["id"] in question_topics:
                count = sum(1 for question in questions if question.get("topic") == topic["id"])
                lines.append(f"- [[{topic_slug(topic['id'])}|{topic['title']}]] — {count} prompts")
        lines.append("")
        if write_page("wiki/questions/index.md", "\n".join(lines)):
            report.pages.append("wiki/questions/index.md")

    public_sources = {
        source_id: record for source_id, record in store.sources.items()
        if not config.is_private_sensitivity(record.get("sensitivity", "internal"))
    }
    stats = dict(store.stats())
    stats["claims"] = len(claims)
    stats["sources"] = len(public_sources)
    stats["withheld_private"] = private
    index_content = render_index(store.schema, claims, questions, public_sources, stats, now)
    if write_page("index.md", index_content):
        report.pages.append("index.md")

    manifest = {
        "generated_at": now,
        "pages": {
            relative: config.short_hash((config.WIKI_ROOT / relative).read_text(encoding="utf-8"), 12)
            for relative in report.pages
            if (config.WIKI_ROOT / relative).exists()
        },
        "claims": len(claims),
        "entities": len(store.entities),
    }
    config.write_json(config.RETRIEVAL_DIR / "render_manifest.json", manifest)
    return report
