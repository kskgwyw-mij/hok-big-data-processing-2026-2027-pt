---
title: Kafka Cluster
type: systems
topic: kafka.cluster
entity_ids:
  - ent_broker
  - ent_kafka
  - ent_isr
  - ent_partition
  - ent_topic
  - ent_kraft
  - ent_docker
  - ent_route
  - ent_plaintext
  - ent_readme
  - ent_zookeeper
  - ent_controller
claim_ids:
  - claim_9e88a2be
  - claim_53496fc3
  - claim_f92824e9
  - claim_0c477e51
  - claim_92b487ef
  - claim_567bee76
  - claim_2aedc4a6
  - claim_063ef7dd
  - claim_83010402
  - claim_5e68579a
  - claim_57484bd1
  - claim_5a71b7fc
  - claim_ecc52249
  - claim_19e7d770
  - claim_5a00e3a8
  - claim_e988a0c0
  - claim_43cbce4b
  - claim_554dceae
  - claim_9e1d77e7
  - claim_a7a586bc
  - claim_c6042067
  - claim_8fd8c7c8
  - claim_e50e2352
  - claim_718e6f59
  - claim_60377287
  - claim_0d7cfce6
  - claim_25aa71e6
  - claim_ad8eb4c3
  - claim_d484f3b4
  - claim_d13bf3c2
  - claim_3e8a2093
  - claim_a3ede20d
  - claim_c8607633
  - claim_107b3832
  - claim_bda738c6
  - claim_fe072d43
  - claim_1c2fb1ef
  - claim_e5c7c705
  - claim_cd2cad94
  - claim_bca5c57a
  - claim_77c05b5b
  - claim_f283eaee
  - claim_2deb6546
  - claim_cc573a04
  - claim_268fed9d
  - claim_cf53da4f
  - claim_3473e7f3
  - claim_be7cf892
  - claim_34ea16fb
  - claim_375bb599
confidence: 0.703
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_41b3a933
  - src_6002d48d
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_cecf99ea
  - src_fc0bfe80
review_required: false
---

# Kafka Cluster

Rendered from 50 claims and 9 sources. Median confidence 0.70; 41 active, 0 disputed, 0 superseded.

## Current Understanding

### Docker compose yml

**Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.**
Confidence 0.83 · active · 3 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p10:3` — “» Topics UI (Landoop): View the topics content » Schema UI (Landoop): Explore the Schema registry » Connect UI (Landoop): Create and monitor Connect tasks » Kafka Manager (Yahoo): Overall…”

**Broker kafka-ui is # optional web UI, only started with --profile ui.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:46` — “kafka-ui: # optional web UI, only started with --profile ui”

**Broker KAFKA_LISTENERS is PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:25` — “KAFKA_LISTENERS: PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093”

**Broker KAFKA_LISTENER_SECURITY_PROTOCOL_MAP is CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:28` — “KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT”

**Broker KAFKA_ADVERTISED_LISTENERS is PLAINTEXT://broker:19092,PLAINTEXT_HOST://localhost:9092.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:26` — “KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://broker:19092,PLAINTEXT_HOST://localhost:9092”

**Broker KAFKA_CONTROLLER_QUORUM_VOTERS is 1@localhost:9093.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:44` — “KAFKA_LOG_SEGMENT_BYTES: 1048576 # 1 MB segments -> several .log files appear quickly”

### Kafka lab exam preparation

**Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.**
Confidence 0.84 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p97:22` — “Another Kafka runs → docker ps, stop it (or stop your Route B port is already allocated broker)”

**Time: 09:00–09:10 — Block: –; What: arrival, broker check (does localhost:9092 answer?); File: this README.**
Confidence 0.81 · active · 2 sources
Evidence: `session-06/README.md:8` — “09:00–09:10 | – | arrival, broker check (does localhost:9092 answer?) | this README”

**Symptom: UnknownTopicOrPartitionError / topic does not exist — Fix: Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:116` — “UnknownTopicOrPartitionError / topic does not exist | Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself”

**Symptom: Broker refuses to start after changing the Kafka version — Fix: python get_kafka.py --reformat.**
Confidence 0.69 · active · 1 source · when: after changing the Kafka version — Fix: python get_kafka
Evidence: `session-06/README.md:114` — “Broker refuses to start after changing the Kafka version | python get_kafka.py --reformat”

**File: docker-compose.yml — What: Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:127` — “docker-compose.yml | Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI”

