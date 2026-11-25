---
title: Unfiled Observations
type: concepts
topic: unfiled
entity_ids:
  - ent_kafka
  - ent_partition
  - ent_assigned
  - ent_delta_lake
  - ent_different
  - ent_f5ce_ba8a
  - ent_faker
  - ent_google_drive
  - ent_keys
  - ent_macos
  - ent_offset
  - ent_path
claim_ids:
  - claim_c84ec78d
  - claim_c5df4b59
  - claim_996139d2
  - claim_68d8d358
  - claim_59e9db05
  - claim_9d2b15fd
  - claim_4514b2c6
  - claim_ce1ffac9
  - claim_5af9f960
  - claim_d2b9f705
  - claim_92e37182
  - claim_130f2688
  - claim_a01288f3
  - claim_9785859c
  - claim_7aab7271
  - claim_a625e27c
  - claim_d963daba
  - claim_872d8421
  - claim_09b28a15
  - claim_1e9bcc33
  - claim_a6d89a64
  - claim_3be1dead
  - claim_1cdebcb1
  - claim_d1b25c7e
  - claim_9f7c996e
confidence: 0.516
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_41b3a933
  - src_4d7c51b1
  - src_576d8a91
  - src_799c8bd7
  - src_b94acce4
  - src_d56cb0d7
  - src_de25e104
  - src_f8b034ea
review_required: false
---

# Unfiled Observations

Rendered from 25 claims and 8 sources. Median confidence 0.52; 1 active, 0 disputed, 0 superseded.

## Current Understanding

### Consumer groups real processes terminal

**C1 prints ASSIGNED partitions [0, 1, 2] and then every message as p @ key=… seq=….**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:23` — “C1 prints ASSIGNED partitions [0, 1, 2] and then every message as p @ key=… seq=….”

**Experiment 3 – a DIFFERENT group.**
Confidence 0.53 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:38` — “Experiment 3 – a DIFFERENT group. Predict: what does B1 receive?”

**Consumers in group-a may now print expected seq … – the same state is spread over partitions read by different consumers.**
Confidence 0.52 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:45` — “Bonus – keys and order: stop the producer and run python producer.py --no-key --interval 0.2. Consumers in group-a may now print expected seq … – the same state is spread over partitions…”

### Get kafka

**The folder must NOT contain a space (the Kafka shell scripts then fail with "Classpath is empty").**
Confidence 0.52 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “Only uses the Python standard library, like get_data.py. Works on macOS and Linux (and in the Codespace). Windows: use the Docker route (README.md, route A) or run this script inside WSL.…”

**Needs Java 17 or newer: macOS: brew install openjdk@17 · Ubuntu: sudo apt install openjdk-17-jre-headless.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/get_kafka.py:1` — “Needs Java 17 or newer: macOS: brew install openjdk@17 · Ubuntu: sudo apt install openjdk-17-jre-headless”

### Kafka data

**The nine Austrian federal states are our message KEYS: a small, fixed set.**
Confidence 0.49 · candidate · 1 source
Evidence: `session-06/kafka_data.py:18` — “# The nine Austrian federal states are our message KEYS: a small, fixed set,”

**Fake data for the Session 6 Kafka lab.**
Confidence 0.42 · candidate · 1 source · when: for the Session 6 Kafka lab
Evidence: `session-06/kafka_data.py:1` — “Fake data for the Session 6 Kafka lab.”

### Kafka python producers consumers consumer

**Library: faker — Why: fake names for the events.**
Confidence 0.59 · candidate · 1 source · when: for the events
Evidence: `session-06/02_kafka_python.ipynb#cell-0:19` — “faker | fake names for the events”

**Endless producers and consumers run in the terminal instead (part 7).**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-0:13` — “All loops in this notebook are bounded (fixed number of messages, consumer stops after a few idle seconds), so no cell runs forever. Endless producers and consumers run in the terminal…”

### At least once

**Your processing should therefore be idempotent (e.g. upsert by an event id instead of count += 1).**
Confidence 0.67 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:2` — “With enable_auto_commit=True the consumer commits after it has received messages, every 5 s. If it crashes after processing but before the next commit, the restarted consumer gets those…”

### Check env

