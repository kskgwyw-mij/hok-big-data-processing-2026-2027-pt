---
title: Questions: Python Execution Model
type: questions
topic: python.execution
question_count: 6
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Python Execution Model

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Warm-up – Threads vs. Processes (and why pandas is slow)

- Question: Why do threads bring no speed-up here?
  - `session-01/00_warmup_threads_vs_processes.ipynb#cell-6:1` · open_question

## Session 1 – Do you really need a cluster? / The question

- At which hour of the day do passengers tip the most (as % of the fare)?
  - `session-01/01_do_you_need_a_cluster.ipynb#cell-5:2` · open_question

## Bonus – Python without the GIL / Questions

- Polars, DuckDB and Spark were fast in the main lab – with the normal Python build. How do they avoid the GIL problem without a free-threaded Python?
  - `session-01/02_bonus_python_without_gil.ipynb#cell-9:11` · open_question
- Look at JOBS in the script and at section 1: how many physical cores does your machine have?
  - `session-01/02_bonus_python_without_gil.ipynb#cell-9:5` · open_question
- What limits the speed-up of run 3?
  - `session-01/02_bonus_python_without_gil.ipynb#cell-9:5` · open_question

## Big Data Processing – Mock exam / Part A – Foundations

- A4 (2 P) What is the Global Interpreter Lock (GIL) in CPython, and what does it prevent?
  - `04_mock_exam-gitdiff.md:158` · exam_prompt
