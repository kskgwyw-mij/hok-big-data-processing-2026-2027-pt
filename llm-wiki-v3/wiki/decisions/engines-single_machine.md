---
title: Single-Machine Engines
type: decisions
topic: engines.single_machine
entity_ids:
  - ent_pandas
  - ent_polars
  - ent_duckdb
  - ent_spark
  - ent_parquet
  - ent_predicate_pushdown
  - ent_pyarrow
  - ent_gil
  - ent_kafka
  - ent_lazy_evaluation
  - ent_python
  - ent_scikit_learn
claim_ids:
  - claim_f0092822
  - claim_c038caf5
  - claim_c906b83c
  - claim_c30f9546
  - claim_af9a5b8d
  - claim_bcb1bb0e
  - claim_67f89ee2
  - claim_5ad49bc2
  - claim_39776e54
  - claim_4eef0593
  - claim_3ed72880
  - claim_8b05e9fa
  - claim_109c744c
  - claim_4eed488d
  - claim_d3def11e
  - claim_0dea7a71
  - claim_bd2a6262
  - claim_b9ec74c0
  - claim_07425f5c
  - claim_49fe41c6
  - claim_5584689f
  - claim_2e41dff4
  - claim_9ccb2228
  - claim_53d0fe6b
  - claim_e10a91e7
  - claim_b42cd60d
  - claim_24464bf6
confidence: 0.703
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_1cebb3bb
  - src_46087206
  - src_59b6ded4
  - src_68fcf2b9
  - src_6e2e5684
  - src_70f9fe3e
  - src_96e79681
  - src_b3356305
  - src_ffd1cdcc
review_required: false
---

# Single-Machine Engines

Rendered from 27 claims and 10 sources. Median confidence 0.70; 26 active, 0 disputed, 0 superseded.

## Current Understanding

### Discussion

**Why are Polars and DuckDB faster even on the same single machine? (Think: GIL, cores, columnar layout, lazy plans.).**
Confidence 0.67 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-20:2` — “1. Why are Polars and DuckDB faster even on the same single machine? (Think: GIL, cores, columnar layout, lazy plans.)”

**Name two situations where a single machine is not enough, even with DuckDB. → That is where Spark (next session) comes in.**
Confidence 0.61 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-20:4` — “3. Name two situations where a single machine is not enough, even with DuckDB. → That is where Spark (next session) comes in.”

### Really need cluster

**Engine: Polars — Execution model: lazy query plans, multi-threaded, columnar (Arrow).**
Confidence 0.89 · active · 3 sources
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:9` — “Polars | lazy query plans, multi-threaded, columnar (Arrow)”

**Engine: pandas — Execution model: eager, (mostly) single-threaded, everything in RAM.**
Confidence 0.70 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:8` — “pandas | eager, (mostly) single-threaded, everything in RAM”

### Duckdb talks pandas polars arrow

**DuckDB can also query a pandas DataFrame by its variable name.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-21:2` — “Results convert with .df(), .pl() or .arrow(). DuckDB can also query a pandas DataFrame by its variable name.”

### Export results

**Read the file back with pandas to check it.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-23:2` — “Your turn (5 min): export the average duration and trip count per pickup borough and hour of day to ../data/borough_hour.parquet with COPY (...) TO ... (FORMAT parquet). Read the file back…”

### Fault tolerance reliability in memory

**» Fault tolerance & reliability » In-memory processing for improved performance » Seamless integration with various data sources and frameworks incl.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p91:3` — “» Fault tolerance & reliability » In-memory processing for improved performance » Seamless integration with various data sources and frameworks incl. Hadoop, Cassandra DB and SQL DB »…”

### Lazy evaluation

**Lazy evaluation: plan first, then run.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p55:1` — “Lazy evaluation: plan first, then run”

### Lazy evaluation create rdds

