# Lab A – Python environments: venv, pyenv and uv  (≈ 35 min)

**Goal:** after this lab you can explain *which Python* and *which packages* your notebook really
uses, and you can rebuild the same environment on another machine.

Work in the **VS Code terminal** of the repository folder.
Every step shows the command for **macOS / Linux** and for **Windows (PowerShell)**.

---

## 0. Two different problems

| Problem | Example | Tool |
|---|---|---|
| **Which Python version?** | Project A needs 3.12, project B still runs on 3.10 | **pyenv** (or `uv python`) |
| **Which packages, in which versions?** | Project A needs pandas 3, project B breaks with pandas 3 | **venv** (or `uv venv`) |

```
  pyenv / uv python          →  installs several Python VERSIONS side by side
        └── python3.12
              └── venv / uv venv   →  one isolated FOLDER of packages per project
                    ├── project-a/.venv   pandas 3.1, pyspark 4.0
                    └── project-b/.venv   pandas 2.3
```

pyenv and venv do **not** compete: pyenv picks the interpreter, venv isolates the packages.
**uv** is one tool that does both (and installs packages much faster).

| | venv | pyenv | uv |
|---|---|---|---|
| Solves | package isolation | Python version management | both |
| Comes with Python | ✓ (standard library) | ✗ separate install | ✗ separate install (one binary) |
| Windows | ✓ | only via the port **pyenv-win** | ✓ |
| How it gets Python | uses the Python you have | **compiles from source** on macOS/Linux (needs build tools, 3–10 min) | downloads a pre-built Python (seconds) |
| Lock file | ✗ (`pip freeze` by hand) | ✗ | ✓ `uv.lock` |
| Typical problem | forgot to activate → packages land in the wrong Python | shell setup (shims, `PATH`) | newer tool, team must agree to use it |

---

## 1. Where is my Python right now?  (5 min)

macOS / Linux:
```bash
python3 --version
which -a python3
python3 session-04/check_env.py
```
Windows (PowerShell):
```powershell
py --list                      # all Pythons the Windows launcher knows
python --version
Get-Command python -All
python session-04\check_env.py
```

**Write down:** the path of the executable and the line `Inside a virtual env?`.

---

## 2. Create and activate a virtual environment with venv  (10 min)

Use Python **3.12** (the same version as the course dev container).

macOS / Linux:
```bash
python3.12 -m venv .venv          # or: python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-local.txt
```
Windows (PowerShell):
```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-local.txt
```
> `requirements-local.txt` = everything except Spark. Spark runs on Kaggle today; the full
> `requirements.txt` (with PySpark, ≈ 400 MB more) is for the dev container or a laptop with Java 17.

> **Windows: "running scripts is disabled on this system"?** Run once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` and activate again.

Now:
1. Run `python session-04/check_env.py` again. What changed in `Executable` and `sys.prefix`?
2. In VS Code: **Ctrl/Cmd + Shift + P → "Python: Select Interpreter" → `.venv`**.
   In a notebook, pick the kernel **`.venv`** (top right).
3. Freeze what you installed:
   ```bash
   pip freeze > requirements-lock.txt
   ```
   Open the file. Why is it much longer than `requirements.txt`?

> `.venv/` is in `.gitignore`. You never commit the environment itself – only the *recipe*
> (`requirements.txt`, lock file) to rebuild it.

---

## 3. Same code, different environment, different result  (10 min)

We create two small environments that differ in **one** package version.

macOS / Linux:
```bash
python3.12 -m venv .venv-pd2
.venv-pd2/bin/pip install -q "pandas<3"
.venv/bin/python     -c "import pandas as pd; print(pd.__version__, pd.Series(['a','b']).dtype)"
.venv-pd2/bin/python -c "import pandas as pd; print(pd.__version__, pd.Series(['a','b']).dtype)"
```
Windows (PowerShell):
```powershell
py -3.12 -m venv .venv-pd2
.venv-pd2\Scripts\pip install -q "pandas<3"
.venv\Scripts\python     -c "import pandas as pd; print(pd.__version__, pd.Series(['a','b']).dtype)"
.venv-pd2\Scripts\python -c "import pandas as pd; print(pd.__version__, pd.Series(['a','b']).dtype)"
```

**Question:** the same line of code prints a different dtype. Which one is "right"?
What does this mean for a notebook you hand over to a colleague without a version file?

Clean up afterwards: delete the folder `.venv-pd2` (it is just a folder!).

---

## 4. The modern shortcut: uv  (10 min)

Install uv (one binary, no admin rights needed):

| OS | Command |
|---|---|
| macOS / Linux | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| macOS (Homebrew) | `brew install uv` |
| Windows | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` |

Open a **new** terminal, then:
```bash
uv python list                           # Python versions uv can see or install
uv venv --python 3.12 .venv-uv           # creates the env; downloads 3.12 if missing
uv pip install --python .venv-uv -r requirements-local.txt
```
Compare: how long did `pip install -r requirements-local.txt` take in step 2, and how long does uv take?
(Your numbers: pip [__ s], uv [__ s].)

Optional – a project with a real lock file:
```bash
mkdir ../uv-demo && cd ../uv-demo
uv init --python 3.12
uv add pandas duckdb
cat uv.lock | head -30          # Windows: Get-Content uv.lock -Head 30
```

---

## 5. pyenv – for reference and homework (not live today)

pyenv installs Python versions and switches between them per folder (`.python-version` file).

| OS | Install |
|---|---|
| macOS | `brew install pyenv` + add the shell lines from `pyenv init` to `~/.zshrc` |
| Linux | `curl -fsSL https://pyenv.run \| bash` (needs build dependencies, see pyenv wiki) |
| Windows | **pyenv-win**: `Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"` |

```bash
pyenv install 3.12          # macOS/Linux: compiles from source – several minutes
pyenv local 3.12            # writes .python-version in this folder
python -m venv .venv        # pyenv chooses the version, venv isolates the packages
```
On Windows, pyenv-win may need the full version number: check `pyenv install --list` first
(e.g. `pyenv install 3.12.10`).

---

## 6. Exam-style questions

1. A colleague says: *"I use pyenv, so I don't need venv."* Explain in two sentences why this is
   only half true.
2. Your notebook runs on your laptop but fails on the server with `AttributeError` in pandas.
   Name **two** files you should have put into the repository to prevent this, and what each contains.
3. You activated `.venv`, ran `pip install duckdb`, and Jupyter still says
   `ModuleNotFoundError: duckdb`. What is the most likely cause, and how do you check it?
4. Scenario: 25 students on Windows, macOS and Linux need the same Python 3.12 environment in
   10 minutes, without admin rights. Choose between pyenv + venv and uv, and justify.
5. Why is `.venv/` in `.gitignore`, while `requirements.txt` is committed?
