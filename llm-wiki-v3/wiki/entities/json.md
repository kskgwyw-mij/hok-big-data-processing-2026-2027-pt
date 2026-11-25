---
title: JSON
type: entity
entity_id: ent_json
entity_type: format
claim_ids:
  - claim_79960e02
  - claim_f74f1f65
  - claim_1adf6473
  - claim_61fb1e16
  - claim_9e8e781d
  - claim_69ffcc24
  - claim_af1b58f3
confidence: 0.703
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_47132aab
  - src_70f9fe3e
  - src_8615b91f
  - src_b289b34c
  - src_fc0bfe80
---

# JSON

Type: format. Mentioned in 7 claims across 5 topics.
Aliases: json.

## Claims

- **» Kafka Topics are roughly analogous to SQL Tables » Topics organize related events » Topics are not queryable like SQL tables » You must create consumers or producers e.g. topic logs, topic purchases » Topics consist of append-only logs » All data in a topic is in key-value form » Many configuration options and considerations » Stored in binary format and not string like JSON.** Confidence 0.77 · [[kafka-log|Kafka Log]]
- **Writing events Analysing data Exchanging with people One record at a time, all fields A few columns of many rows: Readable, works everywhere: CSV, together: Avro, JSON Lines.** Confidence 0.70 · [[data-formats|File Formats]]
- **» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.** Confidence 0.70 · [[data-formats|File Formats]]
- **» YAML stands for "YAML Ain't Markup Language" » a human-friendly, data serialization standard for all programming languages. » Simpler and more readable than XML or JSON » Used in applications like Docker, Kubernetes, and CI/CD pipelines.** Confidence 0.70 · [[tooling-docker|Docker and Dev Containers]]
- **Key and value are just bytes for Kafka. Who turns them back into text or JSON? (→ Block 2: deserializer).** Confidence 0.69 · [[kafka-producers|Kafka Producers]]
- **JSON row · text none, but nested APIs, logs, semi-structured data.** Confidence 0.65 · [[unfiled|Unfiled Observations]]
- **Spark therefore has its own format: a folder with JSON metadata and Parquet files.** Confidence 0.63 · [[data-formats|File Formats]]

## Related Entities

- [[kafka|Kafka]] (3)
- [[avro|Avro]] (2)
- [[csv|CSV]] (2)
- [[docker|Docker]] (1)
- [[parquet|Parquet]] (1)
- [[spark|Spark]] (1)
- [[append_only_log|append-only log]] (1)
- [[topic|topic]] (1)
