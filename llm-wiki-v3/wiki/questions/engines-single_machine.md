---
title: Questions: Single-Machine Engines
type: questions
topic: engines.single_machine
question_count: 9
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: Single-Machine Engines

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part C – Python environments, file formats, DuckDB

- C7 (2 P) Polars scan_parquet is lazy. Name the two pushdown optimisations and what each one saves.
  - `raw/04_mock_exam.md:76` · exam_prompt

## General

- What do you tell them? » 2 GB of data, laptop with 16 GB RAM: Spark, DuckDB or pandas + scikit-learn?
  - `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p40:3` · open_question

## Session 1 – Do you really need a cluster? / The question

- Look at the plan: which columns end up in the scan (projection pushdown)?
  - `session-01/01_do_you_need_a_cluster.ipynb#cell-10:1` · open_question
- Where does the filter end up (predicate pushdown)?
  - `session-01/01_do_you_need_a_cluster.ipynb#cell-10:1` · open_question
- Your turn (5 min): How many columns did pandas read, and how many did we actually need?
  - `session-01/01_do_you_need_a_cluster.ipynb#cell-7:1` · open_question

## Session 1 – Do you really need a cluster? / Discussion

- Estimate: how many months of taxi data could this machine handle with DuckDB? What limits it – RAM, disk, or CPU?
  - `session-01/01_do_you_need_a_cluster.ipynb#cell-20:3` · open_question

## Lab A – Python environments: venv, pyenv and uv / Exam-style questions

- Your notebook runs on your laptop but fails on the server with AttributeError in pandas. Name two files you should have put into the repository to prevent this, and what each contains.
  - `session-04/01_python_environments.md:178` · exam_prompt

## Part 2 · Spark ML: how long will my taxi ride take? / Exam-style questions

- The same task with 2 GB of data on a laptop with 16 GB RAM: Spark, DuckDB or pandas + scikit-learn? Justify.
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:25` · exam_prompt

## Block 3 – Exam circuit / Station 2 – File formats and engines

- 2.3 (4 P) Polars scan_parquet(...).filter(...).select(...) vs. pandas read_parquet(...) followed by the same filter and selection. Explain lazy evaluation and the two optimisations projection pushdown and predicate pushdown. Why can pandas not do them?
  - `session-06/03_exam_circuit.md:39` · exam_prompt
