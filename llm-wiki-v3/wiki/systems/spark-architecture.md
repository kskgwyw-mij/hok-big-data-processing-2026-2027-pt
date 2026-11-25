---
title: Spark Architecture
type: systems
topic: spark.architecture
entity_ids:
  - ent_spark
  - ent_executor
  - ent_spark_task
  - ent_driver
  - ent_spark_job
  - ent_spark_stage
  - ent_cluster_manager
  - ent_shuffle
  - ent_spark_ui
  - ent_action
  - ent_ansi
  - ent_catalyst_optimizer
claim_ids:
  - claim_cefb5f5e
  - claim_fcfd2597
  - claim_e5ed99e6
  - claim_ddf6f32c
  - claim_0326b6f6
  - claim_d2f03bde
  - claim_d16514b4
  - claim_5697da8b
  - claim_ae7e7760
  - claim_30456a9a
  - claim_d897e3e0
  - claim_710695c9
  - claim_f8b8c074
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
  - claim_8808edb0
  - claim_2536bd6c
  - claim_5b33a9f2
  - claim_7482afab
  - claim_f78bd88b
  - claim_40b95771
  - claim_ce4e1a56
  - claim_721dbfc5
  - claim_676794c6
  - claim_e5dbfb2e
  - claim_f9980322
  - claim_f132d7b8
  - claim_946f39f2
confidence: 0.629
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_47132aab
  - src_59b6ded4
  - src_68fcf2b9
  - src_96e79681
review_required: false
---

# Spark Architecture

Rendered from 49 claims and 4 sources. Median confidence 0.63; 35 active, 0 disputed, 0 superseded.

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

### Reading execution plan

**Symbol: HashAggregate — Meaning: Partial or final aggregation.**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:19` — “HashAggregate | Partial or final aggregation”

**Symbol: BroadcastHashJoin — Meaning: Small table broadcast to all executors (no shuffle).**
Confidence 0.69 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:21` — “BroadcastHashJoin | Small table broadcast to all executors (no shuffle)”

**Every DataFrame has a plan. df.explain() shows you how Spark intends to execute a query.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-21:5` — “Every DataFrame has a plan. df.explain() shows you how Spark intends to execute a query.”

### Notebook

**On the slides you saw Spark's architecture: Driver, Executors, SparkSession, RDDs, DataFrames, and the Catalyst Optimizer.**
Confidence 0.63 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:10` — “On the slides you saw Spark's architecture: Driver, Executors, SparkSession, RDDs, DataFrames, and the Catalyst Optimizer. Today you will run all of it.”

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

### Task core everyone

**Show the top 15 results.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-26:26` — “4. Show the top 15 results.”

**The Exchange node in the plan shows.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-28:5` — “- The Exchange node in the plan shows: ...”

### Cleaning ansi mode

**Spark 4 runs in ANSI mode by default: a division by zero stops the job instead of returning NULL. try_divide returns NULL instead.**
Confidence 0.67 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-35:2` — “Spark 4 runs in ANSI mode by default: a division by zero stops the job instead of returning NULL. try_divide returns NULL instead.”

### Core dataframe operations

**--- 4.3 withColumn: create or replace a column --- Add a column with the fare per mile.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-18` — “--- 4.3 withColumn: create or replace a column --- Add a column with the fare per mile”

### Executor broadcasthashjoin sortmergejoin small

**BroadcastHashJoin SortMergeJoin The small table (265 zones) is copied to every executor.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p33:5` — “BroadcastHashJoin SortMergeJoin The small table (265 zones) is copied to every executor. Both tables are large: both are shuffled by the join key and sorted. Each task looks up its trips…”

### Executor core

**Core core core core Executor Executor Executor machine 1 machine 2 machine 3 executor threads run the tasks.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p30:11` — “core core core core Executor Executor Executor machine 1 machine 2 machine 3 executor threads run the tasks”

### Executor driver executors laptop

**Driver and executors: laptop vs. cluster.**
Confidence 0.69 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p30:1` — “Driver and executors: laptop vs. cluster”

### Housekeeping stopping spark

**Always stop the SparkSession when you are done.**
Confidence 0.70 · active · 1 source · when: when you are done
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-41:5` — “Always stop the SparkSession when you are done. This releases the JVM memory and avoids port conflicts if you restart the notebook.”

