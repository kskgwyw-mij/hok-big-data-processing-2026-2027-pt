---
title: DuckDB
type: entity
entity_id: ent_duckdb
entity_type: technology
claim_ids:
  - claim_f0092822
  - claim_27aa18e7
  - claim_af9a5b8d
  - claim_bcb1bb0e
  - claim_23fa33c6
  - claim_80c6829c
  - claim_0afdc8ea
  - claim_8aef6073
  - claim_2e817f5a
  - claim_88fd804c
  - claim_0b06c681
  - claim_84cba204
  - claim_67f89ee2
  - claim_95fe6516
  - claim_b01c67aa
  - claim_854a0f56
  - claim_fbfe301b
  - claim_3ed72880
  - claim_6fb4e772
  - claim_8b05e9fa
  - claim_dfe154cd
confidence: 0.694
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_46087206
  - src_47132aab
  - src_6494d099
  - src_6e2e5684
  - src_8e87808f
  - src_b3356305
  - src_c65c80a3
  - src_ffd1cdcc
---

# DuckDB

Type: technology. Mentioned in 21 claims across 5 topics.
Aliases: duckdb.

## Claims

- **Part: C — Topic: Python environments, file formats, DuckDB; Points: 12.** Confidence 0.80 · [[course-exam|Exam]]
- **Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.** Confidence 0.73 · [[engines-single_machine|Single-Machine Engines]]
- **Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).** Confidence 0.72 · [[data-formats|File Formats]]
- **Uv init --python 3.12 ; uv add pandas duckdb.** Confidence 0.72 · [[engines-single_machine|Single-Machine Engines]]
- **In the comparison table, Tables survive closing Python: in-memory (duckdb.connect()): no, database file (duckdb.connect("taxi.duckdb")): yes.** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **Engine: DuckDB — Execution model: SQL engine, multi-threaded, vectorized, can stream from disk.** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **In the comparison table, Typical use: in-memory (duckdb.connect()): quick queries on files, database file (duckdb.connect("taxi.duckdb")): a local analytics database / small warehouse.** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **In the comparison table, Keeps dtypes: CSV: no, pickle: yes, Parquet: yes.** Confidence 0.69 · [[data-formats|File Formats]]
- **In the comparison table, Data stored in: in-memory (duckdb.connect()): RAM (spills to disk if needed), database file (duckdb.connect("taxi.duckdb")): one compressed, columnar file.** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **In the comparison table, Storage layout: DuckDB: columnar, SQLite: row, PostgreSQL: row, Spark: files (Parquet/Delta).** Confidence 0.69 · [[data-formats|File Formats]]
- **File: requirements-local.txt — Contains: pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6); Use it for: your laptop (default).** Confidence 0.69 · [[engines-single_machine|Single-Machine Engines]]
- **Lab: C — Topic: DuckDB as a database file – homework; Where: laptop, notebook; File: 03_duckdb_database.ipynb.** Confidence 0.68 · [[data-duckdb|DuckDB]]
- **DuckDB is an embedded database: it runs inside your Python process, there is no server in between.** Confidence 0.68 · [[data-duckdb|DuckDB]]
- **Why are Polars and DuckDB faster even on the same single machine? (Think: GIL, cores, columnar layout, lazy plans.).** Confidence 0.67 · [[engines-single_machine|Single-Machine Engines]]
- **DuckDB can also query a pandas DataFrame by its variable name.** Confidence 0.63 · [[engines-single_machine|Single-Machine Engines]]
- **DuckDB is a real database: changes happen inside transactions and can be rolled back.** Confidence 0.63 · [[data-duckdb|DuckDB]]
- **In Session 1 you used DuckDB in memory: duckdb.connect() and SQL straight on Parquet files.** Confidence 0.63 · [[data-duckdb|DuckDB]]
- **Polars (Rust) and DuckDB (C++) run their work outside the GIL on all cores – no multiprocessing tricks needed.** Confidence 0.63 · [[python-execution|Python Execution Model]]
- **Name two situations where a single machine is not enough, even with DuckDB. → That is where Spark (next session) comes in.** Confidence 0.61 · [[engines-single_machine|Single-Machine Engines]]
- **Lab C (03_duckdb_database.ipynb) on your laptop, including the exam-style questions.** Confidence 0.61 · [[course-exam|Exam]]

## Related Entities

- [[polars|Polars]] (6)
- [[parquet|Parquet]] (5)
- [[spark|Spark]] (5)
- [[pandas|pandas]] (4)
- [[topic|topic]] (4)
- [[gil|GIL]] (3)
- [[csv|CSV]] (2)
- [[kafka|Kafka]] (2)
- [[pickle|Pickle]] (2)
- [[scikit_learn|scikit-learn]] (2)
