---
title: Questions: Kafka Cluster
type: questions
topic: kafka.cluster
question_count: 5
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Kafka Cluster

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Block 1 – Kafka broker and command-line tools / Exam-style questions

- (4 P) Your laptop has one broker. Why does --replication-factor 2 fail? In production with 3 brokers, what do Leader, Replicas and Isr mean, and what happens when the leader broker fails?
  - `session-06/01_kafka_cli.md:268` · exam_prompt

## Block 1 – Kafka broker and command-line tools / Create a topic with 3 partitions

- What changes in Isr if one broker crashes?
  - `session-06/01_kafka_cli.md:93` · open_question

## Block 3 – Exam circuit / Station 6 – Kafka and streaming architectures

- 6.2 (4 P) Topic payments has 4 partitions, replication factor 3 on 3 brokers. (a) Group fraud runs 6 consumers, group dashboard runs 1 consumer. Which partitions does each consumer read? (b) What is the ISR, and what happens when the leader broker of partition 2 fails?
  - `session-06/03_exam_circuit.md:112` · exam_prompt

## Big Data Processing – Mock exam / Part E – Kafka and streaming

- E1 (1 P) What does Kafka 4 use instead of ZooKeeper to manage cluster metadata?
  - `04_mock_exam-gitdiff.md:114` · exam_prompt
- E5 (2 P) Replication factor 3: what is the ISR, and what happens when the leader of a partition fails?
  - `04_mock_exam-gitdiff.md:123` · exam_prompt
