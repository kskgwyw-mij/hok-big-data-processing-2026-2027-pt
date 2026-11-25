---
title: Spark job
type: entity
entity_id: ent_spark_job
entity_type: concept
claim_ids:
  - claim_4081509c
  - claim_c958073c
  - claim_cefb5f5e
  - claim_1ba61905
  - claim_95fe6516
  - claim_2536bd6c
  - claim_19133618
confidence: 0.629
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_47132aab
  - src_6e2e5684
  - src_96e79681
  - src_9e752903
---

# Spark job

Type: concept. Mentioned in 7 claims across 4 topics.
Aliases: job, jobs.

## Claims

- **In the comparison table, Runs as: DuckDB: library in your process, SQLite: library in your process, PostgreSQL: server, Spark: cluster (or local).** Confidence 0.69 · [[data-duckdb|DuckDB]]
- **Spark 4 runs in ANSI mode by default: a division by zero stops the job instead of returning NULL. try_divide returns NULL instead.** Confidence 0.67 · [[spark-architecture|Spark Architecture]]
- **Stages – each job is divided into stages; stage boundaries are created by shuffles.** Confidence 0.66 · [[spark-architecture|Spark Architecture]]
- **The same CPU-bound task as in the warm-up: 4 jobs, first one after another (serial), then in 4 threads.** Confidence 0.63 · [[python-execution|Python Execution Model]]
- **Many readers or one writer – fine for one analyst or one batch job, not for 50 dashboard users writing at once.** Confidence 0.63 · [[data-duckdb|DuckDB]]
- **Predict: which of the lines A–D starts a Spark job? python t1 = df.filter(F.col("trip_distance") > 1.0) # A t2 = t1.select("PULocationID", "trip_distance") # B t3 = t2.groupBy("PULocationID").count() # C t3.show(10) # D.** Confidence 0.63 · [[course-dataset|NYC Yellow Taxi Dataset]]
- **We compute the trip duration and count problems in a single pass (one Spark job, not six).** Confidence 0.63 · [[course-dataset|NYC Yellow Taxi Dataset]]

## Related Entities

- [[spark|Spark]] (2)
- [[duckdb|DuckDB]] (1)
- [[spark_stage|Spark stage]] (1)
- [[spark_task|Spark task]] (1)
- [[pip|pip]] (1)
- [[shuffle|shuffle]] (1)
