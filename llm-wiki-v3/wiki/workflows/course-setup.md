---
title: Course Setup
type: workflows
topic: course.setup
entity_ids:
  - ent_kafka
  - ent_git
  - ent_windows
  - ent_macos
  - ent_python
  - ent_apple_silicon
  - ent_linux
  - ent_projects
  - ent_spark
  - ent_apache_spark
  - ent_code
  - ent_dev_container
claim_ids:
  - claim_09f8595a
  - claim_eb2fc0b8
  - claim_1ce93cb5
  - claim_7d93b0d4
  - claim_0fbef9f9
  - claim_2ed8567d
  - claim_26edcb72
  - claim_c4138824
  - claim_b0a1193e
  - claim_caed1b28
  - claim_9d914236
  - claim_80dcb37a
  - claim_3189156b
  - claim_5eb0d493
  - claim_31e0738b
  - claim_64fbf0f7
  - claim_c4c36174
  - claim_ba1a8d00
  - claim_a9842723
  - claim_53ef90ae
  - claim_add9e91e
  - claim_594a2300
  - claim_8b538216
  - claim_52c68d00
  - claim_9d5713e1
  - claim_1728b45d
  - claim_98cdf12b
  - claim_d7d4bf6d
  - claim_e467c9d5
  - claim_4e0c1eb8
  - claim_805d7c98
confidence: 0.636
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_41b3a933
  - src_46087206
  - src_467d2d1e
  - src_6494d099
  - src_8e87808f
  - src_b3356305
  - src_cecf99ea
review_required: false
---

# Course Setup

Rendered from 31 claims and 8 sources. Median confidence 0.64; 21 active, 0 disputed, 0 superseded.

## Current Understanding

### Kafka lab exam preparation

**File: get_kafka.py — What: Route B: downloads and prepares native Kafka 4.4.0 (standard library only).**
Confidence 0.74 · active · 1 source
Evidence: `session-06/README.md:128` — “get_kafka.py | Route B: downloads and prepares native Kafka 4.4.0 (standard library only)”

**Symptom: Apple Silicon (M1–M4) — Fix: Nothing special – the image and Kafka run natively.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:118` — “Apple Silicon (M1–M4) | Nothing special – the image and Kafka run natively”

**File: kafka_data.py — What: fake data: get_registered_user() and keyed events with a per-key sequence number.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:129` — “kafka_data.py | fake data: get_registered_user() and keyed events with a per-key sequence number”

**Time: 10:10–10:25 — What: break.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/README.md:12` — “11:25–11:35 | break”

**If something fails, write down the error message and bring it – or plan to pair up (see below).**
Confidence 0.62 · active · 1 source · when: If something fails
Evidence: `session-06/README.md:23` — “Do this before we meet. If something fails, write down the error message and bring it – or plan to pair up (see below).”

### Reproducible python saving data models

**Symptom: Apple Silicon (M1–M4) — OS: macOS; Fix: Nothing special – all packages have native wheels.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:80` — “Apple Silicon (M1–M4) | macOS | Nothing special – all packages have native wheels”

**Symptom: pip install very slow / times out on campus Wi-Fi — OS: all; Fix: Use uv (Lab A, step 4) – it downloads in parallel and caches.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:77` — “pip install very slow / times out on campus Wi-Fi | all | Use uv (Lab A, step 4) – it downloads in parallel and caches”

**Symptom: python opens the Microsoft Store — OS: Windows; Fix: Use py -3.12 ..., or turn off Settings → Apps → Advanced app settings → App execution aliases → python.exe.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:72` — “python opens the Microsoft Store | Windows | Use py -3.12 ..., or turn off Settings → Apps → Advanced app settings → App execution aliases → python.exe”

**Lab C is homework this time – we only look at one part of it together in class.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:3` — “Today you work in two places: your own laptop (VS Code) for Labs A–C and Kaggle for Lab D (Spark). Lab C is homework this time – we only look at one part of it together in class.”

**Do steps 1–5 before we meet.**
Confidence 0.56 · candidate · 1 source · when: before we meet
Evidence: `session-04/README.md:20` — “Do steps 1–5 before we meet. If something fails, write down the error message and bring it.”

### Route native kafka docker

**The folder path must not contain a space (e.g. …/My Projects/… or … Kopie).**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:69` — “The folder path must not contain a space (e.g. …/My Projects/… or … Kopie). Kafka's scripts then fail with Classpath is empty. get_kafka.py checks this and stops; install somewhere else…”

