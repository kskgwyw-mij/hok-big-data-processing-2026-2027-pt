---
title: ISR
type: entity
entity_id: ent_isr
entity_type: concept
claim_ids:
  - claim_64fbe26b
  - claim_e988a0c0
confidence: 0.749
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_b289b34c
---

# ISR

Type: concept. Mentioned in 2 claims across 2 topics.
Aliases: in-sync replica, in-sync replicas.

## Claims

- **Column: Isr — Meaning: in-sync replicas: the copies that are fully up to date. Only these can become the new leader without losing data.** Confidence 0.80 · [[kafka-cluster|Kafka Cluster]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-log|Kafka Log]]

## Related Entities

- [[broker|broker]] (1)
- [[offset|offset]] (1)
- [[partition|partition]] (1)
