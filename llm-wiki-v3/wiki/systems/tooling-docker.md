---
title: Docker and Dev Containers
type: systems
topic: tooling.docker
entity_ids:
  - ent_docker
  - ent_route
  - ent_wsl
  - ent_docker_compose
  - ent_kafka
  - ent_broker
  - ent_docker_desktop
  - ent_linux
  - ent_macos
  - ent_windows
  - ent_code
  - ent_dev_container
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
confidence: 0.668
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
review_required: false
---

# Docker and Dev Containers

Rendered from 13 claims and 4 sources. Median confidence 0.67; 11 active, 0 disputed, 0 superseded.

## Current Understanding

### Choose route

**In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….**
Confidence 0.73 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:19` — “Where the CLI tools run | inside the container: docker exec -it broker /opt/kafka/bin/ .sh … | on your laptop: .sh …”

**The docker exec … commands below then work from any folder.**
Confidence 0.67 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:30` — “The docker exec … commands below then work from any folder. Docker Desktop may print a What's next: Try Docker Debug … hint after each command – ignore it (or switch it off with export…”

**Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.**
Confidence 0.62 · active · 3 sources
Evidence: `README.md:112` — “A – Docker | Docker Desktop | cd session-06 → docker compose up -d (broker image apache/kafka:4.4.0, ~240 MB; optional web UI: docker compose --profile ui up -d)”

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

**Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.**
Confidence 0.71 · active · 1 source
Evidence: `session-06/README.md:97` — “Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.”

**In the comparison table, Route A: Stop: docker compose stop (start again: docker compose start), Delete all topics and messages: docker compose down – the next up -d starts empty.**
Confidence 0.68 · active · 1 source
Evidence: `session-06/README.md:94` — “Route A | docker compose stop (start again: docker compose start) | docker compose down – the next up -d starts empty”

### Alternative dev container github codespaces

**Local Docker: Docker Desktop + VS Code extension Dev Containers → "Reopen in Container".**
Confidence 0.63 · active · 1 source
Evidence: `README.md:95` — “- Local Docker: Docker Desktop + VS Code extension Dev Containers → "Reopen in Container".”

### Get kafka

**Windows: use the Docker route (README.md, route A) or run this script inside WSL.**
Confidence 0.51 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “Only uses the Python standard library, like get_data.py. Works on macOS and Linux (and in the Codespace). Windows: use the Docker route (README.md, route A) or run this script inside WSL.…”

### Kafka lab

**Docker compose only finds docker-compose.yml in session-06/ – run it from the repo root and you get no configuration file provided: not found.**
Confidence 0.89 · active · 2 sources
Evidence: `session-06/README.md:107` — “no configuration file provided: not found | You are in the repo root → cd session-06, then docker compose up -d again. All docker compose commands (also stop/down) must run in session-06/”

### Route native kafka docker

**For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker).**
Confidence 0.62 · active · 1 source
Evidence: `session-06/README.md:60` — “For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker). Needs Java 17 or newer (java -version; macOS: brew install openjdk@17, Ubuntu: sudo apt install…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/get_kafka.py` | code | 0.80 | 1 | 2026-11-11 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 3 | 2026-11-11 |
| `README.md` | readme | 0.85 | 3 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 9 | 2026-11-11 |

## Related Pages

- [[python-environments|Python Environments and Reproducibility]] (32 shared entities)
- [[kafka-cluster|Kafka Cluster]] (23 shared entities)
- [[kafka-log|Kafka Log]] (20 shared entities)
- [[course-exam|Exam]] (19 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (19 shared entities)
- [[course-setup|Course Setup]] (13 shared entities)

## Open Questions

_No open questions recorded for this topic._

## Timeline

- 2026-11-25: support_update on `claim_69b22720` (0.68 → 0.89)
- 2026-11-25: new_claim on `claim_709eda19`
- 2026-11-25: new_claim on `claim_06905147`
- 2026-11-25: support_update on `claim_0efcddb6` (0.67 → 0.62)
- 2026-11-25: new_claim on `claim_96e7b3fe`
- 2026-11-25: new_claim on `claim_9792e5ba`
- 2026-11-25: new_claim on `claim_326f6e1b`
- 2026-11-25: new_claim on `claim_719c08d9`
