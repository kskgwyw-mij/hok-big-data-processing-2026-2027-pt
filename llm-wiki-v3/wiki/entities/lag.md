---
title: lag
type: entity
entity_id: ent_lag
entity_type: concept
claim_ids:
  - claim_2aedc4a6
  - claim_78ea47b9
  - claim_054df005
  - claim_42099051
  - claim_d13bf3c2
  - claim_6e8f4f34
  - claim_4557e45e
  - claim_21ffc4fc
confidence: 0.73
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_6002d48d
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_cecf99ea
  - src_fc0bfe80
---

# lag

Type: concept. Mentioned in 8 claims across 3 topics.
Aliases: consumer lag.

## Claims

- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.80 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **LAG ✓ What you should see = log-end offset Consumer group 'cli-group' has no active members. − committed offset PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **What is the lag, and give two possible reasons why it is growing. » Your laptop has one broker.** Confidence 0.76 · [[kafka-cluster|Kafka Cluster]]
- **5b No consumer running: produce 5 more 1 3 4 1 messages 2 0 1 1 5c Predict total LAG, then check.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **» More consumers than partitions → idle » Consumer joins or crashes → » lag = log-end offset − committed offset consumers rebalance.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your messages as bytes in a log segment on disk.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Consumers, offsets, auto-commit, lag and at-least-once.** Confidence 0.55 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]

## Related Entities

- [[partition|partition]] (4)
- [[broker|broker]] (3)
- [[offset|offset]] (3)
- [[topic|topic]] (3)
- [[kafka|Kafka]] (2)
- [[consumer_group|consumer group]] (2)
- [[docker|Docker]] (1)
- Kafka log segment (1)
- [[spark_task|Spark task]] (1)
- [[zookeeper|ZooKeeper]] (1)
