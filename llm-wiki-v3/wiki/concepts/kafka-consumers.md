---
title: Kafka Consumers and Consumer Groups
type: concepts
topic: kafka.consumers
entity_ids:
  - ent_kafka
  - ent_partition
  - ent_offset
  - ent_consumer_group
  - ent_lag
  - ent_topic
  - ent_broker
  - ent_docker
  - ent_jupyter
  - ent_kafka_consumer_groups_sh
  - ent_assigned
  - ent_git
claim_ids:
  - claim_78ea47b9
  - claim_145ad645
  - claim_49c44b58
  - claim_d3ae8506
  - claim_0408c31a
  - claim_eecb9552
  - claim_51771b8c
  - claim_8011b4a7
  - claim_eefecc93
  - claim_ee2d1f75
  - claim_48b6dd87
  - claim_37227336
  - claim_9df4265b
  - claim_ab6f52ac
  - claim_2160d506
  - claim_78d6d6b2
  - claim_b2790cc8
  - claim_ea7da484
  - claim_824c5dd8
  - claim_4eec96d9
  - claim_c8c19737
  - claim_54ade2b0
  - claim_963c03cd
  - claim_ef560bf2
  - claim_42099051
  - claim_8134bcca
  - claim_49e11303
  - claim_1d3ee168
  - claim_22bb4cc6
  - claim_a2c72ddb
  - claim_6e8f4f34
  - claim_93340bbe
  - claim_4557e45e
  - claim_97c739ec
  - claim_aca866f9
  - claim_630ccc7b
  - claim_21ffc4fc
  - claim_9b05acf6
  - claim_bf6e1a55
  - claim_3a1a7f1a
confidence: 0.677
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_799c8bd7
  - src_8615b91f
  - src_b289b34c
  - src_b3356305
  - src_b94acce4
  - src_cecf99ea
  - src_f8b034ea
  - src_fc0bfe80
review_required: false
---

# Kafka Consumers and Consumer Groups

Rendered from 40 claims and 8 sources. Median confidence 0.68; 30 active, 0 disputed, 0 superseded.

## Current Understanding

### Consumer groups real processes terminal

**B1 reads everything from the beginning and then the same live messages as group-a: every group gets all messages, inside a group each partition goes to exactly one consumer.**
Confidence 0.75 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p82:3` — “» In a group, each partition is read by exactly one consumer”

**Experiment 1 – one producer, one consumer.**
Confidence 0.73 · active · 2 sources · when: for the consumer-group experiments
Evidence: `session-06/README.md:130` — “producer.py, consumer.py | terminal producer / consumer for the consumer-group experiments”

**Experiment 2 – a second consumer in the SAME group.**
Confidence 0.72 · active · 2 sources
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p95:1` — “Block 2 – Consumer groups with real processes Open 3–4 terminals · activate .venv in each · cd session-06”

**The CONSUMER-ID column shows which consumer owns which partition.**
Confidence 0.62 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:35` — “The CONSUMER-ID column shows which consumer owns which partition. Now start C3 and C4 in the same group. With 3 partitions – what does C4 do? Stop one consumer with Ctrl+C: what happens to…”

**Notebook cells run one after another, so we need separate terminals for parallel consumers.**
Confidence 0.62 · active · 1 source · when: after another; for parallel consumers
Evidence: `session-06/02_kafka_python.ipynb#cell-23:15` — “Notebook cells run one after another, so we need separate terminals for parallel consumers. Open 3–4 terminals in VS Code (+ in the terminal panel), activate .venv in each, cd session-06.”

**Watch C1: REVOKED and a new ASSIGNED line = a rebalance.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:29` — “Watch C1: REVOKED and a new ASSIGNED line = a rebalance. Then look at the assignment from the broker's view:”

**Consumers in group-a may now print expected seq … – the same state is spread over partitions read by different consumers.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:45` — “Bonus – keys and order: stop the producer and run python producer.py --no-key --interval 0.2. Consumers in group-a may now print expected seq … – the same state is spread over partitions…”

