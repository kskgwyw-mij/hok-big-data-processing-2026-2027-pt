---
title: broker
type: entity
entity_id: ent_broker
entity_type: concept
claim_ids:
  - claim_37399599
  - claim_9e88a2be
  - claim_aea8344c
  - claim_53496fc3
  - claim_f92824e9
  - claim_0c477e51
  - claim_92b487ef
  - claim_567bee76
  - claim_2aedc4a6
  - claim_063ef7dd
  - claim_44c56793
  - claim_83010402
  - claim_5e68579a
  - claim_57484bd1
  - claim_5a71b7fc
  - claim_c9e8d488
  - claim_beb90ba1
  - claim_0efcddb6
  - claim_ecc52249
  - claim_19e7d770
  - claim_5a00e3a8
  - claim_43cbce4b
  - claim_c8c19737
  - claim_554dceae
  - claim_9e1d77e7
  - claim_5aae3a4d
  - claim_a7a586bc
  - claim_c6042067
  - claim_8fd8c7c8
  - claim_e50e2352
  - claim_718e6f59
  - claim_60377287
  - claim_0d7cfce6
  - claim_25aa71e6
  - claim_42099051
  - claim_ad8eb4c3
  - claim_d484f3b4
  - claim_d13bf3c2
  - claim_e8488930
  - claim_1833931d
  - claim_3e8a2093
  - claim_c8607633
  - claim_107b3832
  - claim_fe072d43
  - claim_1c2fb1ef
  - claim_e5c7c705
  - claim_cd2cad94
  - claim_8cd2ba0b
  - claim_1c849616
  - claim_bca5c57a
  - claim_77c05b5b
  - claim_f283eaee
  - claim_cc573a04
  - claim_268fed9d
  - claim_cf53da4f
  - claim_be7cf892
  - claim_34ea16fb
  - claim_375bb599
  - claim_c6cd6bf4
  - claim_80290f63
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_41b3a933
  - src_6002d48d
  - src_6e2e5684
  - src_799c8bd7
  - src_8615b91f
  - src_8e87808f
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_bb056c24
  - src_cecf99ea
  - src_fc0bfe80
---

# broker

Type: concept. Mentioned in 60 claims across 7 topics.
Aliases: brokers.

## Claims

