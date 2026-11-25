---
title: shuffle
type: entity
entity_id: ent_shuffle
entity_type: concept
claim_ids:
  - claim_0718eab9
  - claim_531b3248
  - claim_dce6d3cd
  - claim_66d2b535
  - claim_839451a1
  - claim_644c31a0
  - claim_2af15809
  - claim_be79fd03
  - claim_2536bd6c
  - claim_e25a0f01
confidence: 0.709
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_47132aab
  - src_96e79681
  - src_b3356305
---

# shuffle

Type: concept. Mentioned in 10 claims across 3 topics.
Aliases: shuffles, shuffle operation.

## Claims

- **In the plan: Exchange — Meaning: a shuffle: rows move between partitions.** Confidence 0.84 · [[spark-execution|Spark Execution Model]]
- **In the plan: BroadcastHashJoin — Meaning: small table copied to every executor – no shuffle of the big table.** Confidence 0.84 · [[spark-execution|Spark Execution Model]]
- **Part: 1 · Spark fundamentals — What you do: DataFrames, transformations vs. actions, plans, shuffles, joins; Data: NYC taxi January 2024, Parquet (~3 M trips).** Confidence 0.73 · [[course-dataset|NYC Yellow Taxi Dataset]]
- **Folder: session-02/ — Topic: Apache Spark fundamentals: SparkSession, transformations vs. actions, plans, shuffles, joins; Runs on: dev container or a laptop with Java 17.** Confidence 0.72 · [[spark-architecture|Spark Architecture]]
- **Exchange in between — this is the shuffle. After the partial aggregation, all rows with the same PULocationID must land on the same partition before the final merge can happen.** Confidence 0.72 · [[spark-execution|Spark Execution Model]]
- **Type: Narrow — Definition: Each output partition depends on exactly one input partition; Examples: filter, select, withColumn, map; Shuffle?: No.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Symbol: SortMergeJoin — Meaning: Large-large join with shuffle and sort.** Confidence 0.69 · [[spark-execution|Spark Execution Model]]
- **Stages – each job is divided into stages; stage boundaries are created by shuffles.** Confidence 0.66 · [[spark-architecture|Spark Architecture]]
- **HashAggregate appears twice: once for a partial aggregation (per partition, before shuffle) and once for a final merge (after shuffle). This is a standard Spark optimisation.** Confidence 0.66 · [[spark-execution|Spark Execution Model]]
- **Read a physical execution plan and identify where a shuffle occurs.** Confidence 0.61 · [[spark-execution|Spark Execution Model]]

## Related Entities

- [[partition|partition]] (4)
- [[spark|Spark]] (3)
- [[action|action]] (2)
- [[transformation|transformation]] (2)
- [[dev_container|Dev container]] (1)
- [[parquet|Parquet]] (1)
- [[spark_job|Spark job]] (1)
- [[spark_stage|Spark stage]] (1)
- [[executor|executor]] (1)
- [[topic|topic]] (1)
