---
title: broker
type: entity
entity_id: ent_broker
entity_type: concept
claim_ids:
  - claim_37399599
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
  - claim_64fbe26b
  - claim_c9e8d488
  - claim_beb90ba1
  - claim_0efcddb6
  - claim_ecc52249
  - claim_19e7d770
  - claim_5a00e3a8
  - claim_43cbce4b
  - claim_bc86de96
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
confidence: 0.672
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_6002d48d
  - src_6e2e5684
  - src_799c8bd7
  - src_8e87808f
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_bb056c24
  - src_cecf99ea
---

# broker

Type: concept. Mentioned in 35 claims across 7 topics.
Aliases: brokers.

## Claims

- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **Runs locally with your .venv kernel.** Confidence 0.80 · [[python-environments|Python Environments and Reproducibility]]
- **Column: Replicas — Meaning: all brokers that keep a copy (here only broker 1).** Confidence 0.80 · [[kafka-cluster|Kafka Cluster]]
- **If this cell fails with Unable to bootstrap / KafkaTimeoutError: the broker is not running → README.md, Check the broker.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **Column: Leader — Meaning: id of the broker that handles reads and writes for this partition.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **Session 6 runs a real Kafka broker on your laptop.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.73 · [[tooling-docker|Docker and Dev Containers]]
- **Acks="all": the broker answers only when the write is complete on all in-sync replicas. .get(timeout=10) waits for that answer and returns where the message went: partition and offset.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Time: 09:00–09:10 — Block: –; What: arrival, broker check (does localhost:9092 answer?); File: this README.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: UnknownTopicOrPartitionError / topic does not exist — Fix: Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: Broker refuses to start after changing the Kafka version — Fix: python get_kafka.py --reformat.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **File: docker-compose.yml — What: Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.69 · [[course-exam|Exam]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Our broker has auto.create.topics.enable=false: a typo in a topic name gives an error instead of a new, empty topic.** Confidence 0.67 · [[kafka-cluster|Kafka Cluster]]
- **You need a running broker (README.md → Before the session).** Confidence 0.63 · [[kafka-cluster|Kafka Cluster]]
- **The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka download and broker data from Session 6 (session-06/kafka_2.13-*/, session-06/kafka-data/).** Confidence 0.63 · [[kafka-cluster|Kafka Cluster]]
- **Leave that terminal open – Ctrl+C stops the broker.** Confidence 0.63 · [[kafka-cluster|Kafka Cluster]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.62 · [[tooling-docker|Docker and Dev Containers]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **No problem: pair up with a neighbour whose broker runs.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is where your messages live on disk.** Confidence 0.57 · [[kafka-cluster|Kafka Cluster]]
- **Broker kafka-ui is # optional web UI, only started with --profile ui.** Confidence 0.56 · [[kafka-cluster|Kafka Cluster]]
- **Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python get_kafka.py --reformat # wipe the data folder and format again (after a version change) python get_kafka.py --dest ~/kafka-course # install somewhere else (path without spaces).** Confidence 0.52 · [[kafka-cluster|Kafka Cluster]]
- **Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.** Confidence 0.52 · [[kafka-cluster|Kafka Cluster]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py --count 30 --interval 0.2 python producer.py --no-key # same events, but WITHOUT a key python producer.py --data users --topic registered_user # the original lab: fake users, no key.** Confidence 0.50 · [[kafka-producers|Kafka Producers]]
- **Cd session-06 ; python get_kafka.py --start # downloads Kafka 4.4.0 (~130 MB), checks the SHA-512, formats storage, starts the broker.** Confidence 0.48 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_LISTENERS is PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_LISTENER_SECURITY_PROTOCOL_MAP is CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_ADVERTISED_LISTENERS is PLAINTEXT://broker:19092,PLAINTEXT_HOST://localhost:9092.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_CONTROLLER_QUORUM_VOTERS is 1@localhost:9093.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]

## Related Entities

- [[kafka|Kafka]] (23)
- [[topic|topic]] (9)
- [[docker|Docker]] (7)
- [[partition|partition]] (4)
- [[venv|venv]] (3)
- [[kraft|KRaft]] (2)
- [[consumer_group|consumer group]] (2)
- [[docker_compose|docker compose]] (2)
- [[kafka_topics_sh|kafka-topics.sh]] (2)
- [[offset|offset]] (2)
