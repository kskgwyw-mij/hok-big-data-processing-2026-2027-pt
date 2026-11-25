---
title: Questions: Unfiled Observations
type: questions
topic: unfiled
question_count: 3
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Unfiled Observations

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Session 6 · Block 2 – Kafka from Python: producers, consumers, consumer groups / Exam-style questions

- (3 P) Two applications – a fraud detector and a dashboard – both need all payment events. Same group_id or different ones? Justify.
  - `session-06/02_kafka_python.ipynb#cell-23:52` · exam_prompt
- (4 P) An online shop needs all events of one order processed in the correct order, but also wants to scale to many consumers. How do you choose the message key, and why does that solve both requirements?
  - `session-06/02_kafka_python.ipynb#cell-23:56` · exam_prompt

## Session 6 · Block 2 – Kafka from Python: producers, consumers, consumer groups / A keyed producer / Your turn: which partitions did each key use?

- Predict first: how many partitions per key?
  - `session-06/02_kafka_python.ipynb#cell-9:2` · open_question
