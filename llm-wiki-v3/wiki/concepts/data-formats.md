---
title: File Formats
type: concepts
topic: data.formats
entity_ids:
  - ent_parquet
  - ent_csv
  - ent_pickle
  - ent_spark
  - ent_avro
  - ent_duckdb
  - ent_json
  - ent_kaggle
  - ent_copy
  - ent_delta_lake
  - ent_gb_csv
  - ent_kafka
claim_ids:
  - claim_2a12cca0
  - claim_cc02fde9
  - claim_5812744e
  - claim_57adeced
  - claim_545b0436
  - claim_4afed108
  - claim_79960e02
  - claim_aaa609d4
  - claim_741fb458
  - claim_e42b42f7
  - claim_10fe02eb
  - claim_626b051b
  - claim_b01c67aa
  - claim_99cbd193
  - claim_ed48868c
  - claim_55cf95f1
  - claim_025c1f56
  - claim_0d0d6d1d
  - claim_e0cd9ffd
  - claim_7382e401
  - claim_1fdf934a
  - claim_25e669e0
  - claim_d9ff5488
  - claim_854a0f56
  - claim_0ea5b3d9
  - claim_8a9dc815
  - claim_dbc0f70d
  - claim_e03cf725
  - claim_b33f16f1
  - claim_17c46232
  - claim_922f0bd0
  - claim_c70b0237
  - claim_dd4948d8
  - claim_faa91d2c
  - claim_2f4a217d
  - claim_e9ccc6f8
  - claim_e967acaa
  - claim_c49f3c07
  - claim_6fb4e772
  - claim_0f3b938f
  - claim_c658f605
  - claim_77750d7f
  - claim_3880bed7
  - claim_80b31662
  - claim_0d130221
  - claim_b151c716
  - claim_c5f6bab5
  - claim_2a74cbf4
  - claim_a3916661
  - claim_1d8e490a
  - claim_907a6070
  - claim_dc9cc3b7
  - claim_9ab1d146
  - claim_0588f87b
  - claim_ca9b02cb
  - claim_44201d6c
  - claim_6531a3dc
  - claim_404dfda7
  - claim_111df715
  - claim_3e9c420c
  - claim_99ec99df
  - claim_3dc7dd21
  - claim_61fb1e16
  - claim_9e8e781d
  - claim_50851941
confidence: 0.666
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1cebb3bb
  - src_46087206
  - src_47132aab
  - src_59b6ded4
  - src_6494d099
  - src_68fcf2b9
  - src_6e2e5684
  - src_70f9fe3e
  - src_8615b91f
  - src_8e87808f
  - src_96e79681
  - src_b3356305
review_required: false
---

# File Formats

Rendered from 65 claims and 12 sources. Median confidence 0.67; 55 active, 0 disputed, 0 superseded.

## Current Understanding

### Lab saving data models csv

**That is part of the lesson: always benchmark on your own data and hardware.**
Confidence 0.65 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:13` — “We measure all of this ourselves, on real taxi data – your numbers will differ from your neighbour's. That is part of the lesson: always benchmark on your own data and hardware.”

**Sooner or later you save a DataFrame or a trained model to disk.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:6` — “Sooner or later you save a DataFrame or a trained model to disk. The file format decides”

**Who can open it (Excel? Spark? only Python?).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:10` — “- who can open it (Excel? Spark? only Python?),”

**Best of repeat runs in seconds (the minimum is the least noisy estimate).**
Confidence 0.60 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-2` — “best of repeat runs in seconds (the minimum is the least noisy estimate)”

### Never unpickle files trust

**To share data, use Parquet. To share models across languages/tools there are formats such as ONNX (and Spark has its own model.save() – you will see it in Lab D).**
Confidence 0.87 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p19:5` — “Here the function is print. An attacker would use class Surprise: os.system. def reduce(self): return (print, (" ran on LOAD",)) Only load pickles you created yourself or fully trust.…”

**Only load pickles you created yourself or that come from a source you fully trust.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-31:3` — “- Only load pickles you created yourself or that come from a source you fully trust.”

