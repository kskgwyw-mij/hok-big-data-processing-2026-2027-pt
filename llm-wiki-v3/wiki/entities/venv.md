---
title: venv
type: entity
entity_id: ent_venv
entity_type: tool
claim_ids:
  - claim_d775b13c
  - claim_3bfafe94
  - claim_f0092822
  - claim_30d231b5
  - claim_967d35a4
  - claim_0b3e9120
  - claim_6c1111f0
  - claim_ea75a33c
  - claim_d1a72233
  - claim_c9af32ed
  - claim_518f92ee
  - claim_f0885e5f
  - claim_3ec1671b
  - claim_919b7ce7
  - claim_5c8096b2
  - claim_774b3826
  - claim_8734eda7
  - claim_a004b57f
  - claim_60550010
  - claim_b8cad0cb
  - claim_76c23fc7
  - claim_37399599
  - claim_6e6299d7
  - claim_37227336
  - claim_4c4d2c23
  - claim_380aadd3
  - claim_9e1d77e7
  - claim_5aae3a4d
  - claim_d507dd54
  - claim_b73468f4
  - claim_57aa108c
  - claim_e7b26365
  - claim_d63ae2b6
  - claim_b0f6b957
  - claim_8582a503
  - claim_27e1c1a0
  - claim_c59c93a0
  - claim_2b48846c
  - claim_989f4683
  - claim_547806cd
  - claim_f6716f97
confidence: 0.716
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_467d2d1e
  - src_59b6ded4
  - src_6494d099
  - src_6e2e5684
  - src_799c8bd7
  - src_8615b91f
  - src_8e87808f
  - src_b3356305
  - src_b94acce4
  - src_bb056c24
  - src_cecf99ea
---

# venv

Type: tool. Mentioned in 41 claims across 6 topics.
Aliases: virtual environment, .venv.

## Claims

