---
title: NYC Yellow Taxi Dataset
type: concepts
topic: course.dataset
entity_ids:
  - ent_nyc_yellow_taxi_dataset
  - ent_taxi_zone_lookup
  - ent_kaggle
  - ent_parquet
  - ent_spark_job
  - ent_todo
  - ent_action
  - ent_add_input
  - ent_d
  - ent_lab_d
  - ent_locationid_todo
  - ent_nyc_tlc
claim_ids:
  - claim_9f2bb480
  - claim_5f5d2389
  - claim_b32529ab
  - claim_0718eab9
  - claim_4081509c
  - claim_c8164b26
  - claim_94df7093
  - claim_91284a5d
  - claim_f153f7c8
  - claim_2a045acf
  - claim_4feabb5c
  - claim_c958073c
  - claim_bba466d5
  - claim_b4d9a04f
  - claim_ec01ddf2
  - claim_b81bd267
  - claim_3c6cfe61
  - claim_e50a2783
  - claim_e90fb65d
  - claim_8ea3b0fc
  - claim_30109d31
  - claim_91ea9d3f
  - claim_3500f63e
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_467d2d1e
  - src_47132aab
  - src_6494d099
  - src_6e2e5684
  - src_8e87808f
  - src_96e79681
  - src_b3356305
review_required: false
---

# NYC Yellow Taxi Dataset

Rendered from 23 claims and 7 sources. Median confidence 0.63; 20 active, 0 disputed, 0 superseded.

## Current Understanding

### Task add zone names join

**The zone lookup (265 rows) has LocationID, Borough, Zone.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-24:2` — “The location IDs mean nothing to a human. The zone lookup (265 rows) has LocationID, Borough, Zone.”

**Your turn (5 min): join top_locations with zones (PULocationID = LocationID), keep PULocationID, Zone, Borough, trip_count, avg_fare, sort by trip_count descending and show 15 rows.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-24:4` — “Your turn (5 min): join top_locations with zones (PULocationID = LocationID), keep PULocationID, Zone, Borough, trip_count, avg_fare, sort by trip_count descending and show 15 rows. Then…”

**TODO 1: .join(zones, , "left") condition: top_locations.PULocationID == zones.LocationID TODO 2: .select(...) the columns PULocationID, Zone, Borough, trip_count, avg_fare TODO 3: .orderBy(...) trip_count descending.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-26` — “TODO 1: .join(zones, , "left") condition: top_locations.PULocationID == zones.LocationID TODO 2: .select(...) the columns PULocationID, Zone, Borough, trip_count, avg_fare TODO 3:…”

### Get data

**Download NYC Yellow Taxi trip data (Parquet) and the taxi zone lookup into ./data.**
Confidence 0.76 · active · 3 sources
Evidence: `README.md:26` — “get_data.py uses only the Python standard library, so it works even before you set up an environment. It downloads NYC Yellow Taxi trips 2024 (Parquet, ~50 MB per month) and the taxi zone…”

**2024-06 (~300 MB) + taxi zone lookup python get_data.py --months 2 # what Session 4 needs (~100 MB).**
Confidence 0.67 · active · 2 sources
Evidence: `session-04/03_duckdb_database.ipynb#cell-0:3` — “Runs locally with your .venv kernel. Needs two months of taxi data and the zone lookup (python get_data.py --months 2).”

### Lab saving data models csv

**We measure all of this ourselves, on real taxi data – your numbers will differ from your neighbour's.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:13` — “We measure all of this ourselves, on real taxi data – your numbers will differ from your neighbour's. That is part of the lesson: always benchmark on your own data and hardware.”

**Whether the data types survive the round trip.**
Confidence 0.61 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-0:9` — “- whether the data types survive the round trip,”

### Predict run

**Which ones are free? python t1 = df.filter(F.col("trip_distance") > 1.0) # line A t2 = t1.select("PULocationID", "trip_distance") # line B t3 = t2.groupBy("PULocationID").count() # line C result = t3.show(10) # line D Your answer (A / B / C / D – which triggers computation?).**
Confidence 0.68 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-11:16` — “> Q3 – Read the four lines below before running the cell. Which lines start a Spark job? Which ones are free? > > python > t1 = df.filter(F.col("trip_distance") > 1.0) # line A > t2 =…”

**Filter right after the scan — Catalyst pushed the fare_amount > 0 filter down to the scan.**
Confidence 0.61 · active · 1 source · when: after the scan — Catalyst pushed the fare_amount > 0 filter down to the sca
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-24:4` — “- Filter right after the scan — Catalyst pushed the fare_amount > 0 filter down to the scan.”

### Spark kaggle fundamentals ml

**Right panel → Input → + Add Input → search "NYC Yellow Taxi Trip Data" by elemento → add it.**
Confidence 0.77 · active · 2 sources
Evidence: `session-04/README.md:79` — “Kaggle: assert ... Dataset missing | Kaggle | Input → + Add Input → "NYC Yellow Taxi Trip Data" (elemento)”

**Part: 1 · Spark fundamentals — What you do: DataFrames, transformations vs. actions, plans, shuffles, joins; Data: NYC taxi January 2024, Parquet (~3 M trips).**
Confidence 0.73 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:8` — “1 · Spark fundamentals | DataFrames, transformations vs. actions, plans, shuffles, joins | NYC taxi January 2024, Parquet (~3 M trips)”

