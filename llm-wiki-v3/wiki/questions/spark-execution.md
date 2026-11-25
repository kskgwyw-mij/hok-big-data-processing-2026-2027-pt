---
title: Questions: Spark Execution Model
type: questions
topic: spark.execution
question_count: 18
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Spark Execution Model

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Session 2 – Apache Spark Fundamentals / Part 6 – Group Work: NYC Taxi Analysis / Task A – Core (everyone)

- In the Markdown cell below the code, explain: where does the shuffle happen and why?
  - `session-02/02_spark_fundamentals.ipynb#cell-26:27` · open_question

## Part 1 · Spark fundamentals / Reading the execution plan

- Will the plan contain an Exchange (a shuffle)?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-19:3` · open_question

## Part 1 · Spark fundamentals / Task B – Add zone names with a join

- Then look at explain(): which join strategy did Spark choose – and why?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-24:4` · open_question
- Fast groups: where does the orderBy appear in the plan relative to the join?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-27:1` · open_question

## Part 2 · Spark ML: how long will my taxi ride take?

- Your turn (2 min): how many partitions can run at the same time here?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-31:1` · open_question

## Part 2 · Spark ML: how long will my taxi ride take? / Exam-style questions

- Part 2 – Spark ML
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:12` · exam_prompt
- spark.read.csv(...) returned instantly, count() took much longer. Explain with transformation, action and lazy evaluation. Why would inferSchema=True change the first timing?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:14` · exam_prompt
- The linear model needs one-hot encoding for hour, the gradient-boosted trees do not. Why?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:20` · exam_prompt
- Spark 4 runs in ANSI mode. What happens with F.col("a") / F.col("b") when b is 0, and how do you avoid it?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:24` · exam_prompt
- Part 1 – Spark fundamentals
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:3` · exam_prompt
- A groupBy("PULocationID").count() on 8 partitions: why is a shuffle needed, and what do the two HashAggregate steps in the plan do?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:6` · exam_prompt
- Joining 3 million trips with the 265-row zone table, the plan shows BroadcastHashJoin. Why? What is the benefit compared with a sort-merge join, and what could go wrong if you broadcast a very large table?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:9` · exam_prompt

## Block 3 – Exam circuit / Station 4 – Spark execution: lazy evaluation and shuffles

- 4.1 (2 P) Transformation or action? filter, count, groupBy().agg(), show, withColumn, write.parquet.
  - `session-06/03_exam_circuit.md:66` · exam_prompt
- (a) After lines 1–4, Spark has not processed any trips yet. Why not? Which line starts the actual work? (2 P) (b) Which of lines 2, 3 and 4 is a wide transformation? Explain why it needs a shuffle. (2 P) (c) How many shuffles does this job have, and into how many stages does Spark split it? (1 P)
  - `session-06/03_exam_circuit.md:76` · exam_prompt

## Block 3 – Exam circuit / Station 4 – Spark execution and joins: read the plan

- 4.2 (5 P) A colleague ran .explain() and sends you this physical plan (shortened):
  - `03_exam_circuit-gitdiff.md:156` · exam_prompt

## gitdiff / Station 4 – Spark execution: lazy evaluation and shuffles

- 4.2 (5 P) A colleague ran .explain() and sends you this physical plan (shortened): 4.2 (5 P) Look at this PySpark code (the line numbers are not part of the code):
  - `03_exam_circuit-gitdiff.md:272` · exam_prompt

## Block 3 – Exam circuit / Station 6 – Kafka and streaming architectures

- how many partitions and tasks, and how many "waves" of tasks? What happens if the data had only 2 partitions? (a) After lines 1–4, Spark has not processed any trips yet. Why not? Which line starts the actual work? (2 P) (b) Which of lines 2, 3 and 4 is a wide transformation? Explain why it needs a shuffle. (2 P) (c) How many shuffles does this job have, and into how many stages does Spark split it? (1 P)
  - `03_exam_circuit-gitdiff.md:428` · exam_prompt

## Big Data Processing – Mock exam / Part B – Spark architecture, HDFS, MapReduce

- B7 (1 P) Is df.count() a transformation or an action?
  - `04_mock_exam-gitdiff.md:186` · exam_prompt
