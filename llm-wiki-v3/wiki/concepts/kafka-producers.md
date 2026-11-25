---
title: Kafka Producers
type: concepts
topic: kafka.producers
entity_ids:
  - ent_kafka
  - ent_partition
  - ent_topic
  - ent_broker
  - ent_action
  - ent_c1_b1
  - ent_c2_b1
  - ent_json
  - ent_kafka_producers
  - ent_venv
claim_ids:
  - claim_e76e1d3a
  - claim_40d0ccf8
  - claim_3eb671de
  - claim_9299ae2e
  - claim_f74f1f65
  - claim_e5d21816
  - claim_e6c671ef
  - claim_5aae3a4d
  - claim_391db1f4
  - claim_3eea2cc1
  - claim_2fb11576
  - claim_8cd2ba0b
  - claim_f24eb0c0
  - claim_3b676cd6
  - claim_8701c291
  - claim_0d2dbf6f
confidence: 0.657
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_bb056c24
  - src_cecf99ea
  - src_f8b034ea
  - src_fc0bfe80
review_required: false
---

# Kafka Producers

Rendered from 16 claims and 7 sources. Median confidence 0.66; 12 active, 0 disputed, 0 superseded.

## Current Understanding

### Produce messages key

**Start the console producer. parse.key=true + key.separator=: means: the text before the first : is the key.**
Confidence 0.71 · active · 1 source · when: before the first : is the key
Evidence: `session-06/01_kafka_cli.md:102` — “Start the console producer. parse.key=true + key.separator=: means: the text before the first : is the key.”

**The producer picks the partition from the key: partition = hash(key) mod number_of_partitions.**
Confidence 0.66 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:99` — “A Kafka message is a key–value pair. The producer picks the partition from the key: partition = hash(key) mod number_of_partitions. No key → the producer spreads messages over the…”

### Producer

**Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py --count 30 --interval 0.2 python producer.py --no-key # same events, but WITHOUT a key python producer.py --data users --topic registered_user # the original lab: fake users, no key.**
Confidence 0.50 · candidate · 1 source
Evidence: `session-06/producer.py:1` — “Examples (run in the session-06 folder, .venv activated, broker on localhost:9092): python producer.py # keyed events to topic user-events, 1 per second, until Ctrl+C python producer.py…”

**Kafka producer for the Session 6 lab (terminal version of kafka_producer.ipynb).**
Confidence 0.50 · candidate · 1 source · when: for the Session 6 lab (terminal version of kafka_producer
Evidence: `session-06/producer.py:1` — “Kafka producer for the Session 6 lab (terminal version of kafka_producer.ipynb).”

### Broker state tirol seq

**{"state": "Tirol", "seq": 1, serializer broker deserializer "action": "login"} JsonSerializer() bytes localhost:9092 JsonSerializer() dict.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p94:8` — “{"state": "Tirol", "seq": 1, serializer broker deserializer "action": "login"} JsonSerializer() bytes localhost:9092 JsonSerializer() dict”

### C2 b1 terminal p0

**Terminal 1 + 2 p0 C2 B1 $ python consumer.py --group group-b -- name B1 p1 C2 B1 $ python consumer.py --name C1 # bonus: no key p2 C1 B1 $ python producer.py --interval 0.5 $ python producer.py --no-key --interval 0.2.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p95:10` — “Terminal 1 + 2 p0 C2 B1 $ python consumer.py --group group-b -- name B1 p1 C2 B1 $ python consumer.py --name C1 # bonus: no key p2 C1 B1 $ python producer.py --interval 0.5 $ python…”

### Check broker

**Python -c "from kafka import KafkaAdminClient; print(KafkaAdminClient(bootstrap_servers='localhost:9092').list_topics())".**
Confidence 0.43 · candidate · 1 source
Evidence: `session-06/README.md:78` — “python -c "from kafka import KafkaAdminClient; print(KafkaAdminClient(bootstrap_servers='localhost:9092').list_topics())"”

### Consumer groups real processes terminal

