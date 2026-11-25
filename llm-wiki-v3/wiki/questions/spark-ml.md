---
title: Questions: Spark ML
type: questions
topic: spark.ml
question_count: 5
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Spark ML

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Part 2 · Spark ML: how long will my taxi ride take? / Exam-style questions

- Transformer or Estimator: StringIndexer, OneHotEncoder, VectorAssembler, LinearRegression? What does Pipeline.fit() return?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:18` · exam_prompt
- A CrossValidator with 3 × 2 parameter values and numFolds=5: how many models are trained? Why did we tune on a sample?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:21` · exam_prompt

## Block 3 – Exam circuit / Station 5 – Environments, saving data, DuckDB, Spark ML

- 5.3 (4 P) (a) Transformer or Estimator: StringIndexer, VectorAssembler, LinearRegression. (b) A CrossValidator with a 3 × 2 parameter grid and numFolds=5: how many model fits in total? (c) We predict the trip duration at pickup. Why is fare_amount not allowed as a feature? Name the problem.
  - `session-06/03_exam_circuit.md:99` · exam_prompt

## Big Data Processing – Mock exam / Part D – Spark ML and joins

- D3 (2 P) Transformer or Estimator: StringIndexer, VectorAssembler, LinearRegression. What type of object does Pipeline.fit() return?
  - `04_mock_exam-gitdiff.md:217` · exam_prompt
- D4 (1 P) CrossValidator with a parameter grid of 3 × 2 values and numFolds=5. How many model fits in total, including the final refit?
  - `04_mock_exam-gitdiff.md:220` · exam_prompt