**The same applies to pd.read_pickle, joblib.load and older model files from the internet.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-31:1` — “The same applies to pd.read_pickle, joblib.load and older model files from the internet. Rules of thumb:”

**Unpickling does not just read data – it may run code.**
Confidence 0.53 · candidate · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-29:2` — “Unpickling does not just read data – it may run code. An object can tell pickle "to rebuild me, call this function". The demo below is harmless: the function is print. An attacker would…”

### Data

**In the comparison table, Keeps dtypes: CSV: no, pickle: yes, Parquet: yes.**
Confidence 0.69 · active · 1 source · when: for data you share or keep
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-22:13` — “Spark, DuckDB, Polars, R can read it | yes | no (Python only) | yes”

**Each month is ~50 MB of Parquet and ~3 million trips.**
Confidence 0.67 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-2:2` — “Each month is ~50 MB of Parquet and ~3 million trips. Start with 6 months; we scale up later. Run once in the terminal: python get_data.py --months 6”

**Part 2: January 2015 as one 2 GB CSV – the Kaggle dataset you added as input.**
Confidence 0.65 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-3:3` — “- Part 2: January 2015 as one 2 GB CSV – the Kaggle dataset you added as input.”

### Data million real taxi trips

**Your turn (5 min): read the CSV back so that the two timestamp columns are real datetimes and the index column disappears.**
Confidence 0.68 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-9:4` — “Your turn (5 min): read the CSV back so that the two timestamp columns are real datetimes and the index column disappears. Then think: would you want to write this for 50 columns?”

**If your laptop is slow, set N_ROWS = 300_000.**
Confidence 0.63 · active · 1 source · when: If your laptop is slow
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-3:2` — “We take a random sample of 1 million trips from January 2024 (the full month has ~3 million). If your laptop is slow, set N_ROWS = 300_000.”

**The timestamps came back as text.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-9:1` — “The timestamps came back as text. CSV stores only characters – no types, no schema. pandas has to guess the types again on every read, and it cannot guess timestamps or categories.”

### Reading need

**Your turn (5 min): read only tpep_pickup_datetime, trip_distance and tip_amount, and only credit-card trips (payment_type == 1), directly from the Parquet file.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-20:5` — “Your turn (5 min): read only tpep_pickup_datetime, trip_distance and tip_amount, and only credit-card trips (payment_type == 1), directly from the Parquet file. Compare time and memory…”

**Parquet stores each column separately (+ min/max statistics), so it can skip the rest. pickle is one opaque blob: all or nothing.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-20:2` — “In practice you rarely need all 19 columns. Parquet stores each column separately (+ min/max statistics), so it can skip the rest. pickle is one opaque blob: all or nothing.”

**Surprised? pickle can be as fast or faster here: it is close to a raw memory dump, and the whole file fits in RAM.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-22:1` — “Surprised? pickle can be as fast or faster here: it is close to a raw memory dump, and the whole file fits in RAM. The real difference is what has to fit into memory: pickle always loads…”

### Export results

**Your turn (5 min): export the average duration and trip count per pickup borough and hour of day to ../data/borough_hour.parquet with COPY (...) TO.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-23:2` — “Your turn (5 min): export the average duration and trip count per pickup borough and hour of day to ../data/borough_hour.parquet with COPY (...) TO ... (FORMAT parquet). Read the file back…”

**TODO: COPY ( SELECT ... FROM trips_enriched GROUP BY ... ) TO '...' (FORMAT parquet).**
Confidence 0.55 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-24` — “TODO: COPY ( SELECT ... FROM trips_enriched GROUP BY ... ) TO '...' (FORMAT parquet)”

### File formats matter parquet vs

**Parquet is columnar, compressed and stores min/max statistics per row group.**
Confidence 0.80 · active · 2 sources
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p50:13` — “Parquet also compresses well (similar values sit together) and stores min/max statistics per block, so engines can skip blocks entirely.”

