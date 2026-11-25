---
title: Questions: DuckDB
type: questions
topic: data.duckdb
question_count: 8
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: DuckDB

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Session 4 · Lab C – DuckDB as a database file / Exam-style questions

- Explain the difference between duckdb.connect() and duckdb.connect("taxi.duckdb"). Give one situation for each.
  - `session-04/03_duckdb_database.ipynb#cell-26:11` · exam_prompt
- Why is DuckDB called an embedded database? Name one advantage and one limitation that follow from this.
  - `session-04/03_duckdb_database.ipynb#cell-26:12` · exam_prompt
- Scenario: a team of 30 analysts wants a shared dashboard that writes user annotations back to the database every few seconds. Is a single DuckDB file a good choice? Justify and propose an alternative.
  - `session-04/03_duckdb_database.ipynb#cell-26:13` · exam_prompt
- What is the difference between a TABLE created with CREATE TABLE ... AS SELECT and a VIEW? What happens to each when new rows are inserted into trips?
  - `session-04/03_duckdb_database.ipynb#cell-26:15` · exam_prompt
- You run DELETE FROM trips WHERE payment_type = 2 inside BEGIN TRANSACTION and then ROLLBACK. How many rows does trips have afterwards, and which ACID property does this demonstrate?
  - `session-04/03_duckdb_database.ipynb#cell-26:17` · exam_prompt
- Compare the size of your .duckdb file with the Parquet input. Why are both in the same order of magnitude, while a CSV export of the same table would be several times larger?
  - `session-04/03_duckdb_database.ipynb#cell-26:19` · exam_prompt

## Block 3 – Exam circuit / Station 5 – Environments, saving data, DuckDB, Spark ML

- 5.2 (3 P) (a) Someone posts best_model.pkl in a forum. Why should you not load it? (b) Five Python processes want to write into the same taxi.duckdb file at the same time. What happens, and why?
  - `session-06/03_exam_circuit.md:96` · exam_prompt

## Big Data Processing – Mock exam / Part C – Python environments, file formats, DuckDB

- C6 (2 P) Why is DuckDB called an embedded database? Name one consequence for concurrent writing.
  - `04_mock_exam-gitdiff.md:204` · exam_prompt
