---
title: Docker and Dev Containers
type: systems
topic: tooling.docker
entity_ids:
  - ent_docker
  - ent_kafka
  - ent_route
  - ent_docker_compose
  - ent_wsl
  - ent_windows
  - ent_docker_desktop
  - ent_linux
  - ent_macos
  - ent_yaml
  - ent_broker
  - ent_powershell
claim_ids:
  - claim_4e2fb962
  - claim_beb90ba1
  - claim_0efcddb6
  - claim_aa710da7
  - claim_69b22720
  - claim_d3d12f30
  - claim_c8757b57
  - claim_709eda19
  - claim_06905147
  - claim_96e7b3fe
  - claim_9792e5ba
  - claim_326f6e1b
  - claim_719c08d9
  - claim_c68289ac
  - claim_d8c59259
  - claim_f7abd5ff
  - claim_69ffcc24
  - claim_bf3a39fb
  - claim_2873c09a
  - claim_2708c123
  - claim_a7a0d03b
  - claim_bdc608a0
  - claim_122d228d
  - claim_255ff7fa
  - claim_39b9fc3d
  - claim_04a71cb7
  - claim_77b4f69e
  - claim_8335c571
confidence: 0.703
status: disputed
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_41b3a933
  - src_8615b91f
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
  - src_fc0bfe80
review_required: true
---

# Docker and Dev Containers

Rendered from 28 claims and 6 sources. Median confidence 0.70; 24 active, 1 disputed, 0 superseded.

## Current Understanding

### Choose route

**Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.**
Confidence 0.80 · active · 4 sources
Evidence: `README.md:112` — “A – Docker | Docker Desktop | cd session-06 → docker compose up -d (broker image apache/kafka:4.4.0, ~240 MB; optional web UI: docker compose --profile ui up -d)”

**The docker exec … commands below then work from any folder.**
Confidence 0.67 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:30` — “The docker exec … commands below then work from any folder. Docker Desktop may print a What's next: Try Docker Debug … hint after each command – ignore it (or switch it off with export…”

**In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….**
Confidence 0.59 · disputed · 2 sources · needs review
Evidence: `session-06/01_kafka_cli.md:19` — “Where the CLI tools run | inside the container: docker exec -it broker /opt/kafka/bin/ .sh … | on your laptop: .sh …”

### Kafka lab exam preparation

**Symptom: Cannot connect to the Docker daemon / docker: command not found — Fix: Start Docker Desktop and wait until it says running; open a new terminal.**
Confidence 0.74 · active · 1 source
Evidence: `session-06/README.md:106` — “Cannot connect to the Docker daemon / docker: command not found | Start Docker Desktop and wait until it says running; open a new terminal”

**Symptom: No working Java found / UnsupportedClassVersionError — Fix: Install Java 17+ (Route B), or use Docker.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:113` — “No working Java found / UnsupportedClassVersionError | Install Java 17+ (Route B), or use Docker”

### Start kafka broker route docker

**Optional web UI: docker compose --profile ui up -d → http://localhost:8080 (another ~220 MB download).**
Confidence 0.63 · active · 1 source
Evidence: `session-06/README.md:57` — “4. Optional web UI: docker compose --profile ui up -d → http://localhost:8080 (another ~220 MB download).”

**Install Docker Desktop (docker.com → Get Started; Windows needs WSL 2, the installer offers it) and start it.**
Confidence 0.60 · candidate · 1 source
Evidence: `session-06/README.md:46` — “1. Install Docker Desktop (docker.com → Get Started; Windows needs WSL 2, the installer offers it) and start it.”

### Stop clean

**In the comparison table, Route A: Stop: docker compose stop (start again: docker compose start), Delete all topics and messages: docker compose down – the next up -d starts empty.**
Confidence 0.87 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p96:9` — “Kafka UI (Route A only) docker compose stop docker compose down Route A – Docker start again: docker compose with UI: docker compose --profile start ui down $ docker compose --profile ui…”

**Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.**
Confidence 0.71 · active · 1 source
Evidence: `session-06/README.md:97` — “Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.”

### Alternative dev container github codespaces

**Local Docker: Docker Desktop + VS Code extension Dev Containers → "Reopen in Container".**
Confidence 0.63 · active · 1 source
Evidence: `README.md:95` — “- Local Docker: Docker Desktop + VS Code extension Dev Containers → "Reopen in Container".”

### Docker cannot connect

**Cannot connect to the Docker daemon → start Docker Desktop Pair up and type on your neighbour's laptop.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p89:17` — “Broker not running or not on 9092 ✗ If it fails no configuration file provided: not found → repo root: cd session-06, then up -d again Nothing works? Cannot connect to the Docker daemon →…”