**Peek inside the Parquet file: row groups and column statistics.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-17` — “Peek inside the Parquet file: row groups and column statistics”

### Pickle shines python objects trained

**A trained scikit-learn model is a Python object with fitted parameters inside – no table format can store it.**
Confidence 0.68 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-22:20` — “A trained scikit-learn model is a Python object with fitted parameters inside – no table format can store it. We train a small model that predicts the trip duration in minutes (the same…”

**Your turn (3 min): joblib.dump has a compress= parameter.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-25:1` — “Your turn (3 min): joblib.dump has a compress= parameter. Save the model with compress=3. How much smaller is the file, and does loading still give identical predictions?”

### Arbitrary scale level pipelines

**» Level 3: Pipelines of Arbitrary Scale, Data Model, Compression, Usage.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p23:8` — “» Level 3: Pipelines of Arbitrary Scale, Data Model, Compression, Usage”

### Avg distance layout touches

**For avg(distance), the row layout touches every block – the columnar layout reads one contiguous run and skips the rest.**
Confidence 0.70 · active · 1 source · when: For avg (distance)
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p17:14` — “V = vendor · P = pickup time · D = distance · T = tip. For avg(distance), the row layout touches every block – the columnar layout reads one contiguous run and skips the rest.”

### Convert gb csv parquet runs

**We need the 2015 data as Parquet in Part 2.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-7:2` — “We need the 2015 data as Parquet in Part 2. Converting takes a few minutes, so we start it now. A CSV has no types – we write the schema ourselves instead of letting Spark guess…”

### Csv binary formats schema

**But only binary formats with a schema know the types – a CSV reader has to guess whether "28" is a number.**
Confidence 0.81 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p51:19` — “All five can be compressed (gzip, Snappy, zstd …). But only binary formats with a schema know the types – a CSV reader has to guess whether "28" is a number.”

### Csv look data certain

**» Look at data at a certain point in time (e.g. customers at date) » Challenges: » Support data integrity » Availability » Naming conventions » Different CSV Headers » Wrong Time Stamps.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p42:3` — “» Look at data at a certain point in time (e.g. customers at date) » Challenges: » Support data integrity » Availability » Naming conventions » Different CSV Headers » Wrong Time Stamps”

### Csv million real trips

**1 million real trips, January 2024 CSV [] [] [__].**
Confidence 0.72 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p20:7` — “1. 1 million real trips, January 2024 CSV [] [] [__]”

### Csv read csv filter select

**Read.csv filter select count().**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p31:5` — “read.csv filter select count()”

### Csv read csv returned instantly

**» read.csv returned instantly, count() took much longer.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p40:3` — “» read.csv returned instantly, count() took much longer. Explain with transformation, action and lazy evaluation. » Narrow or wide: filter, withColumn, groupBy().agg(), orderBy, select.…”

### Csv text

**CSV row · text none, all text exchange, Excel, small flat files.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p51:7` — “CSV row · text none, all text exchange, Excel, small flat files”

### Download data

**You should now have data/yellow_tripdata_2024-01.parquet, …-02.parquet and data/taxi_zone_lookup.csv.**
Confidence 0.64 · active · 1 source
Evidence: `session-04/README.md:51` — “You should now have data/yellow_tripdata_2024-01.parquet, …-02.parquet and data/taxi_zone_lookup.csv.”

### Duckdb fit

**In the comparison table, Storage layout: DuckDB: columnar, SQLite: row, PostgreSQL: row, Spark: files (Parquet/Delta).**
Confidence 0.69 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-26:5` — “Storage layout | columnar | row | row | files (Parquet/Delta)”

### Five compressed gzip snappy

**All five can be compressed (gzip, Snappy, zstd …).**
Confidence 0.59 · candidate · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p51:19` — “All five can be compressed (gzip, Snappy, zstd …). But only binary formats with a schema know the types – a CSV reader has to guess whether "28" is a number.”

### Five questions file format

**Five questions every file format answers.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p16:1` — “Five questions every file format answers”

### Json writing events analysing

**Writing events Analysing data Exchanging with people One record at a time, all fields A few columns of many rows: Readable, works everywhere: CSV, together: Avro, JSON Lines.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p53:6` — “Writing events Analysing data Exchanging with people One record at a time, all fields A few columns of many rows: Readable, works everywhere: CSV, together: Avro, JSON Lines. Parquet, ORC.…”

### Kafka avro binary stored

**Avro row · binary stored in the file, can evolve Kafka, streams, writing record by record.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p51:12` — “Avro row · binary stored in the file, can evolve Kafka, streams, writing record by record”

### Kafka serializer producer

**» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p101:3` — “» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.…”

### Kaggle read csv count

**Read.csv on Kaggle count() on 12.7 M rows In .explain(), find ReadSchema and PushedFilters – Spark reads only what the plan [__ seconds] [__ seconds] needs.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p31:12` — “read.csv on Kaggle count() on 12.7 M rows In .explain(), find ReadSchema and PushedFilters – Spark reads only what the plan [__ seconds] [__ seconds] needs.”

### Need cluster file formats

**1 2 Do you need a cluster? → File formats & engines 9P 9 P · debrief.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p102:4` — “1 2 Do you need a cluster? → File formats & engines 9P 9 P · debrief”

### Notebook

**Read and explore Parquet data with DataFrames.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:15` — “- Read and explore Parquet data with DataFrames.”

### Parquet columnar compressed typed

**Two compression codecs: snappy (default, fast) and zstd (smaller).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-17:2` — “You know Parquet from Session 1. Two compression codecs: snappy (default, fast) and zstd (smaller).”

### Parquet csv pickle

**CSV, pickle, Parquet, Feather: write, read, size, dtypes pickle [] [] [__].**
Confidence 0.68 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p20:8` — “2. CSV, pickle, Parquet, Feather: write, read, size, dtypes pickle [] [] [__]”

### Parquet csv small data

**Why can CSV not? » On small data pickle can be as fast as Parquet.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p21:3` — “» Name three disadvantages of CSV you measured in Lab B, each with your number. » Which of CSV, pickle and Parquet keep category and nullable-integer dtypes? Why can CSV not? » On small…”

### Parquet export result

**Export a result to Parquet WHERE duration_min <= 0 ) AS non_positive_duration, ... FROM trips.**
Confidence 0.68 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p26:13` — “7. Export a result to Parquet WHERE duration_min <= 0 ) AS non_positive_duration, ... FROM trips”

### Parquet quick sql straight

**Quick SQL straight on Parquet files – Session 1.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p24:7` — “Gone when Python stops. Tables survive. No CREATE DATABASE – connecting creates the file. Quick SQL straight on Parquet files – Session 1. A local analytics database you can hand over as…”

