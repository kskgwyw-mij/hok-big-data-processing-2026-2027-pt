---
title: Kafka Log
type: systems
topic: kafka.log
entity_ids:
  - ent_partition
  - ent_topic
  - ent_kafka
  - ent_offset
  - ent_append_only_log
  - ent_broker
  - ent_kafka_topics_sh
  - ent_assigned
  - ent_docker
  - ent_kdata
  - ent_route
  - ent_sql_databases
claim_ids:
  - claim_03cc6d79
  - claim_aea8344c
  - claim_2ee83bfc
  - claim_4f4f199d
  - claim_2c7ae9c8
  - claim_8132c537
  - claim_44c56793
  - claim_5c173d7d
  - claim_7fe51d3b
  - claim_4cbbd4b8
  - claim_243ef926
  - claim_daf456a4
  - claim_c9e94a4c
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
  - claim_fe4f6640
  - claim_569cd96b
  - claim_1c957019
  - claim_c740d3a4
  - claim_663bce6e
  - claim_45adb47b
  - claim_8877b1bb
  - claim_2fd01ef9
  - claim_cadd58c6
  - claim_e8488930
  - claim_1833931d
  - claim_5fe7584b
  - claim_f7b79bf9
  - claim_f03d9a5f
  - claim_f689757f
  - claim_e7186000
  - claim_ca9c0d00
  - claim_e3af4de4
  - claim_223f3223
  - claim_2413a482
  - claim_4ec3a5b0
  - claim_1c849616
  - claim_d799d04e
  - claim_896c7d01
  - claim_4b99ecdf
  - claim_5d297b70
  - claim_d27c7b7d
  - claim_5110465b
  - claim_45762961
  - claim_af1b58f3
  - claim_74fd87ab
  - claim_80290f63
confidence: 0.703
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_41b3a933
  - src_59b6ded4
  - src_68fcf2b9
  - src_799c8bd7
  - src_8615b91f
  - src_96e79681
  - src_b289b34c
  - src_b3356305
  - src_bb056c24
  - src_cecf99ea
  - src_fc0bfe80
review_required: false
---

# Kafka Log

Rendered from 64 claims and 11 sources. Median confidence 0.70; 56 active, 0 disputed, 0 superseded.

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
Confidence 0.89 · active · 2 sources
Evidence: `session-06/01_kafka_cli.md:70` — “docker exec -it broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic cli-demo --partitions 3 --replication-factor 1 | kafka-topics.sh --bootstrap-server…”

**Stop with Ctrl+C after the messages appear.**
Confidence 0.63 · active · 1 source · when: after the messages appear
Evidence: `session-06/01_kafka_cli.md:130` — “Stop with Ctrl+C after the messages appear. Example (your partition numbers may differ, the pattern will not):”

### Kafka python producers consumers consumer

**Create a topic with 3 partitions from Python – idempotently (safe to run twice).**
Confidence 0.81 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p91:1` — “Block 1 – Create a topic with 3 partitions”

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

**Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).**
Confidence 0.83 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p91:13` — “$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic cli-demo”

**Prediction 4: we change the topic from 3 to 4 partitions.**
Confidence 0.71 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:246` — “Prediction 4: we change the topic from 3 to 4 partitions. Does Tirol still go to the same partition?”

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
Confidence 0.81 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p81:5` — “» Topic → partition → offset » Keys decide the partition topic user-events broker · localhost:9092 partition = hash(key) mod 3 P0 0 1 2 3 4 append →”

**TODO: fill key_to_partitions from sent (each row is: key, seq, partition, offset).**
Confidence 0.56 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-9:2` — “Build a dictionary key -> set of partitions from sent. Predict first: how many partitions per key?”

### Append only log cassandra hbase

**» Cassandra and HBase provide SQL- like interfaces » Use append-only, log-structured streams » Look and act like traditional SQL database to end user » Clusters may consist of thousands of distributed nodes » Popular for batch workloads.**
Confidence 0.71 · active · 1 source · when: for batch workloads
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p45:4` — “» Cassandra and HBase provide SQL- like interfaces » Use append-only, log-structured streams » Look and act like traditional SQL database to end user » Clusters may consist of thousands of…”

### Append only log consist many

