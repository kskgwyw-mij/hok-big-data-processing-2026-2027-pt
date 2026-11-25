---
title: Kaggle Labs
type: workflows
topic: tooling.kaggle
entity_ids:
  - ent_kaggle
  - ent_jupyter
  - ent_spark
  - ent_spark_ml
  - ent_code
  - ent_add_input
  - ent_apache_spark
  - ent_import_notebook
  - ent_internet
  - ent_kafka
  - ent_lab_d
  - ent_labs
claim_ids:
  - claim_94adb0a9
  - claim_b6edbda6
  - claim_7e0bc457
  - claim_e4d61545
  - claim_b0185af6
  - claim_55d3747e
  - claim_451e86a4
  - claim_58de4236
  - claim_67deecb3
  - claim_f71118cb
  - claim_5bf6ea28
  - claim_54f81569
  - claim_51cbe8dd
  - claim_c969c2c1
  - claim_cc58f4f3
  - claim_14a18c46
  - claim_5394357e
  - claim_d82fc010
  - claim_d475bd61
  - claim_ecf67465
  - claim_c840db09
confidence: 0.654
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_47132aab
  - src_59b6ded4
  - src_6494d099
  - src_6e2e5684
  - src_70f9fe3e
  - src_75fe69fe
  - src_799c8bd7
  - src_96e79681
  - src_9e752903
  - src_b3356305
  - src_cecf99ea
review_required: false
---

# Kaggle Labs

Rendered from 21 claims and 12 sources. Median confidence 0.65; 15 active, 0 disputed, 0 superseded.

## Current Understanding

### Reproducible python saving data models

**Lab: D — Topic: Spark fundamentals (Session 2) + Spark ML; Where: Kaggle; File: 04_spark_fundamentals_and_ml.ipynb.**
Confidence 0.79 · active · 2 sources
Evidence: `session-04/README.md:11` — “D | Spark fundamentals (Session 2) + Spark ML | Kaggle | 04_spark_fundamentals_and_ml.ipynb”

**Symptom: Kaggle: pip install or Download failed — OS: Kaggle; Fix: Settings → Internet On (needs phone verification).**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:78` — “Kaggle: pip install or Download failed | Kaggle | Settings → Internet On (needs phone verification)”

**Today you work in two places: your own laptop (VS Code) for Labs A–C and Kaggle for Lab D (Spark).**
Confidence 0.64 · active · 1 source · when: for Labs A–C and Kaggle for Lab D (Spark)
Evidence: `session-04/README.md:3` — “Today you work in two places: your own laptop (VS Code) for Labs A–C and Kaggle for Lab D (Spark). Lab C is homework this time – we only look at one part of it together in class.”

### Spark kaggle fundamentals ml

**Create → New Notebook → File → Import Notebook → upload this .ipynb.**
Confidence 0.84 · active · 3 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p29:5` — “1 kaggle.com → Create → New Notebook → File → Import Notebook → 04_spark_fundamentals_and_ml.ipynb”

**Runs on Kaggle – no Java setup on your laptop needed.**
Confidence 0.77 · active · 2 sources
Evidence: `README.md:8` — “Kaggle – free notebooks in the browser | Apache Spark and Spark ML (no Java setup on your laptop)”

**Right panel → Settings → Internet: On (needs a phone-verified account) · Accelerator: None.**
Confidence 0.77 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p29:9` — “3 Settings → Internet → On · Accelerator → None”

### Spark labs kaggle

**Create a free account on kaggle.com and verify your phone number (Settings) – otherwise notebooks have no internet.**
Confidence 0.60 · candidate · 1 source
Evidence: `README.md:79` — “1. Create a free account on kaggle.com and verify your phone number (Settings) – otherwise notebooks have no internet.”

**Right panel: Input → + Add Input → the dataset named at the top of the notebook.**
Confidence 0.60 · candidate · 1 source
Evidence: `README.md:81` — “3. Right panel: Input → + Add Input → the dataset named at the top of the notebook.”

**Run the cells from the top. The first cell installs Java 17 and PySpark if Kaggle does not have them.**
Confidence 0.60 · candidate · 1 source · when: if Kaggle does not have them
Evidence: `README.md:83` — “5. Run the cells from the top. The first cell installs Java 17 and PySpark if Kaggle does not have them.”

### Apache spark fundamentals

**The same content (plus Spark ML) is in session-04/04_spark_fundamentals_and_ml.ipynb, which runs on Kaggle.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:6` — “> No Java on your laptop? The same content (plus Spark ML) is in session-04/04_spark_fundamentals_and_ml.ipynb, which runs on Kaggle.”

### Benchmark

