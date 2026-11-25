# Extraction contract — `extract_claims_v1`

You are a semantic sensor, not a summariser. Read one chunk of a course source and return structured
observations. Do not write prose. Do not invent facts that the chunk does not state.

## Input

One chunk from `exports/llm/chunks.jsonl`:

```json
{"chunk_id": "src_x_c0", "source_id": "src_x", "path": "session-06/01_kafka_cli.md", "text": "..."}
```

## Output

One JSON object per line, matching `schema.json` and the topic list:

```json
{
  "source_id": "src_x",
  "observations": [
    {
      "claim_key": "kafka.log.segment_files",
      "claim_text": "A partition is a folder that contains segment files, and the .log file is the append-only log.",
      "stance": "supports",
      "confidence": 0.86,
      "evidence_span": "A partition is a folder; inside are segment files. The .log file is the append-only log: messages are only ever added at the end.",
      "locator": "session-06/01_kafka_cli.md:194",
      "entities": ["partition", "Kafka log segment"],
      "relationships": [
        {"subject": "partition", "predicate": "has", "object": "Kafka log segment"}
      ],
      "conditions": [],
      "privacy": "internal",
      "valid_from": "2026-11-11",
      "valid_until": null
    }
  ]
}
```

## Rules

1. **One assertion per observation.** Split lists and compound sentences.
2. **`evidence_span` must be copied verbatim** from the chunk. The engine rejects spans it cannot find.
3. **`claim_key` must start with a topic id from `schema.json`** (`kafka.log`, `spark.execution`, …),
   followed by a short aspect slug. Reuse an existing key when the statement is the same slot.
4. **`claim_text` must stand alone.** No "this", "it", "the above". Expand the subject.
5. **Confidence reflects the source, not your agreement.** A clear normative statement in an exam
   document is 0.9; a hedged remark in a notebook comment is 0.5.
6. **Stance:**
   - `supports` — the chunk asserts the claim
   - `contradicts` — the chunk asserts the opposite of an existing claim
   - `supersedes` — the chunk explicitly replaces earlier material ("no longer", "replaces", "renamed to")
   - `creates_exception` — the chunk narrows a general rule ("premium customers may …")
   - `defines` — the chunk defines a term
   - `new_claim` — nothing in the wiki covers this yet
7. **Questions are not claims.** Exam prompts and exercise questions end up in `state/questions.jsonl`;
   if the chunk contains only a question, return `{"source_id": "...", "observations": []}`.
8. **Skip** navigation text, placeholders (`&nbsp;`, `____`), bare commands, and code fragments that
   are not statements about the domain.
9. **Entities** come from the gazetteer in `schema.json`. Only use gazetteer names in `relationships`;
   free-form capitalised words may appear in `entities` but produce no graph edge.
10. **No summaries.** A paragraph of five facts yields five observations or a subset, never one
    "the section explains …" observation.

## Topic ids

`bigdata.foundations`, `python.execution`, `python.environments`, `data.formats`, `data.duckdb`,
`engines.single_machine`, `hdfs.architecture`, `mapreduce.model`, `spark.architecture`,
`spark.execution`, `spark.ml`, `spark.streaming`, `kafka.log`, `kafka.cluster`, `kafka.producers`,
`kafka.consumers`, `streaming.architecture`, `course.setup`, `course.dataset`, `course.exam`,
`course.policy`, `tooling.kaggle`, `tooling.docker`, `unfiled`.

Use `unfiled` only when the chunk genuinely belongs to none of these; the lint report counts it.
