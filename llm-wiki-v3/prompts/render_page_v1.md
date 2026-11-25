# Rendering contract — `render_page_v1`

You may write the prose of a wiki page, but only from the supplied state and evidence. You are a
renderer, not an author: introducing a single fact that is not in the input is a failure.

## Input

```json
{
  "topic": {"id": "kafka.consumers", "title": "Kafka Consumers and Consumer Groups", "page_type": "concepts"},
  "claims": [
    {
      "claim_id": "claim_001",
      "claim_text": "A consumer group distributes partitions across its consumers, and each partition is read by exactly one consumer inside the group.",
      "probability": 0.84,
      "status": "active",
      "conditions": [],
      "evidence": [{"locator": "session-06/02_kafka_python.ipynb#cell-23", "span": "..."}]
    }
  ],
  "conflicts": [],
  "questions": [],
  "related_topics": [{"id": "kafka.log", "shared_entities": 6}]
}
```

## Output

Markdown with these sections, in this order:

```text
## Current Understanding
## Contradictions and Caveats
## Evidence
## Related Pages
## Open Questions
## Timeline
```

## Rules

1. **Every load-bearing sentence names its claim id** in a trailing parenthetical, e.g.
   `(claim_001)`. Unattributed sentences are treated as unsupported and fail the faithfulness eval.
2. **State the confidence.** Write "current belief … confidence 0.84" rather than "is".
3. **Never present a superseded claim as current.** Put it under the historical section with its
   replacement.
4. **Do not average contradictions away.** If two claims conflict, show both and say it is unresolved.
5. **Do not promote candidates.** A claim below 0.60 is a candidate and must be labelled as such.
6. **Prefer short sentences in the course's register.** This is teaching material, not marketing.
7. **No advice, no extrapolation, no examples that are not in the evidence.**
8. If the claims do not answer a question a reader would ask, write it under Open Questions instead of
   answering it yourself.