**Each measurement is repeated 3 times and the fastest run counts, because other programs on the machine (VS Code, other notebooks) can disturb a single measurement.**
Confidence 0.65 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-5:3` — “The same CPU-bound task as in the warm-up: 4 jobs, first one after another (serial), then in 4 threads. Each measurement is repeated 3 times and the fastest run counts, because other…”

### Exit ticket individual ai

**Answer the following questions in your own words, in this notebook.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-43:5` — “Answer the following questions in your own words, in this notebook. You have 10 minutes. These are representative of exam questions.”

### Housekeeping stopping spark

**This releases the JVM memory and avoids port conflicts if you restart the notebook.**
Confidence 0.68 · active · 1 source · when: if you restart the notebook
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-41:5` — “Always stop the SparkSession when you are done. This releases the JVM memory and avoids port conflicts if you restart the notebook.”

### Jupyter working kaggle following

**In this session we were working on the Kaggle following Kaggle notebook: https://www.kaggle.com/code/tutama/hok-big-data-processing-tutama/.**
Confidence 0.09 · archived · 1 source
Evidence: `session-05/session-05.txt:1` — “In this session we were working on the Kaggle following Kaggle notebook: https://www.kaggle.com/code/tutama/hok-big-data-processing-tutama/”

### Kafka python producers consumers consumer

**Open this notebook from the session-06/ folder – it imports kafka_data.py from there.**
Confidence 0.78 · active · 2 sources
Evidence: `session-06/README.md:117` — “Notebook: ModuleNotFoundError: kafka_data | Open the notebook from the session-06/ folder”

### Kaggle account

**Settings → Phone verification – without it, notebooks cannot use the internet (we need it to install PySpark).**
Confidence 0.65 · active · 1 source
Evidence: `session-04/README.md:55` — “2. Settings → Phone verification – without it, notebooks cannot use the internet (we need it to install PySpark).”

### Kaggle https www datacamp com students https learnsql com

**» https://www.datacamp.com (50% off for students) » https://learnsql.com » https://sqlbolt.com » https://learn.microsoft.com/en-us/training/browse/ » https://cloud.google.com/learn/certification/ » https://aws.amazon.com/certification/?nc1=h_ls » https://www.pluralsight.com/cloud-guru » https://www.freecodecamp.org » https://www.kaggle.com/learn/.**
Confidence 0.74 · active · 1 source · when: for students ) » https://learnsql
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p4:3` — “» https://www.datacamp.com (50% off for students) » https://learnsql.com » https://sqlbolt.com » https://learn.microsoft.com/en-us/training/browse/ »…”

### Kaggle start take

**Start Kaggle, then take your break.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p29:1` — “Start Kaggle, then take your break”

### Kaggle today local

**Kaggle today: local[*] Cluster.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p30:4` — “Kaggle today: local[*] Cluster”

### Lab c duckdb database file

**Start fresh every time you run the notebook top to bottom.**
Confidence 0.54 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-1` — “start fresh every time you run the notebook top to bottom”

### Python environments venv pyenv uv

**Goal: after this lab you can explain which Python and which packages your notebook really uses, and you can rebuild the same environment on another machine.**
Confidence 0.65 · active · 1 source · when: after this lab you can explain which Python and which packages your noteboo
Evidence: `session-04/01_python_environments.md:3` — “Goal: after this lab you can explain which Python and which packages your notebook really uses, and you can rebuild the same environment on another machine.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 1 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 5 | 2026-11-25 |
| `session-04/README.md` | readme | 0.85 | 4 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |
| `session-05/session-05.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 1 | 2026-11-11 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `session-01/02_bonus_python_without_gil.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `README.md` | readme | 0.85 | 5 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 1 | 2026-11-11 |

## Related Pages

- [[engines-single_machine|Single-Machine Engines]] (34 shared entities)
- [[data-formats|File Formats]] (32 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (32 shared entities)
- [[data-duckdb|DuckDB]] (21 shared entities)
- [[spark-architecture|Spark Architecture]] (21 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (19 shared entities)

## Open Questions

1 prompts from the material are collected in [[questions/tooling-kaggle|Questions: Kaggle Labs]].
- What does this mean for a notebook you hand over to a colleague without a version file?

## Timeline

- 2026-11-25: new_claim on `claim_d82fc010`
- 2026-11-25: support_update on `claim_cc58f4f3` (0.63 → 0.78)
- 2026-11-25: new_claim on `claim_d475bd61`
- 2026-11-25: support_update on `claim_b6edbda6` (0.69 → 0.84)
- 2026-11-25: support_update on `claim_7e0bc457` (0.59 → 0.77)
- 2026-11-25: new_claim on `claim_ecf67465`
- 2026-11-25: support_update on `claim_b0185af6` (0.67 → 0.79)
- 2026-11-25: new_claim on `claim_c840db09`
