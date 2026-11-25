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
  - claim_919b7ce7
  - claim_0fbef9f9
  - claim_774b3826
  - claim_b0a1193e
  - claim_9d914236
  - claim_0326b6f6
  - claim_4e2fb962
  - claim_ba1a8d00
  - claim_06905147
  - claim_827edb87
  - claim_2708c123
  - claim_3c7502a9
  - claim_a343b91b
  - claim_122d228d
confidence: 0.667
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_41b3a933
  - src_59b6ded4
  - src_6494d099
  - src_8615b91f
  - src_96e79681
  - src_b3356305
  - src_cecf99ea
---

# Windows

Type: platform. Mentioned in 20 claims across 5 topics.

## Claims

- **You never commit the environment itself – only the recipe (requirements.txt, lock file) to rebuild it.** Confidence 0.89 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, VS Code: Windows: code.visualstudio.com, macOS: code.visualstudio.com, Linux (Ubuntu/Debian): code.visualstudio.com.** Confidence 0.86 · [[course-setup|Course Setup]]
- **In the comparison table, Python 3.12: Windows: winget install Python.Python.3.12 or python.org installer (tick "Add python.exe to PATH" and "py launcher"), macOS: brew install python@3.12 or python.org installer, Linux (Ubuntu/Debian): sudo apt install python3.12 python3.12-venv.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **Run once: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned and activate again.** Confidence 0.79 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Windows: venv: yes, pyenv: only via the port pyenv-win, uv: yes.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Windows — Command: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \; value: iex".** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Windows — Install: pyenv-win: Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1".** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **Docker Desktop for Windows (uses the WSL 2 Windows backend) If asked, enable WSL 2: wsl --install.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **If Disabled: » Restart and enter BIOS (F2, F12, DEL, or ESC). » Enable Intel VT-x or AMD-V under CPU settings. » Step 3: Install WSL2 (for Windows Home users) » Open PowerShell (as Admin) and run:powershell KopierenBearbeiten » Restart your computer. » Step 4: Download Docker » Go to Docker Desktop for Windows. » Click "Download Docker Desktop for Windows". » Step 5: Install Docker » Open the downloaded .exe file. » Follow the installation steps and check: » Enable WSL2 Backend (if asked). » Enable Windows Containers (optional). » Click Install and restart your PC. » Step 6: Verify installation.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Symptom: python opens the Microsoft Store — OS: Windows; Fix: Use py -3.12 ..., or turn off Settings → Apps → Advanced app settings → App execution aliases → python.exe.** Confidence 0.67 · [[course-setup|Course Setup]]
- **Windows: py -3.12 get_data.py --months 2 — macOS / Linux: python3.12 get_data.py --months 2.** Confidence 0.67 · [[course-setup|Course Setup]]
- **» Step 1: Check System Requirements » Windows 10 (Pro, Enterprise, or Education) / Windows 11 » WSL2 (Windows Subsystem for Linux) Enabled » Virtualization Enabled in BIOS » Step 2: Enable Virtualization » Open Task Manager (Ctrl + Shift + Esc). » Go to Performance → CPU. » Check if Virtualization is Enabled.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **MacOS / Linux Windows Compiles Python from source: minutes, needs build tools.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Windows · PowerShell macOS · zsh Linux · bash.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.** Confidence 0.65 · [[spark-architecture|Spark Architecture]]
- **Install Docker Desktop (docker.com → Get Started; Windows needs WSL 2, the installer offers it) and start it.** Confidence 0.60 · [[tooling-docker|Docker and Dev Containers]]
- **On Windows, pyenv-win may need the full version number: check pyenv install --list first (e.g. pyenv install 3.12.10).** Confidence 0.60 · [[python-environments|Python Environments and Reproducibility]]
- **Windows: use the Docker route (README.md, route A) or run this script inside WSL.** Confidence 0.51 · [[tooling-docker|Docker and Dev Containers]]
- **Py --list # all Pythons the Windows launcher knows ; python --version ; python session-04\check_env.py.** Confidence 0.47 · [[course-setup|Course Setup]]
- **Git pull ; python get_data.py --months 2 # Windows: py -3.12 get_data.py --months 2.** Confidence 0.44 · [[course-setup|Course Setup]]

## Related Entities

- [[linux|Linux]] (7)
- [[python|Python 3.12]] (6)
- [[macos|macOS]] (6)
- [[docker|Docker]] (4)
- [[powershell|PowerShell]] (4)
- [[venv|venv]] (4)
- [[wsl|WSL]] (3)
- [[pyenv|pyenv]] (3)
- [[git|Git]] (2)
- [[spark_task|Spark task]] (2)
