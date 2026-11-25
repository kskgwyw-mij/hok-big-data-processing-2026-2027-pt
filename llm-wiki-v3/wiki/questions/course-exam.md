---
title: Questions: Exam
type: questions
topic: course.exam
question_count: 9
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Exam

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Block 3 – Exam circuit / Station 4 – Spark execution: lazy evaluation and shuffles

- 4.2 (5 P) Look at this PySpark code (the line numbers are not part of the code):
  - `session-06/03_exam_circuit.md:68` · exam_prompt

## Block 3 – Exam circuit / Station 4 – Spark execution and joins: read the plan

- (a) Describe in one sentence what the query computes. (1 P) (b) How many shuffles does the plan contain, and which operations cause them? (2 P) (c) Which table is broadcast, and why is that a good choice here? (1 P) (d) What do PushedFilters and ReadSchema tell you about how much data Spark reads? (1 P)
  - `03_exam_circuit-gitdiff.md:173` · exam_prompt

## Big Data Processing – Mock exam / Part D – Spark ML and joins

- How many shuffles are in this fragment? What does that tell you about the size of the two tables?
  - `04_mock_exam-gitdiff.md:108` · exam_prompt
- D2 (2 P) Trips (3 million rows) are joined with the zone table (265 rows). Why does Spark choose a BroadcastHashJoin, and what goes wrong if you force a broadcast of a very large table?
  - `04_mock_exam-gitdiff.md:214` · exam_prompt
- D6 (2 P) Read this plan fragment:
  - `04_mock_exam-gitdiff.md:225` · exam_prompt

## Big Data Processing – Mock exam / Part E – Kafka and streaming

- E4 (2 P) Which ordering guarantee does Kafka give, and how do you make sure all events of one customer are processed in order?
  - `04_mock_exam-gitdiff.md:121` · exam_prompt

## Big Data Processing – Mock exam / Part A – Foundations

- A2 (1 P) Which V describes how trustworthy and accurate the data is?
  - `04_mock_exam-gitdiff.md:154` · exam_prompt
- A3 (2 P) Name one disadvantage of scaling up and one disadvantage of scaling out.
  - `04_mock_exam-gitdiff.md:156` · exam_prompt
- A5 (2 P) Threads or processes? Give one word and a half-sentence reason for each: (a) downloading 200 files from an API, (b) a pure-Python numerical loop that should use all 8 cores.
  - `04_mock_exam-gitdiff.md:160` · exam_prompt
