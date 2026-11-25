---
title: Single-Machine Engines
type: decisions
topic: engines.single_machine
entity_ids:
  - ent_pandas
  - ent_duckdb
  - ent_polars
  - ent_gil
  - ent_kafka
  - ent_pyarrow
  - ent_scikit_learn
  - ent_code
  - ent_csv
  - ent_faker
  - ent_jupyter
  - ent_parquet
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
confidence: 0.679
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_46087206
  - src_6e2e5684
  - src_96e79681
  - src_b3356305
  - src_ffd1cdcc
review_required: false
---

# Single-Machine Engines

Rendered from 12 claims and 6 sources. Median confidence 0.68; 11 active, 0 disputed, 0 superseded.

## Current Understanding

### Discussion

**Why are Polars and DuckDB faster even on the same single machine? (Think: GIL, cores, columnar layout, lazy plans.).**
Confidence 0.67 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-20:2` — “1. Why are Polars and DuckDB faster even on the same single machine? (Think: GIL, cores, columnar layout, lazy plans.)”

**Name two situations where a single machine is not enough, even with DuckDB. → That is where Spark (next session) comes in.**
Confidence 0.61 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-20:4` — “3. Name two situations where a single machine is not enough, even with DuckDB. → That is where Spark (next session) comes in.”

### Really need cluster

**Engine: pandas — Execution model: eager, (mostly) single-threaded, everything in RAM.**
Confidence 0.70 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:8` — “pandas | eager, (mostly) single-threaded, everything in RAM”

**Engine: Polars — Execution model: lazy query plans, multi-threaded, columnar (Arrow).**
Confidence 0.70 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:9` — “Polars | lazy query plans, multi-threaded, columnar (Arrow)”

### Duckdb talks pandas polars arrow

**DuckDB can also query a pandas DataFrame by its variable name.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-21:2` — “Results convert with .df(), .pl() or .arrow(). DuckDB can also query a pandas DataFrame by its variable name.”

### Export results

**Read the file back with pandas to check it.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-23:2` — “Your turn (5 min): export the average duration and trip count per pickup borough and hour of day to ../data/borough_hour.parquet with COPY (...) TO ... (FORMAT parquet). Read the file back…”

### Modern shortcut uv

**Uv init --python 3.12 ; uv add pandas duckdb.**
Confidence 0.72 · active · 2 sources
Evidence: `README.md:7` — “Your laptop – VS Code + Python 3.12 in a virtual environment | pandas, Polars, DuckDB, file formats, scikit-learn, Kafka (Session 6)”

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

### Takeaways

**Bridge to the main lab: pandas runs most operations on one core.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:7` — “Bridge to the main lab: pandas runs most operations on one core. Polars (Rust) and DuckDB (C++) run their work outside the GIL on all cores – no multiprocessing tricks needed. Spark goes…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 1 | 2026-10-28 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 2 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `README.md` | readme | 0.85 | 3 | 2026-11-11 |
| `session-01/00_warmup_threads_vs_processes.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |

## Related Pages

- [[data-formats|File Formats]] (26 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (19 shared entities)
- [[python-execution|Python Execution Model]] (15 shared entities)
- [[course-exam|Exam]] (12 shared entities)
- [[data-duckdb|DuckDB]] (10 shared entities)
- [[course-setup|Course Setup]] (9 shared entities)

## Open Questions

8 prompts from the material are collected in [[questions/engines-single_machine|Questions: Single-Machine Engines]].
- Look at the plan: which columns end up in the scan (projection pushdown)?
- Where does the filter end up (predicate pushdown)?
- Estimate: how many months of taxi data could this machine handle with DuckDB? What limits it – RAM, disk, or CPU?

## Timeline

- 2026-11-25: new_claim on `claim_bcb1bb0e`
- 2026-11-25: new_claim on `claim_67f89ee2`
- 2026-11-25: new_claim on `claim_5ad49bc2`
- 2026-11-25: new_claim on `claim_39776e54`
- 2026-11-25: new_claim on `claim_4eef0593`
- 2026-11-25: new_claim on `claim_3ed72880`
- 2026-11-25: support_update on `claim_f0092822` (0.49 → 0.72)
- 2026-11-25: new_claim on `claim_8b05e9fa`
