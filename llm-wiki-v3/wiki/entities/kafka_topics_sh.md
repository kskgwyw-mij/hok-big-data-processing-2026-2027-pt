---
title: kafka-topics.sh
type: entity
entity_id: ent_kafka_topics_sh
entity_type: command
claim_ids:
  - claim_2aedc4a6
  - claim_c9e8d488
  - claim_0efcddb6
  - claim_4919910b
  - claim_018c1927
  - claim_bca5c57a
  - claim_80290f63
confidence: 0.796
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_6002d48d
  - src_8615b91f
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
  - src_fc0bfe80
---

# kafka-topics.sh

Type: command. Mentioned in 7 claims across 3 topics.
Aliases: kafka-topics.

## Claims

- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).** Confidence 0.83 · [[kafka-log|Kafka Log]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.80 · [[tooling-docker|Docker and Dev Containers]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Delete topic docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --delete --topic my-first-topic.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Export PATH="$PWD/kafka_2.13-4.4.0/bin:$PATH" ; export KDATA="$PWD/kafka-data" ; kafka-topics.sh --version # → 4.4.0.** Confidence 0.49 · [[kafka-log|Kafka Log]]

## Related Entities

- [[kafka|Kafka]] (6)
- [[topic|topic]] (6)
- [[docker|Docker]] (5)
- [[broker|broker]] (5)
- [[partition|partition]] (3)
- [[kafka_console_consumer_sh|kafka-console-consumer.sh]] (2)
- [[kafka_console_producer_sh|kafka-console-producer.sh]] (2)
- [[linux|Linux]] (1)
- [[spark_task|Spark task]] (1)
- [[zookeeper|ZooKeeper]] (1)
