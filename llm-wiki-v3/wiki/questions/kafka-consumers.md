---
title: Questions: Kafka Consumers and Consumer Groups
type: questions
topic: kafka.consumers
question_count: 5
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Kafka Consumers and Consumer Groups

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Block 1 – Kafka broker and command-line tools / Consumer groups and lag

- Prediction 3: what is the total LAG of cli-group now?
  - `session-06/01_kafka_cli.md:168` · open_question

## Session 6 · Block 2 – Kafka from Python: producers, consumers, consumer groups / Consumer groups with real processes – terminal experiments

- Stop one consumer with Ctrl+C: what happens to its partitions?
  - `session-06/02_kafka_python.ipynb#cell-23:35` · open_question

## Session 6 · Block 2 – Kafka from Python: producers, consumers, consumer groups / Exam-style questions

- (3 P) A topic has 3 partitions and one consumer group with 4 consumers. How are the partitions assigned, and what does the 4th consumer do? What changes if one consumer crashes?
  - `session-06/02_kafka_python.ipynb#cell-23:50` · exam_prompt
- (4 P) Explain at-least-once delivery with auto-commit. Describe a concrete situation that creates a duplicate, and one way to make the consumer robust against it.
  - `session-06/02_kafka_python.ipynb#cell-23:54` · exam_prompt

## Big Data Processing – Mock exam / Part E – Kafka and streaming

- E3 (2 P) A topic has 3 partitions. One consumer group runs 5 consumers. How are the partitions assigned, and what do the remaining consumers do?
  - `04_mock_exam-gitdiff.md:118` · exam_prompt
