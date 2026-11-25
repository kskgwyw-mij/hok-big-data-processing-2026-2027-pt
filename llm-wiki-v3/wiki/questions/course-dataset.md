---
title: Questions: NYC Yellow Taxi Dataset
type: questions
topic: course.dataset
question_count: 9
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: NYC Yellow Taxi Dataset

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Session 2 – Apache Spark Fundamentals / Part 6 – Group Work: NYC Taxi Analysis / Task A – Core (everyone)

- Question: Which pickup location IDs generated the most taxi trips in January 2024?
  - `session-02/02_spark_fundamentals.ipynb#cell-26:20` · open_question

## Part 2 · Spark ML: how long will my taxi ride take? / Exam-style questions

- Why is fare_amount (or total_amount) not allowed as a feature for predicting the trip duration here? Name the general problem.
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:16` · exam_prompt
- A colleague writes df2 = df.filter(...), df3 = df2.select(...), df4 = df3.groupBy("PULocationID").count() and says: "Three lines, so Spark ran three operations immediately." Is she right? When does computation start?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:4` · exam_prompt
- df.filter(F.col("fare_amount") > 50).show(10) returns 10 rows. Did Spark read only 10 rows? Explain.
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:8` · exam_prompt

## Part 2 · Spark ML: how long will my taxi ride take? / Homework

- Train the gradient-boosted trees without trip_distance (only haversine_km). How much worse does it get?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:29` · open_question

## Block 3 – Exam circuit / Station 2 – File formats and engines

- 2.2 (3 P) A Parquet file and a CSV file contain the same 19 columns of 50 million trips. Give three reasons why avg(trip_distance) is much faster on the Parquet file.
  - `session-06/03_exam_circuit.md:36` · exam_prompt

## gitdiff / Station 4 – Spark execution: lazy evaluation and shuffles

- AdaptiveSparkPlan isFinalPlan=false +- Sort [trips#120L DESC NULLS LAST], true, 0 +- Exchange rangepartitioning(trips#120L DESC NULLS LAST, 200) +- HashAggregate(keys=[Zone#45], functions=[count(1)]) +- Exchange hashpartitioning(Zone#45, 200) +- HashAggregate(keys=[Zone#45], functions=[partial_count(1)]) +- Project [Zone#45] +- BroadcastHashJoin [PULocationID#7], [LocationID#44], Inner, BuildRight :- Filter (isnotnull(trip_distance#4) AND (trip_distance#4 > 0.0)) : +- FileScan parquet [trip_distance#4,PULocationID#7] : PushedFilters: [IsNotNull(trip_distance), GreaterThan(trip_distance,0.0)], : ReadSchema: struct +- BroadcastExchange HashedRelationBroadcastMode(...) +- FileScan csv [LocationID#44,Zone#45]
  - `03_exam_circuit-gitdiff.md:281` · exam_prompt

## Big Data Processing – Mock exam / Part D – Spark ML and joins

- D1 (1 P) Narrow or wide transformation: groupBy("PULocationID").agg(avg("fare_amount"))?
  - `04_mock_exam-gitdiff.md:212` · exam_prompt
- D5 (2 P) Define target leakage and give an example from the taxi trip-duration model.
  - `04_mock_exam-gitdiff.md:223` · exam_prompt
