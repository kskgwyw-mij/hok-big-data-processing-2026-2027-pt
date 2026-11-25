---
title: ISR
type: entity
entity_id: ent_isr
entity_type: concept
claim_ids:
  - claim_5a71b7fc
  - claim_5a00e3a8
  - claim_e988a0c0
  - claim_d484f3b4
  - claim_a3ede20d
  - claim_c8607633
  - claim_cd2cad94
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
---

# ISR

Type: concept. Mentioned in 7 claims across 1 topics.
Aliases: in-sync replica, in-sync replicas.

## Claims

- **Column: Replicas — Meaning: all brokers that keep a copy (here only broker 1).** Confidence 0.90 · [[kafka-cluster|Kafka Cluster]]
- **Column: Isr — Meaning: in-sync replicas: the copies that are fully up to date. Only these can become the new leader without losing data.** Confidence 0.80 · [[kafka-cluster|Kafka Cluster]]
- **In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails? » A colleague increases a topic from 3 to 6 partitions to get more throughput.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **» Leader broker fails → controller elects a new leader from the ISR followers copy the leader · ISR = {1, 2, 3} » Replication factor ≤ number of brokers.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Leader – broker that handles reads & Replicas – all brokers keeping a Elr / LastKnownElr – new in Kafka Isr – in-sync, fully up-to-date copies writes copy 4, ignore.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Recap 3 · Replication, ISR and KRaft.** Confidence 0.66 · [[kafka-cluster|Kafka Cluster]]

## Related Entities

- [[broker|broker]] (5)
- [[kafka|Kafka]] (2)
- [[partition|partition]] (2)
- [[kraft|KRaft]] (1)
- [[offset|offset]] (1)
- [[replication_factor|replication factor]] (1)
- [[topic|topic]] (1)
