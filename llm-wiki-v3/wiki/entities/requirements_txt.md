---
title: requirements.txt
type: entity
entity_id: ent_requirements_txt
entity_type: concept
claim_ids:
  - claim_3bfafe94
  - claim_518f92ee
  - claim_b0dbd1e0
  - claim_919b7ce7
  - claim_4c4d2c23
  - claim_8b05e9fa
  - claim_54363381
  - claim_201c7650
  - claim_01edbaf1
  - claim_1d96ae1a
  - claim_d507dd54
  - claim_b73468f4
confidence: 0.617
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_b3356305
  - src_cecf99ea
---

# requirements.txt

Type: concept. Mentioned in 12 claims across 2 topics.
Aliases: requirements.

## Claims

- **You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **File: requirements-local.txt — Contains: pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6); Use it for: your laptop (default).** Confidence 0.69 · [[engines-single_machine|Single-Machine Engines]]
- **Symptom: Could not open requirements file: requirements-local.txt — Fix: It lives in the repo root → cd .. first, or pip install -r ../requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: ModuleNotFoundError: kafka.vendor.six.moves — Fix: You have the old kafka-python 2.0.2 → pip install -r requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **File: requirements.txt — Contains: the above + PySpark 4.0 and Delta Lake (needs Java 17+); Use it for: the dev container, or a laptop with Java 17 installed.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **The repository also contains a dev container with Python 3.12, Java 17 and everything from requirements.txt – besides Kaggle, the way to run Spark without installing Java yourself.** Confidence 0.62 · [[python-environments|Python Environments and Reproducibility]]
- **Run the next commands in the repo root (where requirements-local.txt and .venv/ are), not in session-06/.** Confidence 0.62 · [[python-environments|Python Environments and Reproducibility]]
- **Requirements-local.txt = everything except Spark.** Confidence 0.61 · [[python-environments|Python Environments and Reproducibility]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.** Confidence 0.44 · [[python-environments|Python Environments and Reproducibility]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]
- **Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[pip|pip]] (6)
- [[venv|venv]] (5)
- [[kafka|Kafka]] (4)
- [[python|Python 3.12]] (4)
- [[faker|Faker]] (3)
- [[spark|Spark]] (3)
- [[dev_container|Dev container]] (2)
- [[delta_lake|Delta Lake]] (1)
- [[duckdb|DuckDB]] (1)
- [[kaggle|Kaggle]] (1)
