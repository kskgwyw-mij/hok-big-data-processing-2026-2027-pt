---
title: Kafka Cluster
type: systems
topic: kafka.cluster
entity_ids:
  - ent_broker
  - ent_kafka
  - ent_topic
  - ent_route
  - ent_plaintext
  - ent_readme
  - ent_controller
  - ent_docker
  - ent_kraft
  - ent_docker_compose
  - ent_git
  - ent_isr
claim_ids:
  - claim_9e88a2be
  - claim_53496fc3
  - claim_83148947
  - claim_f92824e9
  - claim_0c477e51
  - claim_92b487ef
  - claim_567bee76
  - claim_2aedc4a6
  - claim_063ef7dd
  - claim_83010402
  - claim_5e68579a
  - claim_57484bd1
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
confidence: 0.627
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_6002d48d
  - src_799c8bd7
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_cecf99ea
review_required: false
---

# Kafka Cluster

Rendered from 28 claims and 7 sources. Median confidence 0.63; 16 active, 0 disputed, 0 superseded.

## Current Understanding

### Docker compose yml

**Broker kafka-ui is # optional web UI, only started with --profile ui.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:46` — “kafka-ui: # optional web UI, only started with --profile ui”

**Broker KAFKA_LISTENERS is PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:25` — “KAFKA_LISTENERS: PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093”

**Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/docker-compose.yml:42` — “KAFKA_AUTO_CREATE_TOPICS_ENABLE: "false" # you create topics yourself”

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

**Time: 09:00–09:10 — Block: –; What: arrival, broker check (does localhost:9092 answer?); File: this README.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:8` — “09:00–09:10 | – | arrival, broker check (does localhost:9092 answer?) | this README”

**Symptom: UnknownTopicOrPartitionError / topic does not exist — Fix: Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:116` — “UnknownTopicOrPartitionError / topic does not exist | Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself”

**Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:111` — “port is already allocated (9092 or 8080) | Another Kafka is running: docker ps, stop it – or stop your Route B broker”

**Symptom: Broker refuses to start after changing the Kafka version — Fix: python get_kafka.py --reformat.**
Confidence 0.69 · active · 1 source · when: after changing the Kafka version — Fix: python get_kafka
Evidence: `session-06/README.md:114` — “Broker refuses to start after changing the Kafka version | python get_kafka.py --reformat”

**File: docker-compose.yml — What: Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:127` — “docker-compose.yml | Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI”

### Create topic partitions

**Column: Replicas — Meaning: all brokers that keep a copy (here only broker 1).**
Confidence 0.80 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:89` — “Replicas | all brokers that keep a copy (here only broker 1)”

**Column: Isr — Meaning: in-sync replicas: the copies that are fully up to date. Only these can become the new leader without losing data.**
Confidence 0.80 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:90` — “Isr | in-sync replicas: the copies that are fully up to date. Only these can become the new leader without losing data”

**Column: Leader — Meaning: id of the broker that handles reads and writes for this partition.**
Confidence 0.74 · active · 1 source · when: for this partition
Evidence: `session-06/01_kafka_cli.md:88` — “Leader | id of the broker that handles reads and writes for this partition”

### Get kafka

**What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is where your messages live on disk.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is…”

**Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python get_kafka.py --reformat # wipe the data folder and format again (after a version change) python get_kafka.py --dest ~/kafka-course # install somewhere else (path without spaces).**
Confidence 0.52 · candidate · 1 source · when: after a version change) python get_kafka
Evidence: `session-06/get_kafka.py:1` — “Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python…”

**Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.**
Confidence 0.52 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.”

### Route native kafka docker

**Leave that terminal open – Ctrl+C stops the broker.**
Confidence 0.63 · active · 1 source
Evidence: `session-06/README.md:67` — “Leave that terminal open – Ctrl+C stops the broker. Next time just run python get_kafka.py --start again.”

**Cd session-06 ; python get_kafka.py --start # downloads Kafka 4.4.0 (~130 MB), checks the SHA-512, formats storage, starts the broker.**
Confidence 0.48 · candidate · 1 source
Evidence: `session-06/README.md:63` — “cd session-06 ; python get_kafka.py --start # downloads Kafka 4.4.0 (~130 MB), checks the SHA-512, formats storage, starts the broker”

### Broker

**If this cell fails with Unable to bootstrap / KafkaTimeoutError: the broker is not running → README.md, Check the broker.**
Confidence 0.74 · active · 2 sources · when: If this cell fails with Unable to bootstrap / KafkaTimeoutError: the bro
Evidence: `session-06/02_kafka_python.ipynb#cell-1:2` — “If this cell fails with Unable to bootstrap / KafkaTimeoutError: the broker is not running → README.md, Check the broker.”

### Consumer

**Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.**
Confidence 0.58 · candidate · 1 source · when: after 10 s without new messages
Evidence: `session-06/consumer.py:1` — “Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a…”

### Consumer groups real processes terminal

**Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.**
Confidence 0.87 · active · 2 sources
Evidence: `session-06/01_kafka_cli.md:50` — “docker exec -it broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list | kafka-topics.sh --bootstrap-server localhost:9092 --list”

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

### Laptop cannot run route

**No problem: pair up with a neighbour whose broker runs.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-06/README.md:84` — “No problem: pair up with a neighbour whose broker runs. You type on their laptop in Block 1 and run consumer.py on theirs in Block 2. Everything in Blocks 3 and 4 needs only paper.…”

### Never commit

**The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka download and broker data from Session 6 (session-06/kafka_2.13-*/, session-06/kafka-data/).**
Confidence 0.63 · active · 1 source
Evidence: `README.md:141` — “data/, .venv/, executed notebooks with large outputs, or files with personal information. The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka…”

### Stop clean

**In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).**
Confidence 0.69 · active · 1 source · when: if you used it)
Evidence: `session-06/README.md:95` — “Route B | Ctrl+C in the broker terminal | python get_kafka.py --reformat (plus --dest … if you used it)”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/get_kafka.py` | code | 0.80 | 3 | 2026-11-11 |
| `session-06/docker-compose.yml` | config | 0.75 | 6 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 3 | 2026-11-11 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 5 | 2026-11-11 |
| `README.md` | readme | 0.85 | 2 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 1 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 11 | 2026-11-11 |

## Related Pages

- [[kafka-log|Kafka Log]] (58 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (55 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (55 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (54 shared entities)
- [[course-exam|Exam]] (53 shared entities)
- [[kafka-producers|Kafka Producers]] (53 shared entities)

## Open Questions

5 prompts from the material are collected in [[questions/kafka-cluster|Questions: Kafka Cluster]].
- (4 P) Your laptop has one broker. Why does --replication-factor 2 fail? In production with 3 brokers, what do Leader, Replicas and Isr…
- What changes in Isr if one broker crashes?
- 6.2 (4 P) Topic payments has 4 partitions, replication factor 3 on 3 brokers. (a) Group fraud runs 6 consumers, group dashboard runs 1…

## Timeline

- 2026-11-25: new_claim on `claim_e50e2352`
- 2026-11-25: support_update on `claim_43cbce4b` (0.63 → 0.74)
- 2026-11-25: new_claim on `claim_718e6f59`
- 2026-11-25: new_claim on `claim_60377287`
- 2026-11-25: new_claim on `claim_0d7cfce6`
- 2026-11-25: support_update on `claim_83010402` (0.64 → 0.74)
- 2026-11-25: new_claim on `claim_25aa71e6`
- 2026-11-25: new_claim on `claim_ad8eb4c3`
