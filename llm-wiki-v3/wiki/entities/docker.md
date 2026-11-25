---
title: Docker
type: entity
entity_id: ent_docker
entity_type: tool
claim_ids:
  - claim_37399599
  - claim_4e2fb962
  - claim_2aedc4a6
  - claim_5e68579a
  - claim_c9e8d488
  - claim_4eec96d9
  - claim_beb90ba1
  - claim_0efcddb6
  - claim_aa710da7
  - claim_69b22720
  - claim_c8c19737
  - claim_d3d12f30
  - claim_c8757b57
  - claim_a7a586bc
  - claim_709eda19
  - claim_06905147
  - claim_96e7b3fe
  - claim_9792e5ba
  - claim_326f6e1b
  - claim_719c08d9
  - claim_c831872a
  - claim_c68289ac
  - claim_d8c59259
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
  - claim_bca5c57a
  - claim_80290f63
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_41b3a933
  - src_59b6ded4
  - src_6002d48d
  - src_6e2e5684
  - src_799c8bd7
  - src_8615b91f
  - src_8e87808f
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
  - src_fc0bfe80
---

# Docker

Type: tool. Mentioned in 37 claims across 5 topics.
Aliases: Docker Desktop, docker compose, docker-compose.

## Claims

- **Docker compose only finds docker-compose.yml in session-06/ – run it from the repo root and you get no configuration file provided: not found.** Confidence 0.96 · [[tooling-docker|Docker and Dev Containers]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.89 · [[kafka-log|Kafka Log]]
- **In the comparison table, Route A: Stop: docker compose stop (start again: docker compose start), Delete all topics and messages: docker compose down – the next up -d starts empty.** Confidence 0.87 · [[tooling-docker|Docker and Dev Containers]]
- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.** Confidence 0.84 · [[kafka-cluster|Kafka Cluster]]
- **Broker KAFKA_AUTO_CREATE_TOPICS_ENABLE is false" # you create topics yourself.** Confidence 0.83 · [[kafka-cluster|Kafka Cluster]]
- **Runs locally with your .venv kernel.** Confidence 0.80 · [[python-environments|Python Environments and Reproducibility]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.80 · [[tooling-docker|Docker and Dev Containers]]
- **Cannot connect to the Docker daemon → start Docker Desktop Pair up and type on your neighbour's laptop.** Confidence 0.77 · [[tooling-docker|Docker and Dev Containers]]
- **Symptom: Cannot connect to the Docker daemon / docker: command not found — Fix: Start Docker Desktop and wait until it says running; open a new terminal.** Confidence 0.74 · [[tooling-docker|Docker and Dev Containers]]
- **» Step 1: Check System Requirements » macOS Monterey 12+ (Intel or Apple Silicon) » Minimum 4GB RAM » Enable virtualization (default on Mac) » Step 2: Download Docker » Go to Docker Desktop for Mac. » Click "Download Docker Desktop for Mac". » Choose Apple Chip (for M1/M2/M3) or Intel Chip. » Step 3: Install Docker » Open the downloaded .dmg file. » Drag Docker.app to the Applications folder. » Open Docker from Launchpad or Applications folder. » Step 4: Allow Permissions » When prompted, grant permissions for Docker to run. » Allow Docker privileged access to manage containers. » Step 5: Verify Installation.** Confidence 0.74 · [[tooling-docker|Docker and Dev Containers]]
- **Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.** Confidence 0.71 · [[tooling-docker|Docker and Dev Containers]]
- **» Create new topic „Kafka-arch" docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --create --topic kafka-arch --partitions 1 --replication-factor 1 » Inspect Kafka's on-disk topic folder » Linux path: var/lib/kafka/data » Mac path: /tmp/kafka-logs » List kafka-logs docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs | head -120' docker exec -it broker bash -lc 'ls -lah /tmp/kafka-logs/kafka-arch-0'.** Confidence 0.70 · [[kafka-log|Kafka Log]]
- **» Delete topic docker exec -it broker /opt/kafka/bin/kafka-topics.sh \ --bootstrap-server localhost:9092 \ --delete --topic my-first-topic.** Confidence 0.70 · [[kafka-cluster|Kafka Cluster]]
- **Route A: add the docker exec prefix to every command. · Source: 01_kafka_cli.md.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Docker Desktop for Windows (uses the WSL 2 Windows backend) If asked, enable WSL 2: wsl --install.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **If Disabled: » Restart and enter BIOS (F2, F12, DEL, or ESC). » Enable Intel VT-x or AMD-V under CPU settings. » Step 3: Install WSL2 (for Windows Home users) » Open PowerShell (as Admin) and run:powershell KopierenBearbeiten » Restart your computer. » Step 4: Download Docker » Go to Docker Desktop for Windows. » Click "Download Docker Desktop for Windows". » Step 5: Install Docker » Open the downloaded .exe file. » Follow the installation steps and check: » Enable WSL2 Backend (if asked). » Enable Windows Containers (optional). » Click Install and restart your PC. » Step 6: Verify installation.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Silence Docker $env:DOCKER_CLI_HINTS="false" export DOCKER_CLI_HINTS=false export DOCKER_CLI_HINTS=false hints.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **» YAML stands for "YAML Ain't Markup Language" » a human-friendly, data serialization standard for all programming languages. » Simpler and more readable than XML or JSON » Used in applications like Docker, Kubernetes, and CI/CD pipelines.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Run all docker compose commands inside session-06/.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Remove the image later: docker image rm apache/kafka:4.4.0 · Source: session-06/README.md.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Docker Engine + Docker Compose plugin (or Add your user to the docker group or Linux Docker Desktop for Linux) use sudo.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **CLI Tool: docker-compose used for local dev/test automation with YAML.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **LEVEL 3 LEVEL 1 LEVEL 2 Container requirements.txt Lock file Dev container / Docker: OS, Python The packages you use directly, with pip freeze or uv.lock: every package, and Java pinned too – our version ranges. exact versions.** Confidence 0.70 · [[python-environments|Python Environments and Reproducibility]]
- **» Configure relationships between containers » Save our docker container run settings in easy-to-read file » Create one-liner developer environment setups.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Symptom: No working Java found / UnsupportedClassVersionError — Fix: Install Java 17+ (Route B), or use Docker.** Confidence 0.68 · [[tooling-docker|Docker and Dev Containers]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.67 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **The docker exec … commands below then work from any folder.** Confidence 0.67 · [[tooling-docker|Docker and Dev Containers]]
- **List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix).** Confidence 0.66 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **$ docker --version $ docker pull apache/kafka:4.4.0 $ docker compose version.** Confidence 0.65 · [[tooling-docker|Docker and Dev Containers]]
- **» Compose YAML format has it's own versions: » 1, 2, 2.1, 3, 3.1 » YAML fie can be used with docker-compose command for local docker automation or » With docker directly in production with Swarm (as of V1.13) » docker-compose - -help » docker-compose.yml is default file name but » Any can be used with docker-compose -f.** Confidence 0.65 · [[tooling-docker|Docker and Dev Containers]]
- **Optional web UI: docker compose --profile ui up -d → http://localhost:8080 (another ~220 MB download).** Confidence 0.63 · [[tooling-docker|Docker and Dev Containers]]
- **Local Docker: Docker Desktop + VS Code extension Dev Containers → "Reopen in Container".** Confidence 0.63 · [[tooling-docker|Docker and Dev Containers]]
- **Install Docker Desktop (docker.com → Get Started; Windows needs WSL 2, the installer offers it) and start it.** Confidence 0.60 · [[tooling-docker|Docker and Dev Containers]]
- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.59 · [[tooling-docker|Docker and Dev Containers]]
- **Windows: use the Docker route (README.md, route A) or run this script inside WSL.** Confidence 0.51 · [[tooling-docker|Docker and Dev Containers]]
- **For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker).** Confidence 0.29 · [[tooling-docker|Docker and Dev Containers]]

## Related Entities

- [[kafka|Kafka]] (16)
- [[broker|broker]] (10)
- [[topic|topic]] (7)
- [[wsl|WSL]] (5)
- [[kafka_topics_sh|kafka-topics.sh]] (5)
- [[linux|Linux]] (4)
- [[windows|Windows]] (4)
- [[docker_compose|docker compose]] (4)
- [[macos|macOS]] (3)
- [[partition|partition]] (3)
