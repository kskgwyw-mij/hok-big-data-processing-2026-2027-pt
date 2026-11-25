---
title: Spark Execution Model
type: concepts
topic: spark.execution
entity_ids:
  - ent_shuffle
  - ent_partition
  - ent_spark
  - ent_action
  - ent_transformation
  - ent_catalyst_optimizer
  - ent_delta_lake
  - ent_executor
claim_ids:
  - claim_fd74846a
  - claim_c87f33b4
  - claim_531b3248
  - claim_dce6d3cd
  - claim_75bc76b9
  - claim_6cd04a4d
  - claim_eb823027
  - claim_6594f308
  - claim_8a11dedc
  - claim_8a6b187a
  - claim_bd7417ec
  - claim_1c59b3f6
  - claim_060b38d3
  - claim_1ec5bfb7
  - claim_3f3903b5
  - claim_ca7af28b
  - claim_52ba511d
  - claim_8ee8fb30
  - claim_da9498ca
  - claim_ae31a1fc
  - claim_fb84c6d5
  - claim_66d2b535
  - claim_05153a3f
  - claim_842d6db8
  - claim_b74aab86
  - claim_839451a1
  - claim_644c31a0
  - claim_2af15809
  - claim_be79fd03
  - claim_d2161a39
  - claim_470d4ee1
  - claim_f75e0e93
  - claim_f50f0fd6
confidence: 0.638
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_47132aab
  - src_96e79681
  - src_f8b034ea
review_required: false
---

# Spark Execution Model

Rendered from 33 claims and 3 sources. Median confidence 0.64; 27 active, 0 disputed, 0 superseded.

## Current Understanding

### Feature engineering built in functions

**Your turn (5 min): complete haversine_km – the straight-line distance between pickup and dropoff – using only pyspark.sql.functions (F.radians, F.sin, F.cos, F.asin, F.sqrt).**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-38:4` — “Your turn (5 min): complete haversine_km – the straight-line distance between pickup and dropoff – using only pyspark.sql.functions (F.radians, F.sin, F.cos, F.asin, F.sqrt).”

**F.sin, F.sqrt, … run inside the JVM and are optimised by Catalyst.**
Confidence 0.68 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-41:1` — “> Why not a Python function (UDF)? F.sin, F.sqrt, … run inside the JVM and are optimised by Catalyst. A Python > UDF ships every row to a Python process and back – often 10× slower.”

**$$d = 2R \cdot \arcsin\sqrt{\sin2\left(\tfrac{\Delta\varphi}{2}\right) + \cos\varphi_1 \cos\varphi_2 \sin2\left(\tfrac{\Delta\lambda}{2}\right)}, \quad R = 6371\text{ km}$$ ($\varphi$ = latitude, $\lambda$ = longitude, both in radians).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-38:7` — “$$d = 2R \cdot \arcsin\sqrt{\sin2\left(\tfrac{\Delta\varphi}{2}\right) + \cos\varphi_1 \cos\varphi_2 \sin2\left(\tfrac{\Delta\lambda}{2}\right)}, \quad R = 6371\text{ km}$$ ($\varphi$ =…”

**We use it as a stand-in for the planned route distance a navigation app would give at pickup. haversine_km is truly known at pickup.**
Confidence 0.63 · active · 1 source · when: for the planned route distance a navigation app would give at pickup
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-41:6` — “> Grey zone: trip_distance. It is the metered distance, so strictly it is only known at the end of the ride. > We use it as a stand-in for the planned route distance a navigation app would…”

### Reading execution plan

**In the plan: Exchange — Meaning: a shuffle: rows move between partitions.**
Confidence 0.84 · active · 2 sources · when: after the shuffle)
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-19:10` — “Exchange | a shuffle: rows move between partitions”

**In the plan: BroadcastHashJoin — Meaning: small table copied to every executor – no shuffle of the big table.**
Confidence 0.84 · active · 2 sources
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-19:11` — “BroadcastHashJoin | small table copied to every executor – no shuffle of the big table”

