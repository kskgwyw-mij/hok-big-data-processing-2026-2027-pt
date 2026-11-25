# Session 4 – Reproducible Python, saving data & models, DuckDB, Spark ML

Today you work in **two places**: your **own laptop** (VS Code) for Labs A–C and **Kaggle** for Lab D (Spark).
Lab C is **homework** this time – we only look at one part of it together in class.

| Lab | Topic | Where | File |
|---|---|---|---|
| A | Python environments: venv, pyenv, uv | laptop, terminal | `01_python_environments.md`, `check_env.py` |
| B | CSV vs. pickle vs. Parquet, saving models | laptop, notebook | `02_file_formats_and_pickle.ipynb` |
| C | DuckDB as a database file – **homework** | laptop, notebook | `03_duckdb_database.ipynb` |
| D | Spark fundamentals (Session 2) + Spark ML | Kaggle | `04_spark_fundamentals_and_ml.ipynb` |

**AI rule for the labs:** AI assistants are allowed, but you must be able to explain every line you hand in.
The exam is without AI.

---

## ✅ Before the session (at home, ~20 min)

Do steps 1–5 **before** we meet. If something fails, write down the error message and bring it.

### 1. Install the tools

| | Windows | macOS | Linux (Ubuntu/Debian) |
|---|---|---|---|
| **VS Code** | code.visualstudio.com | code.visualstudio.com | code.visualstudio.com |
| VS Code extensions | **Python**, **Jupyter** (Microsoft) | same | same |
| **Git** | `winget install Git.Git` | `xcode-select --install` | `sudo apt install git` |
| **Python 3.12** | `winget install Python.Python.3.12` or python.org installer (tick **"Add python.exe to PATH"** and **"py launcher"**) | `brew install python@3.12` or python.org installer | `sudo apt install python3.12 python3.12-venv` |

Check in a **new** terminal:

| Windows (PowerShell) | macOS / Linux |
|---|---|
| `py -3.12 --version` | `python3.12 --version` |
| `git --version` | `git --version` |

### 2. Get the newest course material
On GitHub: open **your fork** → **Sync fork**. Then on your laptop:
```bash
git clone https://github.com/<your-username>/hok-big-data-processing-2026-2027-pt.git   # first time only
cd hok-big-data-processing-2026-2027-pt
git pull                                                                                # every session
```

### 3. Download the data (~100 MB, standard library only – no packages needed)
| Windows | macOS / Linux |
|---|---|
| `py -3.12 get_data.py --months 2` | `python3.12 get_data.py --months 2` |

You should now have `data/yellow_tripdata_2024-01.parquet`, `…-02.parquet` and `data/taxi_zone_lookup.csv`.

### 4. Kaggle account
1. Sign up at kaggle.com (free).
2. **Settings → Phone verification** – without it, notebooks cannot use the internet (we need it to install PySpark).
3. Open kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data once – that's the dataset for Lab D, Part 2.
   Part 1 downloads its data itself (needs Internet: On).

### 5. Run the environment check
| Windows | macOS / Linux |
|---|---|
| `py -3.12 session-04\check_env.py` | `python3.12 session-04/check_env.py` |

It's fine if it says *"NO – activate .venv first"* and packages are missing: that's what Lab A is about.

---

## 🛠️ Troubleshooting

| Symptom | OS | Fix |
|---|---|---|
| `python` opens the Microsoft Store | Windows | Use `py -3.12 ...`, or turn off *Settings → Apps → Advanced app settings → App execution aliases → python.exe* |
| `running scripts is disabled on this system` when activating `.venv` | Windows | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then activate again |
| `ensurepip is not available` / `No module named venv` | Ubuntu/Debian | `sudo apt install python3.12-venv` |
| `externally-managed-environment` on `pip install` | macOS (Homebrew), Linux | You are not in a venv – activate `.venv` first; never use `sudo pip` |
| Notebook says `ModuleNotFoundError` although you installed the package | all | The notebook kernel is not your `.venv`. Top right in the notebook → **Select Kernel** → `.venv` |
| `pip install` very slow / times out on campus Wi-Fi | all | Use uv (Lab A, step 4) – it downloads in parallel and caches |
| Kaggle: `pip install` or `Download failed` | Kaggle | Settings → Internet **On** (needs phone verification) |
| Kaggle: `assert ... Dataset missing` | Kaggle | Input → **+ Add Input** → "NYC Yellow Taxi Trip Data" (elemento) |
| Apple Silicon (M1–M4) | macOS | Nothing special – all packages have native wheels |
