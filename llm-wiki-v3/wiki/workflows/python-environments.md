---
title: Python Environments and Reproducibility
type: workflows
topic: python.environments
entity_ids:
  - ent_venv
  - ent_pyenv
  - ent_requirements_txt
  - ent_uv
  - ent_python
  - ent_pip
  - ent_dev_container
  - ent_macos
  - ent_linux
  - ent_jupyter
  - ent_kafka
  - ent_windows
claim_ids:
  - claim_b6b563e5
  - claim_d23729eb
  - claim_d775b13c
  - claim_1fc89e17
  - claim_10fe9fc5
  - claim_2785ec80
  - claim_3bfafe94
  - claim_30d231b5
  - claim_967d35a4
  - claim_e5fbb39c
  - claim_16cf3adc
  - claim_505495af
  - claim_670ad715
  - claim_0b3e9120
  - claim_6c1111f0
  - claim_ea75a33c
  - claim_d1a72233
  - claim_c9af32ed
  - claim_02136040
  - claim_7a967f85
  - claim_2281d11e
  - claim_518f92ee
  - claim_b0dbd1e0
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
  - claim_2162a394
  - claim_079ed9fb
  - claim_3fab2389
  - claim_3eb495fc
  - claim_64a2b1df
  - claim_6e6299d7
  - claim_4c4d2c23
  - claim_380aadd3
  - claim_54363381
  - claim_201c7650
  - claim_0c5c079b
  - claim_01edbaf1
  - claim_1d96ae1a
  - claim_d507dd54
  - claim_b73468f4
  - claim_89b3b9fb
  - claim_57aa108c
  - claim_ebd0c351
  - claim_c831872a
  - claim_e7b26365
  - claim_d63ae2b6
  - claim_b0f6b957
  - claim_27e1c1a0
  - claim_104a768a
  - claim_c59c93a0
  - claim_2b48846c
  - claim_989f4683
  - claim_547806cd
  - claim_2578d2b6
  - claim_f6716f97
confidence: 0.703
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_1cebb3bb
  - src_41b3a933
  - src_467d2d1e
  - src_59b6ded4
  - src_6494d099
  - src_6e2e5684
  - src_799c8bd7
  - src_8615b91f
  - src_8e87808f
  - src_96e79681
  - src_b3356305
  - src_cecf99ea
review_required: false
---

# Python Environments and Reproducibility

Rendered from 64 claims and 13 sources. Median confidence 0.70; 57 active, 0 disputed, 0 superseded.

## Current Understanding

### Create activate virtual environment venv

**You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.**
Confidence 0.89 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p8:6` — “It is just a folder .venv/ Broken? Delete it and rebuild it in a minute. pyvenv.cfg # which base Python bin/ # Scripts\ on Windows activate = change PATH python # → base interpreter Puts…”

**In VS Code: Ctrl/Cmd + Shift + P → "Python: Select Interpreter" → .venv. In a notebook, pick the kernel .venv (top right).**
Confidence 0.79 · active · 2 sources
Evidence: `session-04/01_python_environments.md:86` — “2. In VS Code: Ctrl/Cmd + Shift + P → "Python: Select Interpreter" → .venv. In a notebook, pick the kernel .venv (top right).”

**Run once: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned and activate again.**
Confidence 0.79 · active · 2 sources · when: when activating
Evidence: `session-04/README.md:73` — “running scripts is disabled on this system when activating .venv | Windows | Set-ExecutionPolicy -Scope CurrentUser RemoteSigned, then activate again”

**Use Python 3.12 (the same version as the course dev container).**
Confidence 0.65 · active · 1 source
Evidence: `session-04/01_python_environments.md:62` — “Use Python 3.12 (the same version as the course dev container).”

**Requirements-local.txt = everything except Spark.**
Confidence 0.61 · active · 1 source
Evidence: `session-04/01_python_environments.md:72` — “> requirements-local.txt = everything except Spark. Spark runs on Kaggle today; the full > requirements.txt (with PySpark, ≈ 400 MB more) is for the dev container or a laptop with Java 17.”

**Python3.12 -m venv .venv # or: python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt.**
Confidence 0.41 · candidate · 2 sources
Evidence: `session-04/01_python_environments.md:72` — “py -3.12 -m venv .venv ; python -m pip install --upgrade pip ; pip install -r requirements-local.txt”

### Different problems

**In the comparison table, Lock file: venv: no (pip freeze by hand), pyenv: no, uv: yes uv.lock.**
Confidence 0.86 · active · 2 sources
Evidence: `session-04/01_python_environments.md:35` — “Lock file | no (pip freeze by hand) | no | yes uv.lock”

**In the comparison table, Windows: venv: yes, pyenv: only via the port pyenv-win, uv: yes.**
Confidence 0.78 · active · 1 source
Evidence: `session-04/01_python_environments.md:33` — “Windows | yes | only via the port pyenv-win | yes”

**Problem: Which Python version? — Example: Project A needs 3.12, project B still runs on 3.10; Tool: pyenv (or uv python).**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:16` — “Which packages, in which versions? | Project A needs pandas 3, project B breaks with pandas 3 | venv (or uv venv)”

