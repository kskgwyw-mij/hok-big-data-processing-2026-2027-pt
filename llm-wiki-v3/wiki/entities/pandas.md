---
title: pandas
type: entity
entity_id: ent_pandas
entity_type: technology
claim_ids:
  - claim_f0092822
  - claim_30d231b5
  - claim_c038caf5
  - claim_c30f9546
  - claim_67f89ee2
  - claim_5ad49bc2
  - claim_b33f16f1
  - claim_4eef0593
  - claim_3ed72880
  - claim_8b05e9fa
confidence: 0.662
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_46087206
  - src_6e2e5684
  - src_8e87808f
  - src_b3356305
  - src_ffd1cdcc
---

# pandas

Type: technology. Mentioned in 10 claims across 3 topics.
Aliases: pd.

## Claims

- **Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.** Confidence 0.73 · [[engines-single_machine|Single-Machine Engines]]
- **Problem: Which Python version? — Example: Project A needs 3.12, project B still runs on 3.10; Tool: pyenv (or uv python).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Uv init --python 3.12 ; uv add pandas duckdb.** Confidence 0.72 · [[engines-single_machine|Single-Machine Engines]]
- **Engine: pandas — Execution model: eager, (mostly) single-threaded, everything in RAM.** Confidence 0.70 · [[engines-single_machine|Single-Machine Engines]]
- **File: requirements-local.txt — Contains: pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6); Use it for: your laptop (default).** Confidence 0.69 · [[engines-single_machine|Single-Machine Engines]]
- **Bridge to the main lab: pandas runs most operations on one core.** Confidence 0.63 · [[engines-single_machine|Single-Machine Engines]]
- **DuckDB can also query a pandas DataFrame by its variable name.** Confidence 0.63 · [[engines-single_machine|Single-Machine Engines]]
- **Where does pandas break down on your machine? pandas is skipped automatically once it would run out of memory – a crash would kill the whole kernel.** Confidence 0.63 · [[engines-single_machine|Single-Machine Engines]]
- **The same applies to pd.read_pickle, joblib.load and older model files from the internet.** Confidence 0.63 · [[data-formats|File Formats]]
- **Read the file back with pandas to check it.** Confidence 0.59 · [[engines-single_machine|Single-Machine Engines]]

## Related Entities

- [[duckdb|DuckDB]] (4)
- [[polars|Polars]] (3)
- [[kafka|Kafka]] (2)
- [[scikit_learn|scikit-learn]] (2)
- [[uv|uv]] (2)
- [[venv|venv]] (2)
- [[csv|CSV]] (1)
- [[faker|Faker]] (1)
- [[gil|GIL]] (1)
- [[jupyter|Jupyter]] (1)