**» Create new RDDs by applying » Return results or perform computation/manipulation actions on RDD, triggering » Lazy evaluation, lineage graph execution » Examples: map, filter, flatMap, » Eager evaluation, data reduceByKey sortBy, join movement/computation » Examples: collect, count, first, take, save, foreach.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p119:5` — “» Create new RDDs by applying » Return results or perform computation/manipulation actions on RDD, triggering » Lazy evaluation, lineage graph execution » Examples: map, filter, flatMap, »…”

### Modern shortcut uv

**Uv init --python 3.12 ; uv add pandas duckdb.**
Confidence 0.72 · active · 2 sources
Evidence: `README.md:7` — “Your laptop – VS Code + Python 3.12 in a virtual environment | pandas, Polars, DuckDB, file formats, scikit-learn, Kafka (Session 6)”

### Pandas import pd

**Import pandas as pd import pandas as pd print(pd.version, print(pd.version, pd.Series(['a','b']).dtype) pd.Series(['a','b']).dtype) 2.3.3 object 3.1.0 str.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p6:7` — “import pandas as pd import pandas as pd print(pd.version, print(pd.version, pd.Series(['a','b']).dtype) pd.Series(['a','b']).dtype) 2.3.3 object 3.1.0 str”

### Pandas polars rebuilt

**Polars: pandas, rebuilt for modern hardware.**
Confidence 0.66 · active · 1 source · when: for modern hardware
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p57:1` — “Polars: pandas, rebuilt for modern hardware”

### Pandas streaming engine process

**A streaming engine can also process data larger than RAM. » Strengths: very fast, memory-efficient, a clear expression API (pl.col(...)), no confusing index. » Weaknesses: a different syntax than pandas, and some libraries still expect a pandas DataFrame (.to_pandas() helps). » Link: https://pola.rs.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p57:3` — “» What it is: a DataFrame library written in Rust (since 2020), with Apache Arrow as its memory format. » How it runs: lazy with scan_parquet() / .lazy(): first it builds a query plan,…”

### Pandas web software development

**» Web & software development e.g. Django » Task automation e.g. smtplib (automate emails), shutil (copy files), Pytest (automate tests), etc. » Machine Learning & Data Science e.g. NumPy, Pandas, Matplotlib, Tensorflow, PyTorch, etc. » Financial Analysis e.g. PyBrain » Much more.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p74:3` — “» Web & software development e.g. Django » Task automation e.g. smtplib (automate emails), shutil (copy files), Pytest (automate tests), etc. » Machine Learning & Data Science e.g. NumPy,…”

### Parquet column binary

**Parquet column · binary typed, also nested analytics, data lakes, Spark, DuckDB, Polars.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p51:14` — “Parquet column · binary typed, also nested analytics, data lakes, Spark, DuckDB, Polars”

### Predicate cores pushdown filter

**Predicate all cores. pushdown: filter while reading.**
Confidence 0.66 · active · 1 source · when: while reading
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p55:6` — “Your query Optimizer Execution filter → new columns → group Projection pushdown: read 4 of Parallel, column by column, on by → aggregate 19 columns. Predicate all cores. pushdown: filter…”

### Predicate pushdown built in optimization

**» Built-in Optimization: » Leveraging Spark's Catalyst optimizer for advanced optimizations. » Predicate pushdown, constant folding, loop unrolling. » Interoperability: » Easily convert to/from other data formats (e.g., Pandas DataFrames). » Seamless integration with other data processing tools.**
Confidence 0.70 · active · 1 source · when: for advanced optimizations
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p124:3` — “» Built-in Optimization: » Leveraging Spark's Catalyst optimizer for advanced optimizations. » Predicate pushdown, constant folding, loop unrolling. » Interoperability: » Easily convert…”

### Predicate pushdown is dataframe

**» What it is: a DataFrame library written in Rust (since 2020), with Apache Arrow as its memory format. » How it runs: lazy with scan_parquet() / .lazy(): first it builds a query plan, optimizes it (projection and predicate pushdown), then executes it.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p57:3` — “» What it is: a DataFrame library written in Rust (since 2020), with Apache Arrow as its memory format. » How it runs: lazy with scan_parquet() / .lazy(): first it builds a query plan,…”

### Projection pushdown query optimizer

**Your query Optimizer Execution filter → new columns → group Projection pushdown: read 4 of Parallel, column by column, on by → aggregate 19 columns.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p55:6` — “Your query Optimizer Execution filter → new columns → group Projection pushdown: read 4 of Parallel, column by column, on by → aggregate 19 columns. Predicate all cores. pushdown: filter…”

