---
title: Questions: Python Environments and Reproducibility
type: questions
topic: python.environments
question_count: 9
last_rendered: 2026-11-25T09:51:47Z
---

# Questions: Python Environments and Reproducibility

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Lab A – Python environments: venv, pyenv and uv / The modern shortcut: uv

- Compare: how long did pip install -r requirements-local.txt take in step 2, and how long does uv take?
  - `session-04/01_python_environments.md:141` · open_question

## Lab A – Python environments: venv, pyenv and uv / Exam-style questions

- A colleague says: "I use pyenv, so I don't need venv." Explain in two sentences why this is only half true.
  - `session-04/01_python_environments.md:176` · exam_prompt
- You activated .venv, ran pip install duckdb, and Jupyter still says ModuleNotFoundError: duckdb. What is the most likely cause, and how do you check it?
  - `session-04/01_python_environments.md:180` · exam_prompt
- Scenario: 25 students on Windows, macOS and Linux need the same Python 3.12 environment in 10 minutes, without admin rights. Choose between pyenv + venv and uv, and justify.
  - `session-04/01_python_environments.md:182` · exam_prompt
- Why is .venv/ in .gitignore, while requirements.txt is committed?
  - `session-04/01_python_environments.md:184` · exam_prompt

## Lab A – Python environments: venv, pyenv and uv / Create and activate a virtual environment with venv

- Windows: "running scripts is disabled on this system"?
  - `session-04/01_python_environments.md:81` · open_question

## Block 3 – Exam circuit / Station 5 – Environments, saving data, DuckDB, Spark ML

- 5.1 (3 P) requirements.txt, a lock file (pip freeze / uv.lock) and a dev container: what does each one pin, and why is the container the strongest guarantee for our Spark labs?
  - `session-06/03_exam_circuit.md:93` · exam_prompt

## Big Data Processing – Mock exam / Part C – Python environments, file formats, DuckDB

- C3 (2 P) "I use pyenv, so I don't need venv." Explain why this is only half true.
  - `04_mock_exam-gitdiff.md:198` · exam_prompt
- C4 (2 P) What is the difference between a requirements.txt with version ranges and a lock file?
  - `04_mock_exam-gitdiff.md:200` · exam_prompt
