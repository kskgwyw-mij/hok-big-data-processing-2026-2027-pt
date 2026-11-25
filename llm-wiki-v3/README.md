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
derived state, and new files anywhere under `raw/` are added. It is idempotent — running it twice
changes nothing.

## Adding new material

Drop files into `raw/` — the root of the drop zone or `raw/private/` — then:

```bash
cd llm-wiki-v3 && python3 -m engine ingest
```

Files under `raw/` are ingested **in place**: they are already the immutable copy, so nothing is
copied again. That is what makes 145 MB of lecture decks affordable. (`raw/inbox/` still works the
old way: files there are copied into `raw/<type>/`.)

PDF text is extracted with `pdftotext` (poppler). Pages become `#p1`, `#p2`, … locators, so evidence
points at a page instead of a line. Scanned PDFs without a text layer produce an explicit
`unreadable_source` rejection and a `notice` observation instead of silently disappearing — run OCR first.

Set `lecture_note` authority in `schema.json` (default 0.92, above notebooks and READMEs) if your notes
should outweigh the existing material.

## Private and public knowledge

Teacher material — answer keys and solutions — is ingested but never published. A file is private when
it matches `schema.json → privacy.private_patterns` (`*MODEL_ANSWERS*`, `*_SOLUTION*`, `raw/private/*`).

| | Public | Private |
|---|---|---|
| Sources | `raw/…` | matching a private pattern |
| Observations | `observations/accepted/` | `observations/private/` |
| Claims | `state/claims.jsonl` | `state/private_claims.jsonl` |
| Questions | `state/questions.jsonl` | `state/private_questions.jsonl` |
| Rendered into `wiki/` | yes | **never** |
| Queryable | yes | only with `--include-private` |
| Exported by `llm-batch` | yes | only with `--include-private` |
| Committed to git | yes | no (`.gitignore`) |

The two tiers never merge: the same sentence in a public slide and a private answer key produces two
claims, because the private one must not drag teacher evidence onto a published claim. `query` hides
private claims by default and marks them `**Teacher-only:**` when you ask for them:

```bash
python3 -m engine query "why do threads not speed up CPU-bound Python" --include-private
```

Two checks enforce this: `lint` reports `privacy_leak` if text unique to the private tier appears in
`wiki/`, and `privacy_split` if a private claim is stored in the public file. Both are covered by
`tests/test_engine.py` — including a case that must still catch a real leak.

## Layout

| Path | Meaning |
|---|---|
| `schema.json` | The human-owned ontology: topics, entity gazetteer, decay profiles, source authority, thresholds |
| `engine/` | The pipeline (stdlib only, Python 3.10+) |
| `raw/<type>/` | Immutable copies of every ingested source, named `<source_id>__<file>` |
| `raw/` (root), `raw/private/` | Drop zone: ingested in place, never copied |
| `raw/inbox/` | Legacy drop zone: files here are copied into `raw/<type>/` |
| `observations/accepted/` | Structured observations after filtering |
| `observations/rejected/` | What was dropped and why (`code_fragment`, `fragment_or_lead_in`, …) |
| `state/claims.jsonl` | Current belief per claim: probability, status, evidence, conditions |
| `state/private_claims.jsonl` | Teacher-only claims; gitignored, never rendered |
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

`llm-batch` exports public sources only; add `--include-private` if you are running the extraction
yourself and the answers may contain teacher material.

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

39 sources (28 from the repository, 6 lecture decks, 1 public mock exam, 4 teacher-only documents)
→ 1,306 observations → 990 claims, 89 of them private.

- 121 pages: 23 topic pages, 75 entity pages, 22 question pages, plus the index.
- 839 active / 146 candidate / 2 archived / 2 disputed / 1 stale; 0 superseded, 4 open conflicts.
- 194 unfiled claims (lint warnings) — mostly slide one-liners and bullets that name no keyword.
  `unfiled` is a real answer, not a bug.
- The 4 open conflicts are heuristic false positives from the lecture decks: a two-word slide heading
  ("Global Interpreter Lock (GIL).") counted as a negated restatement of a full sentence, and slide
  "Route A / Route B" labels where one mentions "no Docker". They are surfaced as disputed with a
  caveat, never silently resolved; `engine review resolve` closes them by hand.
- Retrieval eval: recall@5 0.838, recall@10 0.850, MRR 0.648 on 80 evidence→claim queries — slightly
  below the 28-source run (0.850 / 0.938 / 0.707) because 990 claims compete for 10 slots.


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
  copies of sources you later deleted from the repository. Files dropped into `raw/` itself are ingested
  in place instead: re-copying 145 MB of decks would only duplicate them.
- **The privacy boundary is structural, not a filter on output.** Private sources match
  `privacy.private_patterns`; their observations, claims and questions live in separate files, and the
  belief updater refuses to match a private observation against a public claim. Rendering only ever sees
  public state, so a leak requires the ingest to have classified the file wrong — which is why
  `lint` and `eval` both re-check the rendered pages for private-only text.
- **Rendered pages keep their `last_rendered` timestamp** only when content actually changed, so
  re-running `render` produces no diff.
