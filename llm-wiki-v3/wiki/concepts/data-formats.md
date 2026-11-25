---
title: File Formats
type: concepts
topic: data.formats
entity_ids:
  - ent_parquet
  - ent_spark
  - ent_pickle
  - ent_csv
  - ent_duckdb
  - ent_copy
  - ent_gb_csv
  - ent_kaggle
  - ent_scikit_learn
  - ent_taxi_zone_lookup
  - ent_topic
  - ent_delta_lake
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
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_46087206
  - src_47132aab
  - src_6494d099
  - src_6e2e5684
  - src_8e87808f
  - src_96e79681
  - src_b3356305
review_required: false
---

# File Formats

Rendered from 39 claims and 7 sources. Median confidence 0.63; 30 active, 0 disputed, 0 superseded.

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

**Only load pickles you created yourself or that come from a source you fully trust.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-31:3` — “- Only load pickles you created yourself or that come from a source you fully trust.”

**To share data, use Parquet. To share models across languages/tools there are formats such as ONNX (and Spark has its own model.save() – you will see it in Lab D).**
Confidence 0.66 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-31:4` — “- To share data, use Parquet. To share models across languages/tools there are formats such as ONNX (and Spark has its own model.save() – you will see it in Lab D).”

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

**We take a random sample of 1 million trips from January 2024 (the full month has ~3 million).**
Confidence 0.67 · active · 1 source
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
Confidence 0.63 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-15:2` — “Parquet is columnar, compressed and stores min/max statistics per row group. CSV is none of that.”

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

### Convert gb csv parquet runs

**We need the 2015 data as Parquet in Part 2.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-7:2` — “We need the 2015 data as Parquet in Part 2. Converting takes a few minutes, so we start it now. A CSV has no types – we write the schema ourselves instead of letting Spark guess…”

### Download data

**You should now have data/yellow_tripdata_2024-01.parquet, …-02.parquet and data/taxi_zone_lookup.csv.**
Confidence 0.64 · active · 1 source
Evidence: `session-04/README.md:51` — “You should now have data/yellow_tripdata_2024-01.parquet, …-02.parquet and data/taxi_zone_lookup.csv.”

### Duckdb fit

**In the comparison table, Storage layout: DuckDB: columnar, SQLite: row, PostgreSQL: row, Spark: files (Parquet/Delta).**
Confidence 0.69 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-26:5` — “Storage layout | columnar | row | row | files (Parquet/Delta)”

### Notebook

**Read and explore Parquet data with DataFrames.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:15` — “- Read and explore Parquet data with DataFrames.”

### Parquet columnar compressed typed

**Two compression codecs: snappy (default, fast) and zstd (smaller).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-17:2` — “You know Parquet from Session 1. Two compression codecs: snappy (default, fast) and zstd (smaller).”

### Pickle python freeze dry

**Pickle turns any Python object into bytes and back. df.to_pickle() is a thin wrapper around it.**
Confidence 0.68 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-15:2` — “pickle turns any Python object into bytes and back. df.to_pickle() is a thin wrapper around it.”

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
Confidence 0.72 · active · 1 source
Evidence: `session-04/README.md:9` — “B | CSV vs. pickle vs. Parquet, saving models | laptop, notebook | 02_file_formats_and_pickle.ipynb”

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
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `session-04/README.md` | readme | 0.85 | 2 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 21 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `README.md` | readme | 0.85 | 1 | 2026-11-11 |

## Related Pages

- [[engines-single_machine|Single-Machine Engines]] (42 shared entities)
- [[data-duckdb|DuckDB]] (33 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (32 shared entities)
- [[course-setup|Course Setup]] (32 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (16 shared entities)
- [[course-exam|Exam]] (14 shared entities)

## Open Questions

22 prompts from the material are collected in [[questions/data-formats|Questions: File Formats]].
- Does this mean Spark only read 10 rows from the Parquet file?
- Q2 – When you call spark.read.parquet(...), does Spark immediately read all the data into memory?
- From now on, every format gets the same test: write, read, size – and do the dtypes survive?

## Timeline

- 2026-11-25: new_claim on `claim_dd4948d8`
- 2026-11-25: new_claim on `claim_faa91d2c`
- 2026-11-25: new_claim on `claim_2f4a217d`
- 2026-11-25: new_claim on `claim_e9ccc6f8`
- 2026-11-25: support_update on `claim_545b0436` (0.69 → 0.84)
- 2026-11-25: new_claim on `claim_e967acaa`
- 2026-11-25: new_claim on `claim_c49f3c07`
- 2026-11-25: new_claim on `claim_6fb4e772`