**Symbol: SortMergeJoin — Meaning: Large-large join with shuffle and sort.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:22` — “SortMergeJoin | Large-large join with shuffle and sort”

**Predict: by_location is filter → groupBy → agg.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-19:3` — “> Predict: by_location is filter → groupBy → agg. Will the plan contain an Exchange (a shuffle)?”

### Core dataframe operations

**After each cell, note what the operation does and whether it is a transformation or an action.**
Confidence 0.68 · active · 1 source · when: After each cell
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-15:5` — “Work through these cells one by one. After each cell, note what the operation does and whether it is a transformation or an action.”

**Select · filter · withColumn · groupBy + agg · orderBy.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-15:2` — “select · filter · withColumn · groupBy + agg · orderBy”

### Java pyspark

**PySpark is a Python front end for a Java engine (the JVM).**
Confidence 0.68 · active · 1 source · when: for a Java engine (the JVM)
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-1:5` — “PySpark is a Python front end for a Java engine (the JVM). Spark 4 needs Java 17 or newer. This cell checks both and installs what is missing (~1–2 min the first time).”

**Return the major Java version (8, 11, 17, ...) or None if Java is missing.**
Confidence 0.55 · candidate · 1 source · when: if Java is missing
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-2` — “Return the major Java version (8, 11, 17, ...) or None if Java is missing”

### Predict run

**Exchange in between — this is the shuffle. After the partial aggregation, all rows with the same PULocationID must land on the same partition before the final merge can happen.**
Confidence 0.72 · active · 1 source · when: After the partial aggregation; before the final merge can happen
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-24:6` — “- Exchange in between — this is the shuffle. After the partial aggregation, all rows with the same PULocationID must land on the same partition before the final merge can happen.”

**HashAggregate appears twice: once for a partial aggregation (per partition, before shuffle) and once for a final merge (after shuffle). This is a standard Spark optimisation.**
Confidence 0.66 · active · 1 source · when: for a partial aggregation (per partition; before shuffle) and once for a final merge (after shuffle)
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-24:5` — “- HashAggregate appears twice: once for a partial aggregation (per partition, before shuffle) and once for a final merge (after shuffle). This is a standard Spark optimisation.”

### Reading data parquet dataframe

**Unlike an RDD (which is just a distributed collection of objects), a DataFrame lets Catalyst inspect column types and reorder or push down operations automatically.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-6:10` — “Unlike an RDD (which is just a distributed collection of objects), a DataFrame lets Catalyst inspect column types and reorder or push down operations automatically.”

**Processed through the Catalyst Optimizer (logical plan → optimised physical plan).**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-6:8` — “- Processed through the Catalyst Optimizer (logical plan → optimised physical plan).”

### Chaining transformations

**Spark builds one combined logical plan and optimises it.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-13:7` — “In practice, transformations are chained with the dot notation. Spark builds one combined logical plan and optimises it.”

### Convert gb csv parquet runs

**Converting takes a few minutes, so we start it now.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-7:2` — “We need the 2015 data as Parquet in Part 2. Converting takes a few minutes, so we start it now. A CSV has no types – we write the schema ourselves instead of letting Spark guess…”

### Hyper parameter tuning crossvalidator

**2 × 2 parameter combinations × 3 folds = 12 model fits (+1 refit on all training data).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-47:2` — “2 × 2 parameter combinations × 3 folds = 12 model fits (+1 refit on all training data). To keep this within a few minutes we tune on a sample of the training set.”

### Keyedevents

**Key = a state name, e.g. "Tirol" value = {"run": ..., "state": ..., "seq": n, "action": ..., "name": ..., "ts": ...}.**
Confidence 0.52 · candidate · 1 source
Evidence: `session-06/kafka_data.py:35` — “key = a state name, e.g. "Tirol" value = {"run": ..., "state": ..., "seq": n, "action": ..., "name": ..., "ts": ...}”

### Narrow vs wide transformations

**Type: Narrow — Definition: Each output partition depends on exactly one input partition; Examples: filter, select, withColumn, map; Shuffle?: No.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-24:12` — “Narrow | Each output partition depends on exactly one input partition | filter, select, withColumn, map | No”

### Notebook

