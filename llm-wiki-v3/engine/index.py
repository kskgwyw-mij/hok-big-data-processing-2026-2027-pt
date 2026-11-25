"""Hybrid retrieval: BM25, hashed TF-IDF vectors, graph expansion, state filters, RRF."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from typing import Any

from . import config, nlp

VECTOR_BUCKETS = 2048


def _doc_tokens(text: str) -> list[str]:
    return [nlp.stem(token.strip("._-:/+")) for token in nlp.tokens(text) if token not in nlp.STOPWORDS]


def _hashed_vector(tokens: list[str]) -> dict[int, float]:
    counts: dict[int, float] = {}
    for token in tokens:
        bucket = int(config.short_hash("w:" + token, 8), 16) % VECTOR_BUCKETS
        counts[bucket] = counts.get(bucket, 0.0) + 1.0
        if len(token) >= 5:
            for index in range(len(token) - 2):
                trigram = token[index:index + 3]
                bucket = int(config.short_hash("c:" + trigram, 8), 16) % VECTOR_BUCKETS
                counts[bucket] = counts.get(bucket, 0.0) + 0.35
    return counts


def _normalise(vector: dict[int, float]) -> dict[int, float]:
    norm = math.sqrt(sum(value * value for value in vector.values())) or 1.0
    return {key: value / norm for key, value in vector.items()}


def _cosine(a: dict[int, float], b: dict[int, float]) -> float:
    if len(a) > len(b):
        a, b = b, a
    return sum(value * b.get(key, 0.0) for key, value in a.items())


PROCEDURE_RE = re.compile(
    r"^(your turn|lab:|task|todo|try |run |open |read |write |answer |predict |check |click |"
    r"install |start |stop |create |now |next |peek |measure |compare |go to|switch )",
    re.IGNORECASE,
)
PROCEDURAL_INTENT_RE = re.compile(
    r"\b(how|run|start|install|set ?up|create|delete|stop|clean|execute|command)\b", re.IGNORECASE
)
COMPARISON_INTENT_RE = re.compile(r"\b(vs|versus|compare|comparison|difference|better|worse)\b", re.IGNORECASE)


@dataclass
class HybridIndex:
    schema: dict[str, Any]
    claims: list[dict[str, Any]] = field(default_factory=list)
    docs: dict[str, dict[str, Any]] = field(default_factory=dict)
    df: dict[str, int] = field(default_factory=dict)
    idf: dict[str, float] = field(default_factory=dict)
    lengths: dict[str, int] = field(default_factory=dict)
    avg_length: float = 1.0
    vectors: dict[str, dict[int, float]] = field(default_factory=dict)
    entity_claims: dict[str, list[str]] = field(default_factory=dict)
    entity_names: dict[str, str] = field(default_factory=dict)
    topic_claims: dict[str, list[str]] = field(default_factory=dict)

    def build(self, claims: list[dict[str, Any]], entities: dict[str, dict[str, Any]]) -> "HybridIndex":
        self.claims = claims
        self.docs = {}
        self.df = {}
        self.lengths = {}
        self.vectors = {}
        self.entity_claims = {}
        self.entity_names = {}
        self.topic_claims = {}
        for claim in claims:
            text = " ".join([
                claim["current_text"],
                " ".join(claim.get("entities", [])),
                " ".join(claim.get("conditions", [])),
                claim["claim_key"].replace(".", " ").replace("_", " "),
            ])
            tokens = _doc_tokens(text)
            self.docs[claim["claim_id"]] = {"tokens": tokens, "text": text}
            self.lengths[claim["claim_id"]] = len(tokens)
            self.vectors[claim["claim_id"]] = _normalise(_hashed_vector(tokens))
            self.topic_claims.setdefault(claim["topic"], []).append(claim["claim_id"])
            for token in set(tokens):
                self.df[token] = self.df.get(token, 0) + 1
        total = len(claims) or 1
        self.idf = {token: math.log(1 + (total - freq + 0.5) / (freq + 0.5)) for token, freq in self.df.items()}
        self.avg_length = (sum(self.lengths.values()) / total) if claims else 1.0
        for entity in entities.values():
            self.entity_claims[entity["entity_id"]] = list(entity.get("claim_ids", []))
            self.entity_names[entity["entity_id"]] = entity["name"]
        return self

    # ------------------------------------------------------------------ streams

    def bm25(self, query: str, limit: int = 50) -> list[tuple[str, float]]:
        tokens = _doc_tokens(query)
        if not tokens:
            return []
        k1 = float(self.schema["thresholds"]["bm25_k1"])
        b = float(self.schema["thresholds"]["bm25_b"])
        scores: list[tuple[str, float]] = []
        for claim_id, doc in self.docs.items():
            length = self.lengths[claim_id]
            counts: dict[str, int] = {}
            for token in doc["tokens"]:
                counts[token] = counts.get(token, 0) + 1
            score = 0.0
            for token in set(tokens):
                freq = counts.get(token, 0)
                if not freq:
                    continue
                idf = self.idf.get(token, 0.0)
                score += idf * (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * length / self.avg_length))
            if score > 0:
                scores.append((claim_id, score))
        scores.sort(key=lambda item: (-item[1], item[0]))
        return scores[:limit]

    def vector(self, query: str, limit: int = 50) -> list[tuple[str, float]]:
        query_vector = _normalise(_hashed_vector(_doc_tokens(query)))
        scores = [
            (claim_id, _cosine(query_vector, vector))
            for claim_id, vector in self.vectors.items()
        ]
        scores = [(claim_id, score) for claim_id, score in scores if score > 0.02]
        scores.sort(key=lambda item: (-item[1], item[0]))
        return scores[:limit]

    def graph(self, query: str, limit: int = 50) -> list[tuple[str, float]]:
        lowered = query.lower()
        matched: list[str] = []
        for entity_id, name in self.entity_names.items():
            if name.lower() in lowered:
                matched.append(entity_id)
        scores: dict[str, float] = {}
        for entity_id in matched:
            for claim_id in self.entity_claims.get(entity_id, []):
                scores[claim_id] = scores.get(claim_id, 0.0) + 1.0
        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        return ranked[:limit]

    def state_stream(self, query: str, limit: int = 50) -> list[tuple[str, float]]:
        lowered = query.lower()
        wants = None
        for status in ("superseded", "disputed", "stale", "candidate", "archived"):
            if status in lowered:
                wants = status
                break
        explicit_status = re.search(r"status:(\w+)", lowered)
        if explicit_status:
            wants = explicit_status.group(1)
        scores: list[tuple[str, float]] = []
        for claim in self.claims:
            if wants and claim["status"] != wants:
                continue
            if not wants and "confidence" in lowered and "low" in lowered and claim["probability"] >= 0.5:
                continue
            if wants:
                scores.append((claim["claim_id"], claim["probability"]))
        scores.sort(key=lambda item: (-item[1], item[0]))
        return scores[:limit]

    def topic_pages(self, query: str) -> list[str]:
        lowered = query.lower()
        topics = []
        for topic in self.schema["topics"]:
            title = topic["title"].lower()
            if title in lowered or any(word in lowered for word in topic["id"].split(".")):
                topics.append(topic["id"])
        return topics

    # -------------------------------------------------------------------- fuse

    def search(self, query: str, limit: int = 8) -> list[dict[str, Any]]:
        streams = {
            "bm25": self.bm25(query),
            "vector": self.vector(query),
            "graph": self.graph(query),
            "state": self.state_stream(query),
        }
        k = float(self.schema["thresholds"]["rrf_k"])
        fused: dict[str, float] = {}
        provenance: dict[str, list[str]] = {}
        for name, ranked in streams.items():
            for rank, (claim_id, _score) in enumerate(ranked, start=1):
                fused[claim_id] = fused.get(claim_id, 0.0) + 1.0 / (k + rank)
                provenance.setdefault(claim_id, []).append(name)
        by_id = {claim["claim_id"]: claim for claim in self.claims}
        topic_scores = nlp.score_topics(query, "", self.schema)
        query_topic = topic_scores[0][0] if topic_scores and topic_scores[0][1] >= 3 else None
        results = []
        for claim_id, score in fused.items():
            claim = by_id.get(claim_id)
            if claim is None:
                continue
            rerank = score
            rerank += 0.012 * claim["probability"]
            rerank += 0.008 * claim.get("source_authority_weight", 0.0)
            rerank += 0.006 * claim.get("freshness", 1.0)
            if query_topic and claim["topic"] == query_topic:
                rerank += 0.012
            results.append({
                "claim_id": claim_id,
                "score": round(rerank, 6),
                "streams": sorted(set(provenance[claim_id])),
                "claim": claim,
            })
        results.sort(key=lambda item: (-item["score"], item["claim_id"]))
        return results[:limit]

    # ---------------------------------------------------------------- persist

    def save(self) -> None:
        config.write_json(config.RETRIEVAL_DIR / "bm25_index" / "index.json", {
            "idf": self.idf,
            "lengths": self.lengths,
            "avg_length": self.avg_length,
            "documents": len(self.docs),
        })
        config.write_json(config.RETRIEVAL_DIR / "vector_index" / "vectors.json", {
            "buckets": VECTOR_BUCKETS,
            "vectors": {claim_id: {str(key): round(value, 5) for key, value in vector.items()}
                        for claim_id, vector in self.vectors.items()},
        })
        config.write_json(config.RETRIEVAL_DIR / "graph_index" / "adjacency.json", {
            "entities": {entity_id: {"name": self.entity_names.get(entity_id, entity_id), "claims": claims}
                         for entity_id, claims in self.entity_claims.items()},
            "topics": self.topic_claims,
        })
        config.write_json(config.RETRIEVAL_DIR / "fusion_config.json", {
            "method": "reciprocal_rank_fusion",
            "k": self.schema["thresholds"]["rrf_k"],
            "streams": ["bm25", "vector", "graph", "state"],
            "rerank": ["claim_probability", "source_authority", "freshness"],
        })
