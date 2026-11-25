---
title: Kafka Log
type: systems
topic: kafka.log
entity_ids:
  - ent_partition
  - ent_topic
  - ent_kafka
  - ent_offset
  - ent_kafka_topics_sh
  - ent_broker
  - ent_kdata
  - ent_lag
  - ent_route
  - ent_append_only_log
  - ent_consumer_group
  - ent_docker
claim_ids:
  - claim_03cc6d79
  - claim_2ee83bfc
  - claim_4f4f199d
  - claim_2c7ae9c8
  - claim_8132c537
  - claim_44c56793
  - claim_5c173d7d
  - claim_7fe51d3b
  - claim_4cbbd4b8
  - claim_daf456a4
  - claim_c9e94a4c
  - claim_64fbe26b
  - claim_b5c89f2e
  - claim_c9e8d488
  - claim_795df9f4
  - claim_3e36f06c
  - claim_e775c362
  - claim_a6c2c236
  - claim_4f0bb3f2
  - claim_4919910b
  - claim_054df005
  - claim_018c1927
  - claim_839326e1
  - claim_fa88db3a
  - claim_e776b74b
  - claim_6e80714b
  - claim_9303be70
  - claim_42524796
  - claim_67369049
  - claim_4d02ca61
  - claim_a893397a
confidence: 0.636
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_799c8bd7
  - src_96e79681
  - src_b289b34c
  - src_b3356305
  - src_bb056c24
review_required: false
---

# Kafka Log

Rendered from 31 claims and 6 sources. Median confidence 0.64; 25 active, 0 disputed, 0 superseded.

## Current Understanding

### Kafka broker command line tools

**Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your messages as bytes in a log segment on disk.**
Confidence 0.68 · active · 1 source · when: after this block you can create a topic with several partitions
Evidence: `session-06/01_kafka_cli.md:3` — “Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your…”

**Write your predictions down before you press Enter.**
Confidence 0.63 · active · 1 source · when: before you press Enter
Evidence: `session-06/01_kafka_cli.md:9` — “Write your predictions down before you press Enter. The exam asks why, not which command.”

**Work in pairs: one types, one predicts – swap after each part.**
Confidence 0.63 · active · 1 source · when: after each part
Evidence: `session-06/01_kafka_cli.md:7` — “You need a running broker (README.md → Before the session). Work in pairs: one types, one predicts – swap after each part.”

### Choose route

**All commands are written on one line, so they also work in PowerShell (which does not understand \ line breaks).**
Confidence 0.73 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:41` — “All commands are written on one line, so they also work in PowerShell (which does not understand \ line breaks). The message Picked up JAVA_TOOL_OPTIONS … or a hint about KIP-848 can be…”

**Export PATH="$PWD/kafka_2.13-4.4.0/bin:$PATH" ; export KDATA="$PWD/kafka-data" ; kafka-topics.sh --version # → 4.4.0.**
Confidence 0.49 · candidate · 1 source
Evidence: `session-06/01_kafka_cli.md:35` — “export PATH="$PWD/kafka_2.13-4.4.0/bin:$PATH" ; export KDATA="$PWD/kafka-data" ; kafka-topics.sh --version # → 4.4.0”

### Consume beginning

**Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.**
Confidence 0.74 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:70` — “docker exec -it broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic cli-demo --partitions 3 --replication-factor 1 | kafka-topics.sh --bootstrap-server…”

**Stop with Ctrl+C after the messages appear.**
Confidence 0.63 · active · 1 source · when: after the messages appear
Evidence: `session-06/01_kafka_cli.md:130` — “Stop with Ctrl+C after the messages appear. Example (your partition numbers may differ, the pattern will not):”

### Kafka python producers consumers consumer

**Create a topic with 3 partitions from Python – idempotently (safe to run twice).**
Confidence 0.65 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-0:7` — “1. create a topic with 3 partitions from Python – idempotently (safe to run twice),”

**Keyed vs. unkeyed messages: which partition, which order.**
Confidence 0.61 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-0:9` — “3. keyed vs. unkeyed messages: which partition, which order,”

### Messages disk

**A partition is a folder; inside are segment files.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:194` — “A partition is a folder; inside are segment files. The .log file is the append-only log: messages are only ever added at the end. (__consumer_offsets-0 … -49 are the 50 partitions of the…”

**Kafka-dump-log.sh --files "$KDATA/cli-demo-0/00000000000000000000.log" --print-data-log.**
Confidence 0.45 · candidate · 1 source
Evidence: `session-06/01_kafka_cli.md:207` — “kafka-dump-log.sh --files "$KDATA/cli-demo-0/00000000000000000000.log" --print-data-log”

### Partitions later

**Prediction 4: we change the topic from 3 to 4 partitions.**
Confidence 0.71 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:246` — “Prediction 4: we change the topic from 3 to 4 partitions. Does Tirol still go to the same partition?”

**Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).**
Confidence 0.68 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:257` — “Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).”

### Produce messages key

**Older Kafka versions and many tutorials write --property instead of --reader-property.**
Confidence 0.71 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:120` — “> Older Kafka versions and many tutorials write --property instead of --reader-property. In Kafka 4.4 --property still works but is deprecated.”

