---
title: pip
type: entity
entity_id: ent_pip
entity_type: tool
claim_ids:
  - claim_3bfafe94
  - claim_c9af32ed
  - claim_518f92ee
  - claim_60550010
  - claim_80dcb37a
  - claim_58de4236
  - claim_95fe6516
  - claim_4c4d2c23
  - claim_01edbaf1
  - claim_1d96ae1a
  - claim_b73468f4
confidence: 0.668
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_6494d099
  - src_6e2e5684
  - src_b3356305
  - src_cecf99ea
---

# pip

Type: tool. Mentioned in 11 claims across 4 topics.
Aliases: pip install, pip freeze.

## Claims

- **Symptom: externally-managed-environment on pip install — OS: macOS (Homebrew), Linux; Fix: You are not in a venv – activate .venv first; never use sudo pip.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Lock file: venv: no (pip freeze by hand), pyenv: no, uv: yes uv.lock.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **Symptom: Could not open requirements file: requirements-local.txt — Fix: It lives in the repo root → cd .. first, or pip install -r ../requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: ModuleNotFoundError: kafka.vendor.six.moves — Fix: You have the old kafka-python 2.0.2 → pip install -r requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: Kaggle: pip install or Download failed — OS: Kaggle; Fix: Settings → Internet On (needs phone verification).** Confidence 0.67 · [[tooling-kaggle|Kaggle Labs]]
- **Symptom: pip install very slow / times out on campus Wi-Fi — OS: all; Fix: Use uv (Lab A, step 4) – it downloads in parallel and caches.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.** Confidence 0.44 · [[python-environments|Python Environments and Reproducibility]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]
- **Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[requirements_txt|requirements.txt]] (6)
- [[venv|venv]] (6)
- [[kafka|Kafka]] (3)
- [[python|Python 3.12]] (3)
- [[uv|uv]] (3)
- [[faker|Faker]] (2)
- [[duckdb|DuckDB]] (1)
- [[kaggle|Kaggle]] (1)
- [[linux|Linux]] (1)
- [[spark|Spark]] (1)
