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
  - claim_57aa108c
  - claim_c831872a
  - claim_2873c09a
  - claim_3c7502a9
  - claim_989f4683
  - claim_547806cd
  - claim_fa6768d4
  - claim_3a1a7f1a
  - claim_001f29c2
confidence: 0.682
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_59b6ded4
  - src_8615b91f
  - src_b3356305
  - src_cecf99ea
  - src_fc0bfe80
---

# requirements.txt

Type: concept. Mentioned in 21 claims across 5 topics.
Aliases: requirements.

## Claims

- **You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.** Confidence 0.89 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: ModuleNotFoundError: kafka.vendor.six.moves — Fix: You have the old kafka-python 2.0.2 → pip install -r requirements-local.txt.** Confidence 0.83 · [[python-environments|Python Environments and Reproducibility]]
- **✓ What you should see ✗ If it fails Prompt starts with (.venv) · check: Could not open requirements file → you are in session-06/: python -c "import kafka, faker; print(kafka.version)" → 3.x cd.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **Run the next commands in the repo root (where requirements-local.txt and .venv/ are), not in session-06/.** Confidence 0.79 · [[python-environments|Python Environments and Reproducibility]]
- **» Step 1: Check System Requirements » macOS Monterey 12+ (Intel or Apple Silicon) » Minimum 4GB RAM » Enable virtualization (default on Mac) » Step 2: Download Docker » Go to Docker Desktop for Mac. » Click "Download Docker Desktop for Mac". » Choose Apple Chip (for M1/M2/M3) or Intel Chip. » Step 3: Install Docker » Open the downloaded .dmg file. » Drag Docker.app to the Applications folder. » Open Docker from Launchpad or Applications folder. » Step 4: Allow Permissions » When prompted, grant permissions for Docker to run. » Allow Docker privileged access to manage containers. » Step 5: Verify Installation.** Confidence 0.74 · [[tooling-docker|Docker and Dev Containers]]
- **Pip install, live on this laptop uv python install 3.12 # pre-built Python, seconds uv venv --python 3.12 .venv [__ seconds] # interpreter + environment uv pip install -r requirements.txt uv pip install, same packages # parallel downloads, cached uv add pandas duckdb # project mode: writes uv.lock [__ seconds].** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **# no .venv yet? py -m venv .venv # no .venv yet? python3 -m venv .venv # no .venv yet? python3 -m venv .venv PS> .venv\Scripts\Activate.ps1 $ source .venv/bin/activate $ source .venv/bin/activate PS> pip install -r requirements-local.txt $ pip install -r requirements-local.txt $ pip install -r requirements-local.txt.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **LEVEL 3 LEVEL 1 LEVEL 2 Container requirements.txt Lock file Dev container / Docker: OS, Python The packages you use directly, with pip freeze or uv.lock: every package, and Java pinned too – our version ranges. exact versions.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **» Git subfolder „kafka" » Create virtualenv » Install requirements.txt » Run kafka_producer.ipynb » Run kafka_consumer.ipynb » Understand concept of producer & consumer.** Confidence 0.70 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **File: requirements-local.txt — Contains: pandas, Polars, DuckDB, PyArrow, scikit-learn, plots, kafka-python 3.x + Faker (Session 6); Use it for: your laptop (default).** Confidence 0.69 · [[engines-single_machine|Single-Machine Engines]]
- **Symptom: Could not open requirements file: requirements-local.txt — Fix: It lives in the repo root → cd .. first, or pip install -r ../requirements-local.txt.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **File: requirements.txt — Contains: the above + PySpark 4.0 and Delta Lake (needs Java 17+); Use it for: the dev container, or a laptop with Java 17 installed.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **» Kafka is written on the JVM in Java and Scala » The JVM allows Kafka to target many OS architectures » Kafka has a diverse ecosystem of tools and libraries » Kafka's flexibility has made it pervasive in data work » Kafka's few requirements make it easy to build on.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **» Step 1: Check System Requirements » Windows 10 (Pro, Enterprise, or Education) / Windows 11 » WSL2 (Windows Subsystem for Linux) Enabled » Virtualization Enabled in BIOS » Step 2: Enable Virtualization » Open Task Manager (Ctrl + Shift + Esc). » Go to Performance → CPU. » Check if Virtualization is Enabled.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Run pip in the repo root → cd .. or pip install -r ../requirements- Could not open requirements file local.txt.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **The repository also contains a dev container with Python 3.12, Java 17 and everything from requirements.txt – besides Kaggle, the way to run Spark without installing Java yourself.** Confidence 0.62 · [[python-environments|Python Environments and Reproducibility]]
- **Requirements-local.txt = everything except Spark.** Confidence 0.61 · [[python-environments|Python Environments and Reproducibility]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.55 · [[python-environments|Python Environments and Reproducibility]]
- **Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.** Confidence 0.44 · [[python-environments|Python Environments and Reproducibility]]
- **Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[pip|pip]] (11)
- [[venv|venv]] (9)
- [[kafka|Kafka]] (7)
- [[python|Python 3.12]] (6)
- [[faker|Faker]] (4)
- [[dev_container|Dev container]] (3)
- [[duckdb|DuckDB]] (3)
- [[spark|Spark]] (3)
- [[pandas|pandas]] (3)
- [[uv|uv]] (3)