**Needs Java 17 or newer (java -version; macOS: brew install openjdk@17, Ubuntu: sudo apt install openjdk-17-jre-headless).**
Confidence 0.62 · active · 1 source
Evidence: `session-06/README.md:60` — “For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker). Needs Java 17 or newer (java -version; macOS: brew install openjdk@17, Ubuntu: sudo apt install…”

**Next time just run python get_kafka.py --start again.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/README.md:67` — “Leave that terminal open – Ctrl+C stops the broker. Next time just run python get_kafka.py --start again.”

### Big data processing fh kufstein

**Where: Kaggle – free notebooks in the browser — What runs there: Apache Spark and Spark ML (no Java setup on your laptop).**
Confidence 0.68 · active · 1 source
Evidence: `README.md:8` — “Kaggle – free notebooks in the browser | Apache Spark and Spark ML (no Java setup on your laptop)”

**Git pull ; python get_data.py --months 2 # Windows: py -3.12 get_data.py --months 2.**
Confidence 0.44 · candidate · 1 source
Evidence: `README.md:22` — “git pull ; python get_data.py --months 2 # Windows: py -3.12 get_data.py --months 2”

### Kafka lab

**Route B fails if the folder path contains a space (e.g. … Kopie or My Projects). get_kafka.py checks this and stops – then install Kafka somewhere else: python get_kafka.py --dest ~/kafka-course --start.**
Confidence 0.78 · active · 2 sources · when: if the folder path contains a space (e
Evidence: `session-06/README.md:112` — “Classpath is empty | The Kafka folder path contains a space → python get_kafka.py --dest ~/kafka-course”

**Your Python code connects to localhost:9092.**
Confidence 0.57 · candidate · 1 source
Evidence: `README.md:121` — “Your Python code connects to localhost:9092. If neither route works on your laptop, pair up with a neighbour.”

### Newest course material

**On GitHub: open your fork → Sync fork.**
Confidence 0.51 · candidate · 3 sources · when: after "Sync fork" on GitHub
Evidence: `session-04/README.md:39` — “On GitHub: open your fork → Sync fork. Then on your laptop:”

**Git clone https://github.com/ /hok-big-data-processing-2026-2027-pt.git # first time only ; cd hok-big-data-processing-2026-2027-pt ; git pull # every session.**
Confidence 0.48 · candidate · 1 source
Evidence: `session-04/README.md:40` — “git clone https://github.com/ /hok-big-data-processing-2026-2027-pt.git # first time only ; cd hok-big-data-processing-2026-2027-pt ; git pull # every session”

### Alternative dev container github codespaces

**Codespaces: on your fork Code → Codespaces → Create codespace on main; ~3 min for the first build.**
Confidence 0.60 · candidate · 1 source · when: for the first build
Evidence: `README.md:92` — “- Codespaces: on your fork Code → Codespaces → Create codespace on main; ~3 min for the first build. Stop it when you are done (github.com/codespaces → ⋯ → Stop) – otherwise it uses up…”

### Create virtual environment

**Check everything with python session-04/check_env.py.**
Confidence 0.57 · candidate · 1 source
Evidence: `README.md:65` — “Check everything with python session-04/check_env.py. Step-by-step explanations and troubleshooting: session-04/01_python_environments.md and session-04/README.md.”

### Data

**Run once in the terminal: python get_data.py --months 6.**
Confidence 0.61 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-2:2` — “Each month is ~50 MB of Parquet and ~3 million trips. Start with 6 months; we scale up later. Run once in the terminal: python get_data.py --months 6”

### Download data

**Windows: py -3.12 get_data.py --months 2 — macOS / Linux: python3.12 get_data.py --months 2.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:62` — “py -3.12 session-04\check_env.py | python3.12 session-04/check_env.py”

### Get data

**Usage: python get_data.py # 2024-01.**
Confidence 0.45 · candidate · 1 source
Evidence: `get_data.py:1` — “Usage: python get_data.py # 2024-01 .. 2024-06 (~300 MB) + taxi zone lookup python get_data.py --months 2 # what Session 4 needs (~100 MB)”

### Get kafka

**Only uses the Python standard library, like get_data.py.**
Confidence 0.70 · active · 2 sources · when: before you set up an environment
Evidence: `README.md:26` — “get_data.py uses only the Python standard library, so it works even before you set up an environment. It downloads NYC Yellow Taxi trips 2024 (Parquet, ~50 MB per month) and the taxi zone…”

### Install tools

**In the comparison table, VS Code: Windows: code.visualstudio.com, macOS: code.visualstudio.com, Linux (Ubuntu/Debian): code.visualstudio.com.**
Confidence 0.86 · active · 2 sources
Evidence: `README.md:36` — “VS Code + extensions Python and Jupyter | code.visualstudio.com | code.visualstudio.com | code.visualstudio.com”

### Kaggle account

**Settings → Phone verification – without it, notebooks cannot use the internet (we need it to install PySpark).**
Confidence 0.65 · active · 1 source
Evidence: `session-04/README.md:55` — “2. Settings → Phone verification – without it, notebooks cannot use the internet (we need it to install PySpark).”

### Lab saving data models csv

**Needs data/yellow_tripdata_2024-01.parquet (python get_data.py --months 2).**
Confidence 0.61 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:3` — “Runs locally in VS Code with your .venv kernel (Lab A). Needs data/yellow_tripdata_2024-01.parquet (python get_data.py --months 2).”

### Laptop cannot run route

**Everything in Blocks 3 and 4 needs only paper.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:84` — “No problem: pair up with a neighbour whose broker runs. You type on their laptop in Block 1 and run consumer.py on theirs in Block 2. Everything in Blocks 3 and 4 needs only paper.…”

### Newest material update environment

**Check: python -c "import kafka, faker; print(kafka.version)" → 3.x.**
Confidence 0.62 · active · 1 source
Evidence: `session-06/README.md:42` — “Check: python -c "import kafka, faker; print(kafka.version)" → 3.x. (Old tutorials use kafka-python==2.0.2 – it does not work on Python 3.12.)”

### Python right

**Py --list # all Pythons the Windows launcher knows ; python --version ; python session-04\check_env.py.**
Confidence 0.47 · candidate · 1 source
Evidence: `session-04/01_python_environments.md:49` — “py --list # all Pythons the Windows launcher knows ; python --version ; python session-04\check_env.py”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 1 | 2026-10-28 |
| `session-06/get_kafka.py` | code | 0.80 | 1 | 2026-11-11 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `get_data.py` | code | 0.80 | 1 | 2026-10-28 |
| `session-04/README.md` | readme | 0.85 | 10 | 2026-10-28 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `README.md` | readme | 0.85 | 9 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 12 | 2026-11-11 |

## Related Pages

- [[python-environments|Python Environments and Reproducibility]] (32 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (26 shared entities)
- [[spark-architecture|Spark Architecture]] (19 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (18 shared entities)
- [[tooling-kaggle|Kaggle Labs]] (14 shared entities)
- [[unfiled|Unfiled Observations]] (14 shared entities)

## Open Questions

1 prompts from the material are collected in [[questions/course-setup|Questions: Course Setup]].
- Run python session-04/check_env.py again. What changed in Executable and sys.prefix?

## Timeline

- 2026-11-25: new_claim on `claim_1728b45d`
- 2026-11-25: support_update on `claim_26edcb72` (0.61 → 0.51)
- 2026-11-25: new_claim on `claim_98cdf12b`
- 2026-11-25: new_claim on `claim_d7d4bf6d`
- 2026-11-25: new_claim on `claim_e467c9d5`
- 2026-11-25: new_claim on `claim_4e0c1eb8`
- 2026-11-25: evidence_attached on `claim_64fbf0f7` (0.78 → 0.78)
- 2026-11-25: new_claim on `claim_805d7c98`
