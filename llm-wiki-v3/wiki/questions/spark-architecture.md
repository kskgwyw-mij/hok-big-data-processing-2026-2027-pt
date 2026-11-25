---
title: Questions: Spark Architecture
type: questions
topic: spark.architecture
question_count: 15
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: Spark Architecture

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part B – Spark architecture, HDFS, MapReduce

- B6 (3 P) Explain the roles of the driver, the executors and the cluster manager in a Spark application.
  - `raw/04_mock_exam.md:54` · exam_prompt
- B8 (2 P) In Spark, what is a task, and at which kind of operation does a new stage begin?
  - `raw/04_mock_exam.md:58` · exam_prompt

## General

- Entry Point SparkContext SparkSession Supports RDDs?
  - `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p120:8` · open_question

## Session 2 – Apache Spark Fundamentals / Part 3 – Transformations vs. Actions: the most important concept in Spark / Predict before you run

- Which lines start a Spark job?
  - `session-02/02_spark_fundamentals.ipynb#cell-11:16` · open_question

## Session 2 – Apache Spark Fundamentals / Part 5 – Reading the Execution Plan / Predict before you run

- Do you expect to see an Exchange node in the plan?
  - `session-02/02_spark_fundamentals.ipynb#cell-21:26` · open_question

## Session 2 – Apache Spark Fundamentals / Part 6 – Group Work: NYC Taxi Analysis / Task B – Extension: add location names (if Task A is done)

- Run explain() on the joined DataFrame. What kind of join does Spark choose? Why?
  - `session-02/02_spark_fundamentals.ipynb#cell-29:12` · open_question
- Inspect the schema — which column is the join key?
  - `session-02/02_spark_fundamentals.ipynb#cell-29:9` · open_question

## Session 2 – Apache Spark Fundamentals / Part 6 – Group Work: NYC Taxi Analysis / Task C – Plan Challenge (for fast groups)

- Does adding a sort introduce a new Exchange? Why or why not?
  - `session-02/02_spark_fundamentals.ipynb#cell-34:7` · open_question
- Where in the plan does the sort appear relative to the join?
  - `session-02/02_spark_fundamentals.ipynb#cell-34:8` · open_question
- Open the Spark UI (http://localhost:4040): how many stages does this job have? Why?
  - `session-02/02_spark_fundamentals.ipynb#cell-34:9` · open_question

## Session 2 – Apache Spark Fundamentals / Part 1 – The SparkSession: your entry point into Spark / Predict before you run

- Q1 – Before running the cell below: What does calling SparkSession.builder...getOrCreate() actually do?
  - `session-02/02_spark_fundamentals.ipynb#cell-3:18` · open_question

## Session 2 – Apache Spark Fundamentals / Exit Ticket – Individual, no AI

- She says: "Three lines of code, so Spark ran three operations immediately." Is she correct?
  - `session-02/02_spark_fundamentals.ipynb#cell-43:19` · open_question
- What does Spark do in the two HashAggregate steps you see in the plan?
  - `session-02/02_spark_fundamentals.ipynb#cell-43:32` · open_question
- What could go wrong if you accidentally broadcast a very large table?
  - `session-02/02_spark_fundamentals.ipynb#cell-43:61` · open_question

## Block 3 – Exam circuit / Station 3 – HDFS, MapReduce, Spark architecture

- 3.3 (4 P) In a Spark application: what are the roles of the driver, the executors and the cluster manager? One count() starts a job – how is it split into stages and tasks?
  - `session-06/03_exam_circuit.md:56` · exam_prompt