**» Consist of many append-only logs on disk.**
Confidence 0.72 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p44:4` — “» Consist of many append-only logs on disk. Storage indefinitely, size or date. » Files are periodically merged, or joined together into one file » Files are periodically compacted, where…”

### Append only log kafka topics

**» Kafka Topics are roughly analogous to SQL Tables » Topics organize related events » Topics are not queryable like SQL tables » You must create consumers or producers e.g. topic logs, topic purchases » Topics consist of append-only logs » All data in a topic is in key-value form » Many configuration options and considerations » Stored in binary format and not string like JSON.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p53:3` — “» Kafka Topics are roughly analogous to SQL Tables » Topics organize related events » Topics are not queryable like SQL tables » You must create consumers or producers e.g. topic logs,…”

### Append only log key p0

**No key p0 p1 p2 spread – order lost Partition = ordered, append-only log (segment files on disk) Order is guaranteed per partition, not per topic Offset = position inside one partition – unique only there.**
Confidence 0.80 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p81:17` — “no key p0 p1 p2 spread – order lost Partition = ordered, append-only log (segment files on disk) Order is guaranteed per partition, not per topic Offset = position inside one partition –…”

### Append only log logs

**» Append-only logs are files which append events to the end as they arrive.**
Confidence 0.81 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p37:3` — “» Append-only logs are files which append events to the end as they arrive”

### Append only log sync multiple

**» How do I sync multiple SQL databases? » PostgreSQL Write-Ahead Log (WAL) » SQL Databases use append-only logs to communicate and synchronize changes in a process known as Change Data Capture (CDC). » Why not useable for streaming? > Built for replication only.**
Confidence 0.77 · active · 1 source · when: for streaming ? > Built for replication only
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p43:3` — “» How do I sync multiple SQL databases? » PostgreSQL Write-Ahead Log (WAL) » SQL Databases use append-only logs to communicate and synchronize changes in a process known as Change Data…”

### Consume limit

**A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of every partition.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-13:5` — “consumer_timeout_ms=5000 ends the for loop after 5 s without new messages. A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of…”

### Consumer groups lag

**A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.**
Confidence 0.86 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p100:3` — “» Define offset. Is an offset unique within a topic or within a partition? » A topic has 3 partitions. Messages with the key Tirol always arrive in the order they were produced, but…”

### Consumer groups real processes terminal

**C1 prints ASSIGNED partitions [0, 1, 2] and then every message as p @ key=… seq=….**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:23` — “C1 prints ASSIGNED partitions [0, 1, 2] and then every message as p @ key=… seq=….”

### Create topic idempotently

**Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the terminal scripts can create the same topic).**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-3:2` — “Idempotent = running it once or ten times leaves the same state. Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the…”

### Ensure topic

**Create the topic if it does not exist yet (safe to run many times).**
Confidence 0.52 · candidate · 1 source · when: if it does not exist yet (safe to run many times)
Evidence: `session-06/producer.py:21` — “Create the topic if it does not exist yet (safe to run many times).”

### Get kafka

**What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is where your messages live on disk.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is…”

### Kafka apache message

**» Apache Kafka is a message queue based on log-structured, append-only storage » Scales to thousands of distributed nodes » Popular for Stream Processing.**
Confidence 0.81 · active · 1 source · when: for Stream Processing
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p46:4` — “» Apache Kafka is a message queue based on log-structured, append-only storage » Scales to thousands of distributed nodes » Popular for Stream Processing”

### Kafka consumer groups sh explain why kafka consumer groups

**Explain why. » kafka-consumer-groups --describe shows CURRENT-OFFSET 120, LOG-END-OFFSET 200 for one partition.**
Confidence 0.70 · active · 1 source · when: for one partition
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p100:3` — “» Define offset. Is an offset unique within a topic or within a partition? » A topic has 3 partitions. Messages with the key Tirol always arrive in the order they were produced, but…”

### Kafka lab exam preparation

**Symptom: consumer.py prints ASSIGNED partitions [] (several times) — Fix: Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the consumer gets its partitions within a few seconds.**
Confidence 0.69 · active · 1 source · when: if you start the consumer first
Evidence: `session-06/README.md:109` — “consumer.py prints ASSIGNED partitions [] (several times) | Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the…”

### Kafka segment uses

**» Segment uses Kafka as their routing backbone for analytics events.**
Confidence 0.70 · active · 1 source · when: for analytics events
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p50:3` — “» Segment uses Kafka as their routing backbone for analytics events”

### Kafka topics sh create topic kafka arch

**» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p79:3` — “» Produce a few messages docker exec -it broker /opt/kafka/bin/kafka-console-producer.sh \ --bootstrap-server localhost:9092 \ --topic kafka-arch » Show log docker exec -it broker bash -lc…”

### Offset kappa events kafka

**Kappa Events Kafka log · retained, replayable Stream processor Serving Query one path » One code path – reprocess = replay the log from offset 0 with new code.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p84:15` — “Kappa Events Kafka log · retained, replayable Stream processor Serving Query one path » One code path – reprocess = replay the log from offset 0 with new code”

### Offsets commits lag

**0 – the group committed its offsets, so it continues where it stopped.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-19:1` — “0 – the group committed its offsets, so it continues where it stopped. Now produce 5 messages while nobody reads, then compute the lag = log-end offset − committed offset, per partition.”

### Order kept

**Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-17:1` — “Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed. Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from…”

### Partition broker numbers

**The broker numbers each partition separately, starting at 0, so offset 5 exists in every partition.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p98:3` — “» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic. Are they the same message? What exactly does an offset identify? » No, they are two…”

### Partition consumers read data

**» Consumers read data from a topic » They only have to specify the topic name and one broker to connect to, and Kafka will automatically take care of pulling the data from the right brokers » Data is read in order for each partitions.**
Confidence 0.77 · active · 1 source · when: for each partitions
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p27:3` — “» Consumers read data from a topic » They only have to specify the topic name and one broker to connect to, and Kafka will automatically take care of pulling the data from the right…”

### Partition core works

**A core works on one partition at a time.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p35:11` — “A core works on one partition at a time. More cores → more tasks in parallel – until the data has fewer partitions than you have cores.”

### Partition cores tasks parallel

**More cores → more tasks in parallel – until the data has fewer partitions than you have cores.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p35:11` — “A core works on one partition at a time. More cores → more tasks in parallel – until the data has fewer partitions than you have cores.”

### Partition data partitions high

**Data Partitions for High Throughput.**
Confidence 0.66 · active · 1 source · when: for High Throughput
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p67:3` — “» All Kafka topics consist of one or more partitions » A partition contains a strictly-ordered subset of all of the data in the Topic » Partitions enable Kafka to achieve high throughput”

### Partition exactly offset identify

**What exactly does an offset identify? » No, they are two different messages. » An offset is the sequential position of a record inside one partition.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p98:3` — “» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic. Are they the same message? What exactly does an offset identify? » No, they are two…”

### Partition expected seq intended

**# expected seq … = intended group-a group-b Terminal 3 – same group different group = its own copy C1 + C2 share the 3 partitions of every message ✗ If it fails $ python consumer.py --name C2 ASSIGNED partitions [] → topic not created ✓ Tested on the Mac yet.**
Confidence 0.74 · active · 1 source · when: If it fails $ python consumer
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p95:17` — “# expected seq … = intended group-a group-b Terminal 3 – same group different group = its own copy C1 + C2 share the 3 partitions of every message ✗ If it fails $ python consumer.py --name…”

### Partition expected shape numbers

**Expected shape – numbers per partition depend on the keys.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p93:24` — “Expected shape – numbers per partition depend on the keys. Committed offsets live in __consumer_offsets. · Source: 01_kafka_cli.md”

### Partition kafka cluster composed

**» A Kafka cluster is composed of multiple brokers (servers) » Each broker is identified with its ID (integer) » Each broker contains certain topic partitions » After connecting to any broker (called a bootstrap broker), you will be connected to the entire cluster » A good number to get started is 3 brokers, but some big clusters have over 100 brokers » (Diagram boxes shown: Broker 1, Broker 2, Broker 3).**
Confidence 0.70 · active · 1 source · when: After connecting to any broker (called a bootstrap broker)
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p17:3` — “» A Kafka cluster is composed of multiple brokers (servers) » Each broker is identified with its ID (integer) » Each broker contains certain topic partitions » After connecting to any…”

### Partition message offset

**» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p98:3` — “» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic. Are they the same message? What exactly does an offset identify? » No, they are two…”

### Partition numbers differ

