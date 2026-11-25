---
title: kafka-console-consumer.sh
type: entity
entity_id: ent_kafka_console_consumer_sh
entity_type: command
claim_ids:
  - claim_2aedc4a6
  - claim_c9e8d488
confidence: 0.858
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_6002d48d
  - src_8615b91f
  - src_b289b34c
  - src_fc0bfe80
---

# kafka-console-consumer.sh

Type: command. Mentioned in 2 claims across 2 topics.
Aliases: kafka-console-consumer.

## Claims

- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]

## Related Entities

- [[docker|Docker]] (2)
- [[kafka|Kafka]] (2)
- [[broker|broker]] (2)
- [[kafka_topics_sh|kafka-topics.sh]] (2)
- [[topic|topic]] (2)
- [[spark_task|Spark task]] (1)
- [[zookeeper|ZooKeeper]] (1)
- [[kafka_console_producer_sh|kafka-console-producer.sh]] (1)
- [[lag|lag]] (1)
- [[offset|offset]] (1)
