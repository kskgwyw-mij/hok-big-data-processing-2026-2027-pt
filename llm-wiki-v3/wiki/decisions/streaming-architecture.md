---
title: Streaming Architectures
type: decisions
topic: streaming.architecture
entity_ids:
  - ent_kafka
claim_ids:
  - claim_95f17588
  - claim_dbe6518c
confidence: 0.646
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
review_required: false
---

# Streaming Architectures

Rendered from 2 claims and 1 sources. Median confidence 0.65; 1 active, 0 disputed, 0 superseded.

## Current Understanding

### At least once

**Commit …: after processing — Crash in between means: messages processed twice; Name: at-least-once.**
Confidence 0.70 · active · 1 source · when: after processing — Crash in between means: messages processed twice
Evidence: `session-06/02_kafka_python.ipynb#cell-23:9` — “after processing | messages processed twice | at-least-once”

**Kafka also offers exactly-once within Kafka (transactions) – not part of this course.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:12` — “Kafka also offers exactly-once within Kafka (transactions) – not part of this course.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 2 | 2026-11-11 |

## Related Pages

- [[course-exam|Exam]] (1 shared entities)
- [[course-setup|Course Setup]] (1 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (1 shared entities)
- [[hdfs-architecture|HDFS]] (1 shared entities)
- [[kafka-cluster|Kafka Cluster]] (1 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (1 shared entities)

## Open Questions

2 prompts from the material are collected in [[questions/streaming-architecture|Questions: Streaming Architectures]].
- 6.3 (3 P) A company computes the same KPIs twice: a nightly Spark batch job and a streaming job. Name this architecture and its main…
- E6 (2 P) Describe the Lambda and the Kappa architecture in one sentence each. Which role does Kafka play in Kappa?

## Timeline

- 2026-11-25: new_claim on `claim_95f17588`
- 2026-11-25: new_claim on `claim_dbe6518c`
