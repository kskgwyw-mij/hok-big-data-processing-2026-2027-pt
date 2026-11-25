---
title: topic
type: entity
entity_id: ent_topic
entity_type: concept
claim_ids:
  - claim_80c6829c
  - claim_b0185af6
  - claim_76c23fc7
  - claim_e42b42f7
  - claim_2ee83bfc
  - claim_2aedc4a6
  - claim_4f4f199d
  - claim_daf456a4
  - claim_57484bd1
  - claim_c9e8d488
  - claim_3e36f06c
  - claim_4f0bb3f2
  - claim_4919910b
  - claim_054df005
  - claim_3ed72880
  - claim_e25a0f01
  - claim_42524796
  - claim_6fb4e772
  - claim_67369049
  - claim_bc86de96
  - claim_9e1d77e7
  - claim_5aae3a4d
  - claim_a893397a
  - claim_dca588fe
  - claim_8fd8c7c8
  - claim_3eea2cc1
  - claim_42099051
  - claim_326f6e1b
  - claim_ad8eb4c3
  - claim_fc2762ef
  - claim_87ec27e4
  - claim_dfe154cd
  - claim_ac59fce7
confidence: 0.682
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_6002d48d
  - src_6494d099
  - src_799c8bd7
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_bb056c24
  - src_c65c80a3
  - src_cecf99ea
---

# topic

Type: concept. Mentioned in 33 claims across 12 topics.
Aliases: topics.

## Claims

- **Part: A — Topic: Foundations: Big Data, scaling, GIL, threads vs. processes; Points: 12.** Confidence 0.83 · [[course-exam|Exam]]
- **Part: B — Topic: Spark architecture, HDFS, MapReduce; Points: 16.** Confidence 0.80 · [[course-exam|Exam]]
- **Part: C — Topic: Python environments, file formats, DuckDB; Points: 12.** Confidence 0.80 · [[course-exam|Exam]]
- **Part: E — Topic: Kafka and streaming; Points: 10.** Confidence 0.75 · [[course-exam|Exam]]
- **Folder: (Session 5 – no folder) — Topic: Stream processing with Kafka – theory: events, append-only logs, topics and partitions, replication, KRaft; Runs on: Kaggle.** Confidence 0.75 · [[kafka-log|Kafka Log]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.** Confidence 0.73 · [[engines-single_machine|Single-Machine Engines]]
- **Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).** Confidence 0.72 · [[data-formats|File Formats]]
- **Folder: session-02/ — Topic: Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins; Runs on: dev container or a laptop with Java 17.** Confidence 0.72 · [[spark-architecture|Spark Architecture]]
- **Lab: B — Topic: CSV vs. pickle vs. Parquet, saving models; Where: laptop, notebook; File: 02_file_formats_and_pickle.ipynb.** Confidence 0.72 · [[data-formats|File Formats]]
- **Prediction 4: we change the topic from 3 to 4 partitions.** Confidence 0.71 · [[kafka-log|Kafka Log]]
- **Folder: (Session 3 – no folder) — Topic: Groups Work; Runs on: Google Drive.** Confidence 0.69 · [[kafka-log|Kafka Log]]
- **Symptom: UnknownTopicOrPartitionError / topic does not exist — Fix: Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.69 · [[course-exam|Exam]]
- **Lab: C — Topic: DuckDB as a database file – homework; Where: laptop, notebook; File: 03_duckdb_database.ipynb.** Confidence 0.68 · [[data-duckdb|DuckDB]]
- **In the comparison table, Route A: Stop: docker compose stop (start again: docker compose start), Delete all topics and messages: docker compose down – the next up -d starts empty.** Confidence 0.68 · [[tooling-docker|Docker and Dev Containers]]
- **Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your messages as bytes in a log segment on disk.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Symptom: consumer.py prints ASSIGNED partitions [] (several times) — Fix: Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the consumer gets its partitions within a few seconds.** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Our broker has auto.create.topics.enable=false: a typo in a topic name gives an error instead of a new, empty topic.** Confidence 0.67 · [[kafka-cluster|Kafka Cluster]]
- **Lab: A — Topic: Python environments: venv, pyenv, uv; Where: laptop, terminal; File: 01_python_environments.md, check_env.py.** Confidence 0.67 · [[python-environments|Python Environments and Reproducibility]]
- **Lab: D — Topic: Spark fundamentals (Session 2) + Spark ML; Where: Kaggle; File: 04_spark_fundamentals_and_ml.ipynb.** Confidence 0.67 · [[tooling-kaggle|Kaggle Labs]]
- **Create a topic with 3 partitions from Python – idempotently (safe to run twice).** Confidence 0.65 · [[kafka-log|Kafka Log]]
- **Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the terminal scripts can create the same topic).** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **Copy config/server.properties → config/course-server.properties with our data folder, automatic topic creation switched off (you create topics yourself) and small segments (so you can see several segment files in kafka-data/ after a few thousand messages).** Confidence 0.52 · [[kafka-log|Kafka Log]]
- **Create the topic if it does not exist yet (safe to run many times).** Confidence 0.52 · [[kafka-log|Kafka Log]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py --count 30 --interval 0.2 python producer.py --no-key # same events, but WITHOUT a key python producer.py --data users --topic registered_user # the original lab: fake users, no key.** Confidence 0.50 · [[kafka-producers|Kafka Producers]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.46 · [[kafka-cluster|Kafka Cluster]]
- **Python -c "from kafka import KafkaAdminClient; print(KafkaAdminClient(bootstrap_servers='localhost:9092').list_topics())".** Confidence 0.43 · [[kafka-producers|Kafka Producers]]

## Related Entities

- [[kafka|Kafka]] (9)
- [[broker|broker]] (9)
- [[partition|partition]] (8)
- [[duckdb|DuckDB]] (4)
- [[spark|Spark]] (4)
- [[docker|Docker]] (3)
- [[kaggle|Kaggle]] (3)
- [[parquet|Parquet]] (3)
- [[spark_ml|Spark ML]] (3)
- [[consumer_group|consumer group]] (3)
