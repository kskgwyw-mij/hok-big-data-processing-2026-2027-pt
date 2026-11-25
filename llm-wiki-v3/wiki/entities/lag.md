---
title: lag
type: entity
entity_id: ent_lag
entity_type: concept
claim_ids:
  - claim_78ea47b9
  - claim_4cbbd4b8
  - claim_054df005
  - claim_42099051
confidence: 0.654
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_b289b34c
  - src_cecf99ea
---

# lag

Type: concept. Mentioned in 4 claims across 2 topics.
Aliases: consumer lag.

## Claims

- **Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your messages as bytes in a log segment on disk.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Now produce 5 messages while nobody reads, then compute the lag = log-end offset − committed offset, per partition.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **Consumers, offsets, auto-commit, lag and at-least-once.** Confidence 0.55 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]

## Related Entities

- [[partition|partition]] (3)
- [[offset|offset]] (2)
- [[topic|topic]] (2)
- [[kafka|Kafka]] (1)
- Kafka log segment (1)
- [[broker|broker]] (1)
- [[consumer_group|consumer group]] (1)
