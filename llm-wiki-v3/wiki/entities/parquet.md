---
title: Parquet
type: entity
entity_id: ent_parquet
entity_type: format
claim_ids:
  - claim_2a12cca0
  - claim_cc02fde9
  - claim_5812744e
  - claim_5f5d2389
  - claim_342a7d6c
  - claim_545b0436
  - claim_79960e02
  - claim_aaa609d4
  - claim_741fb458
  - claim_e42b42f7
  - claim_88fd804c
  - claim_10fe02eb
  - claim_626b051b
  - claim_b01c67aa
  - claim_6f06a285
  - claim_5eb0d493
  - claim_1fdf934a
  - claim_25e669e0
  - claim_854a0f56
  - claim_922f0bd0
  - claim_2f4a217d
  - claim_e9ccc6f8
  - claim_e967acaa
  - claim_3ed72880
  - claim_6fb4e772
  - claim_80b31662
  - claim_2a74cbf4
  - claim_671b1279
  - claim_a3916661
  - claim_1d8e490a
  - claim_907a6070
  - claim_dc9cc3b7
  - claim_67656973
  - claim_5584689f
  - claim_24464bf6
confidence: 0.683
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_46087206
  - src_467d2d1e
  - src_47132aab
  - src_59b6ded4
  - src_6494d099
  - src_6e2e5684
  - src_70f9fe3e
  - src_8e87808f
  - src_96e79681
  - src_b3356305
---

# Parquet

Type: format. Mentioned in 35 claims across 7 topics.
Aliases: Apache Parquet.

## Claims

