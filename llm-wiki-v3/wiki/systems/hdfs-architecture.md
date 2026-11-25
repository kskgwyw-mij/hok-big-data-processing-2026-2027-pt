---
title: HDFS
type: systems
topic: hdfs.architecture
entity_ids:
  - ent_kafka
  - ent_hdfs
  - ent_namenode
  - ent_partition
  - ent_atomic_append
  - ent_broker
  - ent_chunk_servers
  - ent_commodity_computers
  - ent_data_replication
  - ent_hadoop_file_system
  - ent_highly_fault_tolerant
  - ent_jupyter
claim_ids:
  - claim_f71b3b42
  - claim_9f38d443
  - claim_dc16bc08
  - claim_6a889182
  - claim_9ac05dad
  - claim_36fded37
  - claim_b719bf4b
  - claim_32ae5179
  - claim_4161519a
  - claim_ee2e70d3
  - claim_fba178e0
  - claim_77699260
  - claim_6908d589
  - claim_6ce918d7
  - claim_633a9dc0
  - claim_c6cd6bf4
confidence: 0.696
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_68fcf2b9
  - src_799c8bd7
  - src_8615b91f
  - src_96e79681
  - src_cecf99ea
  - src_e258bafb
  - src_fc0bfe80
review_required: false
---

# HDFS

Rendered from 16 claims and 7 sources. Median confidence 0.70; 15 active, 0 disputed, 0 superseded.

## Current Understanding

### Kafka lab exam preparation

**File: 01_kafka_cli.md — What: Block 1 – step by step, both routes.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:131` — “01_kafka_cli.md | Block 1 – step by step, both routes”

**File: 02_kafka_python.ipynb — What: Block 2 – notebook.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/README.md:132` — “02_kafka_python.ipynb | Block 2 – notebook”

### Big data processing mock exam

**Part: B — Topic: Spark architecture, HDFS, MapReduce; Points: 16.**
Confidence 0.80 · active · 1 source
Evidence: `raw/04_mock_exam.md:12` — “B | Spark architecture, HDFS, MapReduce | 16”

### Hdfs hadoop file system

**Hadoop File System (HDFS).**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p57:1` — “Hadoop Distributed File Storage (HDFS)”

### Kafka python kafka python ipynb

**10:35 Block 2 · Kafka from Python 02_kafka_python.ipynb LAB.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p3:21` — “10:35 Block 2 · Kafka from Python 02_kafka_python.ipynb LAB”

### Kafka python object

**Block 2 – From Python object to Kafka bytes.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p94:1` — “Block 2 – From Python object to Kafka bytes”

### Key features purpose scalable

**» Purpose: Scalable distributed file system for data-intensive applications at Google » Key Features: » Runs on inexpensive commodity hardware. » High fault tolerance and performance through data replication. » Optimized for large files (several GBs) and sequential writes. » Architecture: » Master Node: Manages metadata and chunk placement decisions. » Chunk Servers: Store file blocks (chunks) of 64 MB each. » Clients: Communicate directly with chunk servers for data access. » Innovations: » Atomic Append: Enables consistent appends for concurrent clients. » Snapshots: Efficient copying of files and directory trees. » Results: » Scales to thousands of servers and hundreds of terabytes of storage. » High availability through rapid recovery and data replication.**
Confidence 0.74 · active · 1 source · when: for data -intensive applications at Google » Key Features: » Runs on inexpensiv; for large files (several GBs) and sequential writes
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p52:3` — “» Purpose: Scalable distributed file system for data-intensive applications at Google » Key Features: » Runs on inexpensive commodity hardware. » High fault tolerance and performance…”

### Laptop cannot run route

**Everything in Blocks 3 and 4 needs only paper.**
Confidence 0.69 · active · 1 source
Evidence: `session-06/README.md:84` — “No problem: pair up with a neighbour whose broker runs. You type on their laptop in Block 1 and run consumer.py on theirs in Block 2. Everything in Blocks 3 and 4 needs only paper.…”