**Bonus – keys and order: stop the producer and run python producer.py --no-key --interval 0.2.**
Confidence 0.62 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:45` — “Bonus – keys and order: stop the producer and run python producer.py --no-key --interval 0.2. Consumers in group-a may now print expected seq … – the same state is spread over partitions…”

### Kafka lab exam preparation

**Symptom: can't open file '…/producer.py' — Fix: You are in the repo root → cd session-06.**
Confidence 0.83 · active · 2 sources
Evidence: `session-06/README.md:110` — “can't open file '…/producer.py' | You are in the repo root → cd session-06”

### Kafka step producers

**» Next step » Kafka Producers send data to a topic » Producers are often built with a client library e.g. Python, Java, etc. » Events may be sent one at a time, or in batches » Many configuration options and considerations.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p54:4` — “» Next step » Kafka Producers send data to a topic » Producers are often built with a client library e.g. Python, Java, etc. » Events may be sent one at a time, or in batches » Many…”

### Keyedevents

**A consumer can therefore check: "for key Tirol, did I receive seq 1, 2, 3, ... in this order?" -> ordering per key. run is a short random id per generator, so a restarted producer does not look like "out of order" (its seq starts again at 1, but with a new run id).**
Confidence 0.55 · candidate · 1 source · when: for key Tirol
Evidence: `session-06/kafka_data.py:35` — “seq counts 1, 2, 3, ... separately for every key. A consumer can therefore check: "for key Tirol, did I receive seq 1, 2, 3, ... in this order?" -> ordering per key. run is a short random…”

### Messages disk

**Key and value are just bytes for Kafka. Who turns them back into text or JSON? (→ Block 2: deserializer).**
Confidence 0.69 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:238` — “2. Key and value are just bytes for Kafka. Who turns them back into text or JSON? (→ Block 2: deserializer)”

### Partition producers evenly hash

**» Producers evenly hash data to partitions.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p70:3` — “» Producers evenly hash data to partitions”

### Partition start producer py creates

**Start producer.py: it creates user- events (3 partitions) C1 → [2] · C2 → [0, 1] · 20/20 delivered.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p95:17` — “# expected seq … = intended group-a group-b Terminal 3 – same group different group = its own copy C1 + C2 share the 3 partitions of every message ✗ If it fails $ python consumer.py --name…”

### Serializers python object bytes

**The producer needs a serializer (object → bytes), the consumer a deserializer (bytes → object).**
Confidence 0.62 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-5:2` — “Kafka only stores bytes (Block 1, the hex dump). The producer needs a serializer (object → bytes), the consumer a deserializer (bytes → object). The old lab wrote it by hand – kafka-python…”

### Turn partitions key

**Without a key, the producer spreads the messages – the same state now ends up in several partitions.**
Confidence 0.62 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-13:1` — “Without a key, the producer spreads the messages – the same state now ends up in several partitions. (How exactly it spreads them depends on the client library; the Java client fills one…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 3 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 4 | 2026-11-25 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 3 | 2026-11-11 |
| `session-06/producer.py` | code | 0.80 | 2 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 2 | 2026-11-11 |
| `session-06/kafka_data.py` | code | 0.80 | 1 | 2026-11-11 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |

## Related Pages

- [[kafka-cluster|Kafka Cluster]] (14 shared entities)
- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (14 shared entities)
- [[kafka-log|Kafka Log]] (14 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (14 shared entities)
- [[hdfs-architecture|HDFS]] (13 shared entities)
- [[data-formats|File Formats]] (12 shared entities)

## Open Questions

_No open questions recorded for this topic._

## Timeline

- 2026-11-25: new_claim on `claim_3eea2cc1`
- 2026-11-25: new_claim on `claim_2fb11576`
- 2026-11-25: new_claim on `claim_8cd2ba0b`
- 2026-11-25: new_claim on `claim_f24eb0c0`
- 2026-11-25: new_claim on `claim_3b676cd6`
- 2026-11-25: support_update on `claim_391db1f4` (0.72 → 0.83)
- 2026-11-25: new_claim on `claim_8701c291`
- 2026-11-25: new_claim on `claim_0d2dbf6f`
