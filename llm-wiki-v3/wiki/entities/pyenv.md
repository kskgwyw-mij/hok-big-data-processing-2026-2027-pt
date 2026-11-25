---
title: pyenv
type: entity
entity_id: ent_pyenv
entity_type: tool
claim_ids:
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
  - claim_76c23fc7
  - claim_6fb4e772
confidence: 0.719
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_6494d099
  - src_b3356305
---

# pyenv

Type: tool. Mentioned in 13 claims across 2 topics.

## Claims

- **In the comparison table, Windows: venv: yes, pyenv: only via the port pyenv-win, uv: yes.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).** Confidence 0.72 · [[data-formats|File Formats]]
- **OS: Linux — Install: curl -fsSL https://pyenv.run \; value: bash (needs build dependencies, see pyenv wiki).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Problem: Which Python version? — Example: Project A needs 3.12, project B still runs on 3.10; Tool: pyenv (or uv python).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Windows — Install: pyenv-win: Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1".** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Solves: venv: package isolation, pyenv: Python version management, uv: both.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Lock file: venv: no (pip freeze by hand), pyenv: no, uv: yes uv.lock.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **OS: macOS — Install: brew install pyenv + add the shell lines from pyenv init to ~/.zshrc.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Comes with Python: venv: yes (standard library), pyenv: no separate install, uv: no separate install (one binary).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Pyenv and venv do not compete: pyenv picks the interpreter, venv isolates the packages. uv is one tool that does both (and installs packages much faster).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Lab: A — Topic: Python environments: venv, pyenv, uv; Where: laptop, terminal; File: 01_python_environments.md, check_env.py.** Confidence 0.67 · [[python-environments|Python Environments and Reproducibility]]
- **Pyenv installs Python versions and switches between them per folder (.python-version file).** Confidence 0.65 · [[python-environments|Python Environments and Reproducibility]]
- **On Windows, pyenv-win may need the full version number: check pyenv install --list first (e.g. pyenv install 3.12.10).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[venv|venv]] (8)
- [[uv|uv]] (7)
- [[linux|Linux]] (3)
- [[windows|Windows]] (3)
- [[macos|macOS]] (3)
- [[topic|topic]] (2)
- [[duckdb|DuckDB]] (1)
- [[kaggle|Kaggle]] (1)
- [[parquet|Parquet]] (1)
- [[pickle|Pickle]] (1)
