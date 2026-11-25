---
title: Kafka Consumers and Consumer Groups
type: concepts
topic: kafka.consumers
entity_ids:
  - ent_partition
  - ent_kafka
  - ent_assigned
  - ent_consumer_group
  - ent_lag
  - ent_offset
  - ent_topic
  - ent_broker
  - ent_docker
  - ent_jupyter
  - ent_kafka_consumer_groups_sh
  - ent_revoked
claim_ids:
  - claim_78ea47b9
  - claim_145ad645
  - claim_49c44b58
  - claim_d3ae8506
  - claim_0408c31a
  - claim_eecb9552
  - claim_51771b8c
  - claim_eefecc93
  - claim_ee2d1f75
  - claim_48b6dd87
  - claim_37227336
  - claim_9df4265b
  - claim_ab6f52ac
  - claim_2160d506
  - claim_78d6d6b2
  - claim_ea7da484
  - claim_824c5dd8
  - claim_4eec96d9
  - claim_54ade2b0
  - claim_963c03cd
  - claim_dca588fe
  - claim_ef560bf2
  - claim_42099051
  - claim_8134bcca
confidence: 0.619
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_799c8bd7
  - src_b289b34c
  - src_b94acce4
  - src_cecf99ea
  - src_f8b034ea
review_required: false
---

# Kafka Consumers and Consumer Groups

Rendered from 24 claims and 5 sources. Median confidence 0.62; 14 active, 0 disputed, 0 superseded.

## Current Understanding

### Consumer groups real processes terminal

**Experiment 1 – one producer, one consumer.**
Confidence 0.73 · active · 2 sources · when: for the consumer-group experiments
Evidence: `session-06/README.md:130` — “producer.py, consumer.py | terminal producer / consumer for the consumer-group experiments”

**The CONSUMER-ID column shows which consumer owns which partition.**
Confidence 0.62 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:35` — “The CONSUMER-ID column shows which consumer owns which partition. Now start C3 and C4 in the same group. With 3 partitions – what does C4 do? Stop one consumer with Ctrl+C: what happens to…”

**B1 reads everything from the beginning and then the same live messages as group-a: every group gets all messages, inside a group each partition goes to exactly one consumer.**
Confidence 0.62 · active · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:42` — “B1 reads everything from the beginning and then the same live messages as group-a: every group gets all messages, inside a group each partition goes to exactly one consumer.”

**Experiment 2 – a second consumer in the SAME group.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:25` — “Experiment 2 – a second consumer in the SAME group. Predict first: will C2 get copies of all messages, or a part?”

**Watch C1: REVOKED and a new ASSIGNED line = a rebalance.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-06/02_kafka_python.ipynb#cell-23:29` — “Watch C1: REVOKED and a new ASSIGNED line = a rebalance. Then look at the assignment from the broker's view:”

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
Confidence 0.68 · active · 1 source · when: before processing — Crash in between means: messages lost
Evidence: `session-06/02_kafka_python.ipynb#cell-23:10` — “before processing | messages lost | at-most-once”

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

### Kafka lab exam preparation

**Time: 09:10–10:10 — Block: 1; What: Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk; File: 01_kafka_cli.md.**
Confidence 0.67 · active · 1 source
Evidence: `session-06/README.md:9` — “09:10–10:10 | 1 | Broker & CLI: topics, partitions, keys, consumer groups, lag, log segments on disk | 01_kafka_cli.md”

**Symptom: consumer.py prints ASSIGNED partitions [] (several times) — Fix: Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the consumer gets its partitions within a few seconds.**
Confidence 0.67 · active · 1 source · when: if you start the consumer first
Evidence: `session-06/README.md:109` — “consumer.py prints ASSIGNED partitions [] (several times) | Topic user-events does not exist yet – normal if you start the consumer first. Start producer.py (it creates the topic); the…”

### Order kept

