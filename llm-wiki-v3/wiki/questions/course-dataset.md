---
title: Questions: NYC Yellow Taxi Dataset
type: questions
topic: course.dataset
question_count: 17
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: NYC Yellow Taxi Dataset

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part D – Spark ML and joins

- D1 (1 P) Narrow or wide transformation: groupBy("PULocationID").agg(avg("fare_amount"))?
  - `raw/04_mock_exam.md:82` · exam_prompt
- D2 (2 P) Trips (3 million rows) are joined with the zone table (265 rows). Why does Spark choose a BroadcastHashJoin, and what goes wrong if you force a broadcast of a very large table?
  - `raw/04_mock_exam.md:84` · exam_prompt
- D5 (2 P) Define target leakage and give an example from the taxi trip-duration model.
  - `raw/04_mock_exam.md:93` · exam_prompt

## General

- Only Is it safe to open a and read it? does it take? survive the round Python? file from someone trip? else?
  - `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p16:6` · open_question
- Alternative? » CREATE TABLE … AS SELECT vs. VIEW: what happens to each when new rows arrive in trips? » DELETE inside BEGIN TRANSACTION, then ROLLBACK: how many rows remain, and which ACID property is this?
  - `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p27:3` · open_question
- PySpark and Spark ML Part 1: Spark fundamentals · Part 2: how long will my taxi ride take?
  - `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p28:1` · open_question
- Which ones create an Exchange? » Trips joined with the 265-row zone table: why does Spark pick a BroadcastHashJoin, and what goes wrong if you broadcast a huge table? » Why is fare_amount not allowed as a feature here?
  - `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p40:3` · open_question

## Session 2 – Apache Spark Fundamentals / Part 6 – Group Work: NYC Taxi Analysis / Task A – Core (everyone)

- Question: Which pickup location IDs generated the most taxi trips in January 2024?
  - `session-02/02_spark_fundamentals.ipynb#cell-26:20` · open_question

## Session 4 · Lab C – DuckDB as a database file / Exam-style questions

- What is the difference between a TABLE created with CREATE TABLE ... AS SELECT and a VIEW? What happens to each when new rows are inserted into trips?
  - `session-04/03_duckdb_database.ipynb#cell-26:15` · exam_prompt
- You run DELETE FROM trips WHERE payment_type = 2 inside BEGIN TRANSACTION and then ROLLBACK. How many rows does trips have afterwards, and which ACID property does this demonstrate?
  - `session-04/03_duckdb_database.ipynb#cell-26:17` · exam_prompt

## Part 2 · Spark ML: how long will my taxi ride take? / Exam-style questions

- Why is fare_amount (or total_amount) not allowed as a feature for predicting the trip duration here? Name the general problem.
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:16` · exam_prompt
- A colleague writes df2 = df.filter(...), df3 = df2.select(...), df4 = df3.groupBy("PULocationID").count() and says: "Three lines, so Spark ran three operations immediately." Is she right? When does computation start?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:4` · exam_prompt
- df.filter(F.col("fare_amount") > 50).show(10) returns 10 rows. Did Spark read only 10 rows? Explain.
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:8` · exam_prompt
- Joining 3 million trips with the 265-row zone table, the plan shows BroadcastHashJoin. Why? What is the benefit compared with a sort-merge join, and what could go wrong if you broadcast a very large table?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:9` · exam_prompt

## Part 2 · Spark ML: how long will my taxi ride take? / Homework

- Train the gradient-boosted trees without trip_distance (only haversine_km). How much worse does it get?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:29` · open_question

## Block 3 – Exam circuit / Station 2 – File formats and engines

- 2.2 (3 P) A Parquet file and a CSV file contain the same 19 columns of 50 million trips. Give three reasons why avg(trip_distance) is much faster on the Parquet file.
  - `session-06/03_exam_circuit.md:36` · exam_prompt

## gitdiff / Station 4 – Spark execution: lazy evaluation and shuffles

- AdaptiveSparkPlan isFinalPlan=false +- Sort [trips#120L DESC NULLS LAST], true, 0 +- Exchange rangepartitioning(trips#120L DESC NULLS LAST, 200) +- HashAggregate(keys=[Zone#45], functions=[count(1)]) +- Exchange hashpartitioning(Zone#45, 200) +- HashAggregate(keys=[Zone#45], functions=[partial_count(1)]) +- Project [Zone#45] +- BroadcastHashJoin [PULocationID#7], [LocationID#44], Inner, BuildRight :- Filter (isnotnull(trip_distance#4) AND (trip_distance#4 > 0.0)) : +- FileScan parquet [trip_distance#4,PULocationID#7] : PushedFilters: [IsNotNull(trip_distance), GreaterThan(trip_distance,0.0)], : ReadSchema: struct +- BroadcastExchange HashedRelationBroadcastMode(...) +- FileScan csv [LocationID#44,Zone#45]
  - `03_exam_circuit-gitdiff.md:281` · exam_prompt
