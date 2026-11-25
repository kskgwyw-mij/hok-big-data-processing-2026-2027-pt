---
title: offset
type: entity
entity_id: ent_offset
entity_type: concept
claim_ids:
  - claim_78ea47b9
  - claim_8132c537
  - claim_5c173d7d
  - claim_4cbbd4b8
  - claim_d2b9f705
  - claim_eefecc93
  - claim_64fbe26b
  - claim_c9e8d488
  - claim_3e36f06c
  - claim_4d02ca61
confidence: 0.636
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_b289b34c
  - src_bb056c24
  - src_cecf99ea
---

# offset

Type: concept. Mentioned in 10 claims across 3 topics.
Aliases: offsets.

## Claims

- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **Experiment 1 – one producer, one consumer.** Confidence 0.73 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Now produce 5 messages while nobody reads, then compute the lag = log-end offset − committed offset, per partition.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of every partition.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **0 – the group committed its offsets, so it continues where it stopped.** Confidence 0.57 · [[unfiled|Unfiled Observations]]
- **TODO: fill key_to_partitions from sent (each row is: key, seq, partition, offset).** Confidence 0.56 · [[kafka-log|Kafka Log]]
- **Consumers, offsets, auto-commit, lag and at-least-once.** Confidence 0.55 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Every line shows where the message went: key -> partition @ offset.** Confidence 0.52 · [[kafka-log|Kafka Log]]

## Related Entities

- [[partition|partition]] (7)
- [[kafka|Kafka]] (2)
- [[broker|broker]] (2)
- [[lag|lag]] (2)
- [[topic|topic]] (2)
- [[docker|Docker]] (1)
- [[isr|ISR]] (1)
- [[consumer_group|consumer group]] (1)
- kafka-console-consumer.sh (1)
- [[kafka_topics_sh|kafka-topics.sh]] (1)
