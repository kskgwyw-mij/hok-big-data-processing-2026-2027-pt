---
title: Spark Architecture
type: systems
topic: spark.architecture
entity_ids:
  - ent_spark
  - ent_driver
  - ent_spark_task
  - ent_action
  - ent_executor
  - ent_spark_stage
  - ent_transformation
  - ent_cluster_manager
  - ent_python
  - ent_shuffle
  - ent_spark_job
  - ent_ansi
claim_ids:
  - claim_99f6b8ba
  - claim_cefb5f5e
  - claim_fcfd2597
  - claim_e5ed99e6
  - claim_d679399f
  - claim_ddf6f32c
  - claim_0326b6f6
  - claim_2b27b38d
  - claim_d2f03bde
  - claim_5697da8b
  - claim_068c3f25
  - claim_68812377
  - claim_ae7e7760
  - claim_fec4a40d
  - claim_30456a9a
  - claim_710695c9
  - claim_f8b8c074
  - claim_939d0c3c
  - claim_9b69a920
  - claim_c7ba8d4b
  - claim_221be94f
  - claim_604f9131
  - claim_90b08ded
  - claim_377499bc
  - claim_9296b499
  - claim_6ed7ace9
  - claim_ec63a38f
  - claim_6e4a6518
  - claim_ef3a846d
  - claim_90b5a80a
  - claim_b4eb6118
  - claim_bd9835eb
  - claim_abd51c80
  - claim_0ab9d2bf
  - claim_da6151f2
  - claim_56f7ed81
  - claim_63c78bc1
  - claim_451b6101
  - claim_9a7b91be
  - claim_5997c77e
  - claim_7b9ee7a4
  - claim_79744808
  - claim_8808edb0
  - claim_2536bd6c
  - claim_5b33a9f2
  - claim_7482afab
  - claim_f78bd88b
  - claim_40b95771
  - claim_e25a0f01
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_47132aab
  - src_96e79681
  - src_b3356305
review_required: false
---

# Spark Architecture

Rendered from 49 claims and 3 sources. Median confidence 0.63; 32 active, 0 disputed, 0 superseded.

## Current Understanding

### Predict run

**Stages – each job is divided into stages; stage boundaries are created by shuffles.**
Confidence 0.66 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-5:5` — “- Stages – each job is divided into stages; stage boundaries are created by shuffles.”

**Q4 – Look at the by_location DataFrame above (filter → groupBy → agg).**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:26` — “> Q4 – Look at the by_location DataFrame above (filter → groupBy → agg). > Do you expect to see an Exchange node in the plan? Why or why not? > > Your answer: > > ...”

**Q3 – Read the four lines below before running the cell.**
Confidence 0.63 · active · 1 source · when: before running the cell
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-11:16` — “> Q3 – Read the four lines below before running the cell. Which lines start a Spark job? Which ones are free? > > python > t1 = df.filter(F.col("trip_distance") > 1.0) # line A > t2 =…”

**Tasks – the smallest unit of work, one per partition per stage.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-5:6` — “- Tasks – the smallest unit of work, one per partition per stage.”

**Click on it — you will see how many stages it has and how many tasks ran.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-13:1` — “Check the Spark UI now. You should see one completed job. Click on it — you will see how many stages it has and how many tasks ran.”

**It will fill up as you run actions below.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-5:10` — “Right now the UI is mostly empty. It will fill up as you run actions below.”

**Open http://localhost:4040 in a new browser tab.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-5:3` — “Open http://localhost:4040 in a new browser tab. You will see:”

**Write your answer here (double-click to edit).**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-3:18` — “> Q1 – Before running the cell below: What does calling SparkSession.builder...getOrCreate() actually do? Does it read any data? Does it start any computation? > > Write your answer here…”

**Environment – all config values (useful for debugging).**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-5:8` — “- Environment – all config values (useful for debugging).”

### Group work nyc taxi analysis

**Role: Reviewer (4 people) — Responsibility: Challenges assumptions, checks edge cases.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:12` — “Reviewer (4 people) | Challenges assumptions, checks edge cases”

**Role: Driver — Responsibility: Types and runs the code.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:9` — “Driver | Types and runs the code”

