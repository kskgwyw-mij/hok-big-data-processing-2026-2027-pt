---
title: kafka-consumer-groups.sh
type: entity
entity_id: ent_kafka_consumer_groups_sh
entity_type: command
claim_ids:
  - claim_5e68579a
  - claim_4eec96d9
  - claim_8877b1bb
  - claim_630ccc7b
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
---

# kafka-consumer-groups.sh

Type: command. Mentioned in 4 claims across 3 topics.
Aliases: kafka-consumer-groups.

## Claims

- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **Explain why. » kafka-consumer-groups --describe shows CURRENT-OFFSET 120, LOG-END-OFFSET 200 for one partition.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group cli-group.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix).** Confidence 0.66 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]

## Related Entities

- [[docker|Docker]] (2)
- [[kafka|Kafka]] (2)
- [[offset|OFFSET]] (1)
- [[broker|broker]] (1)
- [[offset|offset]] (1)
- [[partition|partition]] (1)