**In the comparison table, Solves: venv: package isolation, pyenv: Python version management, uv: both.**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:36` — “Typical problem | forgot to activate → packages land in the wrong Python | shell setup (shims, PATH) | newer tool, team must agree to use it”

**In the comparison table, Comes with Python: venv: yes (standard library), pyenv: no separate install, uv: no separate install (one binary).**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:32` — “Comes with Python | yes (standard library) | no separate install | no separate install (one binary)”

**Pyenv and venv do not compete: pyenv picks the interpreter, venv isolates the packages. uv is one tool that does both (and installs packages much faster).**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:26` — “pyenv and venv do not compete: pyenv picks the interpreter, venv isolates the packages. uv is one tool that does both (and installs packages much faster).”

### Pyenv reference homework live today

**OS: Linux — Install: curl -fsSL https://pyenv.run \; value: bash (needs build dependencies, see pyenv wiki).**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:161` — “Linux | curl -fsSL https://pyenv.run \ | bash (needs build dependencies, see pyenv wiki)”

**OS: Windows — Install: pyenv-win: Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1".**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:162` — “Windows | pyenv-win: Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile…”

**OS: macOS — Install: brew install pyenv + add the shell lines from pyenv init to ~/.zshrc.**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:160` — “macOS | brew install pyenv + add the shell lines from pyenv init to ~/.zshrc”

**Pyenv installs Python versions and switches between them per folder (.python-version file).**
Confidence 0.65 · active · 1 source
Evidence: `session-04/01_python_environments.md:156` — “pyenv installs Python versions and switches between them per folder (.python-version file).”

**On Windows, pyenv-win may need the full version number: check pyenv install --list first (e.g. pyenv install 3.12.10).**
Confidence 0.60 · candidate · 1 source
Evidence: `session-04/01_python_environments.md:169` — “On Windows, pyenv-win may need the full version number: check pyenv install --list first (e.g. pyenv install 3.12.10).”

### Modern shortcut uv

**OS: macOS / Linux — Command: curl -LsSf https://astral.sh/uv/install.sh \; value: sh.**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:131` — “macOS / Linux | curl -LsSf https://astral.sh/uv/install.sh \ | sh”

**OS: Windows — Command: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \; value: iex".**
Confidence 0.72 · active · 1 source
Evidence: `session-04/01_python_environments.md:133` — “Windows | powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \ | iex"”

**OS: macOS (Homebrew) — Command: brew install uv.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/01_python_environments.md:132` — “macOS (Homebrew) | brew install uv”

**Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.**
Confidence 0.55 · candidate · 3 sources · when: if missing
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p13:6` — “1. Where is my Python? · 5 min pip install -r requirements-local.txt”

### Reproducible python saving data models

**Lab: A — Topic: Python environments: venv, pyenv, uv; Where: laptop, terminal; File: 01_python_environments.md, check_env.py.**
Confidence 0.83 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p3:8` — “A Python environments: venv, pyenv, uv Laptop · terminal 35 min”

**Symptom: externally-managed-environment on pip install — OS: macOS (Homebrew), Linux; Fix: You are not in a venv – activate .venv first; never use sudo pip.**
Confidence 0.78 · active · 1 source
Evidence: `session-04/README.md:75` — “externally-managed-environment on pip install | macOS (Homebrew), Linux | You are not in a venv – activate .venv first; never use sudo pip”

**Symptom: ensurepip is not available / No module named venv — OS: Ubuntu/Debian; Fix: sudo apt install python3.12-venv.**
Confidence 0.73 · active · 1 source
Evidence: `session-04/README.md:74` — “ensurepip is not available / No module named venv | Ubuntu/Debian | sudo apt install python3.12-venv”

**Symptom: Notebook says ModuleNotFoundError although you installed the package — OS: all; Fix: The notebook kernel is not your .venv. Top right in the notebook → Select Kernel → .venv.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/README.md:76` — “Notebook says ModuleNotFoundError although you installed the package | all | The notebook kernel is not your .venv. Top right in the notebook → Select Kernel → .venv”

