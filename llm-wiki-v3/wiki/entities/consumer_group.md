---
title: consumer group
type: entity
entity_id: ent_consumer_group
entity_type: concept
claim_ids:
  - claim_145ad645
  - claim_37227336
  - claim_3e36f06c
  - claim_c8c19737
  - claim_42099051
  - claim_a2c72ddb
  - claim_21ffc4fc
confidence: 0.765
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
---

# consumer group

Type: concept. Mentioned in 7 claims across 2 topics.
Aliases: consumer groups, group.id.

## Claims

- **A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.** Confidence 0.86 · [[kafka-log|Kafka Log]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.80 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **LAG ✓ What you should see = log-end offset Consumer group 'cli-group' has no active members. − committed offset PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **» Kafka stores the offsets at which a consumer group has been reading » The offsets commit live in a Kafka topic named "__consumer_offsets" » When a consumer has processed data received some Kafka, it should be committing the offsets » If a consumer process dies, it will be able to read back from where it left off thanks to consumer offsets!.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Experiment 2 – a second consumer in the SAME group.** Confidence 0.72 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Consumer groups with real, independent processes (terminal scripts producer.py / consumer.py).** Confidence 0.60 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]

## Related Entities

- [[topic|topic]] (4)
- [[kafka|Kafka]] (3)
- [[offset|offset]] (3)
- [[partition|partition]] (3)
- [[broker|broker]] (2)
- [[lag|lag]] (2)
- [[docker|Docker]] (1)
- [[venv|venv]] (1)
