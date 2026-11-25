---
title: DuckDB
type: systems
topic: data.duckdb
entity_ids:
  - ent_duckdb
  - ent_jupyter
  - ent_olap
  - ent_oltp
  - ent_parquet
  - ent_pip
  - ent_python
  - ent_spark_job
  - ent_topic
  - ent_case
  - ent_ctas
  - ent_filter
claim_ids:
  - claim_27aa18e7
  - claim_80c6829c
  - claim_0afdc8ea
  - claim_8aef6073
  - claim_2e817f5a
  - claim_88fd804c
  - claim_3ed43c97
  - claim_0b06c681
  - claim_84cba204
  - claim_1ba61905
  - claim_95fe6516
  - claim_6f06a285
  - claim_84e46e85
  - claim_2ab2e812
  - claim_dd944da3
  - claim_8582a503
  - claim_f76b7cb7
  - claim_8f88ff28
  - claim_eeeb42e4
  - claim_6bada748
  - claim_7abd95da
  - claim_87c7b259
  - claim_2b441de7
  - claim_48d35ee7
confidence: 0.689
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_46087206
  - src_59b6ded4
  - src_6494d099
  - src_6e2e5684
  - src_8615b91f
  - src_e258bafb
review_required: false
---

# DuckDB

Rendered from 24 claims and 6 sources. Median confidence 0.69; 22 active, 0 disputed, 0 superseded.

## Current Understanding

### Lab c duckdb database file

**In the comparison table, Tables survive closing Python: in-memory (duckdb.connect()): no, database file (duckdb.connect("taxi.duckdb")): yes.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-0:11` — “Tables survive closing Python | no | yes”

**In the comparison table, Typical use: in-memory (duckdb.connect()): quick queries on files, database file (duckdb.connect("taxi.duckdb")): a local analytics database / small warehouse.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-0:13` — “Typical use | quick queries on files | a local analytics database / small warehouse”

**In the comparison table, Data stored in: in-memory (duckdb.connect()): RAM (spills to disk if needed), database file (duckdb.connect("taxi.duckdb")): one compressed, columnar file.**
Confidence 0.69 · active · 1 source · when: if needed)
Evidence: `session-04/03_duckdb_database.ipynb#cell-0:12` — “Data stored in | RAM (spills to disk if needed) | one compressed, columnar file”

**In Session 1 you used DuckDB in memory: duckdb.connect() and SQL straight on Parquet files.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-0:6` — “In Session 1 you used DuckDB in memory: duckdb.connect() and SQL straight on Parquet files. Today we create a persistent database – a single file on disk, like SQLite, but built for…”

### Veracity check line summarize

**Your turn (5 min): SUMMARIZE shows suspicious minimum and maximum values.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-9:1` — “Your turn (5 min): SUMMARIZE shows suspicious minimum and maximum values. Write one query that counts, in a single pass over trips:”

**SUMMARIZE profiles every column: min, max, approx. unique values, null percentage, quartiles.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-7:2` — “SUMMARIZE profiles every column: min, max, approx. unique values, null percentage, quartiles.”

**Hint: count(*) FILTER (WHERE ...) or sum(CASE WHEN.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-9:8` — “Hint: count(*) FILTER (WHERE ...) or sum(CASE WHEN ... THEN 1 ELSE 0 END).”

### Limit writer time

**DuckDB is an embedded database: it runs inside your Python process, there is no server in between.**
Confidence 0.68 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-17:2` — “DuckDB is an embedded database: it runs inside your Python process, there is no server in between. The price: only one process may open the file for writing. We simulate a second user with…”

**Many readers or one writer – fine for one analyst or one batch job, not for 50 dashboard users writing at once.**
Confidence 0.63 · active · 1 source · when: for one analyst or one batch job
Evidence: `session-04/03_duckdb_database.ipynb#cell-19:1` — “Many readers or one writer – fine for one analyst or one batch job, not for 50 dashboard users writing at once. That is the moment for a database server (PostgreSQL) or, for really big…”

### Big data processing mock exam

**Part: C — Topic: Python environments, file formats, DuckDB; Points: 12.**
Confidence 0.80 · active · 1 source
Evidence: `raw/04_mock_exam.md:13` — “C | Python environments, file formats, DuckDB | 12”

### Duckdb client server vs

**Client–server vs. embedded Client–server · PostgreSQL Embedded · DuckDB, SQLite.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p23:4` — “Client–server vs. embedded Client–server · PostgreSQL Embedded · DuckDB, SQLite”

### Duckdb create taxi duckdb load

**Create taxi.duckdb, load 2 months + zones Two Python processes, one database file – what happens.**
Confidence 0.68 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p26:6` — “1. Create taxi.duckdb, load 2 months + zones Two Python processes, one database file – what happens”

