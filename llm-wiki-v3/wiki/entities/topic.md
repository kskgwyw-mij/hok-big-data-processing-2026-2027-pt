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
  - claim_44c56793
  - claim_daf456a4
  - claim_57484bd1
  - claim_c9e8d488
  - claim_3e36f06c
  - claim_4f0bb3f2
  - claim_0efcddb6
  - claim_4919910b
  - claim_054df005
  - claim_3ed72880
  - claim_4560b3b1
  - claim_42524796
  - claim_6fb4e772
  - claim_67369049
  - claim_c8c19737
  - claim_9e1d77e7
  - claim_5aae3a4d
  - claim_a893397a
  - claim_fe4f6640
  - claim_8fd8c7c8
  - claim_3eea2cc1
  - claim_42099051
  - claim_326f6e1b
  - claim_ad8eb4c3
  - claim_663bce6e
  - claim_45adb47b
  - claim_d484f3b4
  - claim_2fd01ef9
  - claim_cadd58c6
  - claim_e8488930
  - claim_1833931d
  - claim_a2c72ddb
  - claim_5fe7584b
  - claim_f689757f
  - claim_223f3223
  - claim_2413a482
  - claim_4ec3a5b0
  - claim_806a5d75
  - claim_5dee5fee
  - claim_87ec27e4
  - claim_dfe154cd
  - claim_ac59fce7
  - claim_633a9dc0
  - claim_48d35ee7
  - claim_af1b58f3
  - claim_8701c291
  - claim_bf6e1a55
  - claim_bca5c57a
  - claim_74fd87ab
  - claim_80290f63
confidence: 0.748
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_41b3a933
  - src_59b6ded4
  - src_6002d48d
  - src_6494d099
  - src_68fcf2b9
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_bb056c24
  - src_c65c80a3
  - src_cecf99ea
  - src_e258bafb
  - src_fc0bfe80
---

# topic

Type: concept. Mentioned in 57 claims across 15 topics.
Aliases: topics.

## Claims