**Role: Navigator — Responsibility: Reads the task, checks logic, predicts results.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:10` — “Navigator | Reads the task, checks logic, predicts results”

**Role: Explainer — Responsibility: Writes the explanation in Markdown cells.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:11` — “Explainer | Writes the explanation in Markdown cells”

**Work in groups of 3–4 people.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:5` — “Work in groups of 3–4 people. Rotate roles every 20 minutes:”

### Sparksession entry point spark

**Component: Driver — Role: Your Python process. Runs your code, plans queries, coordinates execution.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-3:9` — “Driver | Your Python process. Runs your code, plans queries, coordinates execution.”

**Component: SparkSession — Role: The single entry point to all Spark functionality since Spark 2.0.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-3:12` — “SparkSession | The single entry point to all Spark functionality since Spark 2.0.”

**Component: Cluster Manager — Role: Allocates resources (here: local mode – no real cluster).**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-3:10` — “Cluster Manager | Allocates resources (here: local mode – no real cluster).”

**Component: Executors — Role: JVM processes that read data and execute tasks.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-3:11` — “Executors | JVM processes that read data and execute tasks.”

**In local mode (local[*]), the Driver and Executors all run inside one JVM on your machine.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-3:14` — “In local mode (local[*]), the Driver and Executors all run inside one JVM on your machine. You get the full API — the only difference from a real cluster is that there is no network…”

### Task extension add location names

**The result of Task A shows only numeric location IDs.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-29:5` — “The result of Task A shows only numeric location IDs. Join the taxi zone lookup table to add zone names.”

**Join top_locations with zones to add Borough and Zone.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-29:10` — “3. Join top_locations with zones to add Borough and Zone.”

**Task B – join and show Hint: the zone table is small (~265 rows). What join strategy do you expect Spark to pick? YOUR CODE.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-31` — “Task B – join and show Hint: the zone table is small (~265 rows). What join strategy do you expect Spark to pick? YOUR CODE”

**The threshold for automatic broadcasting is controlled by.**
Confidence 0.56 · candidate · 1 source · when: for automatic broadcasting is controlled by
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-33:5` — “- The threshold for automatic broadcasting is controlled by: ...”

**Spark chose a [BroadcastHashJoin / SortMergeJoin] because.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-33:3` — “- Spark chose a [BroadcastHashJoin / SortMergeJoin] because: ...”

### Core dataframe operations

**--- 4.2 filter: keep only valid trips --- Bad rows: negative fares, zero distance, zero or null passengers.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-17` — “--- 4.2 filter: keep only valid trips --- Bad rows: negative fares, zero distance, zero or null passengers”

**--- 4.3 withColumn: create or replace a column --- Add a column with the fare per mile.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-18` — “--- 4.3 withColumn: create or replace a column --- Add a column with the fare per mile”

**--- 4.4 groupBy + agg: aggregate --- Count trips and compute average fare per pickup location.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-19` — “--- 4.4 groupBy + agg: aggregate --- Count trips and compute average fare per pickup location”

### Exit ticket individual ai

**The plan shows a BroadcastHashJoin instead of a SortMergeJoin.**
Confidence 0.62 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-43:58` — “You join the trip data (3 million rows) with the taxi zone lookup table (265 rows). The plan shows a BroadcastHashJoin instead of a SortMergeJoin.”

**Explain the actual behaviour and why it matters for performance.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-43:48` — “Does this mean Spark only read 10 rows from the Parquet file? Explain the actual behaviour and why it matters for performance.”

**Explain what actually happens and when computation starts.**
Confidence 0.58 · candidate · 1 source · when: when computation starts
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-43:19` — “She says: "Three lines of code, so Spark ran three operations immediately." Is she correct? Explain what actually happens and when computation starts.”

### Notebook

**On the slides you saw Spark's architecture: Driver, Executors, SparkSession, RDDs, DataFrames, and the Catalyst Optimizer.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:10` — “On the slides you saw Spark's architecture: Driver, Executors, SparkSession, RDDs, DataFrames, and the Catalyst Optimizer. Today you will run all of it.”

**Distinguish transformations from actions and predict when computation starts.**
Confidence 0.61 · active · 1 source · when: when computation starts
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:14` — “- Distinguish transformations from actions and predict when computation starts.”

**Apply select, filter, withColumn, groupBy, agg, orderBy.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:16` — “- Apply select, filter, withColumn, groupBy, agg, orderBy.”

