---
title: MapReduce
type: concepts
topic: mapreduce.model
entity_ids:
  - ent_map_phase
  - ent_mapreduce
  - ent_reduce_phase
  - ent_shuffle
  - ent_caching
  - ent_hadoop_distributed_file_system
  - ent_hdfs
  - ent_input_phase
  - ent_intermediate_data
  - ent_intermediate_keys
  - ent_key_components
  - ent_output_phase
claim_ids:
  - claim_161796db
  - claim_b930c4cb
  - claim_533151da
  - claim_d98f67d0
confidence: 0.708
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_68fcf2b9
review_required: false
---

# MapReduce

Rendered from 4 claims and 1 sources. Median confidence 0.71; 4 active, 0 disputed, 0 superseded.

## Current Understanding

### Hdfs key components map

**» Key Components: » Map Phase: Splits and maps data. » Reduce Phase: Shuffles and aggregates data. » Works with Hadoop Distributed File System (HDFS). » Supports multiple languages: Java, Python, C++.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p75:3` — “» Key Components: » Map Phase: Splits and maps data. » Reduce Phase: Shuffles and aggregates data. » Works with Hadoop Distributed File System (HDFS). » Supports multiple languages: Java,…”

### Mapreduce caching intermediate data

**» No Caching of Intermediate Data: Reduces efficiency in iterative computations. » Not Suitable for Real-Time Processing: Designed for batch processing only. » Complexity: Writing custom MapReduce jobs can be challenging for beginners.**
Confidence 0.71 · active · 1 source · when: for Real -Time Processing: Designed for batch processing only
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p83:3` — “» No Caching of Intermediate Data: Reduces efficiency in iterative computations. » Not Suitable for Real-Time Processing: Designed for batch processing only. » Complexity: Writing custom…”

### Mapreduce definition programming

**» Definition: MapReduce is a » programming model and » processing framework for parallel computation on large datasets across distributed clusters.**
Confidence 0.76 · active · 1 source · when: for parallel computation on large datasets across distributed clusters
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p74:3` — “» Definition: MapReduce is a » programming model and » processing framework for parallel computation on large datasets across distributed clusters.”

### Shuffle step input phase

**» Step 1: Input Phase » Record Reader extracts raw data and converts it into key-value pairs. » Step 2: Map Phase » User-defined Map function processes key-value pairs to generate intermediate keys. » Step 3: Intermediate Keys & Combiner (Optional) » Combiner groups and summarizes data locally before sending it to reducers. » Step 4: Shuffle & Sort » Shuffling: Groups the same keys together. » Sorting: Orders the grouped data for efficient processing. » Step 5: Reduce Phase » Runs Reducer Function on grouped key-value pairs. » Produces final key-value outputs. » Step 6: Output Phase » Output Formatter converts and writes final results to the file system.**
Confidence 0.70 · active · 1 source · when: before sending it to reducers; for efficient processing
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p80:3` — “» Step 1: Input Phase » Record Reader extracts raw data and converts it into key-value pairs. » Step 2: Map Phase » User-defined Map function processes key-value pairs to generate…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 4 | 2026-11-25 |

## Related Pages

- [[data-duckdb|DuckDB]] (4 shared entities)
- [[course-exam|Exam]] (3 shared entities)
- [[hdfs-architecture|HDFS]] (3 shared entities)
- [[spark-architecture|Spark Architecture]] (3 shared entities)
- [[spark-execution|Spark Execution Model]] (3 shared entities)
- [[unfiled|Unfiled Observations]] (3 shared entities)

## Open Questions

3 prompts from the material are collected in [[questions/mapreduce-model|Questions: MapReduce]].
- B4 (3 P) MapReduce word count on the input lines big data is big and data is fast. Write down the map output, the result of shuffle &…
- B5 (2 P) Name two disadvantages of Hadoop MapReduce that Spark addresses.
- 3.2 (3 P) Word count with MapReduce on the two lines big data is big and data is fast. Write down (a) the output of the map phase, (b)…

## Timeline

- 2026-11-25: new_claim on `claim_161796db`
- 2026-11-25: new_claim on `claim_b930c4cb`
- 2026-11-25: new_claim on `claim_533151da`
- 2026-11-25: new_claim on `claim_d98f67d0`
