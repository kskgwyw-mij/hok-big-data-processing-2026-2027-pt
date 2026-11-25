---
title: Knowledge Index
type: index
last_rendered: 2026-11-25T09:51:47Z
claims: 461
sources: 28
---

# Big Data Processing — Knowledge Index

Rendered from 28 sources into 461 claims. 0 open conflicts, 0 claims flagged for review.

Graph: 74 entities and 26 typed relationships. 153 prompts are collected in the question pages.

The wiki is a view. The source of truth is `raw/`, `observations/`, `state/` and `transitions/`.

## Topics

| Topic | Claims | Active | Disputed | Sources | Median confidence |
|---|---|---|---|---|---|
| [[bigdata-foundations|Big Data Foundations]] | 5 | 3 | 0 | 4 | 0.63 |
| [[python-execution|Python Execution Model]] | 27 | 19 | 0 | 5 | 0.63 |
| [[python-environments|Python Environments and Reproducibility]] | 49 | 42 | 0 | 10 | 0.67 |
| [[data-formats|File Formats]] | 39 | 30 | 0 | 7 | 0.63 |
| [[data-duckdb|DuckDB]] | 15 | 13 | 0 | 3 | 0.63 |
| [[engines-single_machine|Single-Machine Engines]] | 12 | 11 | 0 | 6 | 0.68 |
| [[hdfs-architecture|HDFS]] | 4 | 3 | 0 | 3 | 0.64 |
| [[spark-architecture|Spark Architecture]] | 49 | 32 | 0 | 3 | 0.63 |
| [[spark-execution|Spark Execution Model]] | 33 | 27 | 0 | 3 | 0.64 |
| [[spark-ml|Spark ML]] | 5 | 4 | 0 | 1 | 0.63 |
| [[kafka-log|Kafka Log]] | 31 | 25 | 0 | 6 | 0.64 |
| [[kafka-cluster|Kafka Cluster]] | 28 | 16 | 0 | 7 | 0.63 |
| [[kafka-producers|Kafka Producers]] | 11 | 7 | 0 | 5 | 0.62 |
| [[kafka-consumers|Kafka Consumers and Consumer Groups]] | 24 | 14 | 0 | 5 | 0.62 |
| [[streaming-architecture|Streaming Architectures]] | 2 | 1 | 0 | 1 | 0.65 |
| [[course-setup|Course Setup]] | 31 | 21 | 0 | 8 | 0.64 |
| [[course-dataset|NYC Yellow Taxi Dataset]] | 23 | 20 | 0 | 7 | 0.63 |
| [[course-exam|Exam]] | 16 | 16 | 0 | 8 | 0.74 |
| [[course-policy|Course Rules and Policies]] | 2 | 2 | 0 | 4 | 0.82 |
| [[tooling-kaggle|Kaggle Labs]] | 17 | 10 | 0 | 9 | 0.61 |
| [[tooling-docker|Docker and Dev Containers]] | 13 | 11 | 0 | 4 | 0.67 |
| [[unfiled|Unfiled Observations]] | 25 | 1 | 0 | 8 | 0.52 |

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `03_exam_circuit-gitdiff.md` | exam | 0.95 | 2 | 2026-11-25 |
| `04_mock_exam-gitdiff.md` | exam | 0.95 | 6 | 2026-11-25 |
| `README.md` | readme | 0.85 | 40 | 2026-11-11 |
| `get_data.py` | code | 0.80 | 4 | 2026-10-28 |
| `requirements-local.txt` | config | 0.75 | 1 | 2026-11-11 |
| `requirements.txt` | config | 0.75 | 1 | 2026-10-28 |
| `session-01/00_warmup_threads_vs_processes.ipynb` | notebook | 0.86 | 10 | 2026-10-28 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 18 | 2026-10-28 |
| `session-01/02_bonus_python_without_gil.ipynb` | notebook | 0.86 | 11 | 2026-10-28 |
| `session-01/workers.py` | code | 0.80 | 0 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 82 | 2026-10-28 |
| `session-03/session-03.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 29 | 2026-10-28 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 27 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 24 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 51 | 2026-10-28 |
| `session-04/README.md` | readme | 0.85 | 26 | 2026-10-28 |
| `session-04/check_env.py` | code | 0.80 | 1 | 2026-10-28 |
| `session-05/session-05.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 29 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 51 | 2026-11-11 |
| `session-06/03_exam_circuit.md` | exam | 0.95 | 2 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 49 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 4 | 2026-11-11 |
| `session-06/docker-compose.yml` | config | 0.75 | 6 | 2026-11-11 |
| `session-06/get_kafka.py` | code | 0.80 | 11 | 2026-11-11 |
| `session-06/kafka_data.py` | code | 0.80 | 8 | 2026-11-11 |
| `session-06/producer.py` | code | 0.80 | 4 | 2026-11-11 |

## Questions

153 prompts are collected under [[questions/index|Questions]].

## Using This System

```bash
cd llm-wiki-v3
python3 -m engine query "why is parquet faster than csv"
python3 -m engine lint
python3 -m engine ingest            # after adding PDFs to raw/inbox/
python3 -m engine rebuild           # full re-derivation from raw sources
```
