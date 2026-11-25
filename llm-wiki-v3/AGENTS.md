# AGENTS.md

You are maintaining an LLM Wiki v3 knowledge system for the Big Data Processing course
(FH Kufstein Tirol, winter semester 2026/27).

## Prime directive

Markdown pages are not the truth. The truth is `raw/` (immutable evidence), `observations/`
(what a reader believed a source said), `state/claims.jsonl` (current belief with probabilities),
`transitions/` (append-only history) and the graph/index layers. `wiki/` is rendered from that state.

If a page and the state disagree, the state wins and the page is stale: re-render, do not hand-edit.

## Source rules

- Never edit or delete files in `raw/`. They are the audit trail.
- New material goes into `raw/` (anywhere except the registered type folders) or `raw/private/`, then
  `python3 -m engine ingest`. Files under `raw/` are ingested in place; only `raw/inbox/` files are
  copied into `raw/<type>/`.
- Teacher material — answer keys and solutions — is private by rule: it matches
  `schema.json → privacy.private_patterns`. It is ingested, stored in `observations/private/` and
  `state/private_claims.jsonl`, and never rendered into `wiki/`. Do not "fix" a page by adding a
  solution quote; if the material belongs in the wiki, the classification is wrong, not the filter.
- Every source gets a `source_id`, a content hash, an authority from `schema.json` and a date from git
  (falling back to mtime).
- A source whose hash changes triggers a full rebuild of derived state. That is intended: incremental
  patching of claims from edited prose is how knowledge bases drift.

## Observation rules

When you add or correct knowledge, write observations, not prose:

- `claim_key` — topic-scoped slot, e.g. `kafka.log.partitions`, `spark.ml.crossvalidator`
- `claim_text` — one assertion, self-contained, no pronouns that need the paragraph around them
- `stance` — `supports | contradicts | supersedes | modifies | creates_exception | defines | new_claim`
- `confidence` — 0..1, how sure the *extractor* is that the source says this
- `evidence_span` — verbatim text from the source, never a paraphrase
- `entities`, `relationships`, `conditions`, `source_id`, `locator`

Use `python3 -m engine llm-batch` + `prompts/extract_claims_v1.md` + `llm-apply` when an LLM should do
the reading. Spans that do not occur in the source are rejected automatically; do not work around that
by shortening the source, fix the span.

## State update rules

- One observation, one decision: new claim, support, contradiction, supersession, exception, scope split.
- Do not double-count evidence. A second statement from a source that already supports a claim is
  `evidence_attached`, not a probability change.
- Contradiction requires near-identical statements plus a conflict signal. Two sentences that merely
  share a section are two claims.
- Supersession requires a replacement cue and a source that is not older than the claim.
- Never delete a superseded claim. It keeps history and gets `superseded_by`.

## Rendering rules

Pages are written by `engine/render.py`. Do not hand-edit `wiki/`.

Each page needs: current understanding, confidence, evidence with locators, contested/superseded
material kept visibly separate, related pages, open questions. Do not present a candidate claim as
settled, and never hide a low probability.

## Retrieval rules

Use the hybrid index (`engine/index.py`): BM25 for exact names, hashed TF-IDF for paraphrase, graph
traversal for dependencies, state search for confidence and status. Fuse with reciprocal rank fusion,
then rerank on probability, authority and freshness. Reconstruct the state slice before answering.

## Governance rules

- Audit every ingest, update, decay, review, merge and render.
- Keep `private`/`secret` observations out of shared pages (lint checks this).
- Mark unresolved contradictions for review instead of resolving them by averaging.
- Preserve provenance: every claim keeps at least one source and one evidence span.
- Run `python3 -m engine lint` and `python3 -m engine eval` before claiming the wiki is healthy.

## scope

This build covers one course repository. It is not a general-purpose memory service: the ontology in
`schema.json` is specific to big data teaching material, and it should be edited deliberately.