### Create topic partitions

**Column: Replicas — Meaning: all brokers that keep a copy (here only broker 1).**
Confidence 0.90 · active · 2 sources
Evidence: `session-06/01_kafka_cli.md:89` — “Replicas | all brokers that keep a copy (here only broker 1)”

**Column: Leader — Meaning: id of the broker that handles reads and writes for this partition.**
Confidence 0.84 · active · 2 sources · when: for this partition
Evidence: `session-06/01_kafka_cli.md:88` — “Leader | id of the broker that handles reads and writes for this partition”

**Column: Isr — Meaning: in-sync replicas: the copies that are fully up to date. Only these can become the new leader without losing data.**
Confidence 0.80 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:90` — “Isr | in-sync replicas: the copies that are fully up to date. Only these can become the new leader without losing data”

### Get kafka

**Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python get_kafka.py --reformat # wipe the data folder and format again (after a version change) python get_kafka.py --dest ~/kafka-course # install somewhere else (path without spaces).**
Confidence 0.52 · candidate · 1 source · when: after a version change) python get_kafka
Evidence: `session-06/get_kafka.py:1` — “Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python…”

**Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.**
Confidence 0.52 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.”

### Route native kafka docker

**Leave that terminal open – Ctrl+C stops the broker.**
Confidence 0.80 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p88:18` — “# leave this terminal open – Ctrl+C stops the broker”

**Cd session-06 ; python get_kafka.py --start # downloads Kafka 4.4.0 (~130 MB), checks the SHA-512, formats storage, starts the broker.**
Confidence 0.72 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p88:10` — “$ java -version # needs 17 or newer $ cd session-06 Path contains a space? $ python get_kafka.py --start e.g. "… Kopie" → error Classpath is empty # downloads Kafka 4.4.0 (~130 MB), checks…”

### Broker

**If this cell fails with Unable to bootstrap / KafkaTimeoutError: the broker is not running → README.md, Check the broker.**
Confidence 0.74 · active · 2 sources · when: If this cell fails with Unable to bootstrap / KafkaTimeoutError: the bro
Evidence: `session-06/02_kafka_python.ipynb#cell-1:2` — “If this cell fails with Unable to bootstrap / KafkaTimeoutError: the broker is not running → README.md, Check the broker.”

### Broker brokers building blocks

**» Brokers are the building blocks of Kafka.**
Confidence 0.71 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p63:3` — “» Brokers are the building blocks of Kafka”

### Broker cli kafka cli md

**09:25 Block 1 · Broker & CLI 01_kafka_cli.md LAB.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p3:13` — “09:25 Block 1 · Broker & CLI 01_kafka_cli.md LAB”

### Broker clusters contain brokers

**Clusters contain 1 or more Brokers.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p64:3` — “» Brokers are organized into clusters. Clusters contain 1 or more Brokers.”

### Broker fails name image

**✓ What you should see ✓ What you should see ✗ If it fails NAME IMAGE … STATUS A list, maybe empty: [] KafkaTimeoutError: Unable to bootstrap broker apache/kafka:4.4.0 … Up.**
Confidence 0.71 · active · 1 source · when: If it fails NAME IMAGE … STATUS A list
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p89:12` — “✓ What you should see ✓ What you should see ✗ If it fails NAME IMAGE … STATUS A list, maybe empty: [] KafkaTimeoutError: Unable to bootstrap broker apache/kafka:4.4.0 … Up”

### Broker kafka stores data

**» Kafka stores all of its data in a directory on the broker disk.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p66:3` — “» Kafka stores all of its data in a directory on the broker disk”

### Broker lag give possible

**What is the lag, and give two possible reasons why it is growing. » Your laptop has one broker.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p100:3` — “» Define offset. Is an offset unique within a topic or within a partition? » A topic has 3 partitions. Messages with the key Tirol always arrive in the order they were produced, but…”