### Namenode master maintains

**» Master / NameNode: maintains and manages the DataNodes & stores meta data.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p69:3` — “» Master / NameNode: maintains and manages the DataNodes & stores meta data”

### Namenode signal datanodes sind

**» Signal: DataNodes sind continuously signal to NameNode with status.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p69:9` — “» Signal: DataNodes sind continuously signal to NameNode with status.”

### Namenode standby modern

**Namenode Standby Modern Architecture.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p68:1` — “Namenode Standby Modern Architecture”

### Provides distributed storage

**» Provides Distributed Storage » Implemented on commodity hardware » 100 Servers Enterprise Servers = 10k USD per TB » 100 Commodity Computers 1k USD Per TB » Provides Data Security » No high-end backup available » Data Replication » Highly Fault Tolerant » Damaged machine can easily be switched out.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p70:3` — “» Provides Distributed Storage » Implemented on commodity hardware » 100 Servers Enterprise Servers = 10k USD per TB » 100 Commodity Computers 1k USD Per TB » Provides Data Security » No…”

### Reading data parquet dataframe

**Distributed across partitions (files, HDFS blocks, …).**
Confidence 0.56 · candidate · 1 source
Evidence: `session-02/02_spark_fundamentals.ipynb#cell-6:6` — “- Distributed across partitions (files, HDFS blocks, …).”

### Replication factor default number

**» Default number of replicas can be configured globally » Can't have more replicas than you have brokers » Data replication incurs some overhead » Always enable replication in a Production cluster » Outside your laptop use a replication factor > 1 than to prevent data loss.**
Confidence 0.71 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p77:4` — “» Default number of replicas can be configured globally » Can't have more replicas than you have brokers » Data replication incurs some overhead » Always enable replication in a Production…”

### Slave datanodes store actual

**» Slave / DataNodes: store actual data, does reading, writing and processing.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p69:6` — “» Slave / DataNodes: store actual data, does reading, writing and processing. Performs replication.”

### Turn partitions key

**The Java CLI from Block 1 and this Python client use the same hash function (murmur2), so Tirol lands in the same partition from both.**
Confidence 0.64 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-11:1` — “Each key appears in exactly one partition: partition = hash(key) mod 3. Several keys share a partition – that is fine. The Java CLI from Block 1 and this Python client use the same hash…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 7 | 2026-11-25 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 1 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |
| `session-02/02_spark_fundamentals.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-06/README.md` | readme | 0.85 | 3 | 2026-11-11 |
| `raw/04_mock_exam.md` | exam | 0.95 | 1 | 2026-11-25 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 1 | 2026-11-25 |

## Related Pages

- [[data-duckdb|DuckDB]] (12 shared entities)
- [[course-exam|Exam]] (10 shared entities)
- [[data-formats|File Formats]] (9 shared entities)
- [[kafka-cluster|Kafka Cluster]] (9 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (9 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (9 shared entities)

## Open Questions

5 prompts from the material are collected in [[questions/hdfs-architecture|Questions: HDFS]].
- B1 (1 P) Which HDFS component stores the metadata (which blocks belong to which file, and where they are)?
- B2 (2 P) A 150 MB file, block size 64 MB, replication factor 3. How many blocks does the file have, and how many block copies are stored…
- B3 (2 P) A DataNode fails. How does HDFS notice it, and why is no data lost?

## Timeline

- 2026-11-25: new_claim on `claim_4161519a`
- 2026-11-25: new_claim on `claim_ee2e70d3`
- 2026-11-25: new_claim on `claim_fba178e0`
- 2026-11-25: new_claim on `claim_77699260`
- 2026-11-25: new_claim on `claim_6908d589`
- 2026-11-25: new_claim on `claim_6ce918d7`
- 2026-11-25: new_claim on `claim_633a9dc0`
- 2026-11-25: new_claim on `claim_c6cd6bf4`