**Read a physical execution plan and identify where a shuffle occurs.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:17` — “- Read a physical execution plan and identify where a shuffle occurs.”

### Pipeline gradient boosted trees one hot needed

**Trees split on thresholds, so they can use hour and the raw coordinates directly – and they can learn "from JFK to Midtown at 5 pm takes long", which a linear model cannot.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-51:2` — “Trees split on thresholds, so they can use hour and the raw coordinates directly – and they can learn "from JFK to Midtown at 5 pm takes long", which a linear model cannot.”

### Pipeline linear regression one hot encoding

**Hour, weekday, RateCodeID and VendorID are categories, not quantities (hour 23 is not "twice" hour 11.5).**
Confidence 0.68 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-45:2` — “hour, weekday, RateCodeID and VendorID are categories, not quantities (hour 23 is not "twice" hour 11.5). A linear model needs them one-hot encoded.”

### Saving spark model pickle

**The Python PipelineModel is only a thin wrapper around objects that live in the JVM.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-54:2` — “The Python PipelineModel is only a thin wrapper around objects that live in the JVM. Spark therefore has its own format: a folder with JSON metadata and Parquet files. It can be loaded…”

### Spark kaggle fundamentals ml

**Run all cells of Part 0, then take your break.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:15` — “4. Run all cells of Part 0, then take your break.”

### Spark ml four words

**First, split and set a baseline: always predict the average duration of the training set.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-43:9` — “Spark ML wants all features in one vector column (VectorAssembler). First, split and set a baseline: always predict the average duration of the training set.”

### Spark ml long taxi ride

**The 2015 data is the old TLC schema: GPS coordinates instead of zone IDs.**
Confidence 0.72 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-29:4` — “The task: predict the trip duration in minutes at the moment the passenger gets in. The 2015 data is the old TLC schema: GPS coordinates instead of zone IDs.”

### Sparksession entry point

**On a cluster only master changes – the rest of the code stays the same.**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-5:2` — “local[*] means: driver and executors live in one JVM on this machine and use all its cores. On a cluster only master changes – the rest of the code stays the same.”

### Task add zone names join

**The location IDs mean nothing to a human.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-24:2` — “The location IDs mean nothing to a human. The zone lookup (265 rows) has LocationID, Borough, Zone.”

### Task c plan challenge fast

**Add an orderBy to the joined result and run explain() again.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-34:5` — “Add an orderBy to the joined result and run explain() again.”

### Task trips start

**Show the top 15 and find the Exchange in explain().**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-22:2` — “Your turn (5 min): starting from clean, compute per PULocationID the number of trips (trip_count) and the average fare rounded to 2 decimals (avg_fare), sorted by trip_count descending.…”

### Transformations vs actions important concept

**A transformation describes what to do but does not start execution.**
Confidence 0.64 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-11:5` — “> Rule: Spark is lazy. A transformation describes what to do but does not start execution. Only an action sends the job to the Executors.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 21 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 13 | 2026-10-28 |
| `session-06/kafka_data.py` | code | 0.80 | 1 | 2026-11-11 |

## Related Pages

- [[spark-architecture|Spark Architecture]] (20 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (19 shared entities)
- [[unfiled|Unfiled Observations]] (9 shared entities)
- [[data-formats|File Formats]] (5 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (5 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (4 shared entities)

## Open Questions

18 prompts from the material are collected in [[questions/spark-execution|Questions: Spark Execution Model]].
- In the Markdown cell below the code, explain: where does the shuffle happen and why?
- Will the plan contain an Exchange (a shuffle)?
- Then look at explain(): which join strategy did Spark choose – and why?

## Timeline

- 2026-11-25: new_claim on `claim_644c31a0`
- 2026-11-25: evidence_attached on `claim_644c31a0` (0.69 → 0.69)
- 2026-11-25: new_claim on `claim_2af15809`
- 2026-11-25: new_claim on `claim_be79fd03`
- 2026-11-25: new_claim on `claim_d2161a39`
- 2026-11-25: new_claim on `claim_470d4ee1`
- 2026-11-25: new_claim on `claim_f75e0e93`
- 2026-11-25: new_claim on `claim_f50f0fd6`
