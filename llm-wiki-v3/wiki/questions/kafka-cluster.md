---
title: Questions: Kafka Cluster
type: questions
topic: kafka.cluster
question_count: 7
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: Kafka Cluster

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part E – Kafka and streaming

- E1 (1 P) What does Kafka 4 use instead of ZooKeeper to manage cluster metadata?
  - `raw/04_mock_exam.md:111` · exam_prompt
- E5 (2 P) Replication factor 3: what is the ISR, and what happens when the leader of a partition fails?
  - `raw/04_mock_exam.md:120` · exam_prompt

## General

- Broker not running or not on 9092 ✗ If it fails no configuration file provided: not found → repo root: cd session-06, then up -d again Nothing works?
  - `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p89:17` · open_question

## Block 1 – Kafka broker and command-line tools / Exam-style questions

- (4 P) Your laptop has one broker. Why does --replication-factor 2 fail? In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails?
  - `session-06/01_kafka_cli.md:268` · exam_prompt

## Block 1 – Kafka broker and command-line tools / Create a topic with 3 partitions

- Question: in a cluster with 3 brokers and replication factor 3, what would Replicas and Isr look like?
  - `session-06/01_kafka_cli.md:93` · open_question
- What changes in Isr if one broker crashes?
  - `session-06/01_kafka_cli.md:93` · open_question

## Block 3 – Exam circuit / Station 6 – Kafka and streaming architectures

- 6.2 (4 P) Topic payments has 4 partitions, replication factor 3 on 3 brokers. (a) Group fraud runs 6 consumers, group dashboard runs 1 consumer. Which partitions does each consumer read? (b) What is the ISR, and what happens when the leader broker of partition 2 fails?
  - `session-06/03_exam_circuit.md:112` · exam_prompt