### Note collect topandas

**Quick bar chart of the top 20 pickup locations.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-40` — “Quick bar chart of the top 20 pickup locations”

### Pre flight checklist anything else

**Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.**
Confidence 0.65 · active · 1 source · when: before starting Spark
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-0:25` — “2. Check available memory – run the cell below (works on Linux, macOS and Windows). You need ≥ 4.5 GB available before starting Spark.”

### Spark represents connection introduced

**» Represents the connection to a » Introduced in Spark 2.0 Spark cluster » Unified entry point for interacting with Spark » Coordinates task execution across the cluster » Combines functionalities of SparkContext, SQLContext, » Entry point in earlier versions of HiveContext, and Streaming Spark (1.x) Context » Supports multiple programming languages (Scala, Java, Python, R).**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p111:5` — “» Represents the connection to a » Introduced in Spark 2.0 Spark cluster » Unified entry point for interacting with Spark » Coordinates task execution across the cluster » Combines…”

### Spark requires sqlcontext yes

**No (requires SQLContext) Yes (native support) Supports DataSets No Yes Preferred Approach Deprecated Use SparkSession.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p120:8` — “Entry Point SparkContext SparkSession Supports RDDs? Yes Yes (via .rdd) Supports DataFrames? No (requires SQLContext) Yes (native support) Supports DataSets No Yes Preferred Approach…”

### Spark sparkcontext sparksessions different

**» SparkContext and SparkSessions have different purposes and functionalities » SparkContext is low-level, while SparkSession is higher-level » SparkSession simplifies interaction and supports structured data processing » SparkContext is still supported for backward compatibility » SparkSession is the recommended entry point for Spark applications » Why was SparkSession introduced? » It simplifies the API by combining SQLContext, HiveContext, and SparkContext into one object. » It supports both RDDs and DataFrames in a more user-friendly way. » SparkContext is still available inside SparkSession, but you should use SparkSession instead for modern Spark applications.**
Confidence 0.81 · active · 1 source · when: while SparkSession is higher-level » SparkSession simplifies interaction an; for modern Spark applications
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p115:3` — “» SparkContext and SparkSessions have different purposes and functionalities » SparkContext is low-level, while SparkSession is higher-level » SparkSession simplifies interaction and…”

### Spark ui kaggle cannot

**Kaggle cannot show the Spark UI – I'll show it on my laptop.**
Confidence 0.72 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p39:15` — “Not finished? Sections 2.9–2.12 are fine as homework. Kaggle cannot show the Spark UI – I'll show it on my laptop.”

### Sparksession entry point

**Local[*] means: driver and executors live in one JVM on this machine and use all its cores.**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-5:2` — “local[*] means: driver and executors live in one JVM on this machine and use all its cores. On a cluster only master changes – the rest of the code stays the same.”

### Transformations vs actions important concept

**Only an action sends the job to the Executors.**
Confidence 0.65 · active · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-11:5` — “> Rule: Spark is lazy. A transformation describes what to do but does not start execution. Only an action sends the job to the Executors.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 2 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 4 | 2026-11-25 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 3 | 2026-11-25 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 40 | 2026-10-28 |

## Related Pages

- [[spark-execution|Spark Execution Model]] (40 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (32 shared entities)
- [[unfiled|Unfiled Observations]] (27 shared entities)
- [[data-formats|File Formats]] (25 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (24 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (23 shared entities)

## Open Questions

15 prompts from the material are collected in [[questions/spark-architecture|Questions: Spark Architecture]].
- B6 (3 P) Explain the roles of the driver, the executors and the cluster manager in a Spark application.
- B8 (2 P) In Spark, what is a task, and at which kind of operation does a new stage begin?
- Entry Point SparkContext SparkSession Supports RDDs?

## Timeline

- 2026-11-25: new_claim on `claim_40b95771`
- 2026-11-25: new_claim on `claim_ce4e1a56`
- 2026-11-25: new_claim on `claim_721dbfc5`
- 2026-11-25: new_claim on `claim_676794c6`
- 2026-11-25: new_claim on `claim_e5dbfb2e`
- 2026-11-25: new_claim on `claim_f9980322`
- 2026-11-25: new_claim on `claim_f132d7b8`
- 2026-11-25: new_claim on `claim_946f39f2`