### Duckdb database file

**DuckDB as a database file embedded · columnar · one file.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p22:1` — “DuckDB as a database file embedded · columnar · one file”

### Duckdb db server python

**DB server Your Python process Your Python network disk taxi.duckdb process DuckDB library inside.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p23:7` — “DB server Your Python process Your Python network disk taxi.duckdb process DuckDB library inside”

### Duckdb fit

**In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).**
Confidence 0.81 · active · 2 sources
Evidence: `session-04/03_duckdb_database.ipynb#cell-26:4` — “Runs as | library in your process | library in your process | server | cluster (or local)”

### Duckdb session 04 03 duckdb database ipynb together section

**Session-04/03_duckdb_database.ipynb Now, together: section 7.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p26:4` — “session-04/03_duckdb_database.ipynb Now, together: section 7”

### Joins views

**A view stores the query, not the data.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-11:2` — “A view stores the query, not the data. It is always up to date and costs no disk space.”

### Load data tables

**AS SELECT (CTAS) reads the Parquet files once and stores the result inside the database file.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-4:2` — “CREATE TABLE ... AS SELECT (CTAS) reads the Parquet files once and stores the result inside the database file. We keep the columns we need, rename the timestamps and compute the trip…”

### Olap built analytics

**Built for analytics (OLAP) apps (OLTP) OLTP + some OLAP analytics on many machines.**
Confidence 0.70 · active · 1 source · when: for analytics (OLAP) apps (OLTP) OLTP + some OLAP analytics on many machines
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p25:11` — “Built for analytics (OLAP) apps (OLTP) OLTP + some OLAP analytics on many machines”

### Pip files repository venv

**Which two files should have been in the repository? » .venv is activated, pip install duckdb worked – Jupyter still says ModuleNotFoundError.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p14:3` — “» "I use pyenv, so I don't need venv." Why is this only half true? » Your notebook fails on the server with an AttributeError in pandas. Which two files should have been in the repository?…”

### Really need cluster

**Engine: DuckDB — Execution model: SQL engine, multi-threaded, vectorized, can stream from disk.**
Confidence 0.69 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:10` — “DuckDB | SQL engine, multi-threaded, vectorized, can stream from disk”

### Reproducible python saving data models

**Lab: C — Topic: DuckDB as a database file – homework; Where: laptop, notebook; File: 03_duckdb_database.ipynb.**
Confidence 0.84 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p3:12` — “C DuckDB as a database file – live demo Laptop · notebook homework”

### Spark ml envs duckdb

**5 4 Envs, DuckDB, Spark ML ← Read the plan.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p102:20` — “5 4 Envs, DuckDB, Spark ML ← Read the plan”

### Transactions acid

**DuckDB is a real database: changes happen inside transactions and can be rolled back.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-15:2` — “DuckDB is a real database: changes happen inside transactions and can be rolled back.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 9 | 2026-11-25 |
| `session-04/README.md` | readme | 0.85 | 1 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 13 | 2026-10-28 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |
| `raw/04_mock_exam.md` | exam | 0.95 | 1 | 2026-11-25 |

## Related Pages

- [[engines-single_machine|Single-Machine Engines]] (28 shared entities)
- [[data-formats|File Formats]] (27 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (27 shared entities)
- [[python-execution|Python Execution Model]] (26 shared entities)
- [[course-exam|Exam]] (21 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (19 shared entities)

## Open Questions

8 prompts from the material are collected in [[questions/data-duckdb|Questions: DuckDB]].
- C6 (2 P) Why is DuckDB called an embedded database? Name one consequence for concurrent writing.
- One advantage, one limitation. » 30 analysts, a dashboard that writes annotations every few seconds: is one DuckDB file a good choice?
- » duckdb.connect() vs. duckdb.connect("taxi.duckdb"): give one situation for each. » Why is DuckDB called an embedded database?

## Timeline

- 2026-11-25: new_claim on `claim_eeeb42e4`
- 2026-11-25: new_claim on `claim_6bada748`
- 2026-11-25: support_update on `claim_95fe6516` (0.69 → 0.81)
- 2026-11-25: new_claim on `claim_7abd95da`
- 2026-11-25: new_claim on `claim_87c7b259`
- 2026-11-25: support_update on `claim_80c6829c` (0.68 → 0.84)
- 2026-11-25: new_claim on `claim_2b441de7`
- 2026-11-25: new_claim on `claim_48d35ee7`
