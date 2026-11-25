---
title: replication factor
type: entity
entity_id: ent_replication_factor
entity_type: concept
claim_ids:
  - claim_c8607633
  - claim_c6cd6bf4
confidence: 0.708
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_8615b91f
  - src_fc0bfe80
---

# replication factor

Type: concept. Mentioned in 2 claims across 2 topics.
Aliases: replication.factor.

## Claims

- **» Default number of replicas can be configured globally » Can't have more replicas than you have brokers » Data replication incurs some overhead » Always enable replication in a Production cluster » Outside your laptop use a replication factor > 1 than to prevent data loss.** Confidence 0.71 · [[hdfs-architecture|HDFS]]
- **» Leader broker fails → controller elects a new leader from the ISR followers copy the leader · ISR = {1, 2, 3} » Replication factor ≤ number of brokers.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]

## Related Entities

- [[broker|broker]] (2)
- [[isr|ISR]] (1)
