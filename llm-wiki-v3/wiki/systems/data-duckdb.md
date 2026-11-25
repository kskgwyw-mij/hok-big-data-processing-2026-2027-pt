---
title: DuckDB
type: systems
topic: data.duckdb
entity_ids:
  - ent_duckdb
  - ent_parquet
  - ent_spark_job
  - ent_case
  - ent_ctas
  - ent_filter
  - ent_jupyter
  - ent_olap
  - ent_oltp
  - ent_pip
  - ent_spark
  - ent_summarize
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
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_46087206
  - src_6494d099
  - src_6e2e5684
review_required: false
---

# DuckDB

Rendered from 15 claims and 3 sources. Median confidence 0.63; 13 active, 0 disputed, 0 superseded.

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

### Duckdb fit

**In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).**
Confidence 0.69 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-26:4` — “Runs as | library in your process | library in your process | server | cluster (or local)”

### Joins views

**A view stores the query, not the data.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-11:2` — “A view stores the query, not the data. It is always up to date and costs no disk space.”

### Load data tables

**AS SELECT (CTAS) reads the Parquet files once and stores the result inside the database file.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-4:2` — “CREATE TABLE ... AS SELECT (CTAS) reads the Parquet files once and stores the result inside the database file. We keep the columns we need, rename the timestamps and compute the trip…”

### Really need cluster

**Engine: DuckDB — Execution model: SQL engine, multi-threaded, vectorized, can stream from disk.**
Confidence 0.69 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:10` — “DuckDB | SQL engine, multi-threaded, vectorized, can stream from disk”

### Reproducible python saving data models

**Lab: C — Topic: DuckDB as a database file – homework; Where: laptop, notebook; File: 03_duckdb_database.ipynb.**
Confidence 0.68 · active · 1 source
Evidence: `session-04/README.md:10` — “C | DuckDB as a database file – homework | laptop, notebook | 03_duckdb_database.ipynb”

### Transactions acid

**DuckDB is a real database: changes happen inside transactions and can be rolled back.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-15:2` — “DuckDB is a real database: changes happen inside transactions and can be rolled back.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-04/README.md` | readme | 0.85 | 1 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 13 | 2026-10-28 |

## Related Pages

- [[data-formats|File Formats]] (14 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (14 shared entities)
- [[python-execution|Python Execution Model]] (13 shared entities)
- [[course-exam|Exam]] (11 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (5 shared entities)
- [[course-setup|Course Setup]] (5 shared entities)

## Open Questions

8 prompts from the material are collected in [[questions/data-duckdb|Questions: DuckDB]].
- Explain the difference between duckdb.connect() and duckdb.connect("taxi.duckdb"). Give one situation for each.
- Why is DuckDB called an embedded database? Name one advantage and one limitation that follow from this.
- Scenario: a team of 30 analysts wants a shared dashboard that writes user annotations back to the database every few seconds. Is a single…

## Timeline

- 2026-11-25: new_claim on `claim_95fe6516`
- 2026-11-25: evidence_attached on `claim_95fe6516` (0.69 → 0.69)
- 2026-11-25: evidence_attached on `claim_95fe6516` (0.69 → 0.69)
- 2026-11-25: evidence_attached on `claim_95fe6516` (0.69 → 0.69)
- 2026-11-25: new_claim on `claim_6f06a285`
- 2026-11-25: new_claim on `claim_84e46e85`
- 2026-11-25: new_claim on `claim_2ab2e812`
- 2026-11-25: new_claim on `claim_dd944da3`