### Broker laptop replication factor

**Your laptop: 1 broker → --replication-factor 2 → InvalidReplicationFactorException.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p83:21` — “Your laptop: 1 broker → --replication-factor 2 → InvalidReplicationFactorException”

### Broker leader handles

**Leader – broker that handles reads & Replicas – all brokers keeping a Elr / LastKnownElr – new in Kafka Isr – in-sync, fully up-to-date copies writes copy 4, ignore.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p91:29` — “Leader – broker that handles reads & Replicas – all brokers keeping a Elr / LastKnownElr – new in Kafka Isr – in-sync, fully up-to-date copies writes copy 4, ignore”

### Broker replicas store copy

**» Replicas store a copy of the leader's data, in case the broker is lost.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p74:3` — “» Replicas store a copy of the leader's data, in case the broker is lost”

### Broker replication data written

**» With replication, data is written to multiple brokers, not just the leader.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p72:3` — “» With replication, data is written to multiple brokers, not just the leader”

### Broker step start

**Step 4A - Start the broker · Step 5 - Check it.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p89:1` — “Step 4A - Start the broker · Step 5 - Check it”

### Broker tells clients

**The broker tells clients to use localhost – connecting to their laptop from yours won't work.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p89:17` — “Broker not running or not on 9092 ✗ If it fails no configuration file provided: not found → repo root: cd session-06, then up -d again Nothing works? Cannot connect to the Docker daemon →…”

### Consumer

**Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.**
Confidence 0.58 · candidate · 1 source · when: after 10 s without new messages
Evidence: `session-06/consumer.py:1` — “Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a…”

### Consumer groups real processes terminal

**Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.**
Confidence 0.87 · active · 2 sources
Evidence: `session-06/01_kafka_cli.md:172` — “docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group cli-group | kafka-consumer-groups.sh --bootstrap-server localhost:9092…”

### Create topic idempotently

**Our broker has auto.create.topics.enable=false: a typo in a topic name gives an error instead of a new, empty topic.**
Confidence 0.67 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-3:5` — “Our broker has auto.create.topics.enable=false: a typo in a topic name gives an error instead of a new, empty topic.”

### Kafka broker command line tools

**You need a running broker (README.md → Before the session).**
Confidence 0.63 · active · 1 source · when: Before the session)
Evidence: `session-06/01_kafka_cli.md:7` — “You need a running broker (README.md → Before the session). Work in pairs: one types, one predicts – swap after each part.”

### Kafka lab

**Session 6 runs a real Kafka broker on your laptop.**
Confidence 0.74 · active · 2 sources
Evidence: `README.md:103` — “Session 6 runs a real Kafka broker on your laptop. Set it up at home before the session – full instructions, broker check and troubleshooting: session-06/README.md.”

### Kafka topics sh delete topic docker

**» Delete topic docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --delete --topic my-first-topic.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p59:3` — “» Delete topic docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --delete --topic my-first-topic”

### Kafka x apachezookeeper

**» Kafka 3.x: ApacheZookeeper is used to track cluster state, membership and leadership » Kafka 4.x: Kafka itself tracks cluster state, membership and leadership with Kafka Raft Metadata mode (KRaft).**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p65:3` — “» Kafka 3.x: ApacheZookeeper is used to track cluster state, membership and leadership » Kafka 4.x: Kafka itself tracks cluster state, membership and leadership with Kafka Raft Metadata…”

### Keyed producer

**Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.**
Confidence 0.70 · active · 1 source · when: when the write is complete on all in-sync replicas; for that answer and returns where the message went: partition and offset
Evidence: `session-06/02_kafka_python.ipynb#cell-7:2` — “acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.”

### Kraft recap replication isr

**Recap 3 · Replication, ISR and KRaft.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p83:1` — “Recap 3 · Replication, ISR and KRaft”

### Laptop cannot run route

**No problem: pair up with a neighbour whose broker runs.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-06/README.md:84` — “No problem: pair up with a neighbour whose broker runs. You type on their laptop in Block 1 and run consumer.py on theirs in Block 2. Everything in Blocks 3 and 4 needs only paper.…”

### Never commit

