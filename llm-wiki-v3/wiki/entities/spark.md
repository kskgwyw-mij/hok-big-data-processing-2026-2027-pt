---
title: Spark
type: entity
entity_id: ent_spark
entity_type: technology
claim_ids:
  - claim_b0dbd1e0
  - claim_87320cd4
  - claim_bcb1bb0e
  - claim_57adeced
  - claim_0718eab9
  - claim_6cd04a4d
  - claim_cefb5f5e
  - claim_bd7417ec
  - claim_79960e02
  - claim_c84ec78d
  - claim_b0185af6
  - claim_55d3747e
  - claim_caed1b28
  - claim_8eafee62
  - claim_95fe6516
  - claim_b01c67aa
  - claim_99cbd193
  - claim_854a0f56
  - claim_51de55b2
  - claim_922f0bd0
  - claim_e5ed99e6
  - claim_0326b6f6
  - claim_f71118cb
  - claim_842d6db8
  - claim_f8b8c074
  - claim_939d0c3c
  - claim_e967acaa
  - claim_2af15809
  - claim_6e4a6518
  - claim_ef3a846d
  - claim_abd51c80
  - claim_451b6101
  - claim_f78bd88b
  - claim_e25a0f01
  - claim_6fb4e772
  - claim_54363381
  - claim_53ef90ae
  - claim_d82fc010
  - claim_201c7650
  - claim_0c5c079b
  - claim_87ec27e4
confidence: 0.663
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_1a3d69f8
  - src_46087206
  - src_47132aab
  - src_4d7c51b1
  - src_6494d099
  - src_6e2e5684
  - src_8e87808f
  - src_96e79681
  - src_b3356305
  - src_c65c80a3
---

# Spark

Type: technology. Mentioned in 41 claims across 13 topics.
Aliases: Apache Spark, PySpark, SparkSession.

## Claims

