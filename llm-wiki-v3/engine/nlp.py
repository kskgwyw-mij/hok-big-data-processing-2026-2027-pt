"""Deterministic language helpers: tokenising, similarity, entities, relations, topics."""

from __future__ import annotations

import math
import re
from typing import Any, Iterable

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "than", "that", "this", "these", "those",
    "is", "are", "was", "were", "be", "been", "being", "am", "do", "does", "did", "doing",
    "have", "has", "had", "having", "will", "would", "shall", "should", "can", "could", "may",
    "might", "must", "to", "of", "in", "on", "at", "by", "for", "with", "from", "into", "onto",
    "about", "as", "it", "its", "they", "them", "their", "we", "our", "you", "your", "i", "my",
    "he", "she", "his", "her", "not", "no", "so", "such", "also", "very", "more", "most", "much",
    "some", "any", "all", "each", "every", "both", "either", "neither", "there", "here", "where",
    "when", "while", "how", "why", "what", "which", "who", "whom", "whose", "up", "out", "off",
    "over", "under", "again", "once", "only", "own", "same", "other", "another", "just", "now",
    "see", "e", "g", "i", "eg", "ie", "etc", "vs", "per", "via", "s", "t", "don", "doesn",
    "isn", "aren", "wasn", "weren", "won", "wouldn", "couldn", "shouldn", "let", "like", "get",
    "gets", "got", "make", "makes", "made", "use", "using", "used", "one", "two", "three", "first",
    "second", "next", "last", "good", "bad", "new", "old", "well", "still", "even", "because",
    "before", "after", "between", "through", "during", "without", "within", "across", "around",
}

STOPWORDS |= {
    "col", "row", "e", "g", "n", "b", "i", "dtype", "df", "print", "true", "false", "none",
    "session", "block", "part", "station", "min", "minutes", "approx", "e.g", "i.e",
}

SUFFIXES = ("ations", "ation", "ings", "ing", "ies", "ied", "ers", "er", "ed", "es", "s")

ABBREVIATIONS = {
    "e.g", "i.e", "vs", "etc", "approx", "no", "fig", "al", "cf", "resp", "p", "pp", "min",
}

NEGATION_WORDS = {"not", "no", "never", "cannot", "can't", "don't", "doesn't", "isn't", "aren't",
                  "won't", "without", "none", "neither", "nor", "impossible", "forbidden"}

SUPERSESSION_CUES = (
    "replaces", "replaced by", "has been replaced", "supersedes", "superseded",
    "no longer", "deprecated and removed", "as of version", "now uses", "switched from",
    "renamed to", "moved from", "retired",
)

EXCEPTION_CUES = ("however", "except", "but ", "although", "unless", "only if", "special case",
                  "exception", "additionally", "on the other hand")

COMPARISON_CUES = ("vs", "versus", "compared to", "compared with", "faster than", "slower than",
                   "better than", "instead of", "difference between")

NORMATIVE_CUES = ("must", "never", "always", "required", "requires", "only", "cannot", "do not",
                  "don't", "avoid", "ensure", "should", "need to", "has to")

DEFINITION_CUES = (" is a ", " is an ", " is the ", " means ", " refers to ", " is defined as ",
                   " are ", " describes ")

HEDGE_CUES = ("may", "might", "perhaps", "probably", "usually", "typically", "often", "can be",
              "sometimes", "roughly", "approximately")

WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß][A-Za-z0-9ÄÖÜäöüß_.:+/-]*|\d+(?:[.,]\d+)?")
SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ(0-9\"'])")
QUANTITY_RE = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(%|GB|MB|KB|TB|PB|ms|s|seconds|minutes|hours|days|partitions|columns|rows|million|billion|points?|P\b)",
    re.IGNORECASE,
)


def stem(token: str) -> str:
    if len(token) <= 4:
        return token
    for suffix in SUFFIXES:
        if token.endswith(suffix) and len(token) - len(suffix) >= 3:
            return token[: -len(suffix)]
    return token


def tokens(text: str) -> list[str]:
    return [match.group(0).lower() for match in WORD_RE.finditer(text)]


