# LLM Wiki v3 — Big Data Processing course knowledge base

An implementation of [LLM Wiki v3: A State-Space Knowledge System](https://gist.github.com/HousamKak/ba96124547d1b7c68d270c293106fe53)
over this repository. The wiki is a **rendered view**, not the truth:

```text
raw source  ->  structured observation  ->  belief update  ->  markdown page
             (engine/extract.py)        (engine/state.py)  (engine/render.py)
```

The source of truth is `raw/` (immutable copies), `observations/`, `state/` and `transitions/`.
Every sentence on a wiki page is traceable to a claim id and an evidence locator such as
`session-06/01_kafka_cli.md:194` or `raw/inbox/lecture-07.pdf#p3`.

Built from the 28 files in this repository: **618 observations → 461 claims → 99 pages**, plus
153 question prompts collected from the exam material.

## Quick start

```bash
cd llm-wiki-v3
python3 -m engine stats                     # counts, status distribution
python3 -m engine query "why is Parquet faster than CSV"
python3 -m engine lint                      # writes reports/lint_latest.md
python3 -m engine eval --write              # retrieval, state, faithfulness, governance
python3 -m unittest discover -s tests -v    # 30 unit tests
```

Regenerate everything after editing a source or the ontology:

```bash
python3 -m engine rebuild
```

`ingest` is incremental: unchanged sources are skipped, a changed source triggers a rebuild of the
derived state, and new files in `raw/inbox/` are added. It is idempotent — running it twice changes nothing.

## Adding the lecture PDFs

```bash
cp ~/Downloads/lecture-07.pdf llm-wiki-v3/raw/inbox/
cd llm-wiki-v3 && python3 -m engine ingest
```

PDF text is extracted with `pdftotext` (poppler). Pages become `#p1`, `#p2`, … locators, so evidence
points at a page instead of a line. Scanned PDFs without a text layer produce an explicit
`unreadable_source` rejection and a `notice` observation instead of silently disappearing — run OCR first.

Set `lecture_note` authority in `schema.json` (default 0.92, above notebooks and READMEs) if your notes
should outweigh the existing material.

## Layout

| Path | Meaning |
|---|---|
| `schema.json` | The human-owned ontology: topics, entity gazetteer, decay profiles, source authority, thresholds |
| `engine/` | The pipeline (stdlib only, Python 3.10+) |
| `raw/<type>/` | Immutable copies of every ingested source, named `<source_id>__<file>` |
| `raw/inbox/` | Drop new PDFs/markdown here |
| `observations/accepted/` | Structured observations after filtering |
| `observations/rejected/` | What was dropped and why (`code_fragment`, `fragment_or_lead_in`, …) |
| `state/claims.jsonl` | Current belief per claim: probability, status, evidence, conditions |
| `state/unresolved_conflicts.jsonl` | Contradictions awaiting human review |
| `transitions/transitions.jsonl` | Append-only log of every belief change |
| `transitions/audit_log.jsonl` | Ingest, decay, review, LLM-apply events |
| `graph/`, `retrieval/` | Indexes (BM25, hashed TF-IDF vectors, graph adjacency, RRF config) |
| `wiki/` | Rendered pages: `concepts/ systems/ workflows/ decisions/ questions/ entities/` |
| `index.md` | Dashboard: topics, contested claims, source table |
| `reports/lint_latest.md` | Last lint run |
| `evals/report.md` | Last eval run |
| `prompts/` | Extraction, matching and rendering contracts (section 13 of the spec) |

## How belief updates work

Per observation, `state.py` computes an independent evidence weight:

```text
strength = calibrated(confidence) × source_authority × extraction_quality × recency
delta    = logit(strength) × evidence_scale
posterior_log_odds = prior_log_odds ± delta          (+ for support, − for contradiction)
```

- **Same-source evidence never double-counts.** A source that already supports a claim adds an
  `evidence_attached` transition and leaves the probability alone; independence is what moves belief.
- **Contradiction** needs both a strong text overlap (`contradiction_similarity` 0.70) *and* a conflict
  signal (negation flip, conflicting quantity, antonym). Overlap alone is not a contradiction.
- **Supersession** needs an explicit replacement cue (`replaces`, `no longer`, `renamed to`, …), text
  overlap, and a source that is not older than the claim it would replace.
- **Decay** shrinks certainty toward 0.5 with a per-topic half-life (`concept` 540 d, `procedure` 240 d,
  `implementation_detail` 150 d). `freshness` drives staleness warnings and ranking.
- **Status** is derived, never hand-written: `active ≥ 0.60`, `candidate ≥ 0.30`, `stale ≥ 0.18`, below
  that `archived`; contradictions push a claim to `disputed`; superseded claims stay readable forever.

Thresholds live in `schema.json → thresholds`. Change them, then `rebuild`.

## The semantic sensor

`engine/extract.py` is a deterministic extractor, so the pipeline runs offline and every page can be
reproduced byte-for-byte. It reads markdown blocks (paragraphs, bullets, tables, code comments,
docstrings, config values), splits paragraphs into sentences, and rejects lead-ins, code fragments,
placeholders and questions. Questions are not claims: exam prompts go to `state/questions.jsonl` and
`wiki/questions/`.

Each observation carries a topic-scoped `claim_key` (`kafka.log.partitions`), a stance, a confidence,
a verbatim evidence span, entities from the gazetteer and typed relations. What it does **not** do is
reason: it cannot tell you *why* two statements conflict beyond the signals above.

## Using a real LLM instead of the heuristic sensor

The engine never calls a model itself. It exports chunks and validates answers:

```bash
python3 -m engine llm-batch --size 6000        # exports/llm/chunks.jsonl + prompt.md
# send each chunk to a model with prompts/extract_claims_v1.md
python3 -m engine llm-apply exports/llm/answers.jsonl
```

Every answer is checked against the contract: required fields, valid stance, confidence in range, and
an evidence span that must occur verbatim in the source. Rejected rows are reported, never guessed at.
Accepted rows go through the same belief updater with `extractor.model` set to the external model.

## Review and curation

```bash
python3 -m engine review approve claim_ab12cd34
python3 -m engine review reject  claim_ab12cd34 --note "wrong for the 2026 exam"
python3 -m engine review merge   claim_ab12cd34 --second claim_ef567890
python3 -m engine review resolve claim_ab12cd34 --note "scope split: enterprise only"
```

Each action writes a `human_override` transition and re-renders affected pages.

## What this corpus actually produced

- 99 pages: 21 topic pages, 57 entity pages, 21 question pages, plus the index.
- 328 active / 131 candidate / 2 archived claims, 0 disputed, 0 superseded, 0 open conflicts.
- 25 unfiled claims (lint warnings) — mostly one-liners from `session-06/get_kafka.py` and the
  `session-03`/`session-05` stubs, which are placeholders pointing to external material.
- No real contradiction or supersession in this material. The mechanisms are exercised by the eval
  fixtures instead of being faked on real content: see `engine/evals.py → state_cases`.
- Retrieval eval: recall@5 0.850, recall@10 0.938, MRR 0.707 on 80 evidence→claim queries.

## Known limits

- Retrieval is lexical (BM25 + hashed TF-IDF + graph + state), not embedding-based. It scores the
  state slice honestly but cannot paraphrase.
- Query answers are extractive: the top claims with confidence, status and evidence, plus a link to the
  topic page. No generation step, so no invented sentences — and no multi-hop synthesis either.
- Entity coverage comes from the gazetteer in `schema.json`; extend it when new material introduces
  new tools.
- Topic assignment is keyword scoring with path hints. `unfiled` is a real answer, not a bug.
- `session-03/session-03.txt` and `session-05/session-05.txt` are one-line stubs, so those sessions are
  represented only through the exam and README material.

## Design decisions worth knowing

- **Claim keys are slots, not ids.** Several distinct claims may share `spark.execution.reading_execution_plan`;
  merging is decided by text similarity, not by key equality. Lint reports same-key clusters as
  `same_key_multiple_claims` for human review.
- **Raw sources are copied, never moved.** `rebuild` wipes derived state only; `raw/` survives, including
  copies of sources you later deleted from the repository.
- **Rendered pages keep their `last_rendered` timestamp** only when content actually changed, so
  re-running `render` produces no diff.
