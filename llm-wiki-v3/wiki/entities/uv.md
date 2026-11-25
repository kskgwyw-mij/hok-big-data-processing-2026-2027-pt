---
title: uv
type: entity
entity_id: ent_uv
entity_type: tool
claim_ids:
  - claim_1fc89e17
  - claim_10fe9fc5
  - claim_2785ec80
  - claim_3bfafe94
  - claim_f0092822
  - claim_30d231b5
  - claim_0b3e9120
  - claim_6c1111f0
  - claim_ea75a33c
  - claim_d1a72233
  - claim_c9af32ed
  - claim_80dcb37a
  - claim_76c23fc7
confidence: 0.719
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_6494d099
  - src_b3356305
---

# uv

Type: tool. Mentioned in 13 claims across 3 topics.
Aliases: uv.lock.

## Claims

- **In the comparison table, Windows: venv: yes, pyenv: only via the port pyenv-win, uv: yes.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **OS: macOS / Linux — Command: curl -LsSf https://astral.sh/uv/install.sh \; value: sh.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Windows — Command: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \; value: iex".** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Problem: Which Python version? — Example: Project A needs 3.12, project B still runs on 3.10; Tool: pyenv (or uv python).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Solves: venv: package isolation, pyenv: Python version management, uv: both.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Lock file: venv: no (pip freeze by hand), pyenv: no, uv: yes uv.lock.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Comes with Python: venv: yes (standard library), pyenv: no separate install, uv: no separate install (one binary).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Pyenv and venv do not compete: pyenv picks the interpreter, venv isolates the packages. uv is one tool that does both (and installs packages much faster).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Uv init --python 3.12 ; uv add pandas duckdb.** Confidence 0.72 · [[engines-single_machine|Single-Machine Engines]]
- **OS: macOS (Homebrew) — Command: brew install uv.** Confidence 0.67 · [[python-environments|Python Environments and Reproducibility]]
- **Lab: A — Topic: Python environments: venv, pyenv, uv; Where: laptop, terminal; File: 01_python_environments.md, check_env.py.** Confidence 0.67 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: pip install very slow / times out on campus Wi-Fi — OS: all; Fix: Use uv (Lab A, step 4) – it downloads in parallel and caches.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Uv python list # Python versions uv can see or install ; uv venv --python 3.12 .venv-uv # creates the env; downloads 3.12 if missing ; uv pip install --python .venv-uv -r requirements-local.txt.** Confidence 0.41 · [[python-environments|Python Environments and Reproducibility]]

## Related Entities

- [[venv|venv]] (9)
- [[pyenv|pyenv]] (7)
- [[macos|macOS]] (3)
- [[pip|pip]] (3)
- [[linux|Linux]] (2)
- [[python|Python 3.12]] (2)
- [[windows|Windows]] (2)
- [[pandas|pandas]] (2)
- [[duckdb|DuckDB]] (1)
- [[kafka|Kafka]] (1)