**The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka download and broker data from Session 6 (session-06/kafka_2.13-*/, session-06/kafka-data/).**
Confidence 0.63 · active · 1 source
Evidence: `README.md:141` — “data/, .venv/, executed notebooks with large outputs, or files with personal information. The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka…”

### Partition election complete leads

**» When election is complete we have new leads per broker and partition.**
Confidence 0.66 · active · 1 source · when: When election is complete we have new leads per broker and partition
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p76:3` — “» When election is complete we have new leads per broker and partition”

### Partition leader sends

**» The leader of a partition sends data and coordinates client interactions.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p73:3` — “» The leader of a partition sends data and coordinates client interactions”

### Partition partitions typically distributed

**» Partitions are typically distributed evenly amongst brokers.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p68:3` — “» Partitions are typically distributed evenly amongst brokers”

### Partition production brokers leader

**In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails? » A colleague increases a topic from 3 to 6 partitions to get more throughput.**
Confidence 0.74 · active · 1 source · when: when the leader broker fails? » A colleague increases a topic from 3 to 6
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p100:3` — “» Define offset. Is an offset unique within a topic or within a partition? » A topic has 3 partitions. Messages with the key Tirol always arrive in the order they were produced, but…”

### Replication factor leader broker

**» Leader broker fails → controller elects a new leader from the ISR followers copy the leader · ISR = {1, 2, 3} » Replication factor ≤ number of brokers.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p83:16` — “» Leader broker fails → controller elects a new leader from the ISR followers copy the leader · ISR = {1, 2, 3} » Replication factor ≤ number of brokers”

### Stop clean

**In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).**
Confidence 0.86 · active · 2 sources · when: if you used it); if you used it kafbat/kafka-ui v1
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p96:17` — “Open http://localhost:8080 Route B – python get_kafka.py --reformat Ctrl+C in the broker terminal native plus --dest … if you used it kafbat/kafka-ui v1.5.0 · another ~220 MB download”

### Zookeeper kraft controllers metadata

**KRaft controllers · metadata + leader election · replace ZooKeeper » Leader – handles all reads & writes of a partition.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p83:7` — “KRaft controllers · metadata + leader election · replace ZooKeeper » Leader – handles all reads & writes of a partition”

### Zookeeper leader broker lost

**» When a leader broker is lost, a new leader is elected (with Zookeeper).**
Confidence 0.66 · active · 1 source · when: When a leader broker is lost
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p75:3` — “» When a leader broker is lost, a new leader is elected (with Zookeeper)”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/get_kafka.py` | code | 0.80 | 2 | 2026-11-11 |
| `session-06/docker-compose.yml` | config | 0.75 | 6 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 4 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 18 | 2026-11-25 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 5 | 2026-11-11 |
| `README.md` | readme | 0.85 | 2 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 1 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 11 | 2026-11-11 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 13 | 2026-11-25 |

## Related Pages

- [[kafka-log|Kafka Log]] (102 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (93 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (91 shared entities)
- [[hdfs-architecture|HDFS]] (85 shared entities)
- [[kafka-producers|Kafka Producers]] (85 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (82 shared entities)

## Open Questions

7 prompts from the material are collected in [[questions/kafka-cluster|Questions: Kafka Cluster]].
- E1 (1 P) What does Kafka 4 use instead of ZooKeeper to manage cluster metadata?
- E5 (2 P) Replication factor 3: what is the ISR, and what happens when the leader of a partition fails?
- Broker not running or not on 9092 ✗ If it fails no configuration file provided: not found → repo root: cd session-06, then up -d again…

## Timeline

- 2026-11-25: new_claim on `claim_cc573a04`
- 2026-11-25: new_claim on `claim_268fed9d`
- 2026-11-25: support_update on `claim_19e7d770` (0.74 → 0.84)
- 2026-11-25: new_claim on `claim_cf53da4f`
- 2026-11-25: new_claim on `claim_3473e7f3`
- 2026-11-25: new_claim on `claim_be7cf892`
- 2026-11-25: new_claim on `claim_34ea16fb`
- 2026-11-25: new_claim on `claim_375bb599`