### Python project needs

**Project A needs Python 3.12, project B still runs on Project A needs pandas 3, project B breaks with 3.10. pandas 3.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p7:5` — “Which Python version? Which packages, in which versions? Project A needs Python 3.12, project B still runs on Project A needs pandas 3, project B breaks with 3.10. pandas 3.”

### Reading execution plan

**Symbol: Filter — Meaning: A predicate applied at scan time (predicate pushdown).**
Confidence 0.70 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:17` — “Filter | A predicate applied at scan time (predicate pushdown)”

### Requirements file

**File: requirements-local.txt — Contains: pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6); Use it for: your laptop (default).**
Confidence 0.69 · active · 1 source
Evidence: `README.md:72` — “requirements-local.txt | pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6) | your laptop (default)”

### Scaling experiment

**Where does pandas break down on your machine? pandas is skipped automatically once it would run out of memory – a crash would kill the whole kernel.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-18:2` — “Run the query on 1, 2, 4, … months. Where does pandas break down on your machine? pandas is skipped automatically once it would run out of memory – a crash would kill the whole kernel.”

### Sessions folders

**Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.**
Confidence 0.73 · active · 1 source
Evidence: `README.md:129` — “session-01/ | Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL | laptop”

### Spark pandas vs side

**Pandas 2 vs. 3 side by side · 10 min PySpark (≈ 400 MB) runs on Kaggle today –> install it at home.**
Confidence 0.75 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p13:9` — “3. pandas 2 vs. 3 side by side · 10 min PySpark (≈ 400 MB) runs on Kaggle today –> install it at home.”

### Takeaways

**Bridge to the main lab: pandas runs most operations on one core.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:7` — “Bridge to the main lab: pandas runs most operations on one core. Polars (Rust) and DuckDB (C++) run their work outside the GIL on all cores – no multiprocessing tricks needed. Spark goes…”

### Transformation optimized execution schema

**» Optimized Execution: » Schema information enables query optimization and predicate pushdowns. » Faster and more efficient data processing. » Ease of Use: » High-level, SQL-like interface for data interaction. » Simplified compared to complex RDD transformations. » Integration with Ecosystem: » Seamless integration with Spark's ecosystem (Spark SQL, MLlib, GraphX). » Leverage various libraries and functionalities.**
Confidence 0.74 · active · 1 source · when: for data interaction
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p123:3` — “» Optimized Execution: » Schema information enables query optimization and predicate pushdowns. » Faster and more efficient data processing. » Ease of Use: » High-level, SQL-like interface…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 1 | 2026-10-28 |
| `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 3 | 2026-11-25 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 5 | 2026-11-25 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 2 | 2026-10-28 |
| `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf` | lecture_note | 0.92 | 8 | 2026-11-25 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `README.md` | readme | 0.85 | 3 | 2026-11-11 |
| `session-01/00_warmup_threads_vs_processes.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |

## Related Pages

- [[data-formats|File Formats]] (48 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (39 shared entities)
- [[python-execution|Python Execution Model]] (25 shared entities)
- [[data-duckdb|DuckDB]] (23 shared entities)
- [[course-exam|Exam]] (18 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (17 shared entities)

## Open Questions

9 prompts from the material are collected in [[questions/engines-single_machine|Questions: Single-Machine Engines]].
- C7 (2 P) Polars scan_parquet is lazy. Name the two pushdown optimisations and what each one saves.
- What do you tell them? » 2 GB of data, laptop with 16 GB RAM: Spark, DuckDB or pandas + scikit-learn?
- Look at the plan: which columns end up in the scan (projection pushdown)?

## Timeline

- 2026-11-25: new_claim on `claim_5584689f`
- 2026-11-25: support_update on `claim_c906b83c` (0.81 → 0.89)
- 2026-11-25: new_claim on `claim_2e41dff4`
- 2026-11-25: new_claim on `claim_9ccb2228`
- 2026-11-25: new_claim on `claim_53d0fe6b`
- 2026-11-25: new_claim on `claim_e10a91e7`
- 2026-11-25: new_claim on `claim_b42cd60d`
- 2026-11-25: new_claim on `claim_24464bf6`