**Python consumer.py --name C2 # terminal 3, same default group: group-a.**
Confidence 0.44 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:26` — “python consumer.py --name C2 # terminal 3, same default group: group-a”

**Python consumer.py --name C1 # terminal 1 ; python producer.py --interval 0.5 # terminal 2.**
Confidence 0.44 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:19` — “python consumer.py --name C1 # terminal 1 ; python producer.py --interval 0.5 # terminal 2”

### Kafka python producers consumers consumer

**All loops in this notebook are bounded (fixed number of messages, consumer stops after a few idle seconds), so no cell runs forever.**
Confidence 0.67 · active · 1 source · when: after a few idle seconds)
Evidence: `session-06/02_kafka_python.ipynb#cell-0:13` — “All loops in this notebook are bounded (fixed number of messages, consumer stops after a few idle seconds), so no cell runs forever. Endless producers and consumers run in the terminal…”

**Consumer groups with real, independent processes (terminal scripts producer.py / consumer.py).**
Confidence 0.60 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-0:11` — “5. consumer groups with real, independent processes (terminal scripts producer.py / consumer.py).”

**Consumers, offsets, auto-commit, lag and at-least-once.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-0:10` — “4. consumers, offsets, auto-commit, lag and at-least-once,”

### At least once

**Commit …: before processing — Crash in between means: messages lost; Name: at-most-once.**
Confidence 0.84 · active · 2 sources · when: before processing — Crash in between means: messages lost
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p94:22` — “Commit … Crash in between means Name”

**With enable_auto_commit=True the consumer commits after it has received messages, every 5 s.**
Confidence 0.66 · active · 1 source · when: after it has received messages
Evidence: `session-06/02_kafka_python.ipynb#cell-23:2` — “With enable_auto_commit=True the consumer commits after it has received messages, every 5 s. If it crashes after processing but before the next commit, the restarted consumer gets those…”

### Consumer

**Kafka consumer for the Session 6 lab (terminal version of kafka_consumer.ipynb).**
Confidence 0.50 · candidate · 1 source · when: for the Session 6 lab (terminal version of kafka_consumer
Evidence: `session-06/consumer.py:1` — “Kafka consumer for the Session 6 lab (terminal version of kafka_consumer.ipynb).”

**Every line shows: [consumer name] p @ key=... seq=.**
Confidence 0.50 · candidate · 1 source
Evidence: `session-06/consumer.py:1` — “Every line shows: [consumer name] p @ key=... seq=... "ASSIGNED" lines show which partitions this consumer got after a rebalance.”

### Consumer groups lag

**List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix).**
Confidence 0.66 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:186` — “5e. List all groups (kafka-consumer-groups.sh … --list, Route A with the docker exec … /opt/kafka/bin/ prefix). You will see groups like console-consumer-12345: a console consumer without…”

**Start the consumer of 5a again – with --group cli-group, but this time without --from-beginning.**
Confidence 0.66 · active · 1 source
Evidence: `session-06/01_kafka_cli.md:183` — “5d. Start the consumer of 5a again – with --group cli-group, but this time without --from-beginning. Which messages do you get? Describe the group again: what is the LAG now?”

### Order kept

**We check the seq numbers of our two runs in the order the consumer received them: for every (run, state) the seq must go 1, 2, 3, … – otherwise we count an order violation.**
Confidence 0.68 · active · 1 source · when: for every (run
Evidence: `session-06/02_kafka_python.ipynb#cell-15:2` — “We check the seq numbers of our two runs in the order the consumer received them: for every (run, state) the seq must go 1, 2, 3, … – otherwise we count an order violation.”

**Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from partition 0 can arrive before seq 2 from partition 2.**
Confidence 0.56 · candidate · 1 source · when: before seq 2 from partition 2
Evidence: `session-06/02_kafka_python.ipynb#cell-17:1` — “Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed. Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from…”

### Console consumer group random

