---
title: partition
type: entity
entity_id: ent_partition
entity_type: concept
claim_ids:
  - claim_531b3248
  - claim_03cc6d79
  - claim_644c31a0
  - claim_2af15809
  - claim_be79fd03
  - claim_3500f63e
  - claim_5b33a9f2
  - claim_f71b3b42
  - claim_4f4f199d
  - claim_2c7ae9c8
  - claim_8132c537
  - claim_9f38d443
  - claim_44c56793
  - claim_e76e1d3a
  - claim_5c173d7d
  - claim_eecb9552
  - claim_7fe51d3b
  - claim_243ef926
  - claim_2160d506
  - claim_78d6d6b2
  - claim_b2790cc8
  - claim_5a71b7fc
  - claim_c9e8d488
  - claim_3e36f06c
  - claim_e775c362
  - claim_4f0bb3f2
  - claim_0efcddb6
  - claim_054df005
  - claim_19e7d770
  - claim_e5d21816
  - claim_67369049
  - claim_4d02ca61
  - claim_fe4f6640
  - claim_42099051
  - claim_8134bcca
  - claim_569cd96b
  - claim_1c957019
  - claim_c740d3a4
  - claim_ca9b02cb
  - claim_d484f3b4
  - claim_8877b1bb
  - claim_1d3ee168
  - claim_2fd01ef9
  - claim_cadd58c6
  - claim_e8488930
  - claim_1833931d
  - claim_5fe7584b
  - claim_f7b79bf9
  - claim_6e8f4f34
  - claim_bda738c6
  - claim_e7186000
  - claim_ca9c0d00
  - claim_e3af4de4
  - claim_21ffc4fc
  - claim_3b676cd6
  - claim_223f3223
  - claim_4ec3a5b0
  - claim_1c849616
  - claim_d799d04e
  - claim_74fd87ab
  - claim_268fed9d
  - claim_0d2dbf6f
  - claim_3473e7f3
  - claim_375bb599
  - claim_80290f63
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_47132aab
  - src_59b6ded4
  - src_799c8bd7
  - src_8615b91f
  - src_96e79681
  - src_b289b34c
  - src_b3356305
  - src_bb056c24
  - src_cecf99ea
  - src_f8b034ea
  - src_fc0bfe80
---

# partition

Type: concept. Mentioned in 65 claims across 10 topics.
Aliases: partitions.

## Claims

- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.** Confidence 0.86 · [[kafka-log|Kafka Log]]
- **Column: Leader — Meaning: id of the broker that handles reads and writes for this partition.** Confidence 0.84 · [[kafka-cluster|Kafka Cluster]]
- **In the plan: Exchange — Meaning: a shuffle: rows move between partitions.** Confidence 0.84 · [[spark-execution|Spark Execution Model]]
- **Create a topic with 3 partitions from Python – idempotently (safe to run twice).** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **Each key appears in exactly one partition: partition = hash(key) mod 3.** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **No key p0 p1 p2 spread – order lost Partition = ordered, append-only log (segment files on disk) Order is guaranteed per partition, not per topic Offset = position inside one partition – unique only there.** Confidence 0.80 · [[kafka-log|Kafka Log]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.80 · [[tooling-docker|Docker and Dev Containers]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.80 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **» Consumers read data from a topic » They only have to specify the topic name and one broker to connect to, and Kafka will automatically take care of pulling the data from the right brokers » Data is read in order for each partitions.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **» Offset only have a meaning for a specific partition. » E.g. offset 3 in partition doesn't represent the same data as offset 3 in partition 1. » Order is guaranteed only within a partition (not across partitions). » Data is kept only for a limited time (default is two weeks). » Once the data is written to a partition, it can't be changed (immutability). » Data is assigned randomly to a partition unless a key is provided (more on this later). » You can have as many partitions per topic as you want.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **LAG ✓ What you should see = log-end offset Consumer group 'cli-group' has no active members. − committed offset PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **What exactly does an offset identify? » No, they are two different messages. » An offset is the sequential position of a record inside one partition.** Confidence 0.76 · [[kafka-log|Kafka Log]]
- **B1 reads everything from the beginning and then the same live messages as group-a: every group gets all messages, inside a group each partition goes to exactly one consumer.** Confidence 0.75 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Folder: (Session 5 – no folder) — Topic: Stream processing with Kafka – theory: events, append-only logs, topics and partitions, replication, KRaft; Runs on: Kaggle.** Confidence 0.75 · [[kafka-log|Kafka Log]]
- **# expected seq … = intended group-a group-b Terminal 3 – same group different group = its own copy C1 + C2 share the 3 partitions of every message ✗ If it fails $ python consumer.py --name C2 ASSIGNED partitions [] → topic not created ✓ Tested on the Mac yet.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **2 GB ÷ 128 MB ≈ 16 4 waves one CSV file maxPartitionBytes partitions = 16 tasks on 4 cores.** Confidence 0.74 · [[data-formats|File Formats]]
- **In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails? » A colleague increases a topic from 3 to 6 partitions to get more throughput.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **How do you choose the key, and why? » 3 partitions, one group with 4 consumers.** Confidence 0.74 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Start producer.py: it creates user- events (3 partitions) C1 → [2] · C2 → [0, 1] · 20/20 delivered.** Confidence 0.74 · [[kafka-producers|Kafka Producers]]
- **Exchange in between — this is the shuffle. After the partial aggregation, all rows with the same PULocationID must land on the same partition before the final merge can happen.** Confidence 0.72 · [[spark-execution|Spark Execution Model]]
- **Prediction 4: we change the topic from 3 to 4 partitions.** Confidence 0.71 · [[kafka-log|Kafka Log]]
- **The broker numbers each partition separately, starting at 0, so offset 5 exists in every partition.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **More cores → more tasks in parallel – until the data has fewer partitions than you have cores.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Partitions are typically distributed evenly amongst brokers.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Topics: a particular stream of data » Similar to a table in a database (without all the constraints) » You can have as many topics as you want » A topic is identified by its name.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» The leader of a partition sends data and coordinates client interactions.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Explain why. » kafka-consumer-groups --describe shows CURRENT-OFFSET 120, LOG-END-OFFSET 200 for one partition.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **KRaft controllers · metadata + leader election · replace ZooKeeper » Leader – handles all reads & writes of a partition.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Rule: partition = hash(key) mod number_of_partitions.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Expected shape – numbers per partition depend on the keys.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» A Kafka cluster is composed of multiple brokers (servers) » Each broker is identified with its ID (integer) » Each broker contains certain topic partitions » After connecting to any broker (called a bootstrap broker), you will be connected to the entire cluster » A good number to get started is 3 brokers, but some big clusters have over 100 brokers » (Diagram boxes shown: Broker 1, Broker 2, Broker 3).** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Own offsets → its own copy of every message Today's lab result C4 idle – no partition left.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» More consumers than partitions → idle » Consumer joins or crashes → » lag = log-end offset − committed offset consumers rebalance.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Type: Narrow — Definition: Each output partition depends on exactly one input partition; Examples: filter, select, withColumn, map; Shuffle?: No.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Symptom: consumer.py prints ASSIGNED partitions [] (several times) — Fix: Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the consumer gets its partitions within a few seconds.** Confidence 0.69 · [[kafka-log|Kafka Log]]
- **A partition is a folder; inside are segment files.** Confidence 0.69 · [[kafka-log|Kafka Log]]
- **Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your messages as bytes in a log segment on disk.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **You run a groupBy("PULocationID").count() on a DataFrame with 8 partitions.** Confidence 0.67 · [[course-dataset|NYC Yellow Taxi Dataset]]
- **HashAggregate appears twice: once for a partial aggregation (per partition, before shuffle) and once for a final merge (after shuffle). This is a standard Spark optimisation.** Confidence 0.66 · [[spark-execution|Spark Execution Model]]
- **The producer picks the partition from the key: partition = hash(key) mod number_of_partitions.** Confidence 0.66 · [[kafka-producers|Kafka Producers]]
- **» When election is complete we have new leads per broker and partition.** Confidence 0.66 · [[kafka-cluster|Kafka Cluster]]
- **Each output partition needs one input partition.** Confidence 0.66 · [[kafka-log|Kafka Log]]
- **Data Partitions for High Throughput.** Confidence 0.66 · [[kafka-log|Kafka Log]]
- **A core works on one partition at a time.** Confidence 0.66 · [[kafka-log|Kafka Log]]
- **» Producers evenly hash data to partitions.** Confidence 0.65 · [[kafka-producers|Kafka Producers]]
- **Symbol: Sort — Meaning: Sorting within a partition.** Confidence 0.65 · [[kafka-log|Kafka Log]]
- **C1 prints ASSIGNED partitions [0, 1, 2] and then every message as p @ key=… seq=….** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of every partition.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed.** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **The Java CLI from Block 1 and this Python client use the same hash function (murmur2), so Tirol lands in the same partition from both.** Confidence 0.64 · [[hdfs-architecture|HDFS]]
- **The CONSUMER-ID column shows which consumer owns which partition.** Confidence 0.62 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Without a key, the producer spreads the messages – the same state now ends up in several partitions.** Confidence 0.62 · [[kafka-producers|Kafka Producers]]
- **Tasks – the smallest unit of work, one per partition per stage.** Confidence 0.61 · [[spark-architecture|Spark Architecture]]
- **Keyed vs. unkeyed messages: which partition, which order.** Confidence 0.61 · [[kafka-log|Kafka Log]]
- **Your partition numbers may differ – the pattern will not.** Confidence 0.59 · [[kafka-log|Kafka Log]]
- **Distributed across partitions (files, HDFS blocks, …).** Confidence 0.56 · [[hdfs-architecture|HDFS]]
- **Consumers in group-a may now print expected seq … – the same state is spread over partitions read by different consumers.** Confidence 0.56 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from partition 0 can arrive before seq 2 from partition 2.** Confidence 0.56 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **TODO: fill key_to_partitions from sent (each row is: key, seq, partition, offset).** Confidence 0.56 · [[kafka-log|Kafka Log]]
- **Every line shows where the message went: key -> partition @ offset.** Confidence 0.52 · [[kafka-log|Kafka Log]]
- **Get_registered_user() – the original generator from the old lab (one fake user, no key) KeyedEvents – events WITH a key and a per-key sequence number, for the partition / ordering / consumer-group experiments.** Confidence 0.50 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]

## Related Entities

- [[topic|topic]] (20)
- [[offset|offset]] (17)
- [[broker|broker]] (13)
- [[kafka|Kafka]] (8)
- [[lag|lag]] (4)
- [[shuffle|shuffle]] (4)
- [[docker|Docker]] (3)
- [[spark_task|Spark task]] (3)
- [[consumer_group|consumer group]] (3)
- [[kafka_topics_sh|kafka-topics.sh]] (3)
