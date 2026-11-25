---
title: pip
type: entity
entity_id: ent_pip
entity_type: tool
claim_ids:
  - claim_3bfafe94
  - claim_c9af32ed
  - claim_518f92ee
  - claim_919b7ce7
  - claim_60550010
  - claim_80dcb37a
  - claim_58de4236
  - claim_95fe6516
  - claim_4c4d2c23
  - claim_01edbaf1
  - claim_1d96ae1a
  - claim_b73468f4
  - claim_57aa108c
  - claim_c831872a
  - claim_8582a503
  - claim_f2a67b3e
  - claim_32a2fe7a
  - claim_3a05fc8a
  - claim_989f4683
  - claim_fa6768d4
confidence: 0.692
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_59b6ded4
  - src_6494d099
  - src_68fcf2b9
  - src_6e2e5684
  - src_8615b91f
  - src_b3356305
  - src_cecf99ea
---

# pip

Type: tool. Mentioned in 20 claims across 6 topics.
Aliases: pip install, pip freeze.

## Claims

- **You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.** Confidence 0.89 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Lock file: venv: no (pip freeze by hand), pyenv: no, uv: yes uv.lock.** Confidence 0.86 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: ModuleNotFoundError: kafka.vendor.six.moves — Fix: You have the old kafka-python 2.0.2 → pip install -r requirements-local.txt.** Confidence 0.83 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).** Confidence 0.81 · [[data-duckdb|DuckDB]]
- **Symptom: externally-managed-environment on pip install — OS: macOS (Homebrew), Linux; Fix: You are not in a venv – activate .venv first; never use sudo pip.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **Which two files should have been in the repository? » .venv is activated, pip install duckdb worked – Jupyter still says ModuleNotFoundError.** Confidence 0.77 · [[data-duckdb|DuckDB]]
- **Install, users, ports – but many writers at once. pip install, no server – but one writing process.** Confidence 0.70 · [[python-execution|Python Execution Model]]
- **Pip install, live on this laptop uv python install 3.12 # pre-built Python, seconds uv venv --python 3.12 .venv [__ seconds] # interpreter + environment uv pip install -r requirements.txt uv pip install, same packages # parallel downloads, cached uv add pandas duckdb # project mode: writes uv.lock [__ seconds].** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **# no .venv yet? py -m venv .venv # no .venv yet? python3 -m venv .venv # no .venv yet? python3 -m venv .venv PS> .venv\Scripts\Activate.ps1 $ source .venv/bin/activate $ source .venv/bin/activate PS> pip install -r requirements-local.txt $ pip install -r requirements-local.txt $ pip install -r requirements-local.txt.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **LEVEL 3 LEVEL 1 LEVEL 2 Container requirements.txt Lock file Dev container / Docker: OS, Python The packages you use directly, with pip freeze or uv.lock: every package, and Java pinned too – our version ranges. exact versions.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: Could not open requirements file: requirements-local.txt — Fix: It lives in the repo root → cd .. first, or pip install -r ../requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: Kaggle: pip install or Download failed — OS: Kaggle; Fix: Settings → Internet On (needs phone verification).** Confidence 0.67 · [[tooling-kaggle|Kaggle Labs]]
- **Symptom: pip install very slow / times out on campus Wi-Fi — OS: all; Fix: Use uv (Lab A, step 4) – it downloads in parallel and caches.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Setup pip install built into Python install + admin JVM + cluster.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Run pip in the repo root → cd .. or pip install -r ../requirements- Could not open requirements file local.txt.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Mac Pip Install PySpark.** Confidence 0.60 · [[unfiled|Unfiled Observations]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.55 · [[python-environments|Python Environments and Reproducibility]]
- **Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.** Confidence 0.44 · [[python-environments|Python Environments and Reproducibility]]
- **Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[requirements_txt|requirements.txt]] (11)
- [[venv|venv]] (10)
- [[python|Python 3.12]] (5)
- [[uv|uv]] (5)
- [[duckdb|DuckDB]] (4)
- [[kafka|Kafka]] (3)
- [[lock_file|lock file]] (3)
- [[faker|Faker]] (2)
- [[spark|Spark]] (2)
- [[pandas|pandas]] (2)