- **You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.** Confidence 0.89 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Lock file: venv: no (pip freeze by hand), pyenv: no, uv: yes uv.lock.** Confidence 0.86 · [[python-environments|Python Environments and Reproducibility]]
- **Lab: A — Topic: Python environments: venv, pyenv, uv; Where: laptop, terminal; File: 01_python_environments.md, check_env.py.** Confidence 0.83 · [[python-environments|Python Environments and Reproducibility]]
- **✓ What you should see ✗ If it fails Prompt starts with (.venv) · check: Could not open requirements file → you are in session-06/: python -c "import kafka, faker; print(kafka.version)" → 3.x cd.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Python 3.12: Windows: winget install Python.Python.3.12 or python.org installer (tick "Add python.exe to PATH" and "py launcher"), macOS: brew install python@3.12 or python.org installer, Linux (Ubuntu/Debian): sudo apt install python3.12 python3.12-venv.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **Runs locally with your .venv kernel.** Confidence 0.80 · [[python-environments|Python Environments and Reproducibility]]
- **In VS Code: Ctrl/Cmd + Shift + P → "Python: Select Interpreter" → .venv. In a notebook, pick the kernel .venv (top right).** Confidence 0.79 · [[python-environments|Python Environments and Reproducibility]]
- **Run the next commands in the repo root (where requirements-local.txt and .venv/ are), not in session-06/.** Confidence 0.79 · [[python-environments|Python Environments and Reproducibility]]
- **Run once: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned and activate again.** Confidence 0.79 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Windows: venv: yes, pyenv: only via the port pyenv-win, uv: yes.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: externally-managed-environment on pip install — OS: macOS (Homebrew), Linux; Fix: You are not in a venv – activate .venv first; never use sudo pip.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **Which two files should have been in the repository? » .venv is activated, pip install duckdb worked – Jupyter still says ModuleNotFoundError.** Confidence 0.77 · [[data-duckdb|DuckDB]]
- **» "I use pyenv, so I don't need venv." Why is this only half true? » Your notebook fails on the server with an AttributeError in pandas.** Confidence 0.77 · [[python-environments|Python Environments and Reproducibility]]
- **Your Python code always runs in .venv and connects to localhost:9092.** Confidence 0.77 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: ensurepip is not available / No module named venv — OS: Ubuntu/Debian; Fix: sudo apt install python3.12-venv.** Confidence 0.73 · [[python-environments|Python Environments and Reproducibility]]
- **Problem: Which Python version? — Example: Project A needs 3.12, project B still runs on 3.10; Tool: pyenv (or uv python).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Solves: venv: package isolation, pyenv: Python version management, uv: both.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Comes with Python: venv: yes (standard library), pyenv: no separate install, uv: no separate install (one binary).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Pyenv and venv do not compete: pyenv picks the interpreter, venv isolates the packages. uv is one tool that does both (and installs packages much faster).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Experiment 2 – a second consumer in the SAME group.** Confidence 0.72 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Uv init --python 3.12 ; uv add pandas duckdb.** Confidence 0.72 · [[engines-single_machine|Single-Machine Engines]]
- **Step 1 + 2 - Get the material, activate .venv.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Pip install, live on this laptop uv python install 3.12 # pre-built Python, seconds uv venv --python 3.12 .venv [__ seconds] # interpreter + environment uv pip install -r requirements.txt uv pip install, same packages # parallel downloads, cached uv add pandas duckdb # project mode: writes uv.lock [__ seconds].** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **# no .venv yet? py -m venv .venv # no .venv yet? python3 -m venv .venv # no .venv yet? python3 -m venv .venv PS> .venv\Scripts\Activate.ps1 $ source .venv/bin/activate $ source .venv/bin/activate PS> pip install -r requirements-local.txt $ pip install -r requirements-local.txt $ pip install -r requirements-local.txt.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Checkpoint before the break check_env.py says "Inside a virtual env? yes" – and your notebook kernel is .venv.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Open 02_kafka_python.ipynb from the session-06/ folder · kernel .venv.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: Notebook says ModuleNotFoundError although you installed the package — OS: all; Fix: The notebook kernel is not your .venv. Top right in the notebook → Select Kernel → .venv.** Confidence 0.67 · [[python-environments|Python Environments and Reproducibility]]
- **Open 3–4 terminals in VS Code (+ in the terminal panel), activate .venv in each, cd session-06.** Confidence 0.66 · [[python-environments|Python Environments and Reproducibility]]
- **It's fine if it says "NO – activate .venv first" and packages are missing: that's what Lab A is about.** Confidence 0.66 · [[python-environments|Python Environments and Reproducibility]]
- **Pyenv chooses the interpreter. venv chooses the packages. uv does both.** Confidence 0.65 · [[python-environments|Python Environments and Reproducibility]]
- **Pyenv installs Python versions and switches between them per folder (.python-version file).** Confidence 0.65 · [[python-environments|Python Environments and Reproducibility]]
- **Create and activate .venv · 10 min.** Confidence 0.64 · [[python-environments|Python Environments and Reproducibility]]
- **Data/, .venv/, executed notebooks with large outputs, or files with personal information.** Confidence 0.62 · [[python-environments|Python Environments and Reproducibility]]
- **Clean up afterwards: delete the folder .venv-pd2 (it is just a folder!).** Confidence 0.61 · [[python-environments|Python Environments and Reproducibility]]
- **Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python consumer.py # group group-a, topic user-events, until Ctrl+C python consumer.py --group group-a --name C2 # a SECOND consumer in the same group (2nd terminal) python consumer.py --group group-b # a different group: gets ALL messages again python consumer.py --from latest # a NEW group starts at the end instead of the beginning python consumer.py --idle 10 # stop after 10 s without new messages.** Confidence 0.58 · [[kafka-cluster|Kafka Cluster]]
- **Only uses the Python standard library, so it also runs before you created a virtual environment.** Confidence 0.55 · [[python-environments|Python Environments and Reproducibility]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.55 · [[python-environments|Python Environments and Reproducibility]]
- **Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py --count 30 --interval 0.2 python producer.py --no-key # same events, but WITHOUT a key python producer.py --data users --topic registered_user # the original lab: fake users, no key.** Confidence 0.50 · [[kafka-producers|Kafka Producers]]
- **Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.** Confidence 0.44 · [[python-environments|Python Environments and Reproducibility]]
- **Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[uv|uv]] (11)
- [[pip|pip]] (10)
- [[pyenv|pyenv]] (10)
- [[requirements_txt|requirements.txt]] (9)
- [[python|Python 3.12]] (8)
- [[jupyter|Jupyter]] (7)
- [[kafka|Kafka]] (5)
- [[pandas|pandas]] (5)
- [[duckdb|DuckDB]] (4)
- [[linux|Linux]] (4)
