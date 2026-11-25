---
title: Streaming Architectures
type: decisions
topic: streaming.architecture
entity_ids:
  - ent_kafka
  - ent_kappa_architecture
  - ent_core_idea
  - ent_stream_processing
  - ent_apache_kafka
  - ent_architecture_batch
  - ent_batch_layer
  - ent_case_batch
  - ent_complexity_high_low_fault
  - ent_high_operational_overhead
  - ent_lambda_events_serving
  - ent_message_queue
claim_ids:
  - claim_95f17588
  - claim_dbe6518c
  - claim_2fbd4123
  - claim_622ac978
  - claim_bd7e82f0
  - claim_90d4a0d6
  - claim_fe53537f
  - claim_ef6e1531
  - claim_806a5d75
  - claim_c7b98e03
  - claim_659c4a52
  - claim_ccdee238
  - claim_15d999a8
confidence: 0.703
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_68fcf2b9
  - src_799c8bd7
  - src_8615b91f
  - src_fc0bfe80
review_required: false
---

# Streaming Architectures

Rendered from 13 claims and 4 sources. Median confidence 0.70; 12 active, 0 disputed, 0 superseded.

## Current Understanding

### At least once

**Commit …: after processing — Crash in between means: messages processed twice; Name: at-least-once.**
Confidence 0.82 · active · 2 sources · when: after processing — Crash in between means: messages processed twice; After processing messages processed twice at-least-once
Evidence: `session-06/02_kafka_python.ipynb#cell-23:9` — “after processing | messages processed twice | at-least-once”

**Kafka also offers exactly-once within Kafka (transactions) – not part of this course.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:12` — “Kafka also offers exactly-once within Kafka (transactions) – not part of this course.”

### Changes crashes explain at least once

**What changes if one crashes? » Explain at-least-once delivery with auto-commit.**
Confidence 0.70 · active · 1 source · when: if one crashes? » Explain at-least-once delivery with auto-commit
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p101:3` — “» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.…”

### Companies push log data

**Companies push log data as events into a data stream to perform stream processing.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p19:3` — “» How to solve this messy problem? Companies push log data as events into a data stream to perform stream processing.”

### Core idea purpose handles

**» Purpose: Handles batch and real-time data processing in parallel. » Core Idea: Combines batch and speed layers to provide robust, fault-tolerant analytics. » Components: » Batch Layer: Processes large volumes of data for comprehensive insights. » Speed Layer: Processes real-time data for immediate results. » Serving Layer: Combines outputs from batch and speed layers for query serving. » Advantages: » Fault-tolerant and scalable. » Suitable for systems requiring both historical and real-time analytics. » Disadvantages: » Complexity due to maintaining two separate layers (batch and speed). » Higher development and operational overhead.**
Confidence 0.70 · active · 1 source · when: for comprehensive insights; for immediate results
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p20:3` — “» Purpose: Handles batch and real-time data processing in parallel. » Core Idea: Combines batch and speed layers to provide robust, fault-tolerant analytics. » Components: » Batch Layer:…”

### Differences generalizations hard rules

**» The differences are generalizations, not hard rules. » Most data engineering teams use both batch and stream processing together to achieve their goals. » Stream processing complements batch processing.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p29:3` — “» The differences are generalizations, not hard rules. » Most data engineering teams use both batch and stream processing together to achieve their goals. » Stream processing complements…”

### Kafka purpose simplifies real time

**» Purpose: Simplifies real-time data processing by eliminating the batch layer. » Core Idea: A single real-time layer processes all incoming data. » Components: » Stream Processor: Central component for processing data in real-time. » Message Queue: Stores and delivers data streams (e.g., Kafka). » Advantages: » Simpler and less complex compared to Lambda. » Lower operational overhead due to a single processing layer. » Ideal for real-time systems. » Disadvantages: » Limited to systems where real-time processing is sufficient. » Lacks the robustness of batch processing for comprehensive historical analysis.**
Confidence 0.84 · active · 2 sources · when: for processing data in real-time; for real -time systems
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p22:3` — “» Purpose: Simplifies real-time data processing by eliminating the batch layer. » Core Idea: A single real-time layer processes all incoming data. » Components: » Stream Processor: Central…”

### Kappa architecture describe works

**Describe how this works in a Kappa architecture and which property of the Kafka topic makes it possible.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p99:7` — “» All events of order 4711 must be processed in the order they happened. Which message key do you choose, and why? What happens to the ordering if you send them without a key? » After a…”

### Kappa architecture feature lambda

**Feature Lambda Kappa Use Case Batch + Real-time Real-time Architecture Batch + Speed Layers Single real-time layer Processing Batch + Real-time Real-time Complexity High Low Fault Tolerance High Moderate Scalability High High Operational Overhead High Low Flexibility Medium Low.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p23:5` — “Feature Lambda Kappa Use Case Batch + Real-time Real-time Architecture Batch + Speed Layers Single real-time layer Processing Batch + Real-time Real-time Complexity High Low Fault…”

### Kappa architecture recap lambda

**Recap 4 · Lambda vs. Kappa architecture.**
Confidence 0.69 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p84:1` — “Recap 4 · Lambda vs. Kappa architecture”

### Lambda events serving batch

**Batch layer · all data, recompute Lambda Events Serving layer · merge views Query two paths Speed layer · recent data, stream.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p84:5` — “Batch layer · all data, recompute Lambda Events Serving layer · merge views Query two paths Speed layer · recent data, stream”

### Stream processing

**» Stream Processing applications consist of a streaming data store and the streaming calculation(s).**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p33:3` — “» Stream processing applications are downstream of the data store and perform calculations on one or more data streams, such as aggregations, joins, and filtering. » These calculations…”

### Stream processing potentially

**» A stream is a potentially unbounded sequence of data » Stream Processing is the act of performing continual calculations on a stream.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p6:3` — “» A stream is a potentially unbounded sequence of data » Stream Processing is the act of performing continual calculations on a stream”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 3 | 2026-11-25 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 2 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 5 | 2026-11-25 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 5 | 2026-11-25 |

## Related Pages

- [[kafka-log|Kafka Log]] (7 shared entities)
- [[course-exam|Exam]] (4 shared entities)
- [[data-duckdb|DuckDB]] (4 shared entities)
- [[data-formats|File Formats]] (4 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (4 shared entities)
- [[hdfs-architecture|HDFS]] (4 shared entities)

## Open Questions

2 prompts from the material are collected in [[questions/streaming-architecture|Questions: Streaming Architectures]].
- E6 (2 P) Describe the Lambda and the Kappa architecture in one sentence each. Which role does Kafka play in Kappa?
- 6.3 (3 P) A company computes the same KPIs twice: a nightly Spark batch job and a streaming job. Name this architecture and its main…

## Timeline

- 2026-11-25: new_claim on `claim_806a5d75`
- 2026-11-25: new_claim on `claim_c7b98e03`
- 2026-11-25: new_claim on `claim_659c4a52`
- 2026-11-25: support_update on `claim_622ac978` (0.74 → 0.84)
- 2026-11-25: new_claim on `claim_ccdee238`
- 2026-11-25: evidence_attached on `claim_ccdee238` (0.70 → 0.70)
- 2026-11-25: evidence_attached on `claim_622ac978` (0.84 → 0.84)
- 2026-11-25: new_claim on `claim_15d999a8`
