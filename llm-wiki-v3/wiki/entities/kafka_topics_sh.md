---
title: kafka-topics.sh
type: entity
entity_id: ent_kafka_topics_sh
entity_type: command
claim_ids:
  - claim_5e68579a
  - claim_c9e8d488
  - claim_4919910b
  - claim_018c1927
confidence: 0.709
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_b289b34c
---

# kafka-topics.sh

Type: command. Mentioned in 4 claims across 2 topics.
Aliases: kafka-topics.

## Claims

- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Export PATH="$PWD/kafka_2.13-4.4.0/bin:$PATH" ; export KDATA="$PWD/kafka-data" ; kafka-topics.sh --version # → 4.4.0.** Confidence 0.49 · [[kafka-log|Kafka Log]]

## Related Entities

- [[kafka|Kafka]] (3)
- [[docker|Docker]] (2)
- [[broker|broker]] (2)
- [[topic|topic]] (2)
- kafka-console-consumer.sh (1)
- [[kafka_consumer_groups_sh|kafka-consumer-groups.sh]] (1)
- [[offset|offset]] (1)
- [[partition|partition]] (1)
