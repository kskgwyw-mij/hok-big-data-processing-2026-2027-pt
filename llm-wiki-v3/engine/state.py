"""Belief state: claims, entities, relationships, conflicts, transitions, decay.

The wiki is rendered from this; nothing here reads the wiki back.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from . import config, nlp
from .readers import Source


@dataclass
class ApplyReport:
    new_claims: int = 0
    support_updates: int = 0
    contradiction_updates: int = 0
    supersessions: int = 0
    duplicates: int = 0
    skipped: int = 0
    transitions: int = 0


@dataclass
class StateStore:
    schema: dict[str, Any]
    claims: dict[str, dict[str, Any]] = field(default_factory=dict)
    entities: dict[str, dict[str, Any]] = field(default_factory=dict)
    relationships: dict[str, dict[str, Any]] = field(default_factory=dict)
    conflicts: list[dict[str, Any]] = field(default_factory=list)
    sources: dict[str, dict[str, Any]] = field(default_factory=dict)
    applied: set[str] = field(default_factory=set)
    transitions: list[dict[str, Any]] = field(default_factory=list)
    audit: list[dict[str, Any]] = field(default_factory=list)
    topic_index: dict[str, dict[str, Any]] = field(default_factory=dict)
    threshold: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.topic_index = config.topic_index(self.schema)
        self.threshold = self.schema["thresholds"]

    # ---------------------------------------------------------------- persistence

    @property
    def claims_path(self) -> Path:
        return config.STATE_DIR / "claims.jsonl"

    def load(self) -> "StateStore":
        for row in config.read_jsonl(self.claims_path):
            self.claims[row["claim_id"]] = row
        for row in config.read_jsonl(config.STATE_DIR / "entities.jsonl"):
            self.entities[row["entity_id"]] = row
        for row in config.read_jsonl(config.STATE_DIR / "relationships.jsonl"):
            self.relationships[row["relationship_id"]] = row
        self.conflicts = config.read_jsonl(config.STATE_DIR / "unresolved_conflicts.jsonl")
        for row in config.read_jsonl(config.STATE_DIR / "sources.jsonl"):
            self.sources[row["source_id"]] = row
        snapshot = config.read_json(config.STATE_DIR / "state_snapshot.json", {}) or {}
        self.applied = set(snapshot.get("applied_observations", []))
        self.transitions = config.read_jsonl(config.TRANS_DIR / "transitions.jsonl")
        self.audit = config.read_jsonl(config.TRANS_DIR / "audit_log.jsonl")
        return self

    def save(self) -> None:
        ordered = sorted(self.claims.values(), key=lambda c: (c["topic"], c["claim_key"], c["claim_id"]))
        config.write_jsonl(self.claims_path, ordered)
        config.write_jsonl(config.STATE_DIR / "entities.jsonl",
                           sorted(self.entities.values(), key=lambda e: e["entity_id"]))
        config.write_jsonl(config.STATE_DIR / "relationships.jsonl",
                           sorted(self.relationships.values(), key=lambda r: r["relationship_id"]))
        config.write_jsonl(config.STATE_DIR / "unresolved_conflicts.jsonl", self.conflicts)
        config.write_jsonl(config.STATE_DIR / "sources.jsonl",
                           sorted(self.sources.values(), key=lambda s: s["source_id"]))
        by_status: dict[str, int] = {}
        for claim in self.claims.values():
            by_status[claim["status"]] = by_status.get(claim["status"], 0) + 1
        config.write_json(config.STATE_DIR / "state_snapshot.json", {
            "schema_version": self.schema["schema_version"],
            "generated_at": config.now_iso(),
            "claims": len(self.claims),
            "entities": len(self.entities),
            "relationships": len(self.relationships),
            "conflicts_open": sum(1 for c in self.conflicts if c.get("status") == "open"),
            "sources": len(self.sources),
            "status_counts": dict(sorted(by_status.items())),
            "applied_observations": sorted(self.applied),
            "topic_counts": {
                topic: sum(1 for c in self.claims.values() if c["topic"] == topic)
                for topic in sorted({c["topic"] for c in self.claims.values()})
            },
        })
        config.write_jsonl(config.TRANS_DIR / "transitions.jsonl", self.transitions)
        config.write_jsonl(config.TRANS_DIR / "audit_log.jsonl", self.audit)

    # ------------------------------------------------------------------- decay

    def _half_life(self, claim: dict[str, Any]) -> float:
        profile = claim.get("decay_profile", "concept")
        return float(self.schema["decay_profiles"].get(profile, {}).get("half_life_days", 365))

    def freshness(self, claim: dict[str, Any], now=None) -> float:
        current = now or config.parse_iso(config.now_iso())
        confirmed = config.parse_iso(claim.get("last_confirmed_at")) or config.parse_iso(claim.get("created_at"))
        if confirmed is None:
            return 1.0
        age = max(0.0, config.days_between(confirmed, current))
        return round(math.pow(2, -age / self._half_life(claim)), 4)

    def decay_claim(self, claim: dict[str, Any], now=None) -> bool:
        """Certainty shrinks towards 0.5 as confirmation ages; returns True if state changed."""
        freshness = self.freshness(claim, now)
        base = float(claim.get("probability_basis", claim["probability"]))
        decayed = 0.5 + (base - 0.5) * math.sqrt(freshness)
        changed = abs(decayed - claim["probability"]) > 0.001
        if changed:
            claim["probability"] = round(nlp.clamp(decayed, 0.01, 0.99), 4)
        claim["freshness"] = freshness
        return changed

    def recompute_status(self, claim: dict[str, Any], now=None) -> None:
        if claim["status"] == "superseded":
            return
        probability = claim["probability"]
        freshness = claim.get("freshness", self.freshness(claim, now))
        thresholds = self.threshold
        if probability < thresholds["archive_probability"]:
            claim["status"] = "archived"
        elif probability < thresholds["candidate_probability"]:
            claim["status"] = "stale"
        elif claim["contradicting_observations"] and probability < 0.85:
            claim["status"] = "disputed"
            claim["needs_review"] = True
        elif probability >= thresholds["active_probability"]:
            claim["status"] = "active"
        else:
            claim["status"] = "candidate"
        if freshness < 0.3:
            claim["needs_review"] = True

    # ------------------------------------------------------------- observation

    def _source(self, source_id: str, sources: dict[str, Source]) -> Source | None:
        return sources.get(source_id)

    def _observation_strength(self, observation: dict[str, Any], source: Source) -> float:
        confidence = float(observation["confidence"])
        calibrated = 0.5 + 0.5 * (confidence - 0.30) / 0.65
        quality = float(observation["extractor"].get("quality", 0.8))
        profile = self.topic_index.get(observation.get("topic", ""), {}).get("decay", "concept")
        half_life = float(self.schema["decay_profiles"].get(profile, {}).get("half_life_days", 365))
        created = config.parse_iso(source.created_at)
        age = config.days_between(created, config.parse_iso(config.now_iso())) if created else 0.0
        recency = 0.6 + 0.4 * math.pow(2, -max(0.0, age) / half_life)
        strength = calibrated * source.authority * quality * recency
        return nlp.clamp(strength, 0.05, 0.95)

    def _match(self, observation: dict[str, Any]) -> tuple[dict[str, Any] | None, float, float]:
        """Best matching claim, its blended score, and the raw text similarity."""
        text = observation["claim_text"]
        best: dict[str, Any] | None = None
        best_score = 0.0
        best_text_similarity = 0.0
        for claim in self.claims.values():
            if claim["topic"] != observation["topic"]:
                continue
            if claim["status"] == "superseded":
                continue
            text_similarity = nlp.similarity(text, claim["current_text"])
            score = text_similarity
            if claim["claim_key"] == observation["claim_key"]:
                score += 0.18
            shared = set(observation["entities"]) & set(claim.get("entities", []))
            score += 0.04 * len(shared)
            if score > best_score:
                best, best_score, best_text_similarity = claim, score, text_similarity
        return best, min(best_score, 1.0), best_text_similarity

    def _is_newer(self, source: Source, claim: dict[str, Any]) -> bool:
        """Supersession needs a source at least as new as the claim it would replace."""
        incoming = (source.created_at or "")[:10]
        existing = (claim.get("last_confirmed_at") or claim.get("created_at") or "")[:10]
        if not incoming or not existing:
            return True
        return incoming >= existing

    def _conflict(self, claim: dict[str, Any], observation: dict[str, Any]) -> bool:
        left, right = claim["current_text"], observation["claim_text"]
        left_neg, right_neg = nlp.negation_count(left), nlp.negation_count(right)
        if (left_neg > 0) != (right_neg > 0):
            return True
        left_q = {(round(value, 2), unit) for value, unit in nlp.quantities(left)}
        right_q = {(round(value, 2), unit) for value, unit in nlp.quantities(right)}
        if left_q and right_q and not (left_q & right_q):
            units_left = {unit for _, unit in left_q}
            units_right = {unit for _, unit in right_q}
            if units_left & units_right:
                return True
        antonyms = (("faster", "slower"), ("before", "after"), ("always", "never"), ("enable", "disable"))
        lowered_left, lowered_right = left.lower(), right.lower()
        for a, b in antonyms:
            if (a in lowered_left and b in lowered_right) or (b in lowered_left and a in lowered_right):
                return True
        return False

    # ------------------------------------------------------------------ claims

    def _new_claim(self, observation: dict[str, Any], probability: float, status: str) -> dict[str, Any]:
        claim_id = "claim_" + config.short_hash(
            f"{observation['claim_key']}|{observation['observation_id']}", 8
        )
        topic_spec = self.topic_index.get(observation["topic"], {})
        claim = {
            "claim_id": claim_id,
            "claim_key": observation["claim_key"],
            "current_text": observation["claim_text"],
            "probability": round(probability, 4),
            "probability_basis": round(probability, 4),
            "status": status,
            "scope": "shared",
            "topic": observation["topic"],
            "page_type": topic_spec.get("page_type", "concepts"),
            "supporting_observations": [],
            "contradicting_observations": [],
            "supersedes": [],
            "superseded_by": None,
            "entities": list(observation["entities"]),
            "conditions": list(observation.get("conditions", [])),
            "source_ids": [],
            "evidence": [],
            "last_confirmed_at": observation.get("valid_from") and _day_to_iso(observation["valid_from"]) or config.now_iso(),
            "created_at": config.now_iso(),
            "decay_profile": topic_spec.get("decay", "concept"),
            "source_authority_weight": 0.0,
            "needs_review": False,
            "variant": 1,
            "privacy": observation.get("privacy", "internal"),
            "block": observation.get("block", "paragraph"),
        }
        self.claims[claim_id] = claim
        return claim

    def _attach_evidence(self, claim: dict[str, Any], observation: dict[str, Any], source: Source, stance: str, weight: float) -> None:
        observation_ids = claim["supporting_observations"] if stance == "supports" else claim["contradicting_observations"]
        if observation["observation_id"] not in observation_ids:
            observation_ids.append(observation["observation_id"])
        if source.source_id not in claim["source_ids"]:
            claim["source_ids"].append(source.source_id)
        claim["entities"] = sorted(set(claim.get("entities", [])) | set(observation["entities"]))
        for condition in observation.get("conditions", []):
            if condition not in claim["conditions"]:
                claim["conditions"].append(condition)
        claim["source_authority_weight"] = round(max(
            float(claim.get("source_authority_weight", 0.0)), source.authority
        ), 3)
        claim["evidence"].append({
            "observation_id": observation["observation_id"],
            "source_id": source.source_id,
            "locator": observation["locator"],
            "stance": stance,
            "weight": round(weight, 4),
            "span": observation["evidence_span"],
        })
        claim["evidence"].sort(key=lambda item: (-item["weight"], item["observation_id"]))
        limit = int(self.threshold["max_evidence_per_claim"]) * 2
        claim["evidence"] = claim["evidence"][:limit]

    def _apply_support(self, claim: dict[str, Any], observation: dict[str, Any], source: Source, strength: float) -> None:
        before = claim["probability"]
        claim["probability_basis"] = before
        delta = nlp.logit(strength) * float(self.threshold.get("evidence_scale", 1.6))
        posterior = nlp.sigmoid(nlp.logit(before) + delta)
        claim["probability"] = round(nlp.clamp(posterior, 0.02, 0.99), 4)
        claim["probability_basis"] = claim["probability"]
        confirmed = observation.get("valid_from")
        claim["last_confirmed_at"] = _day_to_iso(confirmed) if confirmed else config.now_iso()
        claim["freshness"] = 1.0
        self._attach_evidence(claim, observation, source, "supports", strength)
        self.recompute_status(claim)
        self._transition("support_update", claim, observation, before, claim["probability"],
                         f"Supporting observation from {source.type} source (authority {source.authority:.2f}).")

    def _apply_contradiction(self, claim: dict[str, Any], observation: dict[str, Any], source: Source, strength: float) -> None:
        before = claim["probability"]
        delta = nlp.logit(strength) * float(self.threshold.get("evidence_scale", 1.6))
        posterior = nlp.sigmoid(nlp.logit(before) - delta)
        claim["probability"] = round(nlp.clamp(posterior, 0.02, 0.99), 4)
        claim["probability_basis"] = claim["probability"]
        self._attach_evidence(claim, observation, source, "contradicts", strength)
        self.recompute_status(claim)
        self.conflicts.append({
            "conflict_id": "cf_" + config.short_hash(f"{claim['claim_id']}|{observation['observation_id']}", 8),
            "claim_id": claim["claim_id"],
            "claim_key": claim["claim_key"],
            "type": "contradiction",
            "observations": [observation["observation_id"]],
            "existing_text": claim["current_text"],
            "incoming_text": observation["claim_text"],
            "reason": f"Observation from {observation['locator']} conflicts with the current text.",
            "created_at": config.now_iso(),
            "status": "open",
        })
        claim["needs_review"] = True
        self._transition("contradiction_update", claim, observation, before, claim["probability"],
                         "Contradicting observation; conflict opened for review.")

    def _apply_supersession(self, old: dict[str, Any], observation: dict[str, Any], source: Source, strength: float, report: ApplyReport) -> None:
        before = old["probability"]
        old["probability"] = round(min(before, float(self.threshold["supersede_probability"])), 4)
        old["probability_basis"] = old["probability"]
        old["status"] = "superseded"
        old["needs_review"] = False
        new = self._new_claim(observation, nlp.clamp(strength + 0.1, 0.3, 0.97), "active")
        new["supersedes"] = [old["claim_id"]]
        new["probability_basis"] = new["probability"]
        old["superseded_by"] = new["claim_id"]
        self._attach_evidence(new, observation, source, "supports", strength)
        self._transition("supersession", old, observation, before, old["probability"],
                         f"Superseded by {new['claim_id']} from a newer source.")
        self._transition("supersession", new, observation, None, new["probability"],
                         f"Replaces {old['claim_id']} ({old['current_text']}).")
        report.supersessions += 1

    def _transition(self, operation: str, claim: dict[str, Any], observation: dict[str, Any],
                    before: float | None, after: float | None, reason: str) -> None:
        self.transitions.append({
            "transition_id": "tr_" + config.short_hash(
                f"{operation}|{claim['claim_id']}|{observation['observation_id']}|{len(self.transitions)}", 10
            ),
            "timestamp": config.now_iso(),
            "operation": operation,
            "claim_id": claim["claim_id"],
            "observation_id": observation["observation_id"],
            "before": {"probability": before, "status": claim.get("status")},
            "after": {"probability": after, "status": claim.get("status")},
            "reason": reason,
            "actor": "state_updater",
            "review_required": bool(claim.get("needs_review")),
        })

    # ------------------------------------------------------------------- graph

    def _upsert_entity(self, name: str, observation: dict[str, Any]) -> str:
        spec = self.schema["entities"].get(name, {"type": "term", "aliases": []})
        entity_id = "ent_" + nlp.slug(name, max_words=4)
        entity = self.entities.get(entity_id)
        if entity is None:
            entity = {
                "entity_id": entity_id,
                "name": name,
                "type": spec["type"],
                "aliases": list(spec.get("aliases", [])),
                "attributes": {},
                "confidence": 0.6,
                "source_observations": [],
                "claim_ids": [],
                "topics": [],
            }
            self.entities[entity_id] = entity
        observations = entity["source_observations"]
        if observation["observation_id"] not in observations:
            observations.append(observation["observation_id"])
            entity["source_observations"] = observations[-40:]
        entity["confidence"] = round(min(0.97, 0.6 + 0.03 * len(entity["source_observations"])), 3)
        return entity_id

    def _upsert_relationship(self, relation: dict[str, str], observation: dict[str, Any], probability: float) -> None:
        subject = self._upsert_entity(relation["subject"], observation)
        obj = self._upsert_entity(relation["object"], observation)
        if subject == obj:
            return
        relationship_id = "rel_" + config.short_hash(f"{subject}|{relation['predicate']}|{obj}", 8)
        record = self.relationships.get(relationship_id)
        if record is None:
            record = {
                "relationship_id": relationship_id,
                "subject_entity": subject,
                "predicate": relation["predicate"],
                "object_entity": obj,
                "qualifiers": {"qualifier": relation.get("qualifier", "")},
                "probability": round(probability, 4),
                "supporting_observations": [],
                "contradicting_observations": [],
                "status": "active",
            }
            self.relationships[relationship_id] = record
        if observation["observation_id"] not in record["supporting_observations"]:
            record["supporting_observations"].append(observation["observation_id"])
        record["probability"] = round(nlp.clamp(record["probability"] + 0.02, 0.0, 0.97), 4)

    def link_claim_entities(self) -> None:
        for claim in self.claims.values():
            for name in claim.get("entities", []):
                entity_id = "ent_" + nlp.slug(name, max_words=4)
                entity = self.entities.get(entity_id)
                if entity is None:
                    continue
                if claim["claim_id"] not in entity["claim_ids"]:
                    entity["claim_ids"].append(claim["claim_id"])
                if claim["topic"] not in entity["topics"]:
                    entity["topics"].append(claim["topic"])

    # ------------------------------------------------------------------ apply

    def apply_observations(
        self, observations: list[dict[str, Any]], sources: dict[str, Source], now=None
    ) -> ApplyReport:
        report = ApplyReport()
        ordered = sorted(
            observations,
            key=lambda o: (o.get("valid_from") or "", o["source_id"], o["locator"], o["observation_id"]),
        )
        for observation in ordered:
            source = self._source(observation["source_id"], sources)
            if source is None or observation["observation_id"] in self.applied:
                report.skipped += 1
                continue
            self.applied.add(observation["observation_id"])
            strength = self._observation_strength(observation, source)
            match, score, text_similarity = self._match(observation)
            threshold = self.threshold

            if (
                observation["stance"] == "supersedes"
                and match is not None
                and text_similarity >= threshold["related_similarity"]
                and self._is_newer(source, match)
            ):
                self._apply_supersession(match, observation, source, strength, report)
                self._wire_graph(observation, match)
                continue

            if match is not None and score >= threshold["match_similarity"]:
                conflicting = self._conflict(match, observation)
                same_source_support = (
                    any(entry["source_id"] == source.source_id and entry["stance"] == "supports"
                        for entry in match["evidence"])
                )
                if conflicting and text_similarity >= threshold["contradiction_similarity"] and not same_source_support:
                    self._apply_contradiction(match, observation, source, strength)
                    report.contradiction_updates += 1
                    self._wire_graph(observation, match)
                    continue
                if not conflicting:
                    if same_source_support:
                        self._attach_evidence(match, observation, source, "supports", strength)
                        report.duplicates += 1
                        self.transitions.append({
                            "transition_id": "tr_" + config.short_hash(f"evidence|{match['claim_id']}|{observation['observation_id']}", 10),
                            "timestamp": config.now_iso(),
                            "operation": "evidence_attached",
                            "claim_id": match["claim_id"],
                            "observation_id": observation["observation_id"],
                            "before": {"probability": match["probability"], "status": match["status"]},
                            "after": {"probability": match["probability"], "status": match["status"]},
                            "reason": "Additional evidence from an already-supporting source; no independent probability change.",
                            "actor": "state_updater",
                            "review_required": False,
                        })
                    else:
                        self._apply_support(match, observation, source, strength)
                        report.support_updates += 1
                    self._wire_graph(observation, match)
                    continue

            claim = self._new_claim(observation, 0.5, "candidate")
            delta = nlp.logit(strength) * float(self.threshold.get("evidence_scale", 1.6))
            claim["probability"] = round(nlp.sigmoid(delta), 4)
            claim["probability_basis"] = claim["probability"]
            self._attach_evidence(claim, observation, source, "supports", strength)
            self.recompute_status(claim)
            self._transition("new_claim", claim, observation, None, claim["probability"],
                             "No existing claim matched closely enough; created from this observation.")
            report.new_claims += 1
            self._wire_graph(observation, claim)
        return report

    def _wire_graph(self, observation: dict[str, Any], claim: dict[str, Any]) -> None:
        for name in observation["entities"]:
            if name in self.schema["entities"]:
                self._upsert_entity(name, observation)
        for relation in observation["relationships"]:
            self._upsert_relationship(relation, observation, claim["probability"])

    # ------------------------------------------------------------------ decay

    def decay_all(self) -> int:
        changed = 0
        for claim in self.claims.values():
            if claim["status"] in {"superseded", "archived"}:
                continue
            before = claim["probability"]
            status_before = claim["status"]
            if self.decay_claim(claim):
                changed += 1
            self.recompute_status(claim)
            if claim["probability"] != before or claim["status"] != status_before:
                self.transitions.append({
                    "transition_id": "tr_" + config.short_hash(f"decay|{claim['claim_id']}|{len(self.transitions)}", 10),
                    "timestamp": config.now_iso(),
                    "operation": "decay_update",
                    "claim_id": claim["claim_id"],
                    "observation_id": None,
                    "before": {"probability": before, "status": status_before},
                    "after": {"probability": claim["probability"], "status": claim["status"]},
                    "reason": f"Time decay applied ({claim['decay_profile']}, freshness {claim.get('freshness', 1.0)}).",
                    "actor": "decay_scheduler",
                    "review_required": bool(claim.get("needs_review")),
                })
        return changed

    def stats(self) -> dict[str, Any]:
        by_status: dict[str, int] = {}
        for claim in self.claims.values():
            by_status[claim["status"]] = by_status.get(claim["status"], 0) + 1
        return {
            "claims": len(self.claims),
            "entities": len(self.entities),
            "relationships": len(self.relationships),
            "sources": len(self.sources),
            "transitions": len(self.transitions),
            "open_conflicts": sum(1 for conflict in self.conflicts if conflict.get("status") == "open"),
            "needs_review": sum(1 for claim in self.claims.values() if claim.get("needs_review")),
            "by_status": dict(sorted(by_status.items())),
        }


def _day_to_iso(day: str) -> str:
    if not day:
        return config.now_iso()
    if len(day) == 10:
        return f"{day}T00:00:00Z"
    return day
