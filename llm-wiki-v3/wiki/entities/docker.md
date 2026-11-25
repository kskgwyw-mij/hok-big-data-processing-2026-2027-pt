---
title: Docker
type: entity
entity_id: ent_docker
entity_type: tool
claim_ids:
  - claim_37399599
  - claim_4e2fb962
  - claim_5e68579a
  - claim_c9e8d488
  - claim_4eec96d9
  - claim_beb90ba1
  - claim_0efcddb6
  - claim_aa710da7
  - claim_69b22720
  - claim_bc86de96
  - claim_d3d12f30
  - claim_c8757b57
  - claim_a7a586bc
  - claim_709eda19
  - claim_06905147
  - claim_96e7b3fe
  - claim_9792e5ba
  - claim_326f6e1b
  - claim_719c08d9
confidence: 0.682
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_6e2e5684
  - src_799c8bd7
  - src_8e87808f
  - src_b289b34c
  - src_b3356305
  - src_cecf99ea
---

# Docker

Type: tool. Mentioned in 19 claims across 6 topics.
Aliases: Docker Desktop, docker compose, docker-compose.

## Claims

- **Docker compose only finds docker-compose.yml in session-06/ – run it from the repo root and you get no configuration file provided: not found.** Confidence 0.89 · [[tooling-docker|Docker and Dev Containers]]
- **Route A (Docker): docker exec -it broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a — Route B (native): kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group-a.** Confidence 0.87 · [[kafka-cluster|Kafka Cluster]]
- **Runs locally with your .venv kernel.** Confidence 0.80 · [[python-environments|Python Environments and Reproducibility]]
- **Symptom: Cannot connect to the Docker daemon / docker: command not found — Fix: Start Docker Desktop and wait until it says running; open a new terminal.** Confidence 0.74 · [[tooling-docker|Docker and Dev Containers]]
- **Route A: docker exec -it broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true — Route B: kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cli-demo --from-beginning --formatter-property print.key=true --formatter-property print.partition=true --formatter-property print.offset=true.** Confidence 0.74 · [[kafka-log|Kafka Log]]
- **In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh …, Route B – native Kafka (get_kafka.py): on your laptop: .sh ….** Confidence 0.73 · [[tooling-docker|Docker and Dev Containers]]
- **Disk space: the image download is ~240 MB (docker image rm apache/kafka:4.4.0 removes it); Route B uses ~140 MB in kafka_2.13-4.4.0/ + kafka-data/ – both are ignored by git.** Confidence 0.71 · [[tooling-docker|Docker and Dev Containers]]
- **Symptom: port is already allocated (9092 or 8080) — Fix: Another Kafka is running: docker ps, stop it – or stop your Route B broker.** Confidence 0.69 · [[kafka-cluster|Kafka Cluster]]
- **Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).** Confidence 0.69 · [[course-exam|Exam]]
- **In the comparison table, Route A: Stop: docker compose stop (start again: docker compose start), Delete all topics and messages: docker compose down – the next up -d starts empty.** Confidence 0.68 · [[tooling-docker|Docker and Dev Containers]]
- **Symptom: No working Java found / UnsupportedClassVersionError — Fix: Install Java 17+ (Route B), or use Docker.** Confidence 0.68 · [[tooling-docker|Docker and Dev Containers]]
- **The docker exec … commands below then work from any folder.** Confidence 0.67 · [[tooling-docker|Docker and Dev Containers]]
- **List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix).** Confidence 0.66 · [[kafka-consumers|Kafka Consumers and Consumer Groups]]
- **Optional web UI: docker compose --profile ui up -d → http://localhost:8080 (another ~220 MB download).** Confidence 0.63 · [[tooling-docker|Docker and Dev Containers]]
- **Local Docker: Docker Desktop + VS Code extension Dev Containers → "Reopen in Container".** Confidence 0.63 · [[tooling-docker|Docker and Dev Containers]]
- **Cd session-06 ; docker compose up -d ; docker compose ps # broker → running.** Confidence 0.62 · [[tooling-docker|Docker and Dev Containers]]
- **For macOS, Linux, WSL or the Codespace (it has Java 17 but no Docker).** Confidence 0.62 · [[tooling-docker|Docker and Dev Containers]]
- **Install Docker Desktop (docker.com → Get Started; Windows needs WSL 2, the installer offers it) and start it.** Confidence 0.60 · [[tooling-docker|Docker and Dev Containers]]
- **Windows: use the Docker route (README.md, route A) or run this script inside WSL.** Confidence 0.51 · [[tooling-docker|Docker and Dev Containers]]

## Related Entities

- [[kafka|Kafka]] (8)
- [[broker|broker]] (7)
- [[wsl|WSL]] (4)
- [[docker_compose|docker compose]] (3)
- [[topic|topic]] (3)
- [[linux|Linux]] (2)
- [[code|VS Code]] (2)
- [[windows|Windows]] (2)
- [[kafka_consumer_groups_sh|kafka-consumer-groups.sh]] (2)
- [[kafka_topics_sh|kafka-topics.sh]] (2)