**We check the seq numbers of our two runs in the order the consumer received them: for every (run, state) the seq must go 1, 2, 3, … – otherwise we count an order violation.**
Confidence 0.68 · active · 1 source · when: for every (run
Evidence: `session-06/02_kafka_python.ipynb#cell-15:2` — “We check the seq numbers of our two runs in the order the consumer received them: for every (run, state) the seq must go 1, 2, 3, … – otherwise we count an order violation.”

**Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from partition 0 can arrive before seq 2 from partition 2.**
Confidence 0.56 · candidate · 1 source · when: before seq 2 from partition 2
Evidence: `session-06/02_kafka_python.ipynb#cell-17:1` — “Keyed: 0 violations – one key = one partition, and inside a partition order is guaranteed. Unkeyed: usually > 0 – the consumer reads partition by partition, so seq 3 of Tirol from…”

### Consume beginning

**Run the command without --from-beginning. Why do you see nothing now? (Slides: by default a consumer only reads what is produced after it connected.).**
Confidence 0.70 · active · 1 source · when: after it connected
Evidence: `session-06/01_kafka_cli.md:144` — “4. Run the command without --from-beginning. Why do you see nothing now? (Slides: by default a consumer only reads what is produced after it connected.)”

### Consume limit

**Consumer_timeout_ms=5000 ends the for loop after 5 s without new messages.**
Confidence 0.66 · active · 1 source · when: for loop after 5 s without new messages
Evidence: `session-06/02_kafka_python.ipynb#cell-13:5` — “consumer_timeout_ms=5000 ends the for loop after 5 s without new messages. A new group_id has no committed offsets yet, so auto_offset_reset="earliest" makes it start at the beginning of…”

### Kafka data

**Get_registered_user() – the original generator from the old lab (one fake user, no key) KeyedEvents – events WITH a key and a per-key sequence number, for the partition / ordering / consumer-group experiments.**
Confidence 0.50 · candidate · 1 source · when: for the partition / ordering / consumer-group experiments
Evidence: `session-06/kafka_data.py:1` — “get_registered_user() – the original generator from the old lab (one fake user, no key) KeyedEvents – events WITH a key and a per-key sequence number, for the partition / ordering /…”

### Laptop cannot run route

**You type on their laptop in Block 1 and run consumer.py on theirs in Block 2.**
Confidence 0.61 · active · 1 source
Evidence: `session-06/README.md:84` — “No problem: pair up with a neighbour whose broker runs. You type on their laptop in Block 1 and run consumer.py on theirs in Block 2. Everything in Blocks 3 and 4 needs only paper.…”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-06/02_kafka_python.ipynb` | notebook | 0.86 | 15 | 2026-11-11 |
| `session-06/01_kafka_cli.md` | lab_guide | 0.90 | 3 | 2026-11-11 |
| `session-06/consumer.py` | code | 0.80 | 2 | 2026-11-11 |
| `session-06/README.md` | readme | 0.85 | 4 | 2026-11-11 |
| `session-06/kafka_data.py` | code | 0.80 | 1 | 2026-11-11 |

## Related Pages

- [[kafka-log|Kafka Log]] (20 shared entities)
- [[kafka-cluster|Kafka Cluster]] (15 shared entities)
- [[kafka-producers|Kafka Producers]] (13 shared entities)
- [[unfiled|Unfiled Observations]] (12 shared entities)
- [[hdfs-architecture|HDFS]] (11 shared entities)
- [[course-exam|Exam]] (10 shared entities)

## Open Questions

5 prompts from the material are collected in [[questions/kafka-consumers|Questions: Kafka Consumers and Consumer Groups]].
- Prediction 3: what is the total LAG of cli-group now?
- Stop one consumer with Ctrl+C: what happens to its partitions?
- (3 P) A topic has 3 partitions and one consumer group with 4 consumers. How are the partitions assigned, and what does the 4th consumer…

## Timeline

- 2026-11-25: new_claim on `claim_54ade2b0`
- 2026-11-25: new_claim on `claim_963c03cd`
- 2026-11-25: new_claim on `claim_dca588fe`
- 2026-11-25: support_update on `claim_eefecc93` (0.57 → 0.73)
- 2026-11-25: evidence_attached on `claim_eefecc93` (0.73 → 0.73)
- 2026-11-25: new_claim on `claim_ef560bf2`
- 2026-11-25: new_claim on `claim_42099051`
- 2026-11-25: new_claim on `claim_8134bcca`
