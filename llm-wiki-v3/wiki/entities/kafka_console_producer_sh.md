---
title: kafka-console-producer.sh
type: entity
entity_id: ent_kafka_console_producer_sh
entity_type: command
claim_ids:
  - claim_2aedc4a6
  - claim_80290f63
confidence: 0.764
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_6002d48d
  - src_8615b91f
  - src_fc0bfe80
---

# kafka-console-producer.sh

Type: command. Mentioned in 2 claims across 2 topics.
Aliases: kafka-console-producer.

## Claims

- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]

## Related Entities

- [[docker|Docker]] (2)
- [[kafka|Kafka]] (2)
- [[broker|broker]] (2)
- [[kafka_topics_sh|kafka-topics.sh]] (2)
- [[topic|topic]] (2)
- [[linux|Linux]] (1)
- [[spark_task|Spark task]] (1)
- [[zookeeper|ZooKeeper]] (1)
- [[kafka_console_consumer_sh|kafka-console-consumer.sh]] (1)
- [[lag|lag]] (1)
