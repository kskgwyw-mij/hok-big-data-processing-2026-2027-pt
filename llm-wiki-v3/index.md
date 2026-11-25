---
title: Knowledge Index
type: index
last_rendered: 2026-11-25T12:11:20Z
claims: 901
sources: 35
---

# Big Data Processing — Knowledge Index

Rendered from 35 sources into 901 claims. 4 open conflicts, 3 claims flagged for review.

Graph: 88 entities and 46 typed relationships. 186 prompts are collected in the question pages.

89 claims come from teacher-only sources and are withheld from this wiki. They stay queryable with `python3 -m engine query --include-private`.

The wiki is a view. The source of truth is `raw/`, `observations/`, `state/` and `transitions/`.

## Topics

| Topic | Claims | Active | Disputed | Sources | Median confidence |
|---|---|---|---|---|---|
| [[bigdata-foundations|Big Data Foundations]] | 29 | 27 | 0 | 10 | 0.70 |
| [[python-execution|Python Execution Model]] | 55 | 46 | 1 | 12 | 0.69 |
| [[python-environments|Python Environments and Reproducibility]] | 64 | 57 | 0 | 13 | 0.70 |
| [[data-formats|File Formats]] | 65 | 55 | 0 | 12 | 0.67 |
| [[data-duckdb|DuckDB]] | 24 | 22 | 0 | 6 | 0.69 |
| [[engines-single_machine|Single-Machine Engines]] | 27 | 26 | 0 | 10 | 0.70 |
| [[hdfs-architecture|HDFS]] | 16 | 15 | 0 | 7 | 0.70 |
| [[mapreduce-model|MapReduce]] | 4 | 4 | 0 | 1 | 0.71 |
| [[spark-architecture|Spark Architecture]] | 49 | 35 | 0 | 4 | 0.63 |
| [[spark-execution|Spark Execution Model]] | 51 | 43 | 0 | 8 | 0.69 |
| [[spark-ml|Spark ML]] | 20 | 19 | 0 | 5 | 0.70 |
| [[spark-streaming|Spark Structured Streaming]] | 2 | 2 | 0 | 2 | 0.70 |
| [[kafka-log|Kafka Log]] | 64 | 56 | 0 | 11 | 0.70 |
| [[kafka-cluster|Kafka Cluster]] | 50 | 41 | 0 | 9 | 0.70 |
| [[kafka-producers|Kafka Producers]] | 16 | 12 | 0 | 7 | 0.66 |
| [[kafka-consumers|Kafka Consumers and Consumer Groups]] | 40 | 30 | 0 | 8 | 0.68 |
| [[streaming-architecture|Streaming Architectures]] | 13 | 12 | 0 | 4 | 0.70 |
| [[course-setup|Course Setup]] | 28 | 19 | 0 | 9 | 0.63 |
| [[course-dataset|NYC Yellow Taxi Dataset]] | 30 | 26 | 0 | 8 | 0.64 |
| [[course-exam|Exam]] | 20 | 20 | 0 | 12 | 0.76 |
| [[course-policy|Course Rules and Policies]] | 3 | 3 | 0 | 5 | 0.74 |
| [[tooling-kaggle|Kaggle Labs]] | 21 | 15 | 0 | 12 | 0.65 |
| [[tooling-docker|Docker and Dev Containers]] | 28 | 24 | 1 | 6 | 0.70 |
| [[unfiled|Unfiled Observations]] | 182 | 159 | 0 | 15 | 0.65 |

## Contested Claims

- In the warm-up we saw that threads bring no speed-up for CPU-bound Python code, because of the Global Interpreter Lock (GIL). — 0.53 (`claim_5b33ee68`)
- In the comparison table, Where the CLI tools run: Route A – Docker (most of you): inside the container: docker exec -it broker /opt/kafka/bin/ .sh… — 0.59 (`claim_beb90ba1`)

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `03_exam_circuit-gitdiff.md` | exam | 0.95 | 2 | 2026-11-25 |
| `04_mock_exam-gitdiff.md` | exam | 0.95 | 6 | 2026-11-25 |
| `README.md` | readme | 0.85 | 40 | 2026-11-11 |
| `get_data.py` | code | 0.80 | 4 | 2026-10-28 |
| `raw/04_mock_exam.md` | exam | 0.95 | 8 | 2026-11-25 |
| `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf` | lecture_note | 0.92 | 58 | 2026-11-25 |
| `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf` | lecture_note | 0.92 | 76 | 2026-11-25 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 80 | 2026-11-25 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 114 | 2026-11-25 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 63 | 2026-11-25 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 145 | 2026-11-25 |
| `requirements-local.txt` | config | 0.75 | 1 | 2026-11-11 |
| `requirements.txt` | config | 0.75 | 1 | 2026-10-28 |
| `session-01/00_warmup_threads_vs_processes.ipynb` | notebook | 0.86 | 10 | 2026-10-28 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 18 | 2026-10-28 |
| `session-01/02_bonus_python_without_gil.ipynb` | notebook | 0.86 | 12 | 2026-10-28 |
| `session-01/workers.py` | code | 0.80 | 0 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 82 | 2026-10-28 |
| `session-03/session-03.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-04/01_python_environments.md` | lab_guide | 0.90 | 29 | 2026-10-28 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 28 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 24 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 52 | 2026-10-28 |
| `session-04/README.md` | readme | 0.85 | 26 | 2026-10-28 |
| `session-04/check_env.py` | code | 0.80 | 1 | 2026-10-28 |
| `session-05/session-05.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 29 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 48 | 2026-11-11 |
| `session-06/03_exam_circuit.md` | exam | 0.95 | 2 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 49 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 4 | 2026-11-11 |
| `session-06/docker-compose.yml` | config | 0.75 | 6 | 2026-11-11 |
| `session-06/get_kafka.py` | code | 0.80 | 11 | 2026-11-11 |
| `session-06/kafka_data.py` | code | 0.80 | 8 | 2026-11-11 |
| `session-06/producer.py` | code | 0.80 | 4 | 2026-11-11 |

## Questions

186 prompts are collected under [[questions/index|Questions]].

## Using This System

```bash
cd llm-wiki-v3
python3 -m engine query "why is parquet faster than csv"
python3 -m engine lint
python3 -m engine ingest            # after adding PDFs to raw/inbox/
python3 -m engine rebuild           # full re-derivation from raw sources
```
