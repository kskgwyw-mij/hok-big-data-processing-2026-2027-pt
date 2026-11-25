---
title: Kaggle Labs
type: workflows
topic: tooling.kaggle
entity_ids:
  - ent_jupyter
  - ent_kaggle
  - ent_spark
  - ent_spark_ml
  - ent_add_input
  - ent_code
  - ent_import_notebook
  - ent_internet
  - ent_kafka
  - ent_lab_d
  - ent_labs
  - ent_notebook
claim_ids:
  - claim_94adb0a9
  - claim_b6edbda6
  - claim_7e0bc457
  - claim_e4d61545
  - claim_b0185af6
  - claim_55d3747e
  - claim_58de4236
  - claim_67deecb3
  - claim_f71118cb
  - claim_5bf6ea28
  - claim_54f81569
  - claim_c969c2c1
  - claim_cc58f4f3
  - claim_715d84b1
  - claim_14a18c46
  - claim_5394357e
  - claim_d82fc010
confidence: 0.614
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_47132aab
  - src_6494d099
  - src_6e2e5684
  - src_75fe69fe
  - src_799c8bd7
  - src_96e79681
  - src_b3356305
  - src_cecf99ea
review_required: false
---

# Kaggle Labs

Rendered from 17 claims and 9 sources. Median confidence 0.61; 10 active, 0 disputed, 0 superseded.

## Current Understanding

### Reproducible python saving data models

**Symptom: Kaggle: pip install or Download failed — OS: Kaggle; Fix: Settings → Internet On (needs phone verification).**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:78` — “Kaggle: pip install or Download failed | Kaggle | Settings → Internet On (needs phone verification)”

**Lab: D — Topic: Spark fundamentals (Session 2) + Spark ML; Where: Kaggle; File: 04_spark_fundamentals_and_ml.ipynb.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:11` — “D | Spark fundamentals (Session 2) + Spark ML | Kaggle | 04_spark_fundamentals_and_ml.ipynb”

**Today you work in two places: your own laptop (VS Code) for Labs A–C and Kaggle for Lab D (Spark).**
Confidence 0.64 · active · 1 source · when: for Labs A–C and Kaggle for Lab D (Spark)
Evidence: `session-04/README.md:3` — “Today you work in two places: your own laptop (VS Code) for Labs A–C and Kaggle for Lab D (Spark). Lab C is homework this time – we only look at one part of it together in class.”

### Spark kaggle fundamentals ml

**Create → New Notebook → File → Import Notebook → upload this .ipynb.**
Confidence 0.69 · active · 2 sources
Evidence: `README.md:80` — “2. Create → New Notebook → File → Import Notebook → upload the notebook from your local repository.”

**Runs on Kaggle – no Java setup on your laptop needed.**
Confidence 0.61 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:3` — “Runs on Kaggle – no Java setup on your laptop needed.”

**Right panel → Settings → Internet: On (needs a phone-verified account) · Accelerator: None.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:14` — “3. Right panel → Settings → Internet: On (needs a phone-verified account) · Accelerator: None.”

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

### Consumer groups real processes terminal

**Notebook cells run one after another, so we need separate terminals for parallel consumers.**
Confidence 0.63 · active · 1 source · when: after another; for parallel consumers
Evidence: `session-06/02_kafka_python.ipynb#cell-23:15` — “Notebook cells run one after another, so we need separate terminals for parallel consumers. Open 3–4 terminals in VS Code (+ in the terminal panel), activate .venv in each, cd session-06.”

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
| `session-04/README.md` | readme | 0.85 | 3 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-05/session-05.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 2 | 2026-11-11 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `README.md` | readme | 0.85 | 4 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 1 | 2026-11-11 |

## Related Pages

- [[course-setup|Course Setup]] (26 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (25 shared entities)
- [[data-formats|File Formats]] (24 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (16 shared entities)
- [[data-duckdb|DuckDB]] (15 shared entities)
- [[python-execution|Python Execution Model]] (13 shared entities)

## Open Questions

1 prompts from the material are collected in [[questions/tooling-kaggle|Questions: Kaggle Labs]].
- What does this mean for a notebook you hand over to a colleague without a version file?

## Timeline

- 2026-11-25: new_claim on `claim_c969c2c1`
- 2026-11-25: new_claim on `claim_cc58f4f3`
- 2026-11-25: new_claim on `claim_715d84b1`
- 2026-11-25: new_claim on `claim_14a18c46`
- 2026-11-25: support_update on `claim_b6edbda6` (0.59 → 0.69)
- 2026-11-25: new_claim on `claim_5394357e`
- 2026-11-25: new_claim on `claim_d82fc010`
- 2026-11-25: support_update on `claim_cc58f4f3` (0.63 → 0.78)
