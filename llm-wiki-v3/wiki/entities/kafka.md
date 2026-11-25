---
title: Kafka
type: entity
entity_id: ent_kafka
entity_type: technology
claim_ids:
  - claim_f0092822
  - claim_9e88a2be
  - claim_3eb495fc
  - claim_53496fc3
  - claim_83148947
  - claim_68d8d358
  - claim_9d2b15fd
  - claim_2ee83bfc
  - claim_f92824e9
  - claim_0c477e51
  - claim_92b487ef
  - claim_567bee76
  - claim_2aedc4a6
  - claim_063ef7dd
  - claim_64a2b1df
  - claim_cc58f4f3
  - claim_95f17588
  - claim_eefecc93
  - claim_5e68579a
  - claim_c9e94a4c
  - claim_d963daba
  - claim_b5c89f2e
  - claim_c9e8d488
  - claim_4eec96d9
  - claim_beb90ba1
  - claim_a6c2c236
  - claim_f74f1f65
  - claim_0efcddb6
  - claim_018c1927
  - claim_5a00e3a8
  - claim_9303be70
  - claim_43cbce4b
  - claim_4c4d2c23
  - claim_64fbf0f7
  - claim_67369049
  - claim_bc86de96
  - claim_554dceae
  - claim_8b05e9fa
  - claim_54ade2b0
  - claim_1e9bcc33
  - claim_e6c671ef
  - claim_a7a586bc
  - claim_c6042067
  - claim_1d96ae1a
  - claim_8b538216
  - claim_e50e2352
  - claim_52c68d00
  - claim_9d5713e1
  - claim_dc16bc08
  - claim_6a889182
  - claim_b73468f4
  - claim_98cdf12b
  - claim_718e6f59
  - claim_e467c9d5
  - claim_3eea2cc1
  - claim_42099051
  - claim_ad8eb4c3
  - claim_719c08d9
  - claim_a6d89a64
  - claim_3be1dead
  - claim_ac59fce7
confidence: 0.66
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_41b3a933
  - src_6002d48d
  - src_799c8bd7
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_bb056c24
  - src_c65c80a3
  - src_cecf99ea
  - src_d56cb0d7
  - src_f8b034ea
---

# Kafka

Type: technology. Mentioned in 61 claims across 13 topics.
Aliases: Apache Kafka, kafka-python, KafkaProducer, KafkaConsumer, KafkaAdminClient.

## Claims

- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **Column: Replicas — Meaning: all brokers that keep a copy (here only broker 1).** Confidence 0.80 · [[kafka-cluster|Kafka Cluster]]
- **Open this notebook from the session-06/ folder – it imports kafka_data.py from there.** Confidence 0.78 · [[tooling-kaggle|Kaggle Labs]]
- **Route B fails if the folder path contains a space (e.g. … Kopie or My Projects). get_kafka.py checks this and stops – then install Kafka somewhere else: python get_kafka.py --dest ~/kafka-course --start.** Confidence 0.78 · [[course-setup|Course Setup]]
- **Part: E — Topic: Kafka and streaming; Points: 10.** Confidence 0.75 · [[course-exam|Exam]]
- **Folder: (Session 5 – no folder) — Topic: Stream processing with Kafka – theory: events, append-only logs, topics and partitions, replication, KRaft; Runs on: Kaggle.** Confidence 0.75 · [[kafka-log|Kafka Log]]
- **File: get_kafka.py — What: Route B: downloads and prepares native Kafka 4.4.0 (standard library only).** Confidence 0.74 · [[course-setup|Course Setup]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **Session 6 runs a real Kafka broker on your laptop.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **Experiment 1 – one producer, one consumer.** Confidence 0.73 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.73 · [[tooling-docker|Docker and Dev Containers]]
- **Uv init --python 3.12 ; uv add pandas duckdb.** Confidence 0.72 · [[engines-single_machine|Single-Machine Engines]]
- **Older Kafka versions and many tutorials write --property instead of --reader-property.** Confidence 0.71 · [[kafka-log|Kafka Log]]
- **Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.** Confidence 0.71 · [[tooling-docker|Docker and Dev Containers]]
- **Kafka only stores bytes (Block 1, the hex dump).** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Key and value are just bytes for Kafka. Who turns them back into text or JSON? (→ Block 2: deserializer).** Confidence 0.69 · [[kafka-producers|Kafka Producers]]
- **Library: kafka-python ≥ 3.0 — Why: pure-Python Kafka client (version 2.0.2 from older tutorials does not work on Python 3.12).** Confidence 0.69 · [[python-environments|Python Environments and Reproducibility]]
- **File: requirements-local.txt — Contains: pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6); Use it for: your laptop (default).** Confidence 0.69 · [[engines-single_machine|Single-Machine Engines]]
- **Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: Broker refuses to start after changing the Kafka version — Fix: python get_kafka.py --reformat.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **File: 01_kafka_cli.md — What: Block 1 – step by step, both routes.** Confidence 0.69 · [[hdfs-architecture|HDFS]]
- **File: docker-compose.yml — What: Route A: one Kafka 4.4.0 broker (KRaft) + optional web UI.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Works on macOS and Linux (and in the Codespace).** Confidence 0.69 · [[python-environments|Python Environments and Reproducibility]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.69 · [[course-exam|Exam]]
- **A Kafka message is a key–value pair.** Confidence 0.69 · [[kafka-log|Kafka Log]]
- **Symptom: ModuleNotFoundError: kafka.vendor.six.moves — Fix: You have the old kafka-python 2.0.2 → pip install -r requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: Apple Silicon (M1–M4) — Fix: Nothing special – the image and Kafka run natively.** Confidence 0.68 · [[course-setup|Course Setup]]
- **File: kafka_data.py — What: fake data: get_registered_user() and keyed events with a per-key sequence number.** Confidence 0.68 · [[course-setup|Course Setup]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix).** Confidence 0.66 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **File: 02_kafka_python.ipynb — What: Block 2 – notebook.** Confidence 0.64 · [[hdfs-architecture|HDFS]]
- **The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka download and broker data from Session 6 (session-06/kafka_2.13-*/, session-06/kafka-data/).** Confidence 0.63 · [[kafka-cluster|Kafka Cluster]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.62 · [[tooling-docker|Docker and Dev Containers]]
- **Check: python -c "import kafka, faker; print(kafka.version)" → 3.x.** Confidence 0.62 · [[course-setup|Course Setup]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Kafka also offers exactly-once within Kafka (transactions) – not part of this course.** Confidence 0.59 · [[streaming-architecture|Streaming Architectures]]
- **The old lab wrote it by hand – kafka-python 3 also ships ready-made ones.** Confidence 0.57 · [[unfiled|Unfiled Observations]]
- **Next time just run python get_kafka.py --start again.** Confidence 0.57 · [[course-setup|Course Setup]]
- **What ends up where (both folders are ignored by git): session-06/kafka_2.13-4.4.0/ the Kafka distribution (bin/, config/, libs/) session-06/kafka-data/ the broker's log segments → this is where your messages live on disk.** Confidence 0.57 · [[kafka-cluster|Kafka Cluster]]
- **Broker kafka-ui is # optional web UI, only started with --profile ui.** Confidence 0.56 · [[kafka-cluster|Kafka Cluster]]
- **The folder must NOT contain a space (the Kafka shell scripts then fail with "Classpath is empty").** Confidence 0.52 · [[unfiled|Unfiled Observations]]
- **Copy config/server.properties → config/course-server.properties with our data folder, automatic topic creation switched off (you create topics yourself) and small segments (so you can see several segment files in kafka-data/ after a few thousand messages).** Confidence 0.52 · [[kafka-log|Kafka Log]]
- **Usage: python get_kafka.py # download, verify, extract, format storage, print the start command python get_kafka.py --start # ... and start the broker right away (Ctrl+C stops it) python get_kafka.py --reformat # wipe the data folder and format again (after a version change) python get_kafka.py --dest ~/kafka-course # install somewhere else (path without spaces).** Confidence 0.52 · [[kafka-cluster|Kafka Cluster]]
- **Download Apache Kafka (binary, KRaft mode) and prepare a single-node broker for Session 6.** Confidence 0.52 · [[kafka-cluster|Kafka Cluster]]
- **Kafka consumer for the Session 6 lab (terminal version of kafka_consumer.ipynb).** Confidence 0.50 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Kafka producer for the Session 6 lab (terminal version of kafka_producer.ipynb).** Confidence 0.50 · [[kafka-producers|Kafka Producers]]
- **Export PATH="$PWD/kafka_2.13-4.4.0/bin:$PATH" ; export KDATA="$PWD/kafka-data" ; kafka-topics.sh --version # → 4.4.0.** Confidence 0.49 · [[kafka-log|Kafka Log]]
- **Cd session-06 ; python get_kafka.py --start # downloads Kafka 4.4.0 (~130 MB), checks the SHA-512, formats storage, starts the broker.** Confidence 0.48 · [[kafka-cluster|Kafka Cluster]]
- **Apache publishes 'kafka_x.tgz: F5CE BA8A ...' (gpg --print-md style) – strip name and spaces.** Confidence 0.46 · [[unfiled|Unfiled Observations]]
- **Broker KAFKA_LISTENERS is PLAINTEXT://:19092,PLAINTEXT_HOST://:9092,CONTROLLER://:9093.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_LISTENER_SECURITY_PROTOCOL_MAP is CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_ADVERTISED_LISTENERS is PLAINTEXT://broker:19092,PLAINTEXT_HOST://localhost:9092.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_CONTROLLER_QUORUM_VOTERS is 1@localhost:9093.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Kafka-dump-log.sh --files "$KDATA/cli-demo-0/00000000000000000000.log" --print-data-log.** Confidence 0.45 · [[kafka-log|Kafka Log]]
- **Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.** Confidence 0.44 · [[python-environments|Python Environments and Reproducibility]]
- **Python -c "from kafka import KafkaAdminClient; print(KafkaAdminClient(bootstrap_servers='localhost:9092').list_topics())".** Confidence 0.43 · [[kafka-producers|Kafka Producers]]
- **Kafka calls these two methods when the group is rebalanced.** Confidence 0.42 · [[unfiled|Unfiled Observations]]
- **Fake data for the Session 6 Kafka lab.** Confidence 0.42 · [[unfiled|Unfiled Observations]]
- **Kafka-python is pinned as >=3.0,<4.** Confidence 0.41 · [[unfiled|Unfiled Observations]]

## Related Entities

- [[broker|broker]] (23)
- [[topic|topic]] (9)
- [[docker|Docker]] (8)
- [[faker|Faker]] (4)
- [[requirements_txt|requirements.txt]] (4)
- [[kraft|KRaft]] (3)
- [[python|Python 3.12]] (3)
- [[kafka_topics_sh|kafka-topics.sh]] (3)
- [[partition|partition]] (3)
- [[pip|pip]] (3)