### Docker cli tool docker compose

**CLI Tool: docker-compose used for local dev/test automation with YAML.**
Confidence 0.70 · active · 1 source · when: for local dev/test automation with YAML
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p61:12` — “» b. CLI Tool: docker-compose used for local dev/test automation with YAML”

### Docker compose yaml

**» Compose YAML format has it's own versions: » 1, 2, 2.1, 3, 3.1 » YAML fie can be used with docker-compose command for local docker automation or » With docker directly in production with Swarm (as of V1.13) » docker-compose - -help » docker-compose.yml is default file name but » Any can be used with docker-compose -f.**
Confidence 0.65 · active · 1 source · when: for local docker automation or » With docker directly in production with Swarm
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p72:3` — “» Compose YAML format has it's own versions: » 1, 2, 2.1, 3, 3.1 » YAML fie can be used with docker-compose command for local docker automation or » With docker directly in production with…”

### Docker configure relationships containers

**» Configure relationships between containers » Save our docker container run settings in easy-to-read file » Create one-liner developer environment setups.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p61:3` — “» Configure relationships between containers » Save our docker container run settings in easy-to-read file » Create one-liner developer environment setups”

### Docker desktop windows

**Docker Desktop for Windows (uses the WSL 2 Windows backend) If asked, enable WSL 2: wsl --install.**
Confidence 0.70 · active · 1 source · when: for Windows (uses the WSL 2 Windows backend) If asked
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p87:6` — “Docker Desktop for Windows (uses the WSL 2 Windows backend) If asked, enable WSL 2: wsl --install”

### Docker disabled restart enter

**If Disabled: » Restart and enter BIOS (F2, F12, DEL, or ESC). » Enable Intel VT-x or AMD-V under CPU settings. » Step 3: Install WSL2 (for Windows Home users) » Open PowerShell (as Admin) and run:powershell KopierenBearbeiten » Restart your computer. » Step 4: Download Docker » Go to Docker Desktop for Windows. » Click "Download Docker Desktop for Windows". » Step 5: Install Docker » Open the downloaded .exe file. » Follow the installation steps and check: » Enable WSL2 Backend (if asked). » Enable Windows Containers (optional). » Click Install and restart your PC. » Step 6: Verify installation.**
Confidence 0.70 · active · 1 source · when: If Disabled: » Restart and enter BIOS (F2; if asked)
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p78:3` — “» Step 1: Check System Requirements » Windows 10 (Pro, Enterprise, or Education) / Windows 11 » WSL2 (Windows Subsystem for Linux) Enabled » Virtualization Enabled in BIOS » Step 2: Enable…”

### Docker engine

**Docker Engine + Docker Compose plugin (or Add your user to the docker group or Linux Docker Desktop for Linux) use sudo.**
Confidence 0.70 · active · 1 source · when: for Linux ) use sudo
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p87:18` — “Docker Engine + Docker Compose plugin (or Add your user to the docker group or Linux Docker Desktop for Linux) use sudo”

### Docker remove image later

**Remove the image later: docker image rm apache/kafka:4.4.0 · Source: session-06/README.md.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p96:30` — “Remove the image later: docker image rm apache/kafka:4.4.0 · Source: session-06/README.md”

### Docker route a add

**Route A: add the docker exec prefix to every command. · Source: 01_kafka_cli.md.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p91:33` — “Your TopicId differs. Route A: add the docker exec prefix to every command. · Source: 01_kafka_cli.md”

### Docker run compose

**Run all docker compose commands inside session-06/.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p96:25` — “Run all docker compose commands inside session-06/”

### Docker silence env docker cli hints

**Silence Docker $env:DOCKER_CLI_HINTS="false" export DOCKER_CLI_HINTS=false export DOCKER_CLI_HINTS=false hints.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p90:24` — “Silence Docker $env:DOCKER_CLI_HINTS="false" export DOCKER_CLI_HINTS=false export DOCKER_CLI_HINTS=false hints”

### Docker step check system