- **Part: A — Topic: Foundations: Big Data, scaling, GIL, threads vs. processes; Points: 12.** Confidence 0.96 · [[python-execution|Python Execution Model]]
- **Part: B — Topic: Spark architecture, HDFS, MapReduce; Points: 16.** Confidence 0.92 · [[course-exam|Exam]]
- **Part: E — Topic: Kafka and streaming; Points: 10.** Confidence 0.90 · [[course-exam|Exam]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **In the comparison table, Route A: Stop: docker compose stop (start again: docker compose start), Delete all topics and messages: docker compose down – the next up -d starts empty.** Confidence 0.87 · [[tooling-docker|Docker and Dev Containers]]
- **In the comparison table, Route B: Stop: Ctrl+C in the broker terminal, Delete all topics and messages: python get_kafka.py --reformat (plus --dest … if you used it).** Confidence 0.86 · [[kafka-cluster|Kafka Cluster]]
- **A consumer group remembers how far it has read: its committed offset per partition, stored in the topic __consumer_offsets.** Confidence 0.86 · [[kafka-log|Kafka Log]]
- **Lab: B — Topic: CSV vs. pickle vs. Parquet, saving models; Where: laptop, notebook; File: 02_file_formats_and_pickle.ipynb.** Confidence 0.86 · [[data-formats|File Formats]]
- **Lab: C — Topic: DuckDB as a database file – homework; Where: laptop, notebook; File: 03_duckdb_database.ipynb.** Confidence 0.84 · [[data-duckdb|DuckDB]]
- **Clean up (optional): kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic cli-demo (Route A with the prefix).** Confidence 0.83 · [[kafka-log|Kafka Log]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]
- **Lab: A — Topic: Python environments: venv, pyenv, uv; Where: laptop, terminal; File: 01_python_environments.md, check_env.py.** Confidence 0.83 · [[python-environments|Python Environments and Reproducibility]]
- **If you have multiple topic ideas, we would be happy to add them to the list. » Students are welcome to contact you directly. » Students should upload their application for the assignment of an MA thesis topic - including a completed proposal - by October 31.** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **Create a topic with 3 partitions from Python – idempotently (safe to run twice).** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **Each key appears in exactly one partition: partition = hash(key) mod 3.** Confidence 0.81 · [[kafka-log|Kafka Log]]
- **No key p0 p1 p2 spread – order lost Partition = ordered, append-only log (segment files on disk) Order is guaranteed per partition, not per topic Offset = position inside one partition – unique only there.** Confidence 0.80 · [[kafka-log|Kafka Log]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.80 · [[tooling-docker|Docker and Dev Containers]]
- **Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.** Confidence 0.80 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Part: C — Topic: Python environments, file formats, DuckDB; Points: 12.** Confidence 0.80 · [[course-exam|Exam]]
- **Part: C — Topic: Python environments, file formats, DuckDB; Points: 12.** Confidence 0.80 · [[data-duckdb|DuckDB]]
- **Part: B — Topic: Spark architecture, HDFS, MapReduce; Points: 16.** Confidence 0.80 · [[hdfs-architecture|HDFS]]
- **Lab: D — Topic: Spark fundamentals (Session 2) + Spark ML; Where: Kaggle; File: 04_spark_fundamentals_and_ml.ipynb.** Confidence 0.79 · [[tooling-kaggle|Kaggle Labs]]
- **» Consumers read data from a topic » They only have to specify the topic name and one broker to connect to, and Kafka will automatically take care of pulling the data from the right brokers » Data is read in order for each partitions.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **» Kafka Topics are roughly analogous to SQL Tables » Topics organize related events » Topics are not queryable like SQL tables » You must create consumers or producers e.g. topic logs, topic purchases » Topics consist of append-only logs » All data in a topic is in key-value form » Many configuration options and considerations » Stored in binary format and not string like JSON.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **» Offset only have a meaning for a specific partition. » E.g. offset 3 in partition doesn't represent the same data as offset 3 in partition 1. » Order is guaranteed only within a partition (not across partitions). » Data is kept only for a limited time (default is two weeks). » Once the data is written to a partition, it can't be changed (immutability). » Data is assigned randomly to a partition unless a key is provided (more on this later). » You can have as many partitions per topic as you want.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **» Kafka stores the offsets at which a consumer group has been reading » The offsets commit live in a Kafka topic named "__consumer_offsets" » When a consumer has processed data received some Kafka, it should be committing the offsets » If a consumer process dies, it will be able to read back from where it left off thanks to consumer offsets!.** Confidence 0.77 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Schwendinger » The full-time faculty members have provided lists of potential topics. » However, these lists are intended merely as inspiration; students are also welcome to propose their own topics.** Confidence 0.76 · [[kafka-log|Kafka Log]]
- **Folder: (Session 5 – no folder) — Topic: Stream processing with Kafka – theory: events, append-only logs, topics and partitions, replication, KRaft; Runs on: Kaggle.** Confidence 0.75 · [[kafka-log|Kafka Log]]
- **» We can create apps which consume data » Consumers retrieve events from Kafka Topic(s) » May consume one or more topics at a time » Keep track of what events have already been seen » Many configuration options and considerations » By default consumers will only consume data that was produced 1st connected to Kafka (historical data not automatically pulled).** Confidence 0.75 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **# expected seq … = intended group-a group-b Terminal 3 – same group different group = its own copy C1 + C2 share the 3 partitions of every message ✗ If it fails $ python consumer.py --name C2 ASSIGNED partitions [] → topic not created ✓ Tested on the Mac yet.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails? » A colleague increases a topic from 3 to 6 partitions to get more throughput.** Confidence 0.74 · [[kafka-cluster|Kafka Cluster]]
- **Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.** Confidence 0.73 · [[engines-single_machine|Single-Machine Engines]]
- **Folder: session-02/ — Topic: Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins; Runs on: dev container or a laptop with Java 17.** Confidence 0.72 · [[spark-execution|Spark Execution Model]]
- **Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).** Confidence 0.72 · [[data-formats|File Formats]]
- **Prediction 4: we change the topic from 3 to 4 partitions.** Confidence 0.71 · [[kafka-log|Kafka Log]]
- **Describe how this works in a Kappa architecture and which property of the Kafka topic makes it possible.** Confidence 0.70 · [[streaming-architecture|Streaming Architectures]]
- **» Topics: a particular stream of data » Similar to a table in a database (without all the constraints) » You can have as many topics as you want » A topic is identified by its name.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Message A has offset 5 in partition 0, message B has offset 5 in partition 2 of the same topic.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Delete topic docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --delete --topic my-first-topic.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **» A Kafka cluster is composed of multiple brokers (servers) » Each broker is identified with its ID (integer) » Each broker contains certain topic partitions » After connecting to any broker (called a bootstrap broker), you will be connected to the entire cluster » A good number to get started is 3 brokers, but some big clusters have over 100 brokers » (Diagram boxes shown: Broker 1, Broker 2, Broker 3).** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **Topic: cli-demo PartitionCount: 3 ReplicationFactor: 1 Configs: …segment.bytes=1048576.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Next step » Kafka Producers send data to a topic » Producers are often built with a client library e.g. Python, Java, etc. » Events may be sent one at a time, or in batches » Many configuration options and considerations.** Confidence 0.70 · [[kafka-producers|Kafka Producers]]
- **Folder: (Session 3 – no folder) — Topic: Groups Work; Runs on: Google Drive.** Confidence 0.69 · [[kafka-log|Kafka Log]]
- **Symptom: UnknownTopicOrPartitionError / topic does not exist — Fix: Our broker does not auto-create topics – create it first (Block 1, part 2). producer.py creates user-events itself.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: consumer.py prints ASSIGNED partitions [] (several times) — Fix: Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the consumer gets its partitions within a few seconds.** Confidence 0.69 · [[kafka-log|Kafka Log]]
- **Goal: after this block you can create a topic with several partitions, explain what --describe shows, predict which partition a keyed message lands in, read consumer lag, and find your messages as bytes in a log segment on disk.** Confidence 0.68 · [[kafka-log|Kafka Log]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Our broker has auto.create.topics.enable=false: a typo in a topic name gives an error instead of a new, empty topic.** Confidence 0.67 · [[kafka-cluster|Kafka Cluster]]
- **Delete all topics and Stop (keep messages) messages.** Confidence 0.66 · [[kafka-log|Kafka Log]]
- **Data Partitions for High Throughput.** Confidence 0.66 · [[kafka-log|Kafka Log]]
- **Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the terminal scripts can create the same topic).** Confidence 0.64 · [[kafka-log|Kafka Log]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **Copy config/server.properties → config/course-server.properties with our data folder, automatic topic creation switched off (you create topics yourself) and small segments (so you can see several segment files in kafka-data/ after a few thousand messages).** Confidence 0.52 · [[kafka-log|Kafka Log]]
- **Create the topic if it does not exist yet (safe to run many times).** Confidence 0.52 · [[kafka-log|Kafka Log]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py --count 30 --interval 0.2 python producer.py --no-key # same events, but WITHOUT a key python producer.py --data users --topic registered_user # the original lab: fake users, no key.** Confidence 0.50 · [[kafka-producers|Kafka Producers]]
- **Python -c "from kafka import KafkaAdminClient; print(KafkaAdminClient(bootstrap_servers='localhost:9092').list_topics())".** Confidence 0.43 · [[kafka-producers|Kafka Producers]]

## Related Entities

- [[kafka|Kafka]] (21)
- [[partition|partition]] (20)
- [[broker|broker]] (16)
- [[offset|offset]] (8)
- [[docker|Docker]] (7)
- [[kafka_topics_sh|kafka-topics.sh]] (6)
- [[duckdb|DuckDB]] (5)
- [[spark|Spark]] (5)
- [[consumer_group|consumer group]] (4)
- [[kaggle|Kaggle]] (3)