- **Column: Replicas — Meaning: all brokers that keep a copy (here only broker 1).** Confidence 0.90 · [[kafka-cluster|Kafka Cluster]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).** Confidence 0.86 · [[kafka-cluster|Kafka Cluster]]
- **Column: Leader — Meaning: id of the broker that handles reads and writes for this partition.** Confidence 0.84 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.** Confidence 0.84 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]
- **Time: 09:00–09:10 — Block: –; What: arrival, broker check (does localhost:9092 answer?); File: this README.** Confidence 0.81 · [[kafka-cluster|Kafka Cluster]]
- **Each key appears in exactly one partition: partition = hash(key) mod 3.** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **Runs locally with your .venv kernel.** Confidence 0.80 · [[python-environments|Python Environments and Reproducibility]]
- **Leave that terminal open – Ctrl+C stops the broker.** Confidence 0.80 · [[kafka-cluster|Kafka Cluster]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.80 · [[tooling-docker|Docker and Dev Containers]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.80 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **» Consumers read data from a topic » They only have to specify the topic name and one broker to connect to, and Kafka will automatically take care of pulling the data from the right brokers » Data is read in order for each partitions.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **What is the lag, and give two possible reasons why it is growing. » Your laptop has one broker.** Confidence 0.76 · [[kafka-cluster|Kafka Cluster]]
- **If this cell fails with Unable to bootstrap / KafkaTimeoutError: the broker is not running → README.md, Check the broker.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails? » A colleague increases a topic from 3 to 6 partitions to get more throughput.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **Session 6 runs a real Kafka broker on your laptop.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **Cd session-06 ; python get_kafka.py --start # downloads Kafka 4.4.0 (~130 MB), checks the SHA-512, formats storage, starts the broker.** Confidence 0.72 · [[kafka-cluster|Kafka Cluster]]
- **✓ What you should see ✓ What you should see ✗ If it fails NAME IMAGE … STATUS A list, maybe empty: [] KafkaTimeoutError: Unable to bootstrap broker apache/kafka:4.4.0 … Up.** Confidence 0.71 · [[kafka-cluster|Kafka Cluster]]
- **» Brokers are the building blocks of Kafka.** Confidence 0.71 · [[kafka-cluster|Kafka Cluster]]
- **» Default number of replicas can be configured globally » Can't have more replicas than you have brokers » Data replication incurs some overhead » Always enable replication in a Production cluster » Outside your laptop use a replication factor > 1 than to prevent data loss.** Confidence 0.71 · [[hdfs-architecture|HDFS]]
- **Your laptop: 1 broker → --replication-factor 2 → InvalidReplicationFactorException.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **The broker numbers each partition separately, starting at 0, so offset 5 exists in every partition.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Partitions are typically distributed evenly amongst brokers.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **09:25 Block 1 · Broker & CLI 01_kafka_cli.md LAB.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Delete topic docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --delete --topic my-first-topic.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Replicas store a copy of the leader's data, in case the broker is lost.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Leader broker fails → controller elects a new leader from the ISR followers copy the leader · ISR = {1, 2, 3} » Replication factor ≤ number of brokers.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» Kafka stores all of its data in a directory on the broker disk.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Leader – broker that handles reads & Replicas – all brokers keeping a Elr / LastKnownElr – new in Kafka Isr – in-sync, fully up-to-date copies writes copy 4, ignore.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» With replication, data is written to multiple brokers, not just the leader.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **The broker tells clients to use localhost – connecting to their laptop from yours won't work.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» A Kafka cluster is composed of multiple brokers (servers) » Each broker is identified with its ID (integer) » Each broker contains certain topic partitions » After connecting to any broker (called a bootstrap broker), you will be connected to the entire cluster » A good number to get started is 3 brokers, but some big clusters have over 100 brokers » (Diagram boxes shown: Broker 1, Broker 2, Broker 3).** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Step 4A - Start the broker · Step 5 - Check it.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **{"state": "Tirol", "seq": 1, serializer broker deserializer "action": "login"} JsonSerializer() bytes localhost:9092 JsonSerializer() dict.** Confidence 0.70 · [[kafka-producers|Kafka Producers]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: UnknownTopicOrPartitionError / topic does not exist — Fix: Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: Broker refuses to start after changing the Kafka version — Fix: python get_kafka.py --reformat.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **File: docker-compose.yml — What: Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Our broker has auto.create.topics.enable=false: a typo in a topic name gives an error instead of a new, empty topic.** Confidence 0.67 · [[kafka-cluster|Kafka Cluster]]
- **» When a leader broker is lost, a new leader is elected (with Zookeeper).** Confidence 0.66 · [[kafka-cluster|Kafka Cluster]]
- **» When election is complete we have new leads per broker and partition.** Confidence 0.66 · [[kafka-cluster|Kafka Cluster]]
- **Clusters contain 1 or more Brokers.** Confidence 0.66 · [[kafka-cluster|Kafka Cluster]]
- **You need a running broker (README.md → Before the session).** Confidence 0.63 · [[kafka-cluster|Kafka Cluster]]
- **The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka download and broker data from Session 6 (session-06/kafka_2.13-*/, session-06/kafka-data/).** Confidence 0.63 · [[kafka-cluster|Kafka Cluster]]
- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.59 · [[tooling-docker|Docker and Dev Containers]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **No problem: pair up with a neighbour whose broker runs.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is where your messages live on disk.** Confidence 0.57 · [[kafka-log|Kafka Log]]
- **Broker kafka-ui is # optional web UI, only started with --profile ui.** Confidence 0.56 · [[kafka-cluster|Kafka Cluster]]
- **Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python get_kafka.py --reformat # wipe the data folder and format again (after a version change) python get_kafka.py --dest ~/kafka-course # install somewhere else (path without spaces).** Confidence 0.52 · [[kafka-cluster|Kafka Cluster]]
- **Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.** Confidence 0.52 · [[kafka-cluster|Kafka Cluster]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py --count 30 --interval 0.2 python producer.py --no-key # same events, but WITHOUT a key python producer.py --data users --topic registered_user # the original lab: fake users, no key.** Confidence 0.50 · [[kafka-producers|Kafka Producers]]
- **Broker KAFKA_LISTENERS is PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_LISTENER_SECURITY_PROTOCOL_MAP is CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_ADVERTISED_LISTENERS is PLAINTEXT://broker:19092,PLAINTEXT_HOST://localhost:9092.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_CONTROLLER_QUORUM_VOTERS is 1@localhost:9093.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]

## Related Entities

- [[kafka|Kafka]] (32)
- [[topic|topic]] (16)
- [[partition|partition]] (13)
- [[docker|Docker]] (10)
- [[isr|ISR]] (5)
- [[kafka_topics_sh|kafka-topics.sh]] (5)
- [[offset|offset]] (4)
- [[lag|lag]] (3)
- [[venv|venv]] (3)
- [[kraft|KRaft]] (2)
