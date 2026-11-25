# Matching contract — `match_claims_v1`

Given a new observation and candidate claims from the current state, decide what the observation does
to the belief state. You are not allowed to rewrite the candidate claims.

## Input

```json
{
  "observation": {
    "observation_id": "obs_1a2b3c4d5e",
    "claim_key": "kafka.log.segment_files",
    "claim_text": "A partition is a folder that contains segment files.",
    "stance": "supports",
    "confidence": 0.86,
    "evidence_span": "A partition is a folder; inside are segment files.",
    "source_id": "src_x"
  },
  "candidates": [
    {"claim_id": "claim_001", "claim_key": "kafka.log.segment_files", "current_text": "...", "probability": 0.71, "status": "active"}
  ]
}
```

## Output

```json
{
  "observation_id": "obs_1a2b3c4d5e",
  "candidate_matches": [
    {
      "claim_id": "claim_001",
      "match_type": "same_claim",
      "confidence": 0.88,
      "reason": "Both describe a partition as a folder of segment files; no scope difference."
    }
  ]
}
```

`match_type` is one of:

| match_type | Meaning | Engine effect |
|---|---|---|
| `same_claim` | Same assertion, same scope | `support_update` unless the source already supported it |
| `related` | Same subject, different assertion | new claim |
| `contradiction` | Same assertion, opposite truth value | `contradiction_update` + open conflict |
| `supersession` | Newer source explicitly replaces the old statement | `supersession`, old claim kept as history |
| `scope_split` | Both true under different conditions | new claim with `conditions`, old claim unchanged |
| `no_match` | Nothing applies | `new_claim` |

## Rules

1. **Prefer the most conservative match.** `same_claim` requires that the two sentences could replace
   each other without changing meaning for a reader of the course.
2. **Two statements in the same section are not automatically the same claim.** Shared heading or key
   is a hint, not evidence.
3. **`contradiction` requires the same subject and predicate**, with a negation, a conflicting quantity
   of the same unit, or an antonym. "Threads do not help CPU-bound code" and "the GIL serialises
   bytecode" are two claims, not a contradiction.
4. **`supersession` requires a cue in the observation**: `replaces`, `no longer`, `renamed to`,
   `deprecated and removed`, `as of version`. A newer date alone is not a supersession.
5. **`scope_split`** is the right answer for a general rule plus a narrower exception. Record the
   condition in the new claim's `conditions`; do not weaken the general rule.
6. Return `no_match` rather than forcing a match at low confidence. Duplicate claims cost more than
   separate ones.