def content_tokens(text: str) -> set[str]:
    out = set()
    for token in tokens(text):
        base = token.strip("._-:/+")
        if not base or base in STOPWORDS:
            continue
        if len(base) < 3 and not base.isdigit():
            continue
        out.add(stem(base))
    return out


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def containment(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def similarity(a_text: str, b_text: str) -> float:
    a, b = content_tokens(a_text), content_tokens(b_text)
    return max(jaccard(a, b), 0.85 * containment(a, b))


def split_sentences(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    parts = SENTENCE_BOUNDARY_RE.split(text)
    merged: list[str] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if merged:
            previous = merged[-1]
            tail = previous.rstrip(".!?").split(" ")[-1].lower().strip("()[]")
            if tail in ABBREVIATIONS or re.fullmatch(r"[a-z]\d+(?:\.\d+)*", tail) or previous.endswith(("e.g.", "i.e.")):
                merged[-1] = f"{previous} {part}"
                continue
        merged.append(part)
    return [m for m in merged if m.strip()]


def slug(text: str, max_words: int = 5) -> str:
    words = [
        word for word in tokens(text)
        if word not in STOPWORDS and not re.fullmatch(r"[\d.,:_-]+", word)
    ]
    cleaned = []
    for word in words[:max_words]:
        word = re.sub(r"[^a-z0-9_]+", "_", word).strip("_")
        if word and word not in cleaned:
            cleaned.append(word)
    return "_".join(cleaned) or "general"


def quantities(text: str) -> list[tuple[float, str]]:
    found = []
    for match in QUANTITY_RE.finditer(text):
        value = float(match.group(1).replace(",", "."))
        unit = match.group(2).lower().rstrip(".")
        found.append((value, unit))
    return found


def has_cue(text: str, cues: Iterable[str]) -> bool:
    lowered = f" {text.lower()} "
    return any(cue in lowered for cue in cues)


def negation_count(text: str) -> int:
    return sum(1 for token in tokens(text) if token in NEGATION_WORDS)


def is_question(text: str) -> bool:
    return text.strip().endswith("?")


TERM_BLOCKLIST = {
    "name", "explain", "compare", "answer", "write", "points", "sort", "define", "describe",
    "give", "argue", "look", "read", "open", "run", "start", "stop", "note", "hint", "tip",
    "warning", "goal", "goals", "step", "steps", "part", "station", "session", "block", "task",
    "lab", "chapter", "section", "table", "figure", "example", "exercise", "homework", "total",
    "the", "this", "these", "here", "there", "each", "every", "if", "why", "what", "which",
    "how", "when", "where", "who", "your", "you", "we", "our", "it", "no", "yes", "and", "or",
    "but", "for", "with", "from", "into", "that", "then", "than", "also", "only", "all", "none",
}


def title_case_terms(text: str) -> list[str]:
    terms = []
    for match in re.finditer(r"\b([A-ZÄÖÜ][A-Za-zÄÖÜäöüß0-9]*(?:\s+[A-ZÄÖÜ][A-Za-zÄÖÜäöüß0-9]*){0,3})\b", text):
        term = match.group(1)
        if len(term) < 3 or term.lower() in STOPWORDS or term.lower() in TERM_BLOCKLIST:
            continue
        if match.start() == 0:
            continue
        terms.append(term)
    return terms


def build_gazetteer(schema: dict[str, Any]) -> list[tuple[str, str, str]]:
    """(alias_lower, canonical_name, type) sorted longest alias first."""
    entries: list[tuple[str, str, str]] = []
    for name, spec in schema["entities"].items():
        entries.append((name.lower(), name, spec["type"]))
        for alias in spec.get("aliases", []):
            entries.append((alias.lower(), name, spec["type"]))
    entries.sort(key=lambda item: len(item[0]), reverse=True)
    return entries


def extract_entities(text: str, gazetteer: list[tuple[str, str, str]], limit: int = 8) -> list[str]:
    lowered = text.lower()
    consumed: list[tuple[int, int]] = []
    found: list[str] = []
    for alias, canonical, _ in gazetteer:
        if len(alias) < 2:
            continue
        for match in re.finditer(re.escape(alias), lowered):
            span = (match.start(), match.end())
            if any(span[0] < end and start < span[1] for start, end in consumed):
                continue
            if span[0] > 0 and lowered[span[0] - 1].isalnum() and alias[0].isalnum():
                continue
            if span[1] < len(lowered) and lowered[span[1]].isalnum() and alias[-1].isalnum():
                continue
            consumed.append(span)
            if canonical not in found:
                found.append(canonical)
            break
    if len(found) < limit:
        for term in title_case_terms(text):
            words = term.split()
            if len(words) < 2 and not (term.isupper() and len(term) >= 2) and not re.search(r"\d", term):
                continue
            if term not in found and len(term) > 3:
                found.append(term)
    return found[:limit]


RELATION_PATTERNS = [
    (re.compile(r"\b(is|are)\b[^.;]{0,30}\b(a|an|the)\b", re.IGNORECASE), "is_a"),
    (re.compile(r"\b(uses?|using|relies on|depends on|based on)\b", re.IGNORECASE), "uses"),
    (re.compile(r"\b(requires?|needs?|needs to|must have)\b", re.IGNORECASE), "requires"),
    (re.compile(r"\b(produces?|generates?|creates?|writes?)\b", re.IGNORECASE), "produces"),
    (re.compile(r"\b(has|have|contains?|includes?|consists of)\b", re.IGNORECASE), "has"),
    (re.compile(r"\b(replaces?|instead of|no longer uses|supersedes?)\b", re.IGNORECASE), "replaces"),
    (re.compile(r"\b(vs\.?|versus|compared to|compared with)\b", re.IGNORECASE), "compares_with"),
    (re.compile(r"\bfaster than\b", re.IGNORECASE), "faster_than"),
    (re.compile(r"\bruns? on\b", re.IGNORECASE), "runs_on"),
]


def extract_relations(
    text: str, entities: list[str], known: set[str] | None = None, limit: int = 4
) -> list[dict[str, str]]:
    """Mention-pair patterns: the words between two entities decide the predicate.

    Only gazetteer entities become graph edges; free-text capitalised terms would
    otherwise produce confident nonsense in the graph.
    """
    if known is not None:
        entities = [entity for entity in entities if entity in known]
    if len(entities) < 2:
        return []
    positions: list[tuple[int, int, str]] = []
    lowered = text.lower()
    for entity in entities:
        index = lowered.find(entity.lower())
        if index >= 0:
            positions.append((index, index + len(entity), entity))
    positions.sort()
    relations: list[dict[str, str]] = []
    for (_, first_end, first), (second_start, _, second) in zip(positions, positions[1:]):
        if second_start < first_end or first == second:
            continue
        between = text[first_end:second_start].strip()
        if len(between) > 60:
            continue
        for pattern, predicate in RELATION_PATTERNS:
            if pattern.search(f" {between} "):
                relations.append({
                    "subject": first,
                    "predicate": predicate,
                    "object": second,
                    "qualifier": between.strip(" ,;:"),
                })
                break
        if len(relations) >= limit:
            break
    return relations


def score_topics(text: str, rel_path: str, schema: dict[str, Any]) -> list[tuple[str, float]]:
    lowered = f" {text.lower()} "
    scores: list[tuple[str, float]] = []
    for topic in schema["topics"]:
        score = 0.0
        for phrase, weight in topic.get("keywords", {}).items():
            # Slide decks pluralise freely ("Brokers", "Batches"); accept the inflected form.
            pattern = r"(?<![a-z0-9])" + re.escape(phrase.lower()) + r"(?:e?s|'s)?(?![a-z0-9])"
            if re.search(pattern, lowered):
                score += float(weight)
        for hint in topic.get("path_hints", []):
            if rel_path == hint or rel_path.endswith("/" + hint) or rel_path.startswith(hint):
                score += 1.5
                break
        if score > 0:
            scores.append((topic["id"], score))
    scores.sort(key=lambda item: (-item[1], item[0]))
    return scores


def best_topic(text: str, rel_path: str, schema: dict[str, Any], minimum: float = 2.0) -> tuple[str, float, str | None]:
    scores = score_topics(text, rel_path, schema)
    if scores and scores[0][1] >= minimum:
        runner_up = scores[1][0] if len(scores) > 1 else None
        return scores[0][0], scores[0][1], runner_up
    for topic in schema["topics"]:
        for hint in topic.get("path_hints", []):
            if rel_path == hint or rel_path.endswith("/" + hint) or rel_path.startswith(hint):
                return topic["id"], 0.0, None
    return "unfiled", 0.0, None


def logit(probability: float) -> float:
    probability = min(max(probability, 1e-4), 1 - 1e-4)
    return math.log(probability / (1 - probability))


def sigmoid(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1 / (1 + z)
    z = math.exp(value)
    return z / (1 + z)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sentence_case(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    return text[0].upper() + text[1:]
