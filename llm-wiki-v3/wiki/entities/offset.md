---
title: offset
type: entity
entity_id: ent_offset
entity_type: concept
claim_ids:
  - claim_78ea47b9
  - claim_8132c537
  - claim_44c56793
  - claim_5c173d7d
  - claim_4cbbd4b8
  - claim_eefecc93
  - claim_5a71b7fc
  - claim_c9e8d488
  - claim_3e36f06c
  - claim_4d02ca61
  - claim_8877b1bb
  - claim_2fd01ef9
  - claim_cadd58c6
  - claim_a2c72ddb
  - claim_5fe7584b
  - claim_f7b79bf9
  - claim_6e8f4f34
  - claim_f03d9a5f
  - claim_aca866f9
  - claim_21ffc4fc
  - claim_9b05acf6
  - claim_4ec3a5b0
  - claim_1c849616
  - claim_d799d04e
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_bb056c24
  - src_cecf99ea
---

# offset

Type: concept. Mentioned in 24 claims across 3 topics.
Aliases: offsets.

## Claims

- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.** Confidence 0.86 · [[kafka-log|Kafka Log]]
- **Each key appears in exactly one partition: partition = hash(key) mod 3.** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **No key p0 p1 p2 spread – order lost Partition = ordered, append-only log (segment files on disk) Order is guaranteed per partition, not per topic Offset = position inside one partition – unique only there.** Confidence 0.80 · [[kafka-log|Kafka Log]]
- **» Offset only have a meaning for a specific partition. » E.g. offset 3 in partition doesn't represent the same data as offset 3 in partition 1. » Order is guaranteed only within a partition (not across partitions). » Data is kept only for a limited time (default is two weeks). » Once the data is written to a partition, it can't be changed (immutability). » Data is assigned randomly to a partition unless a key is provided (more on this later). » You can have as many partitions per topic as you want.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **LAG ✓ What you should see = log-end offset Consumer group 'cli-group' has no active members. − committed offset PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **» Kafka stores the offsets at which a consumer group has been reading » The offsets commit live in a Kafka topic named "__consumer_offsets" » When a consumer has processed data received some Kafka, it should be committing the offsets » If a consumer process dies, it will be able to read back from where it left off thanks to consumer offsets!.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **What exactly does an offset identify? » No, they are two different messages. » An offset is the sequential position of a record inside one partition.** Confidence 0.76 · [[kafka-log|Kafka Log]]
- **Producer settings Consumer settings acks="all" · retries=5 · linger_ms=10 group_id · auto_offset_reset="earliest" · enable_auto_commit=True (every 5 s).** Confidence 0.74 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Experiment 1 – one producer, one consumer.** Confidence 0.73 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **The broker numbers each partition separately, starting at 0, so offset 5 exists in every partition.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Topics: a particular stream of data » Similar to a table in a database (without all the constraints) » You can have as many topics as you want » A topic is identified by its name.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Explain why. » kafka-consumer-groups --describe shows CURRENT-OFFSET 120, LOG-END-OFFSET 200 for one partition.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Kappa Events Kafka log · retained, replayable Stream processor Serving Query one path » One code path – reprocess = replay the log from offset 0 with new code.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Own offsets → its own copy of every message Today's lab result C4 idle – no partition left.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» More consumers than partitions → idle » Consumer joins or crashes → » lag = log-end offset − committed offset consumers rebalance.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Committed offsets live in __consumer_offsets. · Source: 01_kafka_cli.md.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **0 – the group committed its offsets, so it continues where it stopped.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of every partition.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **TODO: fill key_to_partitions from sent (each row is: key, seq, partition, offset).** Confidence 0.56 · [[kafka-log|Kafka Log]]
- **Consumers, offsets, auto-commit, lag and at-least-once.** Confidence 0.55 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Every line shows where the message went: key -> partition @ offset.** Confidence 0.52 · [[kafka-log|Kafka Log]]

## Related Entities

- [[partition|partition]] (17)
- [[topic|topic]] (8)
- [[kafka|Kafka]] (5)
- [[broker|broker]] (4)
- [[consumer_group|consumer group]] (3)
- [[lag|lag]] (3)
- [[docker|Docker]] (1)
- [[isr|ISR]] (1)
- [[kappa_architecture|Kappa architecture]] (1)
- [[offset|OFFSET]] (1)
