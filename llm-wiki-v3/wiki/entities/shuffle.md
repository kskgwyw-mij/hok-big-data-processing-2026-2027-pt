---
title: shuffle
type: entity
entity_id: ent_shuffle
entity_type: concept
claim_ids:
  - claim_342a7d6c
  - claim_531b3248
  - claim_dce6d3cd
  - claim_66d2b535
  - claim_d897e3e0
  - claim_839451a1
  - claim_644c31a0
  - claim_2af15809
  - claim_be79fd03
  - claim_2536bd6c
  - claim_4560b3b1
  - claim_cc6d1116
  - claim_9b8db10e
  - claim_ab6cb6ae
  - claim_b930c4cb
  - claim_533151da
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1cebb3bb
  - src_47132aab
  - src_59b6ded4
  - src_68fcf2b9
  - src_96e79681
  - src_b3356305
---

# shuffle

Type: concept. Mentioned in 16 claims across 3 topics.
Aliases: shuffles, shuffle operation.

## Claims

- **In the plan: Exchange — Meaning: a shuffle: rows move between partitions.** Confidence 0.84 · [[spark-execution|Spark Execution Model]]
- **Part: 1 · Spark fundamentals — What you do: DataFrames, transformations vs. actions, plans, shuffles, joins; Data: NYC taxi January 2024, Parquet (~3 M trips).** Confidence 0.84 · [[spark-execution|Spark Execution Model]]
- **3 Spark performance: shuffles, joins, skew Volume.** Confidence 0.74 · [[spark-execution|Spark Execution Model]]
- **Folder: session-02/ — Topic: Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins; Runs on: dev container or a laptop with Java 17.** Confidence 0.72 · [[spark-execution|Spark Execution Model]]
- **Exchange in between — this is the shuffle. After the partial aggregation, all rows with the same PULocationID must land on the same partition before the final merge can happen.** Confidence 0.72 · [[spark-execution|Spark Execution Model]]
- **Two shuffles – expensive, but always works.** Confidence 0.72 · [[spark-execution|Spark Execution Model]]
- **» Step 1: Input Phase » Record Reader extracts raw data and converts it into key-value pairs. » Step 2: Map Phase » User-defined Map function processes key-value pairs to generate intermediate keys. » Step 3: Intermediate Keys & Combiner (Optional) » Combiner groups and summarizes data locally before sending it to reducers. » Step 4: Shuffle & Sort » Shuffling: Groups the same keys together. » Sorting: Orders the grouped data for efficient processing. » Step 5: Reduce Phase » Runs Reducer Function on grouped key-value pairs. » Produces final key-value outputs. » Step 6: Output Phase » Output Formatter converts and writes final results to the file system.** Confidence 0.70 · [[mapreduce-model|MapReduce]]
- **No network, Every output needs data from all inputs: shuffle = Exchange in same stage. the plan, new stage.** Confidence 0.70 · [[spark-execution|Spark Execution Model]]
- **» Key Components: » Map Phase: Splits and maps data. » Reduce Phase: Shuffles and aggregates data. » Works with Hadoop Distributed File System (HDFS). » Supports multiple languages: Java, Python, C++.** Confidence 0.70 · [[mapreduce-model|MapReduce]]
- **Type: Narrow — Definition: Each output partition depends on exactly one input partition; Examples: filter, select, withColumn, map; Shuffle?: No.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Symbol: SortMergeJoin — Meaning: Large-large join with shuffle and sort.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Symbol: BroadcastHashJoin — Meaning: Small table broadcast to all executors (no shuffle).** Confidence 0.69 · [[spark-architecture|Spark Architecture]]
- **In the plan: BroadcastHashJoin — Meaning: small table copied to every executor – no shuffle of the big table.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Stages – each job is divided into stages; stage boundaries are created by shuffles.** Confidence 0.66 · [[spark-architecture|Spark Architecture]]
- **HashAggregate appears twice: once for a partial aggregation (per partition, before shuffle) and once for a final merge (after shuffle). This is a standard Spark optimisation.** Confidence 0.66 · [[spark-execution|Spark Execution Model]]
- **Read a physical execution plan and identify where a shuffle occurs.** Confidence 0.61 · [[spark-execution|Spark Execution Model]]

## Related Entities

- [[spark|Spark]] (4)
- [[partition|partition]] (4)
- [[spark_stage|Spark stage]] (2)
- [[action|action]] (2)
- [[executor|executor]] (2)
- [[transformation|transformation]] (2)
- [[dev_container|Dev container]] (1)
- [[hdfs|HDFS]] (1)
- [[parquet|Parquet]] (1)
- [[spark_job|Spark job]] (1)
