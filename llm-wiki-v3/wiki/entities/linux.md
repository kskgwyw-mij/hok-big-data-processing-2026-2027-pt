---
title: Linux
type: entity
entity_id: ent_linux
entity_type: platform
claim_ids:
  - claim_1fc89e17
  - claim_967d35a4
  - claim_16cf3adc
  - claim_6c1111f0
  - claim_0fbef9f9
  - claim_774b3826
  - claim_b0a1193e
  - claim_60550010
  - claim_0326b6f6
  - claim_3eb495fc
  - claim_beb90ba1
  - claim_9792e5ba
  - claim_827edb87
  - claim_3c7502a9
  - claim_a343b91b
  - claim_a7a0d03b
  - claim_2578d2b6
  - claim_80290f63
confidence: 0.696
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1a3d69f8
  - src_41b3a933
  - src_59b6ded4
  - src_6494d099
  - src_8615b91f
  - src_96e79681
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
  - src_fc0bfe80
---

# Linux

Type: platform. Mentioned in 18 claims across 6 topics.

## Claims

- **In the comparison table, VS Code: Windows: code.visualstudio.com, macOS: code.visualstudio.com, Linux (Ubuntu/Debian): code.visualstudio.com.** Confidence 0.86 · [[course-setup|Course Setup]]
- **In the comparison table, Python 3.12: Windows: winget install Python.Python.3.12 or python.org installer (tick "Add python.exe to PATH" and "py launcher"), macOS: brew install python@3.12 or python.org installer, Linux (Ubuntu/Debian): sudo apt install python3.12 python3.12-venv.** Confidence 0.81 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: externally-managed-environment on pip install — OS: macOS (Homebrew), Linux; Fix: You are not in a venv – activate .venv first; never use sudo pip.** Confidence 0.78 · [[python-environments|Python Environments and Reproducibility]]
- **OS: Linux — Install: curl -fsSL https://pyenv.run \; value: bash (needs build dependencies, see pyenv wiki).** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **OS: macOS / Linux — Command: curl -LsSf https://astral.sh/uv/install.sh \; value: sh.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **In the comparison table, Solves: venv: package isolation, pyenv: Python version management, uv: both.** Confidence 0.72 · [[python-environments|Python Environments and Reproducibility]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **No Java 17? » For macOS, Linux, WSL, Codespace – needs Java 17+ mac: brew install openjdk@17.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **Docker Engine + Docker Compose plugin (or Add your user to the docker group or Linux Docker Desktop for Linux) use sudo.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Works on macOS and Linux (and in the Codespace).** Confidence 0.69 · [[python-environments|Python Environments and Reproducibility]]
- **Windows: py -3.12 get_data.py --months 2 — macOS / Linux: python3.12 get_data.py --months 2.** Confidence 0.67 · [[course-setup|Course Setup]]
- **» Step 1: Check System Requirements » Windows 10 (Pro, Enterprise, or Education) / Windows 11 » WSL2 (Windows Subsystem for Linux) Enabled » Virtualization Enabled in BIOS » Step 2: Enable Virtualization » Open Task Manager (Ctrl + Shift + Esc). » Go to Performance → CPU. » Check if Virtualization is Enabled.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **MacOS / Linux Windows Compiles Python from source: minutes, needs build tools.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Windows · PowerShell macOS · zsh Linux · bash.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Pyenv installs Python versions and switches between them per folder (.python-version file).** Confidence 0.65 · [[python-environments|Python Environments and Reproducibility]]
- **Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.** Confidence 0.65 · [[spark-architecture|Spark Architecture]]
- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.59 · [[tooling-docker|Docker and Dev Containers]]
- **For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker).** Confidence 0.29 · [[tooling-docker|Docker and Dev Containers]]

## Related Entities

- [[macos|macOS]] (14)
- [[windows|Windows]] (7)
- [[docker|Docker]] (4)
- [[kafka|Kafka]] (4)
- [[wsl|WSL]] (4)
- [[venv|venv]] (4)
- [[dev_container|Dev container]] (3)
- [[powershell|PowerShell]] (3)
- [[python|Python 3.12]] (3)
- [[pyenv|pyenv]] (3)
