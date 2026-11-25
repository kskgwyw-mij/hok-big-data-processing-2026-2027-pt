---
title: Questions: HDFS
type: questions
topic: hdfs.architecture
question_count: 5
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: HDFS

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part B – Spark architecture, HDFS, MapReduce

- B1 (1 P) Which HDFS component stores the metadata (which blocks belong to which file, and where they are)?
  - `raw/04_mock_exam.md:42` · exam_prompt
- B2 (2 P) A 150 MB file, block size 64 MB, replication factor 3. How many blocks does the file have, and how many block copies are stored in the cluster?
  - `raw/04_mock_exam.md:44` · exam_prompt
- B3 (2 P) A DataNode fails. How does HDFS notice it, and why is no data lost?
  - `raw/04_mock_exam.md:47` · exam_prompt

## Block 1 – Kafka broker and command-line tools / Create a topic with 3 partitions

- What happens if you ask for replication factor 2?
  - `session-06/01_kafka_cli.md:60` · open_question

## Block 3 – Exam circuit / Station 3 – HDFS, MapReduce, Spark architecture

- 3.1 (3 P) A 150 MB file is stored in HDFS with 64 MB blocks and replication factor 3. How many blocks, and how many block copies are stored in total? What does the NameNode store, what do the DataNodes store?
  - `session-06/03_exam_circuit.md:50` · exam_prompt