- **Part: B — Topic: Spark architecture, HDFS, MapReduce; Points: 16.** Confidence 0.80 · [[course-exam|Exam]]
- **Stage boundaries in Spark are always at wide transformations.** Confidence 0.74 · [[spark-architecture|Spark Architecture]]
- **Part: 1 · Spark fundamentals — What you do: DataFrames, transformations vs. actions, plans, shuffles, joins; Data: NYC taxi January 2024, Parquet (~3 M trips).** Confidence 0.73 · [[course-dataset|NYC Yellow Taxi Dataset]]
- **Part: 0 · Setup — What you do: Java + PySpark, download data, start Spark, convert a 2 GB CSV – run it before the break; Data: –.** Confidence 0.73 · [[data-formats|File Formats]]
- **Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).** Confidence 0.72 · [[data-formats|File Formats]]
- **Folder: session-02/ — Topic: Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins; Runs on: dev container or a laptop with Java 17.** Confidence 0.72 · [[spark-architecture|Spark Architecture]]
- **Always stop the SparkSession when you are done.** Confidence 0.70 · [[spark-architecture|Spark Architecture]]
- **In the comparison table, Keeps dtypes: CSV: no, pickle: yes, Parquet: yes.** Confidence 0.69 · [[data-formats|File Formats]]
- **In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **Component: SparkSession — Role: The single entry point to all Spark functionality since Spark 2.0.** Confidence 0.69 · [[spark-architecture|Spark Architecture]]
- **In the comparison table, Storage layout: DuckDB: columnar, SQLite: row, PostgreSQL: row, Spark: files (Parquet/Delta).** Confidence 0.69 · [[data-formats|File Formats]]
- **Your turn (5 min): complete haversine_km – the straight-line distance between pickup and dropoff – using only pyspark.sql.functions (F.radians, F.sin, F.cos, F.asin, F.sqrt).** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **PySpark is a Python front end for a Java engine (the JVM).** Confidence 0.68 · [[spark-execution|Spark Execution Model]]
- **That is the moment for a database server (PostgreSQL) or, for really big data, a lakehouse with Spark.** Confidence 0.68 · [[bigdata-foundations|Big Data Foundations]]
- **Where: Kaggle – free notebooks in the browser — What runs there: Apache Spark and Spark ML (no Java setup on your laptop).** Confidence 0.68 · [[course-setup|Course Setup]]
- **File: requirements.txt — Contains: the above + PySpark 4.0 and Delta Lake (needs Java 17+); Use it for: the dev container, or a laptop with Java 17 installed.** Confidence 0.68 · [[python-environments|Python Environments and Reproducibility]]
- **FileScan parquet at the bottom — this is always where Spark starts (bottom to top).** Confidence 0.67 · [[data-formats|File Formats]]
- **Lab: D — Topic: Spark fundamentals (Session 2) + Spark ML; Where: Kaggle; File: 04_spark_fundamentals_and_ml.ipynb.** Confidence 0.67 · [[tooling-kaggle|Kaggle Labs]]
- **Spark 4 runs in ANSI mode by default: a division by zero stops the job instead of returning NULL. try_divide returns NULL instead.** Confidence 0.67 · [[spark-architecture|Spark Architecture]]
- **HashAggregate appears twice: once for a partial aggregation (per partition, before shuffle) and once for a final merge (after shuffle). This is a standard Spark optimisation.** Confidence 0.66 · [[spark-execution|Spark Execution Model]]
- **To share data, use Parquet. To share models across languages/tools there are formats such as ONNX (and Spark has its own model.save() – you will see it in Lab D).** Confidence 0.66 · [[data-formats|File Formats]]
- **A Codespace has 8 GB RAM and effectively one physical CPU core: fine for learning Spark, not for speed comparisons.** Confidence 0.65 · [[python-environments|Python Environments and Reproducibility]]
- **Settings → Phone verification – without it, notebooks cannot use the internet (we need it to install PySpark).** Confidence 0.65 · [[course-setup|Course Setup]]
- **Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.** Confidence 0.65 · [[spark-architecture|Spark Architecture]]
- **Today you work in two places: your own laptop (VS Code) for Labs A–C and Kaggle for Lab D (Spark).** Confidence 0.64 · [[tooling-kaggle|Kaggle Labs]]
- **We train a small model that predicts the trip duration in minutes (the same task we will scale up with Spark later).** Confidence 0.63 · [[bigdata-foundations|Big Data Foundations]]
- **Spark therefore has its own format: a folder with JSON metadata and Parquet files.** Confidence 0.63 · [[data-formats|File Formats]]
- **Spark builds one combined logical plan and optimises it.** Confidence 0.63 · [[spark-execution|Spark Execution Model]]
- **On the slides you saw Spark's architecture: Driver, Executors, SparkSession, RDDs, DataFrames, and the Catalyst Optimizer.** Confidence 0.63 · [[spark-architecture|Spark Architecture]]
- **A DataFrame is Spark's primary data abstraction since Spark 2.0.** Confidence 0.63 · [[spark-architecture|Spark Architecture]]
- **Every DataFrame has a plan. df.explain() shows you how Spark intends to execute a query.** Confidence 0.63 · [[spark-architecture|Spark Architecture]]
- **Who can open it (Excel? Spark? only Python?).** Confidence 0.63 · [[data-formats|File Formats]]
- **The repository also contains a dev container with Python 3.12, Java 17 and everything from requirements.txt – besides Kaggle, the way to run Spark without installing Java yourself.** Confidence 0.62 · [[python-environments|Python Environments and Reproducibility]]
- **The same content (plus Spark ML) is in session-04/04_spark_fundamentals_and_ml.ipynb, which runs on Kaggle.** Confidence 0.61 · [[tooling-kaggle|Kaggle Labs]]
- **Name two situations where a single machine is not enough, even with DuckDB. → That is where Spark (next session) comes in.** Confidence 0.61 · [[engines-single_machine|Single-Machine Engines]]
- **Requirements-local.txt = everything except Spark.** Confidence 0.61 · [[python-environments|Python Environments and Reproducibility]]
- **Run the cells from the top. The first cell installs Java 17 and PySpark if Kaggle does not have them.** Confidence 0.60 · [[tooling-kaggle|Kaggle Labs]]
- **Task B – join and show Hint: the zone table is small (~265 rows). What join strategy do you expect Spark to pick? YOUR CODE.** Confidence 0.58 · [[spark-architecture|Spark Architecture]]
- **Spark's optimizer (Session 2) does exactly the same thing.** Confidence 0.58 · [[python-execution|Python Execution Model]]
- **Spark chose a [BroadcastHashJoin / SortMergeJoin] because.** Confidence 0.56 · [[spark-architecture|Spark Architecture]]
- **Pyspark is pinned as >=4.0,<4.1.** Confidence 0.39 · [[unfiled|Unfiled Observations]]

## Related Entities

- [[kaggle|Kaggle]] (7)
- [[parquet|Parquet]] (7)
- [[duckdb|DuckDB]] (5)
- [[spark_ml|Spark ML]] (5)
- [[dev_container|Dev container]] (4)
- [[topic|topic]] (4)
- [[delta_lake|Delta Lake]] (3)
- [[requirements_txt|requirements.txt]] (3)
- [[shuffle|shuffle]] (3)
- [[csv|CSV]] (2)
