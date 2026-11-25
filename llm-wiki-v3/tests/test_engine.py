"""Unit tests for the LLM Wiki v3 engine.

Hermetic: every test builds its own sources in a temporary directory and never
writes to the repository's state/ or wiki/ directories.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine import extract, index, llm, nlp, readers, render, state  # noqa: E402
from engine.readers import Segment, Source  # noqa: E402

SCHEMA = json.loads((Path(__file__).resolve().parent.parent / "schema.json").read_text(encoding="utf-8"))


def make_source(path: Path, source_id: str = "src_test", source_type: str = "exam",
                authority: float = 0.9, created_at: str | None = None) -> Source:
    return Source(
        source_id=source_id,
        rel_path=path.name,
        abs_path=path,
        type=source_type,
        authority=authority,
        created_at=created_at or "2026-11-01T00:00:00Z",
        author="test",
        scope="shared",
        sensitivity="internal",
        title=path.stem,
        content_hash="0" * 64,
    )


def observation(key: str, text: str, source_id: str = "src_a", stance: str = "supports",
                confidence: float = 0.8, block: str = "paragraph", locator: str | None = None) -> dict:
    return {
        "observation_id": "obs_" + hashlib.sha1(f"{text}|{source_id}|{locator}".encode()).hexdigest()[:10],
        "source_id": source_id,
        "source_path": f"{source_id}.md",
        "source_type": "exam",
        "extracted_at": "2026-11-01T00:00:00Z",
        "extractor": {"model": "test", "prompt_version": "test", "version": "1", "quality": 0.9},
        "claim_key": key,
        "claim_text": text,
        "stance": stance,
        "confidence": confidence,
        "evidence_span": text,
        "locator": locator or f"{source_id}.md:1",
        "entities": [],
        "relationships": [],
        "conditions": [],
        "valid_from": "2026-11-01",
        "valid_until": None,
        "privacy": "internal",
        "topic": key.split(".")[0] + "." + key.split(".")[1] if "." in key else "unfiled",
        "topic_score": 3.0,
        "topic_runner_up": None,
        "block": block,
        "heading": "",
        "labels": [],
    }


class ReaderTests(unittest.TestCase):
    def test_markdown_blocks_and_heading_stack(self) -> None:
        text = (
            "# Session 6\n\n"
            "## 2. Partitions\n\n"
            "A topic is split into partitions.\n\n"
            "- Each partition is an ordered log.\n"
            "- Consumers keep an offset.\n"
        )
        segments = readers.read_markdown(text, "x.md")
        blocks = [segment.block for segment in segments]
        self.assertEqual(blocks, ["paragraph", "bullet", "bullet"])
        self.assertEqual(segments[0].heading_path, ("Session 6", "Partitions"))
        self.assertIn("ordered log", segments[1].text)

    def test_matrix_table_becomes_readable_claims(self) -> None:
        text = (
            "### Formats\n"
            "| | CSV | Parquet |\n"
            "|---|---|---|\n"
            "| Keeps dtypes | ✗ | ✓ |\n"
            "| Read single columns | ✗ | ✓ |\n"
        )
        segments = [s for s in readers.read_markdown(text, "x.md") if s.block == "table_row"]
        self.assertEqual(len(segments), 2)
        self.assertIn("Keeps dtypes", segments[0].text)
        self.assertIn("Parquet: yes", segments[0].text)
        self.assertIn("matrix", segments[0].labels)

    def test_identifiers_survive_formatting(self) -> None:
        self.assertEqual(
            readers.clean_inline("run `get_data.py --months 2` on yellow_tripdata_2024-*.parquet"),
            "run get_data.py --months 2 on yellow_tripdata_2024-*.parquet",
        )
        self.assertEqual(readers.clean_inline("**bold** and *italic*"), "bold and italic")

    def test_diff_wrapper_is_unwrapped(self) -> None:
        text = "* session-06/03_exam_circuit.md\n\n@@ -0,0 +1,3 @@\n# Block 3\n\nA topic has partitions.\n"
        segments = readers.read_markdown(text, "diff.md")
        self.assertTrue(any(segment.block == "paragraph" for segment in segments))
        self.assertFalse(any("@@ -0,0" in segment.text for segment in segments))
        heading = [segment for segment in segments if segment.heading_path][0]
        self.assertEqual(heading.heading_path, ("Block 3",))

    def test_unreadable_pdf_produces_a_notice(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "lecture.pdf"
            path.write_bytes(b"%PDF-1.4 not really a pdf")
            segments = readers.read_pdf(path, "lecture.pdf")
            self.assertEqual(segments[0].block, "notice")
            self.assertIn("unreadable_pdf", segments[0].labels)


class NlpTests(unittest.TestCase):
    def test_similarity_prefers_restatements(self) -> None:
        same = nlp.similarity(
            "A topic is split into partitions.",
            "Each topic is split into several partitions.",
        )
        different = nlp.similarity(
            "A topic is split into partitions.",
            "The broker stores the cluster metadata in KRaft.",
        )
        self.assertGreater(same, 0.6)
        self.assertLess(different, 0.3)

    def test_slug_drops_numbers_and_stopwords(self) -> None:
        self.assertEqual(nlp.slug("Station 1 – Do you need a cluster?"), "need_cluster")
        self.assertEqual(nlp.slug("6.2 Kafka from Python"), "kafka_python")

    def test_quantities_and_negation(self) -> None:
        self.assertIn((64.0, "mb"), nlp.quantities("HDFS uses 64 MB blocks"))
        self.assertEqual(nlp.negation_count("This is not the same and never was"), 2)

    def test_entities_skip_bare_capitalised_words(self) -> None:
        gazetteer = nlp.build_gazetteer(SCHEMA)
        entities = nlp.extract_entities("Copy the Parquet file to DuckDB", gazetteer)
        self.assertIn("Parquet", entities)
        self.assertIn("DuckDB", entities)
        self.assertNotIn("Copy", entities)

    def test_relations_require_gazetteer_entities(self) -> None:
        known = set(SCHEMA["entities"])
        relations = nlp.extract_relations("Kafka uses the KRaft controller", ["Kafka", "KRaft"], known)
        self.assertEqual(len(relations), 1)
        self.assertEqual(relations[0]["predicate"], "uses")
        self.assertEqual(nlp.extract_relations("Copy X to Y", ["Copy", "Y"], known), [])


class ExtractorTests(unittest.TestCase):
    def test_offers_are_rejected_but_prompts_become_questions(self) -> None:
        text = (
            "## Station 1 – Do you need a cluster?\n\n"
            "**1.1 (2 P)** Name the three Vs of Big Data and explain one with an example.\n\n"
            "## How it works\n\n"
            "Points show the expected depth: 2 P means name, 4 P means justify.\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "exam.md"
            path.write_text(text, encoding="utf-8")
            source = make_source(path)
            result = extract.extract_source(source, readers.read_source(source), SCHEMA)
        self.assertEqual(len(result.questions), 1)
        self.assertEqual(result.questions[0]["kind"], "exam_prompt")
        self.assertTrue(all("Name the three" not in row["claim_text"] for row in result.observations))
        self.assertTrue(any("Points show the expected depth" in row["claim_text"] for row in result.observations))

    def test_lead_ins_and_code_fragments_are_dropped(self) -> None:
        text = (
            "# Lab\n\n"
            "Then we open the notebook and load the parquet files:\n\n"
            "```python\n"
            "# spark chose a [BroadcastHashJoin] because\n"
            "# register the schema and read the parquet files with inferSchema off\n"
            "```\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "lab.md"
            path.write_text(text, encoding="utf-8")
            source = make_source(path, source_type="lab_guide")
            result = extract.extract_source(source, readers.read_source(source), SCHEMA)
        texts = [row["claim_text"] for row in result.observations]
        self.assertTrue(all(not text.startswith("Then we open") for text in texts))
        reasons = {row["reason"] for row in result.rejected}
        self.assertIn("code_fragment", reasons)
        self.assertIn("fragment_or_lead_in", reasons)

    def test_observation_schema_is_complete(self) -> None:
        text = "# Kafka\n\nA consumer group remembers its committed offset per partition.\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "kafka.md"
            path.write_text(text, encoding="utf-8")
            source = make_source(path)
            result = extract.extract_source(source, readers.read_source(source), SCHEMA)
        row = result.observations[0]
        for field in ("observation_id", "source_id", "claim_key", "claim_text", "stance", "confidence",
                      "evidence_span", "locator", "entities", "relationships", "conditions"):
            self.assertIn(field, row)
        self.assertGreaterEqual(row["confidence"], 0.3)
        self.assertLessEqual(row["confidence"], 0.95)
        self.assertTrue(row["evidence_span"] in text)


class StateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = state.StateStore(SCHEMA)
        self.sources = {"src_a": make_source(Path("a.md"), "src_a")}

    def test_support_and_independent_confirmation(self) -> None:
        self.store.apply_observations([observation("kafka.log.topic", "A topic is split into partitions.")], self.sources)
        claim = next(iter(self.store.claims.values()))
        after_first = claim["probability"]
        self.store.apply_observations(
            [observation("kafka.log.topic", "A topic is split into partitions.", "src_b")],
            {"src_b": make_source(Path("b.md"), "src_b")},
        )
        self.assertGreater(claim["probability"], after_first)
        self.assertEqual(len(claim["source_ids"]), 2)

    def test_same_source_does_not_double_count(self) -> None:
        self.store.apply_observations([observation("kafka.log.topic", "A topic is split into partitions.")], self.sources)
        claim = next(iter(self.store.claims.values()))
        before = claim["probability"]
        self.store.apply_observations(
            [observation("kafka.log.topic", "A topic is split into partitions.", locator="a.md:99")], self.sources
        )
        self.assertAlmostEqual(claim["probability"], before, places=4)
        self.assertEqual(self.store.transitions[-1]["operation"], "evidence_attached")

    def test_contradiction_lowers_and_opens_conflict(self) -> None:
        self.store.apply_observations([observation("kafka.log.topic", "A topic is split into partitions.")], self.sources)
        claim = next(iter(self.store.claims.values()))
        before = claim["probability"]
        self.store.apply_observations(
            [observation("kafka.log.topic", "A topic is not split into partitions.", "src_c")],
            {"src_c": make_source(Path("c.md"), "src_c")},
        )
        self.assertLess(claim["probability"], before)
        self.assertEqual(claim["status"], "disputed")
        self.assertEqual(len(self.store.conflicts), 1)
        self.assertEqual(self.store.conflicts[0]["type"], "contradiction")

    def test_weak_overlap_is_not_a_contradiction(self) -> None:
        self.store.apply_observations(
            [observation("python.execution.gil", "Threads bring no speed-up for CPU-bound Python code because of the GIL.")],
            self.sources,
        )
        self.store.apply_observations(
            [observation("python.execution.gil", "We need one fact about Python: the Global Interpreter Lock.", "src_d")],
            {"src_d": make_source(Path("d.md"), "src_d")},
        )
        self.assertEqual(len([claim for claim in self.store.claims.values() if claim["status"] == "disputed"]), 0)
        self.assertEqual(self.store.conflicts, [])

    def test_supersession_keeps_history(self) -> None:
        self.store.apply_observations(
            [observation("retrieval.primary_store", "Cosmos DB is the primary retrieval store.")], self.sources
        )
        self.store.apply_observations(
            [observation("retrieval.primary_store", "Azure AI Search replaces Cosmos DB as the primary retrieval store.",
                         "src_new", stance="supersedes")],
            {"src_new": make_source(Path("new.md"), "src_new", created_at="2026-12-01T00:00:00Z")},
        )
        superseded = [claim for claim in self.store.claims.values() if claim["status"] == "superseded"]
        replacement = [claim for claim in self.store.claims.values() if claim["status"] != "superseded"]
        self.assertEqual(len(superseded), 1)
        self.assertEqual(superseded[0]["superseded_by"], replacement[0]["claim_id"])
        self.assertLessEqual(superseded[0]["probability"], SCHEMA["thresholds"]["supersede_probability"])

    def test_older_source_cannot_supersede(self) -> None:
        self.store.apply_observations(
            [observation("retrieval.primary_store", "Cosmos DB is the primary retrieval store.")],
            {"src_new": make_source(Path("new.md"), "src_new", created_at="2026-12-01T00:00:00Z")},
        )
        self.store.apply_observations(
            [observation("retrieval.primary_store", "Azure AI Search replaces Cosmos DB as the primary retrieval store.",
                         "src_old", stance="supersedes")],
            {"src_old": make_source(Path("old.md"), "src_old", created_at="2024-01-01T00:00:00Z")},
        )
        self.assertEqual([claim for claim in self.store.claims.values() if claim["status"] == "superseded"], [])

    def test_decay_reduces_certainty(self) -> None:
        self.store.apply_observations(
            [observation("kafka.log.topic", "A topic is split into partitions.")],
            {"src_a": make_source(Path("a.md"), "src_a")},
        )
        self.store.apply_observations(
            [observation("kafka.log.topic", "A topic is split into partitions.", "src_b")],
            {"src_b": make_source(Path("b.md"), "src_b")},
        )
        claim = next(iter(self.store.claims.values()))
        claim["last_confirmed_at"] = "2024-01-01T00:00:00Z"
        before = claim["probability"]
        self.store.decay_all()
        self.assertLess(claim["probability"], before)
        self.assertLess(claim["freshness"], 1.0)

    def test_status_follows_probability(self) -> None:
        claim = {
            "claim_id": "claim_x", "claim_key": "k", "current_text": "t", "probability": 0.9,
            "probability_basis": 0.9, "status": "candidate", "contradicting_observations": [],
            "last_confirmed_at": "2026-11-01T00:00:00Z", "created_at": "2026-11-01T00:00:00Z",
            "decay_profile": "concept", "needs_review": False,
        }
        self.store.recompute_status(claim)
        self.assertEqual(claim["status"], "active")
        claim["probability"] = 0.4
        self.store.recompute_status(claim)
        self.assertEqual(claim["status"], "candidate")
        claim["probability"] = 0.2
        self.store.recompute_status(claim)
        self.assertEqual(claim["status"], "stale")
        claim["probability"] = 0.05
        self.store.recompute_status(claim)
        self.assertEqual(claim["status"], "archived")


class IndexTests(unittest.TestCase):
    def build(self) -> index.HybridIndex:
        store = state.StateStore(SCHEMA)
        sources = {"src_a": make_source(Path("a.md"), "src_a")}
        for text in (
            "Parquet is columnar and stores min/max statistics per row group.",
            "A consumer group commits its offset per partition.",
            "The broker container image is apache/kafka:4.4.0.",
        ):
            store.apply_observations([observation("data.formats.parquet", text)], sources)
        return index.HybridIndex(SCHEMA).build(list(store.claims.values()), store.entities)

    def test_bm25_finds_exact_terms(self) -> None:
        hybrid = self.build()
        top = hybrid.bm25("columnar parquet")[0][0]
        self.assertIn("columnar", hybrid.docs[top]["text"])

    def test_fusion_returns_claims_with_streams(self) -> None:
        hybrid = self.build()
        results = hybrid.search("how does a consumer group track its offset", limit=3)
        self.assertTrue(results)
        self.assertIn("streams", results[0])
        self.assertGreaterEqual(results[0]["score"], results[-1]["score"])

    def test_procedural_claims_rank_lower_for_factual_questions(self) -> None:
        hybrid = self.build()
        results = hybrid.search("consumer group committed offset", limit=3)
        self.assertTrue(results)
        self.assertTrue(any("consumer" in item["claim"]["current_text"].lower() for item in results))


class RenderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = state.StateStore(SCHEMA)
        self.sources = {"src_a": make_source(Path("a.md"), "src_a")}
        self.store.apply_observations(
            [observation("kafka.log.topic", "A topic is split into partitions.")], self.sources
        )
        self.store.sources = {"src_a": self.sources["src_a"].record()}
        self.store.link_claim_entities()

    def test_topic_page_has_frontmatter_and_sections(self) -> None:
        page = render.render_topic(
            SCHEMA, "kafka.log", list(self.store.claims.values()), [], self.store.sources,
            self.store.entities, [], "2026-11-25T00:00:00Z",
        )
        self.assertTrue(page.startswith("---\ntitle:"))
        for section in ("## Current Understanding", "## Sources", "## Related Pages", "## Open Questions"):
            self.assertIn(section, page)
        self.assertIn("Confidence 0.", page)
        self.assertIn("Evidence:", page)

    def test_superseded_claims_are_not_in_current_understanding(self) -> None:
        claim = next(iter(self.store.claims.values()))
        claim["status"] = "superseded"
        claim["superseded_by"] = "claim_other"
        page = render.render_topic(
            SCHEMA, "kafka.log", list(self.store.claims.values()), [], self.store.sources,
            self.store.entities, [], "2026-11-25T00:00:00Z",
        )
        current, _, superseded = page.partition("## Superseded")
        self.assertNotIn("A topic is split into partitions", current)
        self.assertIn("A topic is split into partitions", superseded)


class LlmContractTests(unittest.TestCase):
    def test_valid_observation_passes(self) -> None:
        observation_row = {
            "claim_key": "kafka.log.partitions",
            "claim_text": "A topic is split into partitions.",
            "stance": "supports",
            "confidence": 0.9,
            "evidence_span": "A topic is split into partitions.",
        }
        self.assertEqual(llm.validate(observation_row, "Intro. A topic is split into partitions. End."), [])

    def test_fabricated_span_is_rejected(self) -> None:
        observation_row = {
            "claim_key": "kafka.log.partitions",
            "claim_text": "A topic is split into partitions.",
            "stance": "supports",
            "confidence": 0.9,
            "evidence_span": "Kafka guarantees global ordering.",
        }
        errors = llm.validate(observation_row, "A topic is split into partitions.")
        self.assertTrue(errors)
        self.assertIn("does not occur", errors[0])

    def test_invalid_stance_and_confidence_are_rejected(self) -> None:
        base = {
            "claim_key": "k", "claim_text": "A topic is split into partitions.",
            "comparison": None, "evidence_span": "A topic is split into partitions.",
        }
        self.assertTrue(llm.validate({**base, "stance": "maybe", "confidence": 0.9}, "A topic is split into partitions."))
        self.assertTrue(llm.validate({**base, "stance": "supports", "confidence": 1.7}, "A topic is split into partitions."))


class PipelineTests(unittest.TestCase):
    def test_small_corpus_end_to_end(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "session-06").mkdir()
            (root / "session-06" / "cli.md").write_text(
                "# Block 1 – Kafka CLI\n\n"
                "## 2. Create a topic\n\n"
                "A topic is split into partitions. Each partition is an ordered, append-only log.\n\n"
                "## 3. Consumer groups\n\n"
                "A consumer group remembers its committed offset per partition.\n\n"
                "A consumer group remembers how far it has read by storing the offset in __consumer_offsets.\n",
                encoding="utf-8",
            )
            source = make_source(root / "session-06" / "cli.md", "src_cli", "lab_guide", 0.9)
            source.rel_path = "session-06/cli.md"
            result = extract.extract_source(source, readers.read_source(source), SCHEMA)
            store = state.StateStore(SCHEMA)
            store.apply_observations(result.observations, {"src_cli": source})
            store.link_claim_entities()

            self.assertGreaterEqual(len(store.claims), 2)
            claims = list(store.claims.values())
            self.assertTrue(all(claim["claim_key"].startswith("kafka.") for claim in claims))
            self.assertTrue(all(claim["supporting_observations"] for claim in claims))
            self.assertTrue(all(claim["evidence"] for claim in claims))
            self.assertTrue(any(len(claim["supporting_observations"]) > 1 for claim in claims))

            hybrid = index.HybridIndex(SCHEMA).build(claims, store.entities)
            results = hybrid.search("committed offset consumer group", limit=3)
            self.assertTrue(results)
            self.assertIn("offset", results[0]["claim"]["current_text"].lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