### Parquet read columns time

**Read 3 columns only – time and memory Parquet [] [] [__].**
Confidence 0.78 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p20:10` — “3. Read 3 columns only – time and memory Parquet [] [] [__]”

### Parquet storage columnar files

**Storage columnar row row files (Parquet, Delta).**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p25:9` — “Storage columnar row row files (Parquet, Delta)”

### Partition gb mb waves

**2 GB ÷ 128 MB ≈ 16 4 waves one CSV file maxPartitionBytes partitions = 16 tasks on 4 cores.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p35:6` — “2 GB ÷ 128 MB ≈ 16 4 waves one CSV file maxPartitionBytes partitions = 16 tasks on 4 cores”

### Pickle loading run

**Loading a pickle can run code.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p19:1` — “Loading a pickle can run code”

### Pickle python freeze dry

**Pickle turns any Python object into bytes and back. df.to_pickle() is a thin wrapper around it.**
Confidence 0.80 · active · 2 sources
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-15:2` — “pickle turns any Python object into bytes and back. df.to_pickle() is a thin wrapper around it.”

### Pickle save model

**Save a model with pickle and joblib.**
Confidence 0.64 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p20:12` — “4. Save a model with pickle and joblib”

### Pickle session 04 02 file formats and pickle ipynb laptop write

**Session-04/02_file_formats_and_pickle.ipynb Your laptop write read MB.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p20:6` — “session-04/02_file_formats_and_pickle.ipynb Your laptop write read MB”

### Pickle works together environment

**A pickled model stores references to classes (sklearn.ensemble...HistGradientBoostingRegressor), not their code.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-27:2` — “A pickled model stores references to classes (sklearn.ensemble...HistGradientBoostingRegressor), not their code. Load it with a different scikit-learn version and you may get a warning,…”

### Pre flight checklist anything else

**Check your data – run the second cell. You need at least one month of Parquet data.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:26` — “3. Check your data – run the second cell. You need at least one month of Parquet data.”

### Predict run

**FileScan parquet at the bottom — this is always where Spark starts (bottom to top).**
Confidence 0.67 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-24:3` — “- FileScan parquet at the bottom — this is always where Spark starts (bottom to top).”

