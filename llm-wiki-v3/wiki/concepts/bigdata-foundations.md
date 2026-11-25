---
title: Big Data Foundations
type: concepts
topic: bigdata.foundations
entity_ids:
  - ent_scale
  - ent_big_data
  - ent_spark
  - ent_big_data_processing
  - ent_fh_kufstein_tirol
  - ent_spark_task
  - ent_winter_semester
claim_ids:
  - claim_fd7e6030
  - claim_ad6a62dd
  - claim_8eafee62
  - claim_51de55b2
  - claim_3ce08fd1
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_46087206
  - src_6e2e5684
  - src_8e87808f
  - src_96e79681
review_required: false
---

# Big Data Foundations

Rendered from 5 claims and 4 sources. Median confidence 0.63; 3 active, 0 disputed, 0 superseded.

## Current Understanding

### Data

**The engine comparison uses 2 months – safe for an 8 GB machine. We scale up to all months in section 7.**
Confidence 0.58 · candidate · 1 source · when: for an 8 GB machine
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-3` — “The engine comparison uses 2 months – safe for an 8 GB machine. We scale up to all months in section 7.”

**Start with 6 months; we scale up later.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-2:2` — “Each month is ~50 MB of Parquet and ~3 million trips. Start with 6 months; we scale up later. Run once in the terminal: python get_data.py --months 6”

### Apache spark fundamentals

**FH Kufstein Tirol · Big Data Processing (DPR.1) · Winter Semester 2026/27.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:2` — “FH Kufstein Tirol · Big Data Processing (DPR.1) · Winter Semester 2026/27”

### Limit writer time

**That is the moment for a database server (PostgreSQL) or, for really big data, a lakehouse with Spark.**
Confidence 0.68 · active · 1 source · when: for a database server (PostgreSQL) or; for really big data
Evidence: `session-04/03_duckdb_database.ipynb#cell-19:1` — “Many readers or one writer – fine for one analyst or one batch job, not for 50 dashboard users writing at once. That is the moment for a database server (PostgreSQL) or, for really big…”

### Pickle shines python objects trained

**We train a small model that predicts the trip duration in minutes (the same task we will scale up with Spark later).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-22:20` — “A trained scikit-learn model is a Python object with fitted parameters inside – no table format can store it. We train a small model that predicts the trip duration in minutes (the same…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 2 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |

## Related Pages

- [[course-exam|Exam]] (4 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (3 shared entities)
- [[python-execution|Python Execution Model]] (3 shared entities)
- [[spark-architecture|Spark Architecture]] (3 shared entities)
- [[course-setup|Course Setup]] (2 shared entities)
- [[data-duckdb|DuckDB]] (2 shared entities)

## Open Questions

4 prompts from the material are collected in [[questions/bigdata-foundations|Questions: Big Data Foundations]].
- Big Data is not only Volume. Which of the other Vs did today's lab ignore completely?
- 1.1 (2 P) Name the three original Vs of Big Data and explain one additional V (Variability, Veracity or Value) with an example from the…
- 1.2 (3 P) Compare scale up and scale out: one advantage and one disadvantage of each. Which rule of thumb did we use in this course?

## Timeline

- 2026-11-25: new_claim on `claim_fd7e6030`
- 2026-11-25: new_claim on `claim_ad6a62dd`
- 2026-11-25: new_claim on `claim_8eafee62`
- 2026-11-25: new_claim on `claim_51de55b2`
- 2026-11-25: new_claim on `claim_3ce08fd1`