### Task extension add location names

**Join the taxi zone lookup table to add zone names.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-43:58` — “You join the trip data (3 million rows) with the taxi zone lookup table (265 rows). The plan shows a BroadcastHashJoin instead of a SortMergeJoin.”

**Show the top 15 with location name, borough, trip count, and average fare.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-29:11` — “4. Show the top 15 with location name, borough, trip count, and average fare.”

### Task trips start

**Your turn (5 min): starting from clean, compute per PULocationID the number of trips (trip_count) and the average fare rounded to 2 decimals (avg_fare), sorted by trip_count descending.**
Confidence 0.69 · active · 2 sources
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-22:2` — “Your turn (5 min): starting from clean, compute per PULocationID the number of trips (trip_count) and the average fare rounded to 2 decimals (avg_fare), sorted by trip_count descending.…”

**TODO 1: add a second aggregate: the average fare_amount, rounded to 2 decimals, named "avg_fare" TODO 2: sort by trip_count, highest first.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-23` — “TODO 1: add a second aggregate: the average fare_amount, rounded to 2 decimals, named "avg_fare" TODO 2: sort by trip_count, highest first”

### Exit ticket individual ai

**You run a groupBy("PULocationID").count() on a DataFrame with 8 partitions.**
Confidence 0.67 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-43:30` — “You run a groupBy("PULocationID").count() on a DataFrame with 8 partitions. Explain:”

### Kaggle account

**Open kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data once – that's the dataset for Lab D, Part 2. Part 1 downloads its data itself (needs Internet: On).**
Confidence 0.60 · candidate · 1 source
Evidence: `session-04/README.md:56` — “3. Open kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data once – that's the dataset for Lab D, Part 2. Part 1 downloads its data itself (needs Internet: On).”

### Load data tables

**We keep the columns we need, rename the timestamps and compute the trip duration on the way in.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-4:2` — “CREATE TABLE ... AS SELECT (CTAS) reads the Parquet files once and stores the result inside the database file. We keep the columns we need, rename the timestamps and compute the trip…”

### Reading need

**In practice you rarely need all 19 columns.**
Confidence 0.62 · active · 1 source
Evidence: `session-04/02_file_formats_and_pickle.ipynb#cell-20:2` — “In practice you rarely need all 19 columns. Parquet stores each column separately (+ min/max statistics), so it can skip the rest. pickle is one opaque blob: all or nothing.”

### Spark ml long taxi ride

**The task: predict the trip duration in minutes at the moment the passenger gets in.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-29:4` — “The task: predict the trip duration in minutes at the moment the passenger gets in. The 2015 data is the old TLC schema: GPS coordinates instead of zone IDs.”

### Task core everyone

**Aggregate to get trip count and average fare per pickup location.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:24` — “2. Aggregate to get trip count and average fare per pickup location.”

### Transformations vs actions

**Predict: which of the lines A–D starts a Spark job? python t1 = df.filter(F.col("trip_distance") > 1.0) # A t2 = t1.select("PULocationID", "trip_distance") # B t3 = t2.groupBy("PULocationID").count() # C t3.show(10) # D.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-13:3` — “> Predict: which of the lines A–D starts a Spark job? > python > t1 = df.filter(F.col("trip_distance") > 1.0) # A > t2 = t1.select("PULocationID", "trip_distance") # B > t3 =…”

### Veracity dirty data

**We compute the trip duration and count problems in a single pass (one Spark job, not six).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-33:2` — “We compute the trip duration and count problems in a single pass (one Spark job, not six).”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `get_data.py` | code | 0.80 | 2 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 11 | 2026-10-28 |
| `session-04/README.md` | readme | 0.85 | 2 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 2 | 2026-10-28 |
| `session-04/02_file_formats_and_pickle.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 7 | 2026-10-28 |
| `README.md` | readme | 0.85 | 1 | 2026-11-11 |

## Related Pages

- [[data-formats|File Formats]] (13 shared entities)
- [[course-setup|Course Setup]] (9 shared entities)
- [[spark-architecture|Spark Architecture]] (8 shared entities)
- [[data-duckdb|DuckDB]] (5 shared entities)
- [[spark-execution|Spark Execution Model]] (5 shared entities)
- [[python-execution|Python Execution Model]] (4 shared entities)

## Open Questions

9 prompts from the material are collected in [[questions/course-dataset|Questions: NYC Yellow Taxi Dataset]].
- Question: Which pickup location IDs generated the most taxi trips in January 2024?
- Why is fare_amount (or total_amount) not allowed as a feature for predicting the trip duration here? Name the general problem.
- Train the gradient-boosted trees without trip_distance (only haversine_km). How much worse does it get?

## Timeline

- 2026-11-25: new_claim on `claim_e90fb65d`
- 2026-11-25: new_claim on `claim_8ea3b0fc`
- 2026-11-25: support_update on `claim_c8164b26` (0.63 → 0.69)
- 2026-11-25: new_claim on `claim_30109d31`
- 2026-11-25: new_claim on `claim_91ea9d3f`
- 2026-11-25: new_claim on `claim_3500f63e`
- 2026-11-25: evidence_attached on `claim_91ea9d3f` (0.63 → 0.63)
- 2026-11-25: support_update on `claim_5f5d2389` (0.62 → 0.76)
