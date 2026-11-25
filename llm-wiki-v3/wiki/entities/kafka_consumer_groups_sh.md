---
title: kafka-consumer-groups.sh
type: entity
entity_id: ent_kafka_consumer_groups_sh
entity_type: command
claim_ids:
  - claim_5e68579a
  - claim_4eec96d9
confidence: 0.765
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_b289b34c
---

# kafka-consumer-groups.sh

Type: command. Mentioned in 2 claims across 2 topics.
Aliases: kafka-consumer-groups.

## Claims

- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix).** Confidence 0.66 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]

## Related Entities

- [[docker|Docker]] (2)
- [[kafka|Kafka]] (2)
- [[broker|broker]] (1)
- [[kafka_topics_sh|kafka-topics.sh]] (1)