**It only reads information; it changes nothing on your machine.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-04/check_env.py:1` — “It only reads information; it changes nothing on your machine.”

### Create topic idempotently

**Idempotent = running it once or ten times leaves the same state.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-3:2` — “Idempotent = running it once or ten times leaves the same state. Creating a topic that already exists raises TopicAlreadyExistsError – we catch it, so you can re-run this cell (and the…”

### Expected sha512

**Apache publishes 'kafka_x.tgz: F5CE BA8A ...' (gpg --print-md style) – strip name and spaces.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/get_kafka.py:68` — “Apache publishes 'kafka_x.tgz: F5CE BA8A ...' (gpg --print-md style) – strip name and spaces.”

### Google drive please check

**Please check the Google Drive link with the group assignment.**
Confidence 0.09 · archived · 1 source
Evidence: `session-03/session-03.txt:1` — “Please check the Google Drive link with the group assignment”

### Java major

**Return the major version of java on PATH (or JAVA_HOME), or None.**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/get_kafka.py:32` — “Return the major version of java on PATH (or JAVA_HOME), or None.”

### Keyed producer

**Every event has a key (an Austrian state) and a seq number that counts per key: Tirol 1, 2, 3, ….**
Confidence 0.53 · candidate · 2 sources · when: for every key
Evidence: `session-06/02_kafka_python.ipynb#cell-7:5` — “Every event has a key (an Austrian state) and a seq number that counts per key: Tirol 1, 2, 3, …”

### Keyedevents

**Produces (key, value) pairs.**
Confidence 0.42 · candidate · 1 source
Evidence: `session-06/kafka_data.py:35` — “Produces (key, value) pairs.”

### Offsets commits lag

**0 – the group committed its offsets, so it continues where it stopped.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-19:1` — “0 – the group committed its offsets, so it continues where it stopped. Now produce 5 messages while nobody reads, then compute the lag = log-end offset − committed offset, per partition.”

### Printassignment

**Kafka calls these two methods when the group is rebalanced.**
Confidence 0.42 · candidate · 1 source · when: when the group is rebalanced
Evidence: `session-06/consumer.py:21` — “Kafka calls these two methods when the group is rebalanced.”

### Registered user

**One fake registered user (original lab function, unchanged output).**
Confidence 0.46 · candidate · 1 source
Evidence: `session-06/kafka_data.py:26` — “One fake registered user (original lab function, unchanged output).”

### Requirements local txt

**Kafka-python is pinned as >=3.0,<4.**
Confidence 0.41 · candidate · 1 source
Evidence: `requirements-local.txt:22` — “kafka-python>=3.0,<4”

### Requirements txt

**Pyspark is pinned as >=4.0,<4.1.**
Confidence 0.39 · candidate · 1 source
Evidence: `requirements.txt:10` — “pyspark>=4.0,<4.1”

### Serializers python object bytes

**The old lab wrote it by hand – kafka-python 3 also ships ready-made ones.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-5:2` — “Kafka only stores bytes (Block 1, the hex dump). The producer needs a serializer (object → bytes), the consumer a deserializer (bytes → object). The old lab wrote it by hand – kafka-python…”

### Turn lag partition total

**Use end and committed from the cell above.**
Confidence 0.53 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-21:2` — “Use end and committed from the cell above. The total must be 5 – why?”

### Turn partitions key

**Build a dictionary key -> set of partitions from sent.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-9:2` — “Build a dictionary key -> set of partitions from sent. Predict first: how many partitions per key?”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/get_kafka.py` | code | 0.80 | 4 | 2026-11-11 |
| `requirements.txt` | config | 0.75 | 1 | 2026-10-28 |
| `session-03/session-03.txt` | session_stub | 0.35 | 1 | 2026-11-11 |
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 12 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 1 | 2026-11-11 |
| `requirements-local.txt` | config | 0.75 | 1 | 2026-11-11 |
| `session-04/check_env.py` | code | 0.80 | 1 | 2026-10-28 |
| `session-06/kafka_data.py` | code | 0.80 | 5 | 2026-11-11 |

## Related Pages

- [[kafka-consumers|Kafka Consumers and Consumer Groups]] (10 shared entities)
- [[kafka-log|Kafka Log]] (10 shared entities)
- [[python-environments|Python Environments and Reproducibility]] (10 shared entities)
- [[course-setup|Course Setup]] (9 shared entities)
- [[hdfs-architecture|HDFS]] (9 shared entities)
- [[kafka-cluster|Kafka Cluster]] (9 shared entities)

## Open Questions

3 prompts from the material are collected in [[questions/unfiled|Questions: Unfiled Observations]].
- (3 P) Two applications – a fraud detector and a dashboard – both need all payment events. Same group_id or different ones? Justify.
- (4 P) An online shop needs all events of one order processed in the correct order, but also wants to scale to many consumers. How do you…
- Predict first: how many partitions per key?

## Timeline

- 2026-11-25: new_claim on `claim_09b28a15`
- 2026-11-25: new_claim on `claim_1e9bcc33`
- 2026-11-25: new_claim on `claim_a6d89a64`
- 2026-11-25: new_claim on `claim_3be1dead`
- 2026-11-25: new_claim on `claim_1cdebcb1`
- 2026-11-25: new_claim on `claim_d1b25c7e`
- 2026-11-25: new_claim on `claim_9f7c996e`
- 2026-11-25: support_update on `claim_872d8421` (0.57 → 0.53)