**Your partition numbers may differ – the pattern will not.**
Confidence 0.59 · candidate · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p92:21` — “# Ctrl+C to stop Text before the first : is the key. Your partition numbers may differ – the pattern will not.”

### Partition offset meaning specific

**» Offset only have a meaning for a specific partition. » E.g. offset 3 in partition doesn't represent the same data as offset 3 in partition 1. » Order is guaranteed only within a partition (not across partitions). » Data is kept only for a limited time (default is two weeks). » Once the data is written to a partition, it can't be changed (immutability). » Data is assigned randomly to a partition unless a key is provided (more on this later). » You can have as many partitions per topic as you want.**
Confidence 0.77 · active · 1 source · when: for a specific partition; for a limited time (default is two weeks)
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p16:3` — “» Offset only have a meaning for a specific partition. » E.g. offset 3 in partition doesn't represent the same data as offset 3 in partition 1. » Order is guaranteed only within a…”

### Partition offsets copy message

**Own offsets → its own copy of every message Today's lab result C4 idle – no partition left.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p82:19` — “Own offsets → its own copy of every message Today's lab result C4 idle – no partition left”

### Partition output needs

**Each output partition needs one input partition.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p32:19` — “Each output partition needs one input partition. No network, Every output needs data from all inputs: shuffle = Exchange in same stage. the plan, new stage.”

### Partition rule hash

**» Rule: partition = hash(key) mod number_of_partitions.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p92:3` — “» Rule: partition = hash(key) mod number_of_partitions”

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

### Topic cli demo partitioncount

**Topic: cli-demo PartitionCount: 3 ReplicationFactor: 1 Configs: …segment.bytes=1048576.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p91:19` — “Topic: cli-demo PartitionCount: 3 ReplicationFactor: 1 Configs: …segment.bytes=1048576”

### Topic delete topics stop

**Delete all topics and Stop (keep messages) messages.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p96:5` — “Delete all topics and Stop (keep messages) messages”

### Topic multiple ideas

**If you have multiple topic ideas, we would be happy to add them to the list. » Students are welcome to contact you directly. » Students should upload their application for the assignment of an MA thesis topic - including a completed proposal - by October 31.**
Confidence 0.81 · active · 1 source · when: If you have multiple topic ideas; for the assignment of an MA thesis topic - including a completed proposal - b
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p3:3` — “Feedback Prof. Schwendinger » The full-time faculty members have provided lists of potential topics. » However, these lists are intended merely as inspiration; students are also welcome to…”

### Topic schwendinger full time faculty

**Schwendinger » The full-time faculty members have provided lists of potential topics. » However, these lists are intended merely as inspiration; students are also welcome to propose their own topics.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p3:3` — “Feedback Prof. Schwendinger » The full-time faculty members have provided lists of potential topics. » However, these lists are intended merely as inspiration; students are also welcome to…”

### Topic topics particular stream

**» Topics: a particular stream of data » Similar to a table in a database (without all the constraints) » You can have as many topics as you want » A topic is identified by its name.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p14:3` — “» Topics: a particular stream of data » Similar to a table in a database (without all the constraints) » You can have as many topics as you want » A topic is identified by its name »…”

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
| `session-06/get_kafka.py` | code | 0.80 | 2 | 2026-11-11 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 3 | 2026-11-25 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 10 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 22 | 2026-11-25 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 15 | 2026-11-11 |
| `README.md` | readme | 0.85 | 2 | 2026-11-11 |
| `session-06/producer.py` | code | 0.80 | 2 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 1 | 2026-11-11 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 9 | 2026-11-25 |

## Related Pages

- [[kafka-cluster|Kafka Cluster]] (117 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (111 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (98 shared entities)
- [[kafka-producers|Kafka Producers]] (89 shared entities)
- [[hdfs-architecture|HDFS]] (88 shared entities)
- [[data-formats|File Formats]] (84 shared entities)

## Open Questions

16 prompts from the material are collected in [[questions/kafka-log|Questions: Kafka Log]].
- E2 (1 P) Is a Kafka offset unique within a topic or within a partition?
- Prediction 2: will the three Tirol messages end up in one partition or in different ones?
- Is the output in the order you typed? Which order is guaranteed?

## Timeline

- 2026-11-25: new_claim on `claim_d27c7b7d`
- 2026-11-25: new_claim on `claim_5110465b`
- 2026-11-25: new_claim on `claim_45762961`
- 2026-11-25: new_claim on `claim_af1b58f3`
- 2026-11-25: new_claim on `claim_74fd87ab`
- 2026-11-25: evidence_attached on `claim_74fd87ab` (0.66 → 0.66)
- 2026-11-25: new_claim on `claim_80290f63`
- 2026-11-25: evidence_attached on `claim_80290f63` (0.70 → 0.70)