**Console consumer without --group → random group like console-consumer-12345.**
Confidence 0.65 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p93:19` — “Console consumer without --group → random group like console-consumer-12345”

### Consume beginning

**Run the command without --from-beginning. Why do you see nothing now? (Slides: by default a consumer only reads what is produced after it connected.).**
Confidence 0.70 · active · 1 source · when: after it connected
Evidence: `session-06/01_kafka_cli.md:144` — “4. Run the command without --from-beginning. Why do you see nothing now? (Slides: by default a consumer only reads what is produced after it connected.)”

### Consume limit

**Consumer_timeout_ms=5000 ends the for loop after 5 s without new messages.**
Confidence 0.66 · active · 1 source · when: for loop after 5 s without new messages
Evidence: `session-06/02_kafka_python.ipynb#cell-13:5` — “consumer_timeout_ms=5000 ends the for loop after 5 s without new messages. A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of…”

### Consumer group kafka stores

**» Kafka stores the offsets at which a consumer group has been reading » The offsets commit live in a Kafka topic named "__consumer_offsets" » When a consumer has processed data received some Kafka, it should be committing the offsets » If a consumer process dies, it will be able to read back from where it left off thanks to consumer offsets!.**
Confidence 0.77 · active · 1 source · when: When a consumer has processed data received some Kafka; If a consumer process dies
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p34:3` — “» Kafka stores the offsets at which a consumer group has been reading » The offsets commit live in a Kafka topic named "__consumer_offsets" » When a consumer has processed data received…”

### Consumer group lag log end

**LAG ✓ What you should see = log-end offset Consumer group 'cli-group' has no active members. − committed offset PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p93:8` — “LAG ✓ What you should see = log-end offset Consumer group 'cli-group' has no active members. − committed offset PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG”

### Describe situation creates duplicate

**Describe a situation that creates a duplicate, and one way to make the consumer robust.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p101:3` — “» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.…”

### Group a consumers

**Group-a · 2 consumers group-a · 4 consumers group-b · 1 consumer.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p82:8` — “group-a · 2 consumers group-a · 4 consumers group-b · 1 consumer”

### Justify online shop needs

**Justify. » An online shop needs all events of one order in order, but wants to scale to many consumers.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p101:3` — “» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.…”

### Kafka consumer groups sh bootstrap server localhost 9092

**$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group cli-group.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p93:5` — “$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group cli-group”

### Kafka data

**Get_registered_user() – the original generator from the old lab (one fake user, no key) KeyedEvents – events WITH a key and a per-key sequence number, for the partition / ordering / consumer-group experiments.**
Confidence 0.50 · candidate · 1 source · when: for the partition / ordering / consumer-group experiments
Evidence: `session-06/kafka_data.py:1` — “get_registered_user() – the original generator from the old lab (one fake user, no key) KeyedEvents – events WITH a key and a per-key sequence number, for the partition / ordering /…”

### Kafka lab exam preparation

**Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.**
Confidence 0.80 · active · 2 sources
Evidence: `session-06/README.md:9` — “09:10–10:10 | 1 | Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk | 01_kafka_cli.md”

### Lag consumer running produce

**5b No consumer running: produce 5 more 1 3 4 1 messages 2 0 1 1 5c Predict total LAG, then check.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p93:15` — “5b No consumer running: produce 5 more 1 3 4 1 messages 2 0 1 1 5c Predict total LAG, then check”

### Laptop cannot run route

**You type on their laptop in Block 1 and run consumer.py on theirs in Block 2.**
Confidence 0.61 · active · 1 source
Evidence: `session-06/README.md:84` — “No problem: pair up with a neighbour whose broker runs. You type on their laptop in Block 1 and run consumer.py on theirs in Block 2. Everything in Blocks 3 and 4 needs only paper.…”

### Offset committed offsets live

**Committed offsets live in __consumer_offsets. · Source: 01_kafka_cli.md.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p93:24` — “Expected shape – numbers per partition depend on the keys. Committed offsets live in __consumer_offsets. · Source: 01_kafka_cli.md”

### Offset producer settings consumer