- **To share data, use Parquet. To share models across languages/tools there are formats such as ONNX (and Spark has its own model.save() – you will see it in Lab D).** Confidence 0.87 · [[data-formats|File Formats]]
- **Lab: B — Topic: CSV vs. pickle vs. Parquet, saving models; Where: laptop, notebook; File: 02_file_formats_and_pickle.ipynb.** Confidence 0.86 · [[data-formats|File Formats]]
- **In the plan: FileScan parquet — Meaning: reading the file – the plan is read bottom to top.** Confidence 0.84 · [[data-formats|File Formats]]
- **Part: 1 · Spark fundamentals — What you do: DataFrames, transformations vs. actions, plans, shuffles, joins; Data: NYC taxi January 2024, Parquet (~3 M trips).** Confidence 0.84 · [[spark-execution|Spark Execution Model]]
- **Parquet is columnar, compressed and stores min/max statistics per row group.** Confidence 0.80 · [[data-formats|File Formats]]
- **Read 3 columns only – time and memory Parquet [] [] [__].** Confidence 0.78 · [[data-formats|File Formats]]
- **Download NYC Yellow Taxi trip data (Parquet) and the taxi zone lookup into ./data.** Confidence 0.76 · [[course-dataset|NYC Yellow Taxi Dataset]]
- **Why does Parquet still scale better for 3 of 19 columns of 50 GB? » A model will be used by a server batch job in six months.** Confidence 0.74 · [[course-dataset|NYC Yellow Taxi Dataset]]
- **12.7 M trips, cleaned Pipeline to saved model CSV vs. Parquet · data quality in one pass · ANSI mode · Baseline · Pipeline · CrossValidator · gradient-boosted trees · features save().** Confidence 0.74 · [[spark-ml|Spark ML]]
- **Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.** Confidence 0.73 · [[engines-single_machine|Single-Machine Engines]]
- **Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).** Confidence 0.72 · [[data-formats|File Formats]]
- **» What it is: a DataFrame library written in Rust (since 2020), with Apache Arrow as its memory format. » How it runs: lazy with scan_parquet() / .lazy(): first it builds a query plan, optimizes it (projection and predicate pushdown), then executes it.** Confidence 0.70 · [[engines-single_machine|Single-Machine Engines]]
- **Parquet column · binary typed, also nested analytics, data lakes, Spark, DuckDB, Polars.** Confidence 0.70 · [[engines-single_machine|Single-Machine Engines]]
- **Quick SQL straight on Parquet files – Session 1.** Confidence 0.70 · [[data-formats|File Formats]]
- **In the comparison table, Keeps dtypes: CSV: no, pickle: yes, Parquet: yes.** Confidence 0.69 · [[data-formats|File Formats]]
- **In the comparison table, Storage layout: DuckDB: columnar, SQLite: row, PostgreSQL: row, Spark: files (Parquet/Delta).** Confidence 0.69 · [[data-formats|File Formats]]
- **Your turn (5 min): read only tpep_pickup_datetime, trip_distance and tip_amount, and only credit-card trips (payment_type == 1), directly from the Parquet file.** Confidence 0.69 · [[data-formats|File Formats]]
- **CSV, pickle, Parquet, Feather: write, read, size, dtypes pickle [] [] [__].** Confidence 0.68 · [[data-formats|File Formats]]
- **Export a result to Parquet WHERE duration_min <= 0 ) AS non_positive_duration, ... FROM trips.** Confidence 0.68 · [[data-formats|File Formats]]
- **FileScan parquet at the bottom — this is always where Spark starts (bottom to top).** Confidence 0.67 · [[data-formats|File Formats]]
- **Each month is ~50 MB of Parquet and ~3 million trips.** Confidence 0.67 · [[data-formats|File Formats]]
- **Storage columnar row row files (Parquet, Delta).** Confidence 0.66 · [[data-formats|File Formats]]
- **Why can CSV not? » On small data pickle can be as fast as Parquet.** Confidence 0.65 · [[data-formats|File Formats]]
- **You should now have data/yellow_tripdata_2024-01.parquet, …-02.parquet and data/taxi_zone_lookup.csv.** Confidence 0.64 · [[data-formats|File Formats]]
- **Your turn (5 min): export the average duration and trip count per pickup borough and hour of day to ../data/borough_hour.parquet with COPY (...) TO.** Confidence 0.63 · [[data-formats|File Formats]]
- **Parquet stores each column separately (+ min/max statistics), so it can skip the rest. pickle is one opaque blob: all or nothing.** Confidence 0.63 · [[data-formats|File Formats]]
- **AS SELECT (CTAS) reads the Parquet files once and stores the result inside the database file.** Confidence 0.63 · [[data-duckdb|DuckDB]]
- **Spark therefore has its own format: a folder with JSON metadata and Parquet files.** Confidence 0.63 · [[data-formats|File Formats]]
- **In Session 1 you used DuckDB in memory: duckdb.connect() and SQL straight on Parquet files.** Confidence 0.63 · [[data-duckdb|DuckDB]]
- **Needs data/yellow_tripdata_2024-01.parquet (python get_data.py --months 2).** Confidence 0.61 · [[course-setup|Course Setup]]
- **Check your data – run the second cell. You need at least one month of Parquet data.** Confidence 0.61 · [[data-formats|File Formats]]
- **We need the 2015 data as Parquet in Part 2.** Confidence 0.58 · [[data-formats|File Formats]]
- **Read and explore Parquet data with DataFrames.** Confidence 0.56 · [[data-formats|File Formats]]
- **TODO: COPY ( SELECT ... FROM trips_enriched GROUP BY ... ) TO '...' (FORMAT parquet).** Confidence 0.55 · [[data-formats|File Formats]]
- **Peek inside the Parquet file: row groups and column statistics.** Confidence 0.55 · [[data-formats|File Formats]]

## Related Entities

- [[spark|Spark]] (8)
- [[pickle|Pickle]] (7)
- [[csv|CSV]] (6)
- [[duckdb|DuckDB]] (6)
- [[nyc_yellow_taxi_dataset|NYC Yellow Taxi dataset]] (3)
- [[polars|Polars]] (3)
- [[topic|topic]] (3)
- [[delta_lake|Delta Lake]] (2)
- [[taxi_zone_lookup|Taxi zone lookup]] (2)
- [[crossvalidator|CrossValidator]] (1)