### Code different environment result

**We create two small environments that differ in one package version.**
Confidence 0.65 · active · 1 source
Evidence: `session-04/01_python_environments.md:101` — “We create two small environments that differ in one package version.”

**Question: the same line of code prints a different dtype.**
Confidence 0.61 · active · 1 source
Evidence: `session-04/01_python_environments.md:118` — “Question: the same line of code prints a different dtype. Which one is "right"? What does this mean for a notebook you hand over to a colleague without a version file?”

**Clean up afterwards: delete the folder .venv-pd2 (it is just a folder!).**
Confidence 0.61 · active · 1 source
Evidence: `session-04/01_python_environments.md:121` — “Clean up afterwards: delete the folder .venv-pd2 (it is just a folder!).”

### Alternative dev container github codespaces

**A Codespace has 8 GB RAM and effectively one physical CPU core: fine for learning Spark, not for speed comparisons.**
Confidence 0.65 · active · 1 source · when: for learning Spark; for speed comparisons
Evidence: `README.md:97` — “A Codespace has 8 GB RAM and effectively one physical CPU core: fine for learning Spark, not for speed comparisons.”

**The repository also contains a dev container with Python 3.12, Java 17 and everything from requirements.txt – besides Kaggle, the way to run Spark without installing Java yourself.**
Confidence 0.62 · active · 1 source
Evidence: `README.md:89` — “The repository also contains a dev container with Python 3.12, Java 17 and everything from requirements.txt – besides Kaggle, the way to run Spark without installing Java yourself.”

### Kafka lab exam preparation

**Symptom: ModuleNotFoundError: kafka.vendor.six.moves — Fix: You have the old kafka-python 2.0.2 → pip install -r requirements-local.txt.**
Confidence 0.83 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p97:19` — “ModuleNotFoundError: kafka.vendor.six.moves Old kafka-python 2.0.2 → pip install -r requirements-local.txt”

**Symptom: Could not open requirements file: requirements-local.txt — Fix: It lives in the repo root → cd .. first, or pip install -r ../requirements-local.txt.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:108` — “Could not open requirements file: requirements-local.txt | It lives in the repo root → cd .. first, or pip install -r ../requirements-local.txt”

### Newest material update environment

**Run the next commands in the repo root (where requirements-local.txt and .venv/ are), not in session-06/.**
Confidence 0.79 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p86:9` — “2 Run in the REPO ROOT (folder with requirements-local.txt and .venv/), not in session-06/”

**Source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker.**
Confidence 0.44 · candidate · 1 source
Evidence: `session-06/README.md:33` — “source .venv/bin/activate ; pip install -r requirements-local.txt # new: kafka-python and faker”

### Pre flight checklist anything else

**Work with one month only today – this keeps memory usage well below the 8 GB Codespace limit.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:27` — “4. Work with one month only today – this keeps memory usage well below the 8 GB Codespace limit.”

**Close all other notebook kernels – VS Code: Jupyter panel → right-click each other kernel → Shut Down Kernel.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:24` — “1. Close all other notebook kernels – VS Code: Jupyter panel → right-click each other kernel → Shut Down Kernel.”

### Consumer groups real processes terminal

**Open 3–4 terminals in VS Code (+ in the terminal panel), activate .venv in each, cd session-06.**
Confidence 0.66 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:15` — “Notebook cells run one after another, so we need separate terminals for parallel consumers. Open 3–4 terminals in VS Code (+ in the terminal panel), activate .venv in each, cd session-06.”

### Dev container github codespace

**» Github Codespace » Your local environment » READ.me.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p16:3` — “» Github Codespace » Your local environment » READ.me”

### Dev container java macos

**No Java 17? » For macOS, Linux, WSL, Codespace – needs Java 17+ mac: brew install openjdk@17.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p88:5` — “No Java 17? » For macOS, Linux, WSL, Codespace – needs Java 17+ mac: brew install openjdk@17”

### Get data

**Only uses the Python standard library, so it also runs before you created a virtual environment.**
Confidence 0.55 · candidate · 1 source · when: before you created a virtual environment
Evidence: `get_data.py:1` — “Only uses the Python standard library, so it also runs before you created a virtual environment.”

### Get kafka

**Works on macOS and Linux (and in the Codespace).**
Confidence 0.69 · active · 2 sources
Evidence: `README.md:113` — “B – native Kafka | Java 17+ (macOS, Linux, WSL or the Codespace) | python get_kafka.py --start (downloads Kafka 4.4.0, ~130 MB)”

### Install tools

