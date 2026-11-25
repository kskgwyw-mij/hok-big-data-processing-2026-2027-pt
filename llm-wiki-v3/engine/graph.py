"""Export the belief graph: entities, claims, and the typed edges between them."""

from __future__ import annotations

from typing import Any

from . import config, nlp


def export(store) -> dict[str, Any]:
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    for entity in store.entities.values():
        nodes.append({
            "node_id": entity["entity_id"],
            "kind": "entity",
            "label": entity["name"],
            "entity_type": entity["type"],
            "confidence": entity["confidence"],
            "topics": entity.get("topics", []),
        })

    for claim in store.claims.values():
        nodes.append({
            "node_id": claim["claim_id"],
            "kind": "claim",
            "label": claim["current_text"],
            "topic": claim["topic"],
            "claim_key": claim["claim_key"],
            "probability": claim["probability"],
            "status": claim["status"],
        })

    for relationship in store.relationships.values():
        edges.append({
            "edge_id": relationship["relationship_id"],
            "source": relationship["subject_entity"],
            "target": relationship["object_entity"],
            "type": relationship["predicate"],
            "probability": relationship["probability"],
            "supporting_observations": relationship["supporting_observations"],
        })

    known_entities = set(store.entities)
    for claim in store.claims.values():
        for name in claim.get("entities", []):
            entity_id = "ent_" + nlp.slug(name, max_words=4)
            if entity_id in known_entities:
                edges.append({
                    "edge_id": "edge_" + config.short_hash(f"{claim['claim_id']}|{entity_id}", 10),
                    "source": claim["claim_id"],
                    "target": entity_id,
                    "type": "mentions",
                    "probability": claim["probability"],
                })
        for replaced in claim.get("supersedes", []):
            edges.append({
                "edge_id": "edge_" + config.short_hash(f"{claim['claim_id']}|supersedes|{replaced}", 10),
                "source": claim["claim_id"],
                "target": replaced,
                "type": "supersedes",
                "probability": claim["probability"],
            })
        for observation_id in claim.get("contradicting_observations", []):
            edges.append({
                "edge_id": "edge_" + config.short_hash(f"{claim['claim_id']}|contests|{observation_id}", 10),
                "source": claim["claim_id"],
                "target": observation_id,
                "type": "contested_by",
                "probability": claim["probability"],
            })

    config.write_jsonl(config.GRAPH_DIR / "nodes.jsonl", nodes)
    config.write_jsonl(config.GRAPH_DIR / "edges.jsonl", edges)
    snapshot = {
        "generated_at": config.now_iso(),
        "nodes": len(nodes),
        "edges": len(edges),
        "claims": sum(1 for node in nodes if node["kind"] == "claim"),
        "entities": sum(1 for node in nodes if node["kind"] == "entity"),
        "edge_types": {},
    }
    for edge in edges:
        snapshot["edge_types"][edge["type"]] = snapshot["edge_types"].get(edge["type"], 0) + 1
    snapshot["edge_types"] = dict(sorted(snapshot["edge_types"].items()))
    config.write_json(config.GRAPH_DIR / "graph_snapshot.json", snapshot)
    return snapshot
