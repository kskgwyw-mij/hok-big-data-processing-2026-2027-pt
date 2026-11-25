---
title: Python Execution Model
type: concepts
topic: python.execution
entity_ids:
  - ent_gil
  - ent_global_interpreter_lock
  - ent_jupyter
  - ent_duckdb
  - ent_polars
  - ent_spark
  - ent_spark_job
  - ent_spark_task
claim_ids:
  - claim_422e5bc3
  - claim_a14b9b66
  - claim_87320cd4
  - claim_399330a4
  - claim_fde9b785
  - claim_57368c52
  - claim_19fdcf51
  - claim_1a0fc8d5
  - claim_5b33ee68
  - claim_8d7591e3
  - claim_ebc419b5
  - claim_e9110347
  - claim_19133618
  - claim_e0f7c50a
  - claim_199fa0d3
  - claim_b0affde9
  - claim_6a40c8fe
  - claim_3f8994a4
  - claim_c1017303
  - claim_573e711b
  - claim_ee7d46d3
  - claim_ba1a0b7e
  - claim_887203d3
  - claim_ae291429
  - claim_875dccdd
  - claim_52d2f069
  - claim_fbfe301b
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_46087206
  - src_47132aab
  - src_6e2e5684
  - src_9e752903
  - src_ffd1cdcc
review_required: false
---

# Python Execution Model

Rendered from 27 claims and 5 sources. Median confidence 0.63; 19 active, 0 disputed, 0 superseded.

## Current Understanding

### Bonus python gil

**Run: 1 — Python: 3.12, normal build (our kernel); GIL: always on.**
Confidence 0.75 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-0:12` — “1 | 3.12, normal build (our kernel) | always on”

**In the first two runs, 4 threads are no faster than 1 thread (speed-up column ≈ 1.0x). Why? (The speed-up compares threads with serial within one run, not one run with another.).**
Confidence 0.70 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-9:3` — “1. In the first two runs, 4 threads are no faster than 1 thread (speed-up column ≈ 1.0x). Why? (The speed-up compares threads with serial within one run, not one run with another.)”

**You cannot switch the GIL off in the normal build – you need that separate build.**
Confidence 0.69 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-0:7` — “You cannot switch the GIL off in the normal build – you need that separate build. In this notebook we install it next to our normal Python and run the same benchmark three times:”

**In the warm-up we saw that threads bring no speed-up for CPU-bound Python code, because of the Global Interpreter Lock (GIL).**
Confidence 0.63 · active · 1 source · when: for CPU -bound Python code
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-0:3` — “In the warm-up we saw that threads bring no speed-up for CPU-bound Python code, because of the Global Interpreter Lock (GIL). Since Python 3.13 there is a separate free-threaded build…”

**Compare the serial times of run 1 and run 3.**
Confidence 0.61 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-9:8` — “3. Compare the serial times of run 1 and run 3. Two things differ: the Python version and the GIL. Which one explains the difference? (Hint: Python 3.11+ made the interpreter itself much…”

**In the cloud, one "vCPU" is often one hyperthread – two vCPUs can share one physical core.**
Confidence 0.50 · candidate · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-2` — “In the cloud, one "vCPU" is often one hyperthread – two vCPUs can share one physical core.”

### Warm up threads vs processes pandas

**Before we compare big-data engines, we need one fact about Python: the Global Interpreter Lock (GIL) lets only one thread execute Python code at a time.**
Confidence 0.69 · active · 1 source · when: Before we compare big-data engines
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-0:3` — “Before we compare big-data engines, we need one fact about Python: the Global Interpreter Lock (GIL) lets only one thread execute Python code at a time.”

**Question: Threads and processes are equally fast here.**
Confidence 0.64 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-4:1` — “Question: Threads and processes are equally fast here. Why doesn't the GIL matter for waiting?”

**This notebook uses multiprocessing with functions defined in the notebook.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-0:11` — “This notebook uses multiprocessing with functions defined in the notebook. Functions used by ProcessPoolExecutor live in workers.py, because processes started with spawn (macOS/Windows)…”

**I/O-bound – downloading web pages.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-0:9` — “3. I/O-bound – downloading web pages”

**Waiting (chores) – nothing to compute, just waiting.**
Confidence 0.56 · candidate · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-0:7` — “1. Waiting (chores) – nothing to compute, just waiting”

### Takeaways

**Work type: CPU-bound Python code — Use: processes; Why: each process has its own GIL – but no shared memory.**
Confidence 0.69 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:5` — “CPU-bound Python code | processes | each process has its own GIL – but no shared memory”

**Work type: waiting / I/O — Use: threads; Why: the GIL is released while waiting.**
Confidence 0.69 · active · 1 source · when: while waiting
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:4` — “waiting / I/O | threads | the GIL is released while waiting”

**Outlook: Python 3.13+ offers an experimental free-threaded build without the GIL (PEP 703).**
Confidence 0.63 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:11` — “Outlook: Python 3.13+ offers an experimental free-threaded build without the GIL (PEP 703).”