**Producer settings Consumer settings acks="all" · retries=5 · linger_ms=10 group_id · auto_offset_reset="earliest" · enable_auto_commit=True (every 5 s).**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p94:15` — “Producer settings Consumer settings acks="all" · retries=5 · linger_ms=10 group_id · auto_offset_reset="earliest" · enable_auto_commit=True (every 5 s)”

### Partition choose key partitions

**How do you choose the key, and why? » 3 partitions, one group with 4 consumers.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p101:3` — “» What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV? » A fraud detector and a dashboard both need all payment events.…”

### Partition consumers partitions idle

**» More consumers than partitions → idle » Consumer joins or crashes → » lag = log-end offset − committed offset consumers rebalance.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf#p82:25` — “» More consumers than partitions → idle » Consumer joins or crashes → » lag = log-end offset − committed offset consumers rebalance”

### Requirements txt git subfolder kafka

**» Git subfolder „kafka" » Create virtualenv » Install requirements.txt » Run kafka_producer.ipynb » Run kafka_consumer.ipynb » Understand concept of producer & consumer.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p60:4` — “» Git subfolder „kafka" » Create virtualenv » Install requirements.txt » Run kafka_producer.ipynb » Run kafka_consumer.ipynb » Understand concept of producer & consumer”

### Sessions folders

**Folder: session-06/ — Topic: Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation (03_exam_circuit.md, 04_mock_exam.md); Runs on: laptop with Docker or native Kafka (Java 17+).**
Confidence 0.67 · active · 1 source
Evidence: `README.md:134` — “session-06/ | Kafka lab: broker and CLI (01_kafka_cli.md), Python producers and consumers (02_kafka_python.ipynb, producer.py, consumer.py), consumer groups · exam preparation…”

### Topic create apps consume

**» We can create apps which consume data » Consumers retrieve events from Kafka Topic(s) » May consume one or more topics at a time » Keep track of what events have already been seen » Many configuration options and considerations » By default consumers will only consume data that was produced 1st connected to Kafka (historical data not automatically pulled).**
Confidence 0.75 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p55:3` — “» We can create apps which consume data » Consumers retrieve events from Kafka Topic(s) » May consume one or more topics at a time » Keep track of what events have already been seen » Many…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 17 | 2026-11-11 |
| `raw/20261113-FH-Kufstein-Big Data-Processing-6.pdf` | lecture_note | 0.92 | 16 | 2026-11-25 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 3 | 2026-11-11 |
| `README.md` | readme | 0.85 | 1 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 2 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 3 | 2026-11-11 |
| `session-06/kafka_data.py` | code | 0.80 | 1 | 2026-11-11 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |

## Related Pages

- [[kafka-log|Kafka Log]] (47 shared entities)
- [[kafka-cluster|Kafka Cluster]] (41 shared entities)
- [[tooling-docker|Docker and Dev Containers]] (28 shared entities)
- [[hdfs-architecture|HDFS]] (26 shared entities)
- [[kafka-producers|Kafka Producers]] (25 shared entities)
- [[data-formats|File Formats]] (24 shared entities)

## Open Questions

7 prompts from the material are collected in [[questions/kafka-consumers|Questions: Kafka Consumers and Consumer Groups]].
- E3 (2 P) A topic has 3 partitions. One consumer group runs 5 consumers. How are the partitions assigned, and what do the remaining…
- How are partitions assigned, and what does the 4th consumer do?
- Prediction 3: what is the total LAG of cli-group now?

## Timeline

- 2026-11-25: new_claim on `claim_aca866f9`
- 2026-11-25: new_claim on `claim_630ccc7b`
- 2026-11-25: new_claim on `claim_21ffc4fc`
- 2026-11-25: new_claim on `claim_9b05acf6`
- 2026-11-25: support_update on `claim_51771b8c` (0.68 → 0.84)
- 2026-11-25: evidence_attached on `claim_37227336` (0.72 → 0.72)
- 2026-11-25: new_claim on `claim_bf6e1a55`
- 2026-11-25: new_claim on `claim_3a1a7f1a`