**In the comparison table, Python 3.12: Windows: winget install Python.Python.3.12 or python.org installer (tick "Add python.exe to PATH" and "py launcher"), macOS: brew install python@3.12 or python.org installer, Linux (Ubuntu/Debian): sudo apt install python3.12 python3.12-venv.**
Confidence 0.81 · active · 2 sources
Evidence: `README.md:38` — “Python 3.12 | winget install Python.Python.3.12 (tick "Add to PATH" in the python.org installer) | brew install python@3.12 | sudo apt install python3.12 python3.12-venv”

### Jupyter checkpoint break check env py

**Checkpoint before the break check_env.py says "Inside a virtual env? yes" – and your notebook kernel is .venv.**
Confidence 0.70 · active · 1 source · when: before the break check_env
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p13:13` — “Checkpoint before the break check_env.py says "Inside a virtual env? yes" – and your notebook kernel is .venv.”

### Jupyter open kafka python ipynb session 06

**Open 02_kafka_python.ipynb from the session-06/ folder · kernel .venv.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p94:3` — “Open 02_kafka_python.ipynb from the session-06/ folder · kernel .venv”

### Jupyter pyenv need venv

**» "I use pyenv, so I don't need venv." Why is this only half true? » Your notebook fails on the server with an AttributeError in pandas.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p14:3` — “» "I use pyenv, so I don't need venv." Why is this only half true? » Your notebook fails on the server with an AttributeError in pandas. Which two files should have been in the repository?…”

### Kafka lab

**Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).**
Confidence 0.60 · candidate · 1 source
Evidence: `README.md:106` — “1. Update your environment: activate .venv, then pip install -r requirements-local.txt (adds kafka-python 3.x and Faker; the old kafka-python 2.0.2 does not work on Python 3.12).”

### Kafka python producers consumers consumer

**Library: kafka-python ≥ 3.0 — Why: pure-Python Kafka client (version 2.0.2 from older tutorials does not work on Python 3.12).**
Confidence 0.69 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-0:18` — “kafka-python ≥ 3.0 | pure-Python Kafka client (version 2.0.2 from older tutorials does not work on Python 3.12)”

### Lab c duckdb database file

**Runs locally with your .venv kernel.**
Confidence 0.80 · active · 3 sources
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:3` — “Runs locally in VS Code with your .venv kernel (Lab A). Needs data/yellow_tripdata_2024-01.parquet (python get_data.py --months 2).”

### Never commit

**Data/, .venv/, executed notebooks with large outputs, or files with personal information.**
Confidence 0.62 · active · 1 source
Evidence: `README.md:141` — “data/, .venv/, executed notebooks with large outputs, or files with personal information. The .gitignore already excludes data files, virtual environments and caches, as well as the Kafka…”

### Path typical trap forgot

**Typical trap forgot to activate shell setup, PATH team must agree on it.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p11:17` — “Typical trap forgot to activate shell setup, PATH team must agree on it”

### Predict run

**Use January 2024 only – enough data, fits comfortably in the Codespace.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-7` — “Use January 2024 only – enough data, fits comfortably in the Codespace”

### Pyenv chooses interpreter

**Pyenv chooses the interpreter. venv chooses the packages. uv does both.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p7:13` — “pyenv chooses the interpreter. venv chooses the packages. uv does both.”

### Python environments venv pyenv uv

**Work in the VS Code terminal of the repository folder.**
Confidence 0.65 · active · 1 source
Evidence: `session-04/01_python_environments.md:6` — “Work in the VS Code terminal of the repository folder. Every step shows the command for macOS / Linux and for Windows (PowerShell).”

### Python reads folder runs

**Reads the folder's runs you type first on PATH .python-version Python 3.12 python pyenv shim ~/.pyenv/versions/ → 3.12.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p9:5` — “reads the folder's runs you type first on PATH .python-version Python 3.12 python pyenv shim ~/.pyenv/versions/ → 3.12”

### Python right

**Write down: the path of the executable and the line Inside a virtual env?.**
Confidence 0.65 · active · 1 source
Evidence: `session-04/01_python_environments.md:56` — “Write down: the path of the executable and the line Inside a virtual env?.”

### Requirements file

**File: requirements.txt — Contains: the above + PySpark 4.0 and Delta Lake (needs Java 17+); Use it for: the dev container, or a laptop with Java 17 installed.**
Confidence 0.68 · active · 1 source
Evidence: `README.md:73` — “requirements.txt | the above + PySpark 4.0 and Delta Lake (needs Java 17+) | the dev container, or a laptop with Java 17 installed”

### Requirements txt fails prompt starts

