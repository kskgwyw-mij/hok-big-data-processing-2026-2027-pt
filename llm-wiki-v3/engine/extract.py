"""The semantic sensor: segments become structured observations, never summaries."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from . import config, nlp
from .readers import Segment, Source

BOILERPLATE = {
    "skip to content", "sign in", "sign up", "download zip", "raw", "clone this repository",
    "save to your computer and use it in github desktop", "learn more about clone urls",
    "you must be signed in to star a gist", "select an option", "no results found",
}

GENERIC_HEADINGS = {
    "introduction", "overview", "summary", "setup", "before the session", "goal", "goals",
    "troubleshooting", "files in this folder", "what you already know", "why this matters",
    "next steps", "questions", "exam style questions", "how it works", "rules",
}

PROMPT_HEADING_RE = re.compile(r"^\s*(?:station\s+\d+|part\s+[a-e])\b", re.IGNORECASE)
EXAM_STYLE_RE = re.compile(r"exam[- ]style|exam questions", re.IGNORECASE)
NUMBERING_PREFIX_RE = re.compile(
    r"^(?:station|part|chapter|step|block|lab)\s+[0-9a-z]+\s*[–\-—:]\s*", re.IGNORECASE
)

CONDITION_RE = re.compile(
    r"\b(if|when|unless|while|before|after|for (?:each|all|every|[a-z]+))\b([^.;,]{4,70})",
    re.IGNORECASE,
)

CODE_FRAGMENT_RE = re.compile(r"[\[\]{}]|print\(|\bdef \w+\(|=\s*[\"'\[]|\bimport\s+\w+|\w+\.\w+\(")

ANAPHORIC_OPENERS = (
    "that is why", "that is what", "that's why", "this is why", "this means", "that means",
    "these are", "those are", "they are", "it is", "there is", "there are", "such ",
    "which is", "therefore", "hence", "as a result", "in this case", "for example",
    "so why", "but this", "and this", "and the", "but the",
)

MAX_CODE_CLAIM_CHARS = 220

QUALITY_BY_BLOCK = {
    "paragraph": 0.92, "bullet": 0.90, "table_row": 0.94, "code_comment": 0.84,
    "docstring": 0.86, "code": 0.78, "config": 0.90, "notice": 0.40,
}


@dataclass
class ExtractionResult:
    observations: list[dict[str, Any]] = field(default_factory=list)
    questions: list[dict[str, Any]] = field(default_factory=list)
    rejected: list[dict[str, Any]] = field(default_factory=list)


def heading_aspect(heading_path: tuple[str, ...]) -> str | None:
    for heading in reversed(heading_path):
        cleaned = nlp.normalize_text(heading)
        if not cleaned:
            continue
        if cleaned.lower() in GENERIC_HEADINGS:
            continue
        cleaned = NUMBERING_PREFIX_RE.sub("", cleaned)
        aspect = nlp.slug(cleaned, max_words=5)
        if aspect and aspect != "general":
            return aspect
    return None


def is_prompt_block(segment: Segment, source: Source) -> bool:
    headings = list(segment.heading_path)
    if any(EXAM_STYLE_RE.search(heading) for heading in headings):
        return segment.block in {"paragraph", "bullet"}
    if source.type == "exam" and any(PROMPT_HEADING_RE.match(heading) for heading in headings):
        return True
    return False


def derive_aspect(segment: Segment, claim_text: str, entities: list[str]) -> str:
    heading = heading_aspect(segment.heading_path)
    if heading:
        return heading
    if entities:
        return nlp.slug(f"{entities[0]} {claim_text}", max_words=4)
    return nlp.slug(claim_text, max_words=4)


def extract_conditions(text: str) -> list[str]:
    conditions = []
    for match in CONDITION_RE.finditer(text):
        phrase = f"{match.group(1)} {match.group(2)}".strip()
        phrase = re.sub(r"\s+", " ", phrase).strip(" ,;:")
        if 4 <= len(phrase) <= 80 and phrase not in conditions:
            conditions.append(phrase)
    return conditions[:3]


def classify_stance(text: str) -> str:
    lowered = f" {text.lower()} "
    if nlp.has_cue(lowered, nlp.SUPERSESSION_CUES):
        return "supersedes"
    if nlp.has_cue(lowered, nlp.EXCEPTION_CUES) and re.search(r"\bif\b|\bfor\b", lowered):
        return "creates_exception"
    if nlp.has_cue(f" {lowered} ", nlp.DEFINITION_CUES):
        return "defines"
    return "supports"


def confidence_for(text: str, block: str, source: Source, topic: str) -> float:
    lowered = f" {text.lower()} "
    score = 0.62
    if nlp.has_cue(lowered, nlp.NORMATIVE_CUES):
        score += 0.07
    if nlp.has_cue(lowered, nlp.DEFINITION_CUES):
        score += 0.06
    if nlp.has_cue(lowered, nlp.COMPARISON_CUES):
        score += 0.04
    if nlp.QUANTITY_RE.search(text):
        score += 0.04
    if block == "table_row":
        score += 0.05
    if block == "code":
        score -= 0.05
    if nlp.has_cue(lowered, nlp.HEDGE_CUES):
        score -= 0.06
    if len(nlp.content_tokens(text)) < 6:
        score -= 0.05
    if source.type == "session_stub":
        score -= 0.15
    if topic == "unfiled":
        score -= 0.05
    return round(nlp.clamp(score, 0.30, 0.95), 3)


def claim_text_for(segment: Segment) -> str:
    if segment.block == "table_row":
        pairs = [pair.strip().rstrip(".") for pair in segment.text.split(";") if pair.strip()]
        if len(pairs) == 1:
            text = f"In the comparison table, {pairs[0]}"
        else:
            head, *rest = pairs
            text = f"{head} — " + "; ".join(rest)
    else:
        text = segment.text.rstrip(" .,;:")
    text = re.sub(r"\s+", " ", nlp.sentence_case(text)).strip()
    return re.sub(r"\.{2,}$", ".", text + ".") if not text.endswith(".") else re.sub(r"\.{2,}$", ".", text)


def candidate_units(segment: Segment) -> list[str]:
    if segment.block in {"table_row", "config", "code", "notice"}:
        return [segment.text]
    if segment.block in {"bullet", "code_comment"} and len(segment.text) < 240:
        return [segment.text]
    sentences = nlp.split_sentences(segment.text)
    return sentences or [segment.text]


def is_boilerplate(text: str) -> bool:
    lowered = text.lower().strip(" .")
    if lowered in BOILERPLATE:
        return True
    if re.fullmatch(r"[\W_]+", text):
        return True
    if re.search(r"https?://\S+$", text) and len(nlp.tokens(text)) < 6:
        return True
    return False


def observation_id(source_id: str, claim_key: str, evidence: str) -> str:
    return "obs_" + config.short_hash(f"{source_id}|{claim_key}|{evidence}", 10)


def extract_source(
    source: Source,
    segments: list[Segment],
    schema: dict[str, Any],
    extracted_at: str | None = None,
) -> ExtractionResult:
    result = ExtractionResult()
    gazetteer = nlp.build_gazetteer(schema)
    known_entities = set(schema["entities"])
    thresholds = schema["thresholds"]
    seen_texts: set[str] = set()
    extracted_at = extracted_at or config.now_iso()
    extractor = schema["extractor"]

    for segment in segments:
        if segment.block == "notice" or "unreadable_pdf" in segment.labels:
            result.rejected.append({
                "source_id": source.source_id, "locator": segment.locator,
                "text": segment.text, "reason": "unreadable_source",
            })
            continue
        if is_prompt_block(segment, source):
            if segment.block == "code":
                result.rejected.append({
                    "source_id": source.source_id, "locator": segment.locator,
                    "text": segment.text[:160], "reason": "exam_code_sample",
                })
                continue
            text = nlp.normalize_text(segment.text)
            if len(text) >= 15:
                topic, _, _ = nlp.best_topic(text, source.rel_path, schema)
                result.questions.append({
                    "text": text,
                    "source_id": source.source_id,
                    "locator": segment.locator,
                    "topic": topic,
                    "kind": "exam_prompt",
                    "heading": " / ".join(segment.heading_path),
                })
            continue
        for unit in candidate_units(segment):
            text = nlp.normalize_text(unit)
            if len(text) < 20 or is_boilerplate(text):
                result.rejected.append({
                    "source_id": source.source_id, "locator": segment.locator,
                    "text": text[:160], "reason": "too_short_or_boilerplate",
                })
                continue
            if len(nlp.content_tokens(text)) < thresholds["min_tokens"]:
                result.rejected.append({
                    "source_id": source.source_id, "locator": segment.locator,
                    "text": text[:160], "reason": "too_few_content_tokens",
                })
                continue
            if segment.block == "code_comment" and (
                CODE_FRAGMENT_RE.search(text) or len(nlp.content_tokens(text)) < 7
            ):
                result.rejected.append({
                    "source_id": source.source_id, "locator": segment.locator,
                    "text": text[:160], "reason": "code_fragment",
                })
                continue
            if segment.block == "code" and len(text) > MAX_CODE_CLAIM_CHARS:
                result.rejected.append({
                    "source_id": source.source_id, "locator": segment.locator,
                    "text": text[:160], "reason": "code_block_too_long",
                })
                continue
            lowered_text = text.lower()
            if text.startswith("(") or lowered_text.startswith(ANAPHORIC_OPENERS) or text.endswith(":"):
                result.rejected.append({
                    "source_id": source.source_id, "locator": segment.locator,
                    "text": text[:160], "reason": "fragment_or_lead_in",
                })
                continue
            topic, topic_score, runner_up = nlp.best_topic(text, source.rel_path, schema)
            if nlp.is_question(text):
                result.questions.append({
                    "text": text,
                    "source_id": source.source_id,
                    "locator": segment.locator,
                    "topic": topic,
                    "kind": "exam_prompt" if topic == "course.exam" else "open_question",
                    "heading": " / ".join(segment.heading_path),
                })
                continue
            claim_text = claim_text_for(Segment(
                segment.rel_path, segment.locator, segment.block, segment.heading_path,
                text, segment.raw, segment.header, segment.cells, segment.labels,
            ))
            normalized = nlp.normalize_text(claim_text).lower()
            if normalized in seen_texts:
                continue
            seen_texts.add(normalized)
            entities = nlp.extract_entities(claim_text, gazetteer)
            aspect = derive_aspect(segment, claim_text, entities)
            claim_key = f"{topic}.{aspect}"
            span = nlp.normalize_text(segment.raw or unit)
            if len(span) > thresholds["max_evidence_span_chars"]:
                span = span[: thresholds["max_evidence_span_chars"]].rsplit(" ", 1)[0] + " …"
            result.observations.append({
                "observation_id": observation_id(source.source_id, claim_key, span),
                "source_id": source.source_id,
                "source_path": source.rel_path,
                "source_type": source.type,
                "extracted_at": extracted_at,
                "extractor": {
                    "model": extractor["model"],
                    "prompt_version": extractor["prompt_version"],
                    "version": extractor["version"],
                    "quality": QUALITY_BY_BLOCK.get(segment.block, 0.8),
                },
                "claim_key": claim_key,
                "claim_text": claim_text,
                "stance": classify_stance(claim_text),
                "confidence": confidence_for(claim_text, segment.block, source, topic),
                "evidence_span": span,
                "locator": segment.locator,
                "entities": entities,
                "relationships": nlp.extract_relations(claim_text, entities, known_entities),
                "conditions": extract_conditions(claim_text),
                "valid_from": source.created_at[:10] if source.created_at else None,
                "valid_until": None,
                "privacy": source.sensitivity,
                "topic": topic,
                "topic_score": round(topic_score, 2),
                "topic_runner_up": runner_up,
                "block": segment.block,
                "heading": " / ".join(segment.heading_path),
                "labels": list(segment.labels),
            })
    return result
