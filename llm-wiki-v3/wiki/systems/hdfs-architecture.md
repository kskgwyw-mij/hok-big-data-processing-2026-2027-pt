---
title: HDFS
type: systems
topic: hdfs.architecture
entity_ids:
  - ent_kafka
  - ent_partition
  - ent_hdfs
  - ent_jupyter
claim_ids:
  - claim_f71b3b42
  - claim_9f38d443
  - claim_dc16bc08
  - claim_6a889182
confidence: 0.64
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_96e79681
  - src_cecf99ea
review_required: false
---

# HDFS

Rendered from 4 claims and 3 sources. Median confidence 0.64; 3 active, 0 disputed, 0 superseded.

## Current Understanding

### Kafka lab exam preparation

**File: 01_kafka_cli.md — What: Block 1 – step by step, both routes.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:131` — “01_kafka_cli.md | Block 1 – step by step, both routes”

**File: 02_kafka_python.ipynb — What: Block 2 – notebook.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/README.md:132` — “02_kafka_python.ipynb | Block 2 – notebook”

### Reading data parquet dataframe

**Distributed across partitions (files, HDFS blocks, …).**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-6:6` — “- Distributed across partitions (files, HDFS blocks, …).”

### Turn partitions key

**The Java CLI from Block 1 and this Python client use the same hash function (murmur2), so Tirol lands in the same partition from both.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-11:1` — “Each key appears in exactly one partition: partition = hash(key) mod 3. Several keys share a partition – that is fine. The Java CLI from Block 1 and this Python client use the same hash…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 1 | 2026-11-11 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-06/README.md` | readme | 0.85 | 2 | 2026-11-11 |

## Related Pages

- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (5 shared entities)
- [[kafka-cluster|Kafka Cluster]] (4 shared entities)
- [[kafka-log|Kafka Log]] (4 shared entities)
- [[kafka-producers|Kafka Producers]] (4 shared entities)
- [[unfiled|Unfiled Observations]] (4 shared entities)
- [[course-exam|Exam]] (3 shared entities)

## Open Questions

6 prompts from the material are collected in [[questions/hdfs-architecture|Questions: HDFS]].
- What happens if you ask for replication factor 2?
- Question: in a cluster with 3 brokers and replication factor 3, what would Replicas and Isr look like?
- 3.1 (3 P) A 150 MB file is stored in HDFS with 64 MB blocks and replication factor 3. How many blocks, and how many block copies are…

## Timeline

- 2026-11-25: new_claim on `claim_f71b3b42`
- 2026-11-25: new_claim on `claim_9f38d443`
- 2026-11-25: new_claim on `claim_dc16bc08`
- 2026-11-25: new_claim on `claim_6a889182`
