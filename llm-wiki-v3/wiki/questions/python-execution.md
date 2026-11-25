---
title: Questions: Python Execution Model
type: questions
topic: python.execution
question_count: 11
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: Python Execution Model

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part A – Foundations

- A4 (2 P) What is the Global Interpreter Lock (GIL) in CPython, and what does it prevent?
  - `raw/04_mock_exam.md:28` · exam_prompt
- A5 (2 P) Threads or processes? Give one word and a half-sentence reason for each: (a) downloading 200 files from an API, (b) a pure-Python numerical loop that should use all 8 cores.
  - `raw/04_mock_exam.md:30` · exam_prompt

## General

- 1 · Chores 2 · CPU-bound 3 · I/O-bound Waiting tasks: single thread, threads, Why do threads bring no speed-up?
  - `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p40:6` · open_question
- How many threads until it stops processes. helping?
  - `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p40:6` · open_question
- » Parallelism is essential for optimizing data science workflows. » Multithreading and multiprocessing can handle intensive tasks efficiently. » How do threads and processes differ, and when should you use them?
  - `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p41:4` · open_question

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

## Block 3 – Exam circuit / Station 1 – Do you need a cluster?

- 1.3 (4 P) Two jobs, one laptop with 8 cores: (a) download 300 Parquet files from a web server, (b) compute a feature with a pure-Python loop over 50 million rows. For each job: threads or processes? Justify with the GIL.
  - `session-06/03_exam_circuit.md:22` · exam_prompt
