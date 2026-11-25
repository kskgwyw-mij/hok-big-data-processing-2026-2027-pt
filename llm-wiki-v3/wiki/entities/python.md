---
title: Python 3.12
type: entity
entity_id: ent_python
entity_type: technology
claim_ids:
  - claim_3bfafe94
  - claim_f0092822
  - claim_30d231b5
  - claim_2281d11e
  - claim_518f92ee
  - claim_919b7ce7
  - claim_0fbef9f9
  - claim_774b3826
  - claim_b0a1193e
  - claim_9d914236
  - claim_a004b57f
  - claim_5134bf38
  - claim_56f7ed81
  - claim_64a2b1df
  - claim_4c4d2c23
  - claim_ba1a8d00
  - claim_201c7650
  - claim_5934cd9f
  - claim_57aa108c
  - claim_c831872a
  - claim_eeeb42e4
  - claim_87c7b259
  - claim_0dea7a71
  - claim_104a768a
  - claim_6ce918d7
confidence: 0.694
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_1cebb3bb
  - src_59b6ded4
  - src_6494d099
  - src_70f9fe3e
  - src_799c8bd7
  - src_8615b91f
  - src_96e79681
  - src_b3356305
---

# Python 3.12

Type: technology. Mentioned in 25 claims across 8 topics.
Aliases: py -3.12, python3.12.

## Claims

- **You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.** Confidence 0.89 · [[python-environments|Python Environments and Reproducibility]]
- **» Why Is CPython Written in C and Not Python? » Self-hosted compilers are compilers written in the same language they go on compiling, such as the Go compiler. » Source-to-source compilers are first written in another language that already possesses a compiler. » CPython is written in C, following a source-to-source compiler model.** Confidence 0.86 · [[unfiled|Unfiled Observations]]
- **In the comparison table, VS Code: Windows: code.visualstudio.com, macOS: code.visualstudio.com, Linux (Ubuntu/Debian): code.visualstudio.com.** Confidence 0.86 · [[course-setup|Course Setup]]
- **In the comparison table, Python 3.12: Windows: winget install Python.Python.3.12 or python.org installer (tick "Add python.exe to PATH" and "py launcher"), macOS: brew install python@3.12 or python.org installer, Linux (Ubuntu/Debian): sudo apt install python3.12 python3.12-venv.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: ensurepip is not available / No module named venv — OS: Ubuntu/Debian; Fix: sudo apt install python3.12-venv.** Confidence 0.73 · [[python-environments|Python Environments and Reproducibility]]
- **Problem: Which Python version? — Example: Project A needs 3.12, project B still runs on 3.10; Tool: pyenv (or uv python).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Uv init --python 3.12 ; uv add pandas duckdb.** Confidence 0.72 · [[engines-single_machine|Single-Machine Engines]]
- **Project A needs Python 3.12, project B still runs on Project A needs pandas 3, project B breaks with 3.10. pandas 3.** Confidence 0.70 · [[engines-single_machine|Single-Machine Engines]]
- **DB server Your Python process Your Python network disk taxi.duckdb process DuckDB library inside.** Confidence 0.70 · [[data-duckdb|DuckDB]]
- **Reads the folder's runs you type first on PATH .python-version Python 3.12 python pyenv shim ~/.pyenv/versions/ → 3.12.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Pip install, live on this laptop uv python install 3.12 # pre-built Python, seconds uv venv --python 3.12 .venv [__ seconds] # interpreter + environment uv pip install -r requirements.txt uv pip install, same packages # parallel downloads, cached uv add pandas duckdb # project mode: writes uv.lock [__ seconds].** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **LEVEL 3 LEVEL 1 LEVEL 2 Container requirements.txt Lock file Dev container / Docker: OS, Python The packages you use directly, with pip freeze or uv.lock: every package, and Java pinned too – our version ranges. exact versions.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Return value: Transformations: A new DataFrame, Actions: A Python value or side-effect.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Component: Driver — Role: Your Python process. Runs your code, plans queries, coordinates execution.** Confidence 0.69 · [[spark-architecture|Spark Architecture]]
- **Library: kafka-python ≥ 3.0 — Why: pure-Python Kafka client (version 2.0.2 from older tutorials does not work on Python 3.12).** Confidence 0.69 · [[python-environments|Python Environments and Reproducibility]]
- **Create taxi.duckdb, load 2 months + zones Two Python processes, one database file – what happens.** Confidence 0.68 · [[data-duckdb|DuckDB]]
- **Symptom: python opens the Microsoft Store — OS: Windows; Fix: Use py -3.12 ..., or turn off Settings → Apps → Advanced app settings → App execution aliases → python.exe.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Windows: py -3.12 get_data.py --months 2 — macOS / Linux: python3.12 get_data.py --months 2.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Block 2 – From Python object to Kafka bytes.** Confidence 0.66 · [[hdfs-architecture|HDFS]]
- **Use Python 3.12 (the same version as the course dev container).** Confidence 0.65 · [[python-environments|Python Environments and Reproducibility]]
- **The repository also contains a dev container with Python 3.12, Java 17 and everything from requirements.txt – besides Kaggle, the way to run Spark without installing Java yourself.** Confidence 0.62 · [[python-environments|Python Environments and Reproducibility]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.55 · [[python-environments|Python Environments and Reproducibility]]
- **Git pull ; python get_data.py --months 2 # Windows: py -3.12 get_data.py --months 2.** Confidence 0.44 · [[course-setup|Course Setup]]
- **Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[venv|venv]] (9)
- [[requirements_txt|requirements.txt]] (7)
- [[windows|Windows]] (6)
- [[pip|pip]] (6)
- [[duckdb|DuckDB]] (5)
- [[pandas|pandas]] (5)
- [[uv|uv]] (5)
- [[kafka|Kafka]] (4)
- [[dev_container|Dev container]] (3)
- [[linux|Linux]] (3)
