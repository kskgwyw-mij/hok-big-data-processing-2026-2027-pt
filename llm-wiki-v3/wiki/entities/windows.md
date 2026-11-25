---
title: Windows
type: entity
entity_id: ent_windows
entity_type: platform
claim_ids:
  - claim_2785ec80
  - claim_505495af
  - claim_670ad715
  - claim_d1a72233
  - claim_09f8595a
  - claim_f0885e5f
  - claim_0fbef9f9
  - claim_774b3826
  - claim_b0a1193e
  - claim_9d914236
  - claim_0326b6f6
  - claim_4e2fb962
  - claim_ba1a8d00
  - claim_06905147
confidence: 0.668
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_41b3a933
  - src_6494d099
  - src_96e79681
  - src_b3356305
  - src_cecf99ea
---

# Windows

Type: platform. Mentioned in 14 claims across 4 topics.

## Claims

- **In the comparison table, VS Code: Windows: code.visualstudio.com, macOS: code.visualstudio.com, Linux (Ubuntu/Debian): code.visualstudio.com.** Confidence 0.86 · [[course-setup|Course Setup]]
- **In the comparison table, Python 3.12: Windows: winget install Python.Python.3.12 or python.org installer (tick "Add python.exe to PATH" and "py launcher"), macOS: brew install python@3.12 or python.org installer, Linux (Ubuntu/Debian): sudo apt install python3.12 python3.12-venv.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **Run once: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned and activate again.** Confidence 0.79 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Windows: venv: yes, pyenv: only via the port pyenv-win, uv: yes.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Windows — Command: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \; value: iex".** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Windows — Install: pyenv-win: Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1".** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: python opens the Microsoft Store — OS: Windows; Fix: Use py -3.12 ..., or turn off Settings → Apps → Advanced app settings → App execution aliases → python.exe.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Windows: py -3.12 get_data.py --months 2 — macOS / Linux: python3.12 get_data.py --months 2.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.** Confidence 0.65 · [[spark-architecture|Spark Architecture]]
- **Install Docker Desktop (docker.com → Get Started; Windows needs WSL 2, the installer offers it) and start it.** Confidence 0.60 · [[tooling-docker|Docker and Dev Containers]]
- **On Windows, pyenv-win may need the full version number: check pyenv install --list first (e.g. pyenv install 3.12.10).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Windows: use the Docker route (README.md, route A) or run this script inside WSL.** Confidence 0.51 · [[tooling-docker|Docker and Dev Containers]]
- **Py --list # all Pythons the Windows launcher knows ; python --version ; python session-04\check_env.py.** Confidence 0.47 · [[course-setup|Course Setup]]
- **Git pull ; python get_data.py --months 2 # Windows: py -3.12 get_data.py --months 2.** Confidence 0.44 · [[course-setup|Course Setup]]

## Related Entities

- [[python|Python 3.12]] (5)
- [[linux|Linux]] (4)
- [[macos|macOS]] (4)
- [[pyenv|pyenv]] (3)
- [[venv|venv]] (3)
- [[docker|Docker]] (2)
- [[git|Git]] (2)
- [[powershell|PowerShell]] (2)
- [[wsl|WSL]] (2)
- [[uv|uv]] (2)