**Polars (Rust) and DuckDB (C++) run their work outside the GIL on all cores – no multiprocessing tricks needed.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:7` — “Bridge to the main lab: pandas runs most operations on one core. Polars (Rust) and DuckDB (C++) run their work outside the GIL on all cores – no multiprocessing tricks needed. Spark goes…”

### Benchmark

**The same CPU-bound task as in the warm-up: 4 jobs, first one after another (serial), then in 4 threads.**
Confidence 0.63 · active · 1 source · when: after another (serial)
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-5:3` — “The same CPU-bound task as in the warm-up: 4 jobs, first one after another (serial), then in 4 threads. Each measurement is repeated 3 times and the fastest run counts, because other…”

**Run fn several times and keep the fastest run – removes noise from other programs.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-6` — “run fn several times and keep the fastest run – removes noise from other programs”

### Know

**Python 3.13 called free-threading experimental; from 3.14 it is officially supported, and the single-thread slowdown is much smaller.**
Confidence 0.61 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-9:15` — “- Python 3.13 called free-threading experimental; from 3.14 it is officially supported, and the single-thread slowdown is much smaller.”

**Not every library is ready yet. If you import a C extension that is not marked as free-threading-safe, Python switches the GIL back on and prints a warning.**
Confidence 0.61 · active · 1 source · when: If you import a C extension that is not marked as free-threading-safe
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-9:17` — “- Not every library is ready yet. If you import a C extension that is not marked as free-threading-safe, Python switches the GIL back on and prints a warning.”

### Question

**Only credit-card payments (payment_type == 1), only fares > 0.**
Confidence 0.69 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-5:2` — “> At which hour of the day do passengers tip the most (as % of the fare)? > Only credit-card payments (payment_type == 1), only fares > 0.”

**Spark's optimizer (Session 2) does exactly the same thing.**
Confidence 0.58 · candidate · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-10:1` — “Look at the plan: which columns end up in the scan (projection pushdown)? Where does the filter end up (predicate pushdown)? Spark's optimizer (Session 2) does exactly the same thing.”

### Really need cluster

**Keep an eye on three things throughout: runtime, memory, and how much data is actually read.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:12` — “Keep an eye on three things throughout: runtime, memory, and how much data is actually read.”

**Goal: Find out how far a single machine gets before we need distributed processing.**
Confidence 0.63 · active · 1 source · when: before we need distributed processing
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-0:3` — “Goal: Find out how far a single machine gets before we need distributed processing. We run the same analysis on NYC Yellow Taxi data with three engines:”

### Feature engineering built in functions

**A Python UDF ships every row to a Python process and back – often 10× slower.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-41:1` — “> Why not a Python function (UDF)? F.sin, F.sqrt, … run inside the JVM and are optimised by Catalyst. A Python > UDF ships every row to a Python process and back – often 10× slower.”

### Install free threaded build

**It puts Python 3.14t into your home folder; nothing in the course environment changes.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-3:3` — “We use uv, a fast Python installer. It puts Python 3.14t into your home folder; nothing in the course environment changes.”

### Limit writer time

**The price: only one process may open the file for writing.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-17:2` — “DuckDB is an embedded database: it runs inside your Python process, there is no server in between. The price: only one process may open the file for writing. We simulate a second user with…”

### Scaling experiment

**Run the query on 1, 2, 4, … months.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-18:2` — “Run the query on 1, 2, 4, … months. Where does pandas break down on your machine? pandas is skipped automatically once it would run out of memory – a crash would kill the whole kernel.”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `session-01/02_bonus_python_without_gil.ipynb` | notebook | 0.86 | 11 | 2026-10-28 |
| `session-01/00_warmup_threads_vs_processes.ipynb` | notebook | 0.86 | 9 | 2026-10-28 |

## Related Pages

- [[engines-single_machine|Single-Machine Engines]] (14 shared entities)
- [[course-exam|Exam]] (11 shared entities)
- [[data-duckdb|DuckDB]] (5 shared entities)
- [[data-formats|File Formats]] (5 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (3 shared entities)
- [[course-setup|Course Setup]] (3 shared entities)

## Open Questions

6 prompts from the material are collected in [[questions/python-execution|Questions: Python Execution Model]].
- Question: Why do threads bring no speed-up here?
- At which hour of the day do passengers tip the most (as % of the fare)?
- Polars, DuckDB and Spark were fast in the main lab – with the normal Python build. How do they avoid the GIL problem without a…

## Timeline

- 2026-11-25: new_claim on `claim_573e711b`
- 2026-11-25: new_claim on `claim_ee7d46d3`
- 2026-11-25: new_claim on `claim_ba1a0b7e`
- 2026-11-25: new_claim on `claim_887203d3`
- 2026-11-25: new_claim on `claim_ae291429`
- 2026-11-25: new_claim on `claim_875dccdd`
- 2026-11-25: new_claim on `claim_52d2f069`
- 2026-11-25: new_claim on `claim_fbfe301b`