**» Step 1: Check System Requirements » macOS Monterey 12+ (Intel or Apple Silicon) » Minimum 4GB RAM » Enable virtualization (default on Mac) » Step 2: Download Docker » Go to Docker Desktop for Mac. » Click "Download Docker Desktop for Mac". » Choose Apple Chip (for M1/M2/M3) or Intel Chip. » Step 3: Install Docker » Open the downloaded .dmg file. » Drag Docker.app to the Applications folder. » Open Docker from Launchpad or Applications folder. » Step 4: Allow Permissions » When prompted, grant permissions for Docker to run. » Allow Docker privileged access to manage containers. » Step 5: Verify Installation.**
Confidence 0.74 · active · 1 source · when: When prompted; for Docker to run
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p77:3` — “» Step 1: Check System Requirements » macOS Monterey 12+ (Intel or Apple Silicon) » Minimum 4GB RAM » Enable virtualization (default on Mac) » Step 2: Download Docker » Go to Docker…”

### Docker version

**$ docker --version $ docker pull apache/kafka:4.4.0 $ docker compose version.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p87:25` — “$ docker --version $ docker pull apache/kafka:4.4.0 $ docker compose version”

### Docker yaml stands

**» YAML stands for "YAML Ain't Markup Language" » a human-friendly, data serialization standard for all programming languages. » Simpler and more readable than XML or JSON » Used in applications like Docker, Kubernetes, and CI/CD pipelines.**
Confidence 0.70 · active · 1 source · when: for all programming languages
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p62:3` — “» YAML stands for "YAML Ain't Markup Language" » a human-friendly, data serialization standard for all programming languages. » Simpler and more readable than XML or JSON » Used in…”

### Get kafka

**Windows: use the Docker route (README.md, route A) or run this script inside WSL.**
Confidence 0.51 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “Only uses the Python standard library, like get_data.py. Works on macOS and Linux (and in the Codespace). Windows: use the Docker route (README.md, route A) or run this script inside WSL.…”

### Kafka lab

**Docker compose only finds docker-compose.yml in session-06/ – run it from the repo root and you get no configuration file provided: not found.**
Confidence 0.96 · active · 3 sources
Evidence: `session-06/README.md:107` — “no configuration file provided: not found | You are in the repo root → cd session-06, then docker compose up -d again. All docker compose commands (also stop/down) must run in session-06/”

### Route native kafka docker

**For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker).**
Confidence 0.29 · stale · 2 sources · needs review
Evidence: `session-06/README.md:60` — “For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker). Needs Java 17 or newer (java -version; macOS: brew install openjdk@17, Ubuntu: sudo apt install…”

### Yaml file describes solution

**YAML file: that describes our solution options for: » Containers » Networks » Volumes.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p61:7` — “» a. YAML file: that describes our solution options for: » Containers » Networks » Volumes”

## Contested

These claims received observations that pull in the opposite direction. They are not settled.

- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.59, status disputed.
  - against: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p88:1` — “Route B - Native Kafka without Docker”
- **For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker).** Confidence 0.29, status stale.
  - against: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p85:15` — “Route A – recommended Route B – Native Kafka Pair up Docker needs Java 17+ · ~130 MB type on a neighbour's laptop image apache/kafka:4.4.0 · ~240 MB…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/get_kafka.py` | code | 0.80 | 1 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 19 | 2026-11-25 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 3 | 2026-11-11 |
| `README.md` | readme | 0.85 | 3 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 9 | 2026-11-11 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |

## Related Pages

- [[python-environments|Python Environments and Reproducibility]] (59 shared entities)
- [[kafka-log|Kafka Log]] (48 shared entities)
- [[kafka-cluster|Kafka Cluster]] (46 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (42 shared entities)
- [[course-setup|Course Setup]] (28 shared entities)
- [[unfiled|Unfiled Observations]] (27 shared entities)

## Open Questions

2 prompts from the material are collected in [[questions/tooling-docker|Questions: Docker and Dev Containers]].
- Can you install Docker Desktop / Docker Engine?
- » Step 5 · Route A or B » Step 4A · Route A (Docker) # .venv active + broker running $ cd session-06 # docker-compose.yml lives here $…

## Timeline

- 2026-11-25: new_claim on `claim_255ff7fa`
- 2026-11-25: new_claim on `claim_39b9fc3d`
- 2026-11-25: new_claim on `claim_04a71cb7`
- 2026-11-25: new_claim on `claim_77b4f69e`
- 2026-11-25: new_claim on `claim_8335c571`
- 2026-11-25: support_update on `claim_326f6e1b` (0.68 → 0.87)
- 2026-11-25: support_update on `claim_69b22720` (0.89 → 0.96)
- 2026-11-25: support_update on `claim_0efcddb6` (0.62 → 0.80)