**✓ What you should see ✗ If it fails Prompt starts with (.venv) · check: Could not open requirements file → you are in session-06/: python -c "import kafka, faker; print(kafka.version)" → 3.x cd.**
Confidence 0.81 · active · 1 source · when: If it fails Prompt starts with (
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p86:23` — “✓ What you should see ✗ If it fails Prompt starts with (.venv) · check: Could not open requirements file → you are in session-06/: python -c "import kafka, faker; print(kafka.version)" →…”

### Requirements txt level

**LEVEL 3 LEVEL 1 LEVEL 2 Container requirements.txt Lock file Dev container / Docker: OS, Python The packages you use directly, with pip freeze or uv.lock: every package, and Java pinned too – our version ranges. exact versions.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p12:6` — “LEVEL 3 LEVEL 1 LEVEL 2 Container requirements.txt Lock file Dev container / Docker: OS, Python The packages you use directly, with pip freeze or uv.lock: every package, and Java pinned…”

### Requirements txt pip install live

**Pip install, live on this laptop uv python install 3.12 # pre-built Python, seconds uv venv --python 3.12 .venv [__ seconds] # interpreter + environment uv pip install -r requirements.txt uv pip install, same packages # parallel downloads, cached uv add pandas duckdb # project mode: writes uv.lock [__ seconds].**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p10:6` — “pip install, live on this laptop uv python install 3.12 # pre-built Python, seconds uv venv --python 3.12 .venv [__ seconds] # interpreter + environment uv pip install -r requirements.txt…”

### Requirements txt venv yet py

**# no .venv yet? py -m venv .venv # no .venv yet? python3 -m venv .venv # no .venv yet? python3 -m venv .venv PS> .venv\Scripts\Activate.ps1 $ source .venv/bin/activate $ source .venv/bin/activate PS> pip install -r requirements-local.txt $ pip install -r requirements-local.txt $ pip install -r requirements-local.txt.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p86:13` — “# no .venv yet? py -m venv .venv # no .venv yet? python3 -m venv .venv # no .venv yet? python3 -m venv .venv PS> .venv\Scripts\Activate.ps1 $ source .venv/bin/activate $ source…”

### Run environment check

**It's fine if it says "NO – activate .venv first" and packages are missing: that's what Lab A is about.**
Confidence 0.66 · active · 1 source · when: if it says "NO – activate
Evidence: `session-04/README.md:64` — “It's fine if it says "NO – activate .venv first" and packages are missing: that's what Lab A is about.”

### Venv create activate

**Create and activate .venv · 10 min.**
Confidence 0.64 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p13:8` — “2. Create and activate .venv · 10 min”

### Venv python code always

**Your Python code always runs in .venv and connects to localhost:9092.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p85:25` — “Your Python code always runs in .venv and connects to localhost:9092”

### Venv step material activate

**Step 1 + 2 - Get the material, activate .venv.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p86:1` — “Step 1 + 2 - Get the material, activate .venv”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 26 | 2026-10-28 |
| `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |
| `session-06/get_kafka.py` | code | 0.80 | 1 | 2026-11-11 |
| `get_data.py` | code | 0.80 | 1 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 12 | 2026-11-25 |
| `session-04/README.md` | readme | 0.85 | 7 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 3 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 8 | 2026-11-25 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `README.md` | readme | 0.85 | 10 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 4 | 2026-11-11 |

## Related Pages

- [[engines-single_machine|Single-Machine Engines]] (112 shared entities)
- [[course-setup|Course Setup]] (96 shared entities)
- [[data-duckdb|DuckDB]] (82 shared entities)
- [[unfiled|Unfiled Observations]] (82 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (69 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (68 shared entities)

## Open Questions

12 prompts from the material are collected in [[questions/python-environments|Questions: Python Environments and Reproducibility]].
- C3 (2 P) "I use pyenv, so I don't need venv." Explain why this is only half true.
- C4 (2 P) What is the difference between a requirements.txt with version ranges and a lock file?
- Justify. » Why is .venv/ in .gitignore while requirements.txt is committed?

## Timeline

- 2026-11-25: new_claim on `claim_c59c93a0`
- 2026-11-25: new_claim on `claim_2b48846c`
- 2026-11-25: new_claim on `claim_989f4683`
- 2026-11-25: new_claim on `claim_547806cd`
- 2026-11-25: support_update on `claim_d507dd54` (0.62 → 0.79)
- 2026-11-25: new_claim on `claim_2578d2b6`
- 2026-11-25: new_claim on `claim_f6716f97`
- 2026-11-25: support_update on `claim_1d96ae1a` (0.68 → 0.83)