### Reading execution plan

**In the plan: FileScan parquet — Meaning: reading the file – the plan is read bottom to top.**
Confidence 0.84 · active · 2 sources
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-19:8` — “PushedFilters | filters handed to the Parquet reader (skips row groups)”

### Reproducible python saving data models

**Lab: B — Topic: CSV vs. pickle vs. Parquet, saving models; Where: laptop, notebook; File: 02_file_formats_and_pickle.ipynb.**
Confidence 0.86 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p3:10` — “B CSV vs. pickle vs. Parquet, saving models Laptop · notebook 35 min”

### Saving spark model pickle

**Spark therefore has its own format: a folder with JSON metadata and Parquet files.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-54:2` — “The Python PipelineModel is only a thin wrapper around objects that live in the JVM. Spark therefore has its own format: a folder with JSON metadata and Parquet files. It can be loaded…”

### Sessions folders

**Folder: session-04/ — Topic: Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML; Runs on: laptop (Labs A–C) · Kaggle (Lab D).**
Confidence 0.72 · active · 1 source
Evidence: `README.md:132` — “session-04/ | Reproducible Python (venv, pyenv, uv), CSV vs. pickle vs. Parquet, DuckDB as a database file, Spark fundamentals + Spark ML | laptop (Labs A–C) · Kaggle (Lab D)”

### Smaller dtypes remembers

**Many columns use far bigger types than needed: VendorID is 1 or 2 but stored as a 32-bit integer, store_and_fwd_flag is "Y"/"N" but stored as a string per row.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-11:2` — “Many columns use far bigger types than needed: VendorID is 1 or 2 but stored as a 32-bit integer, store_and_fwd_flag is "Y"/"N" but stored as a string per row.”

### Spark job orc column

**ORC column · binary typed, also nested Hive and Hadoop batch jobs.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p51:16` — “ORC column · binary typed, also nested Hive and Hadoop batch jobs”

### Spark kaggle fundamentals ml

**Part: 0 · Setup — What you do: Java + PySpark, download data, start Spark, convert a 2 GB CSV – run it before the break; Data: –.**
Confidence 0.73 · active · 1 source · when: before the break
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:7` — “0 · Setup | Java + PySpark, download data, start Spark, convert a 2 GB CSV – run it before the break | –”

### Task extension add location names

**Read ../data/taxi_zone_lookup.csv into a DataFrame called zones.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-29:8` — “1. Read ../data/taxi_zone_lookup.csv into a DataFrame called zones.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 19 | 2026-11-25 |
| `session-04/README.md` | readme | 0.85 | 2 | 2026-10-28 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf` | lecture_note | 0.92 | 7 | 2026-11-25 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 21 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `README.md` | readme | 0.85 | 1 | 2026-11-11 |

## Related Pages

- [[spark-ml|Spark ML]] (71 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (69 shared entities)
- [[data-duckdb|DuckDB]] (45 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (44 shared entities)
- [[spark-execution|Spark Execution Model]] (43 shared entities)
- [[unfiled|Unfiled Observations]] (34 shared entities)

## Open Questions

22 prompts from the material are collected in [[questions/data-formats|Questions: File Formats]].
- A6 (4 P) Your team has an 8 GB Parquet dataset (one year of trips) and laptops with 16 GB RAM and 8 cores. A colleague wants to rent a…
- C1 (1 P) Which of these formats are columnar: CSV, JSON, Avro, Parquet, ORC?
- C2 (1 P) Which row-oriented binary format with an embedded schema is commonly used for Kafka events?

## Timeline

- 2026-11-25: new_claim on `claim_404dfda7`
- 2026-11-25: new_claim on `claim_111df715`
- 2026-11-25: new_claim on `claim_3e9c420c`
- 2026-11-25: new_claim on `claim_99ec99df`
- 2026-11-25: new_claim on `claim_3dc7dd21`
- 2026-11-25: new_claim on `claim_61fb1e16`
- 2026-11-25: new_claim on `claim_9e8e781d`
- 2026-11-25: new_claim on `claim_50851941`
