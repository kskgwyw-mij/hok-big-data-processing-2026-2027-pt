---
title: Questions: Kafka Log
type: questions
topic: kafka.log
question_count: 16
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: Kafka Log

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part E – Kafka and streaming

- E2 (1 P) Is a Kafka offset unique within a topic or within a partition?
  - `raw/04_mock_exam.md:113` · exam_prompt

## Block 1 – Kafka broker and command-line tools / Produce messages with a key

- Prediction 2: will the three Tirol messages end up in one partition or in different ones?
  - `session-06/01_kafka_cli.md:118` · open_question

## Block 1 – Kafka broker and command-line tools / Consume from the beginning

- Is the output in the order you typed? Which order is guaranteed?
  - `session-06/01_kafka_cli.md:141` · open_question
- Every partition starts at offset 0. What is an offset, and is it unique in the topic or only in a partition?
  - `session-06/01_kafka_cli.md:142` · open_question
- Two different keys (Wien, Salzburg) can share a partition. Why is that not a problem?
  - `session-06/01_kafka_cli.md:143` · open_question

## Block 1 – Kafka broker and command-line tools / Your messages on disk

- Messages are grouped in batches (baseOffset … lastOffset … count). Who creates the batches?
  - `session-06/01_kafka_cli.md:237` · open_question
- The folder also has .index and .timeindex files. What could they be good for when a consumer asks for offset 4 711?
  - `session-06/01_kafka_cli.md:239` · open_question
- With 1 MB segments (our course setting), what happens to the folder after a few thousand messages?
  - `session-06/01_kafka_cli.md:240` · open_question

## Block 1 – Kafka broker and command-line tools / Exam-style questions

- (2 P) Define offset. Is an offset unique within a topic or within a partition?
  - `session-06/01_kafka_cli.md:263` · exam_prompt
- (3 P) A topic has 3 partitions. Messages with the key Tirol always arrive in the order they were produced, but messages without a key do not. Explain why.
  - `session-06/01_kafka_cli.md:264` · exam_prompt
- (3 P) kafka-consumer-groups --describe shows CURRENT-OFFSET 120, LOG-END-OFFSET 200 for one partition. What is the lag, and give two possible reasons why it is growing.
  - `session-06/01_kafka_cli.md:266` · exam_prompt
- (4 P) A colleague increases a topic from 3 to 6 partitions to get more throughput. Their downstream job relies on all events of one customer being processed in order. What can go wrong, and what would you do?
  - `session-06/01_kafka_cli.md:270` · exam_prompt

## Block 1 – Kafka broker and command-line tools / Which topics exist?

- On a fresh broker the list is empty or shows only __consumer_offsets (an internal topic – what might it store?
  - `session-06/01_kafka_cli.md:52` · open_question

## Session 6 · Block 2 – Kafka from Python: producers, consumers, consumer groups / A keyed producer / Your turn: which partitions did each key use?

- Predict first: how many partitions per key?
  - `session-06/02_kafka_python.ipynb#cell-9:2` · open_question

## Block 3 – Exam circuit / Station 6 – Kafka and streaming architectures

- 6.1 (3 P) Define topic, partition and offset. What does Kafka 4 use to manage cluster metadata instead of ZooKeeper?
  - `session-06/03_exam_circuit.md:110` · exam_prompt

## Block 3 – Exam circuit / Station 4 – Spark execution: lazy evaluation and shuffles

- 4.3 (3 P) Spark splits a 2 GB (= 2048 MB) file into partitions of 128 MB each. Each partition is processed by one task. Your laptop has 4 cores, and each core works on one task at a time. (a) How many partitions, and therefore tasks, does Spark create? (1 P) (b) How many rounds ("waves") are needed until all tasks are done? (1 P) (c) If the file had only 2 partitions, how many of the 4 cores would be busy? Name one function that fixes this. (1 P)
  - `session-06/03_exam_circuit.md:80` · exam_prompt