**A Kafka message is a key–value pair.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:99` — “A Kafka message is a key–value pair. The producer picks the partition from the key: partition = hash(key) mod number_of_partitions. No key → the producer spreads messages over the…”

### Sessions folders

**Folder: (Session 5 – no folder) — Topic: Stream processing with Kafka – theory: events, append-only logs, topics and partitions, replication, KRaft; Runs on: Kaggle.**
Confidence 0.75 · active · 1 source
Evidence: `README.md:133` — “(Session 5 – no folder) | Stream processing with Kafka – theory: events, append-only logs, topics and partitions, replication, KRaft | Kaggle”

**Folder: (Session 3 – no folder) — Topic: Groups Work; Runs on: Google Drive.**
Confidence 0.69 · active · 1 source
Evidence: `README.md:131` — “(Session 3 – no folder) | Groups Work | Google Drive”

### Turn partitions key

**Each key appears in exactly one partition: partition = hash(key) mod 3.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-11:1` — “Each key appears in exactly one partition: partition = hash(key) mod 3. Several keys share a partition – that is fine. The Java CLI from Block 1 and this Python client use the same hash…”

**TODO: fill key_to_partitions from sent (each row is: key, seq, partition, offset).**
Confidence 0.56 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-10` — “TODO: fill key_to_partitions from sent (each row is: key, seq, partition, offset)”

### Consume limit

**A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of every partition.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-13:5` — “consumer_timeout_ms=5000 ends the for loop after 5 s without new messages. A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of…”

### Consumer groups lag

**A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:150` — “A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets. Lag = log-end offset − committed offset = messages written but…”

### Create topic idempotently

**Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the terminal scripts can create the same topic).**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-3:2` — “Idempotent = running it once or ten times leaves the same state. Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the…”

### Ensure topic

**Create the topic if it does not exist yet (safe to run many times).**
Confidence 0.52 · candidate · 1 source · when: if it does not exist yet (safe to run many times)
Evidence: `session-06/producer.py:21` — “Create the topic if it does not exist yet (safe to run many times).”

### Keyed producer

**Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.**
Confidence 0.70 · active · 1 source · when: when the write is complete on all in-sync replicas; for that answer and returns where the message went: partition and offset
Evidence: `session-06/02_kafka_python.ipynb#cell-7:2` — “acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.”

### Offsets commits lag

**Now produce 5 messages while nobody reads, then compute the lag = log-end offset − committed offset, per partition.**
Confidence 0.64 · active · 1 source · when: while nobody reads
Evidence: `session-06/02_kafka_python.ipynb#cell-19:1` — “0 – the group committed its offsets, so it continues where it stopped. Now produce 5 messages while nobody reads, then compute the lag = log-end offset − committed offset, per partition.”

### Order kept

**Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-17:1` — “Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed. Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from…”

### Producer

**Every line shows where the message went: key -> partition @ offset.**
Confidence 0.52 · candidate · 1 source
Evidence: `session-06/producer.py:1` — “Every line shows where the message went: key -> partition @ offset”

### Reading execution plan

**Symbol: Sort — Meaning: Sorting within a partition.**
Confidence 0.65 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:20` — “Sort | Sorting within a partition”

### Serializers python object bytes

**Kafka only stores bytes (Block 1, the hex dump).**
Confidence 0.70 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-5:2` — “Kafka only stores bytes (Block 1, the hex dump). The producer needs a serializer (object → bytes), the consumer a deserializer (bytes → object). The old lab wrote it by hand – kafka-python…”

### Topics exist

**From it, the client learns about the whole cluster.**
Confidence 0.63 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:54` — “--bootstrap-server localhost:9092 = "the first broker I talk to". From it, the client learns about the whole cluster.”

### Write course config

**Copy config/server.properties → config/course-server.properties with our data folder, automatic topic creation switched off (you create topics yourself) and small segments (so you can see several segment files in kafka-data/ after a few thousand messages).**
Confidence 0.52 · candidate · 1 source · when: after a few thousand messages)
Evidence: `session-06/get_kafka.py:92` — “Copy config/server.properties → config/course-server.properties with our data folder, automatic topic creation switched off (you create topics yourself) and small segments (so you can see…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/get_kafka.py` | code | 0.80 | 1 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 10 | 2026-11-11 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 15 | 2026-11-11 |
| `README.md` | readme | 0.85 | 2 | 2026-11-11 |
| `session-06/producer.py` | code | 0.80 | 2 | 2026-11-11 |

## Related Pages

- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (48 shared entities)
- [[kafka-cluster|Kafka Cluster]] (43 shared entities)
- [[kafka-producers|Kafka Producers]] (37 shared entities)
- [[unfiled|Unfiled Observations]] (31 shared entities)
- [[spark-architecture|Spark Architecture]] (27 shared entities)
- [[hdfs-architecture|HDFS]] (24 shared entities)

## Open Questions

15 prompts from the material are collected in [[questions/kafka-log|Questions: Kafka Log]].
- Prediction 2: will the three Tirol messages end up in one partition or in different ones?
- Is the output in the order you typed? Which order is guaranteed?
- Every partition starts at offset 0. What is an offset, and is it unique in the topic or only in a partition?

## Timeline

- 2026-11-25: evidence_attached on `claim_c9e8d488` (0.74 → 0.74)
- 2026-11-25: evidence_attached on `claim_c9e8d488` (0.74 → 0.74)
- 2026-11-25: new_claim on `claim_6e80714b`
- 2026-11-25: new_claim on `claim_9303be70`
- 2026-11-25: new_claim on `claim_42524796`
- 2026-11-25: new_claim on `claim_67369049`
- 2026-11-25: new_claim on `claim_4d02ca61`
- 2026-11-25: new_claim on `claim_a893397a`