### Reading data parquet dataframe

**A DataFrame is Spark's primary data abstraction since Spark 2.0.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-6:5` — “A DataFrame is Spark's primary data abstraction since Spark 2.0. It is:”

**Typed with a schema known to the Driver at planning time.**
Confidence 0.61 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-6:7` — “- Typed with a schema known to the Driver at planning time.”

### Reading execution plan

**Symbol: HashAggregate — Meaning: Partial or final aggregation.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:19` — “HashAggregate | Partial or final aggregation”

**Every DataFrame has a plan. df.explain() shows you how Spark intends to execute a query.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:5` — “Every DataFrame has a plan. df.explain() shows you how Spark intends to execute a query.”

### Task core everyone

**Show the top 15 results.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:26` — “4. Show the top 15 results.”

**The Exchange node in the plan shows.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-28:5` — “- The Exchange node in the plan shows: ...”

### Chaining transformations

**In practice, transformations are chained with the dot notation.**
Confidence 0.64 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-13:7` — “In practice, transformations are chained with the dot notation. Spark builds one combined logical plan and optimises it.”

### Cleaning ansi mode

**Spark 4 runs in ANSI mode by default: a division by zero stops the job instead of returning NULL. try_divide returns NULL instead.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-35:2` — “Spark 4 runs in ANSI mode by default: a division by zero stops the job instead of returning NULL. try_divide returns NULL instead.”

### Collect topandas small results

**Both actions bring all rows to the driver.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-27:4` — “Both actions bring all rows to the driver. On an aggregated result that's fine; on the raw trips it can crash the driver.”

### Housekeeping stopping spark

**Always stop the SparkSession when you are done.**
Confidence 0.70 · active · 1 source · when: when you are done
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-41:5` — “Always stop the SparkSession when you are done. This releases the JVM memory and avoids port conflicts if you restart the notebook.”

### Narrow vs wide transformations

**Stage boundaries in Spark are always at wide transformations.**
Confidence 0.74 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-24:15` — “Stage boundaries in Spark are always at wide transformations.”

### Note collect topandas

**Quick bar chart of the top 20 pickup locations.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-40` — “Quick bar chart of the top 20 pickup locations”

### Pre flight checklist anything else

**Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.**
Confidence 0.65 · active · 1 source · when: before starting Spark
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:25` — “2. Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.”

### Sessions folders

**Folder: session-02/ — Topic: Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins; Runs on: dev container or a laptop with Java 17.**
Confidence 0.72 · active · 1 source
Evidence: `README.md:130` — “session-02/ | Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins | dev container or a laptop with Java 17”

### Sparksession entry point

**Local[*] means: driver and executors live in one JVM on this machine and use all its cores.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-5:2` — “local[*] means: driver and executors live in one JVM on this machine and use all its cores. On a cluster only master changes – the rest of the code stays the same.”

### Transformations vs actions important concept

**In the comparison table, Return value: Transformations: A new DataFrame, Actions: A Python value or side-effect.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-11:12` — “Cost | Nearly free (just graph nodes) | Executes the full plan”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 3 | 2026-10-28 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 45 | 2026-10-28 |
| `README.md` | readme | 0.85 | 1 | 2026-11-11 |

## Related Pages

- [[course-dataset|NYC Yellow Taxi Dataset]] (31 shared entities)
- [[spark-execution|Spark Execution Model]] (27 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (19 shared entities)
- [[python-execution|Python Execution Model]] (19 shared entities)
- [[course-setup|Course Setup]] (18 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (17 shared entities)

## Open Questions

14 prompts from the material are collected in [[questions/spark-architecture|Questions: Spark Architecture]].
- Which lines start a Spark job?
- Do you expect to see an Exchange node in the plan?
- Run explain() on the joined DataFrame. What kind of join does Spark choose? Why?

## Timeline

- 2026-11-25: new_claim on `claim_79744808`
- 2026-11-25: new_claim on `claim_8808edb0`
- 2026-11-25: new_claim on `claim_2536bd6c`
- 2026-11-25: new_claim on `claim_5b33a9f2`
- 2026-11-25: new_claim on `claim_7482afab`
- 2026-11-25: new_claim on `claim_f78bd88b`
- 2026-11-25: new_claim on `claim_40b95771`
- 2026-11-25: new_claim on `claim_e25a0f01`
