---
title: Python Execution Model
type: concepts
topic: python.execution
entity_ids:
  - ent_gil
  - ent_spark_task
  - ent_global_interpreter_lock
  - ent_cpython
  - ent_jupyter
  - ent_spark
  - ent_spark_job
  - ent_big_data
  - ent_duckdb
  - ent_filter
  - ent_global_interpreter_lock_optional
  - ent_key_characteristics
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
  - claim_e78c7a48
  - claim_f2a67b3e
  - claim_7824f6df
  - claim_2de7f5ba
  - claim_8c6cb0a3
  - claim_a1963478
  - claim_a95b3cef
  - claim_b2a3332a
  - claim_49233044
  - claim_b5481149
  - claim_8b765c09
  - claim_cb8ff06c
  - claim_65d94b8d
  - claim_48244837
  - claim_f3ac0802
  - claim_ebea729f
  - claim_047b830a
  - claim_3f03e4a1
  - claim_67d6b852
  - claim_ff0fe4b9
  - claim_1f6eadbc
  - claim_fa6e3524
  - claim_5001acbe
  - claim_e5d27670
  - claim_adf70625
  - claim_5dee5fee
  - claim_b6fec17a
  - claim_61490bda
confidence: 0.694
status: disputed
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1cebb3bb
  - src_46087206
  - src_47132aab
  - src_59b6ded4
  - src_68fcf2b9
  - src_6e2e5684
  - src_70f9fe3e
  - src_9e752903
  - src_c65c80a3
  - src_e258bafb
  - src_fc0bfe80
  - src_ffd1cdcc
review_required: true
---

# Python Execution Model

Rendered from 55 claims and 12 sources. Median confidence 0.69; 46 active, 1 disputed, 0 superseded.

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

**Compare the serial times of run 1 and run 3.**
Confidence 0.61 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-9:8` — “3. Compare the serial times of run 1 and run 3. Two things differ: the Python version and the GIL. Which one explains the difference? (Hint: Python 3.11+ made the interpreter itself much…”

**In the warm-up we saw that threads bring no speed-up for CPU-bound Python code, because of the Global Interpreter Lock (GIL).**
Confidence 0.53 · disputed · 3 sources · when: for CPU -bound Python code · needs review
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p38:13` — “CPU-bound Python code no speed-up – the GIL speed-up up to #cores”

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

**Work type: waiting / I/O — Use: threads; Why: the GIL is released while waiting.**
Confidence 0.81 · active · 2 sources · when: while waiting
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:4` — “waiting / I/O | threads | the GIL is released while waiting”

**Work type: CPU-bound Python code — Use: processes; Why: each process has its own GIL – but no shared memory.**
Confidence 0.69 · active · 1 source
Evidence: `session-01/00_warmup_threads_vs_processes.ipynb#cell-8:5` — “CPU-bound Python code | processes | each process has its own GIL – but no shared memory”

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

### Big data processing mock exam

**Part: A — Topic: Foundations: Big Data, scaling, GIL, threads vs. processes; Points: 12.**
Confidence 0.96 · active · 2 sources
Evidence: `04_mock_exam-gitdiff.md:14` — “A | Foundations: Big Data, scaling, GIL, threads vs. processes | 12”

### Cpython gil mutex mutual

**» What is the GIL? » A mutex (mutual exclusion lock) that protects access to Python objects in CPython (the default Python implementation). » Ensures that only one thread executes Python bytecode at a time. » Why does it exist? » Simplifies memory management in CPython, especially with reference counting for garbage collection. » Avoids race conditions and ensures thread safety in single-threaded contexts. » Implications for Multithreading » Limits true parallelism in CPU-bound tasks, as only one thread can execute Python code at any moment. » I/O-bound tasks can still benefit from multithreading since the GIL is released during I/O operations (e.g., file I/O, network requests).**
Confidence 0.95 · active · 2 sources · when: for garbage collection; for Multithreading » Limits true parallelism in CPU-bound tasks
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p81:3` — “» What is the GIL? » A mutex (mutual exclusion lock) that protects access to Python objects in CPython (the default Python implementation). » Ensures that only one thread executes Python…”

### Crashes take whole process

**If one crashes can take the whole process down the others keep running.**
Confidence 0.70 · active · 1 source · when: If one crashes can take the whole process down the others keep running
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p48:12` — “If one crashes can take the whole process down the others keep running”

### Feature engineering built in functions

**A Python UDF ships every row to a Python process and back – often 10× slower.**
Confidence 0.57 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-41:1` — “> Why not a Python function (UDF)? F.sin, F.sqrt, … run inside the JVM and are optimised by Catalyst. A Python > UDF ships every row to a Python process and back – often 10× slower.”

### Filter processes file lock

**Two processes, one file: the lock count(*) FILTER (.**
Confidence 0.64 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p26:12` — “6. Two processes, one file: the lock count(*) FILTER (”

### Gil concurrency multiple threads

**» Concurrency via multiple threads in single process » Best for I/O-bound tasks (e.g., network calls, file operations) » Threads share memory space, leading to lower memory overhead » Limitation: Subject to the Global Interpreter Lock (GIL).**
Confidence 0.85 · active · 2 sources · when: for I /O-bound tasks (e
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p44:3` — “» Concurrency via multiple threads in single process » Best for I/O-bound tasks (e.g., network calls, file operations) » Threads share memory space, leading to lower memory overhead »…”

### Gil pep making global

**PEP 703 – Making the Global Interpreter Lock Optional in CPython.**
Confidence 0.85 · active · 2 sources
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p8:1` — “PEP 703 – Making the Global Interpreter Lock Optional in CPython”

### Gil python thread runs

**In Python one thread runs Python code at a time real parallelism, each process has its own GIL (normal build) (GIL).**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p48:14` — “In Python one thread runs Python code at a time real parallelism, each process has its own GIL (normal build) (GIL)”

### Gil uses cores outside

**It uses all cores, outside the GIL.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p57:3` — “» What it is: a DataFrame library written in Rust (since 2020), with Apache Arrow as its memory format. » How it runs: lazy with scan_parquet() / .lazy(): first it builds a query plan,…”

### Gil waiting i o downloads

**Waiting / I/O (downloads, files) fast – GIL is released while waiting fast.**
Confidence 0.70 · active · 1 source · when: while waiting fast
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p38:9` — “Waiting / I/O (downloads, files) fast – GIL is released while waiting fast”

### Install free threaded build

**It puts Python 3.14t into your home folder; nothing in the course environment changes.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/02_bonus_python_without_gil.ipynb#cell-3:3` — “We use uv, a fast Python installer. It puts Python 3.14t into your home folder; nothing in the course environment changes.”

### Instead processing purchase real time

**Instead of processing every purchase in real-time, the retailer processes the batches of each store's daily revenue totals at the end of the day.**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p43:3` — “» Data collected in „Batches" and then fed into Analytics System » No realtime available » Storage is required like database, filesystem, etc. » Great for ad-hoc analysis » Ideal for…”

### Kitchen fridge seen

**What's in one kitchen's fridge can't be seen from another kitchen. » A thread is a cook in that kitchen.**
Confidence 0.86 · active · 2 sources
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p47:3` — “» A process is a kitchen. It has its own fridge (memory), its own stove and its own recipes (code). What's in one kitchen's fridge can't be seen from another kitchen. » A thread is a cook…”

### Lack ability process

**Lack of ability to Ability to process process unstructured everything type of data data.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p55:16` — “Lack of ability to Ability to process process unstructured everything type of data data”

### Limit writer time

**The price: only one process may open the file for writing.**
Confidence 0.59 · candidate · 1 source
Evidence: `session-04/03_duckdb_database.ipynb#cell-17:2` — “DuckDB is an embedded database: it runs inside your Python process, there is no server in between. The price: only one process may open the file for writing. We simulate a second user with…”

### Logs hard process batch

**» Logs are hard to process in batch systems due to the speed and size of data.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p18:3` — “» Logs are hard to process in batch systems due to the speed and size of data”

### Memory shared threads isolated

**Memory shared with the other threads own, isolated.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p48:6` — “Memory shared with the other threads own, isolated”

### Multithreading concurrency multiprocessing increasing

**Multithreading is concurrency. » Multiprocessing is for increasing speed.**
Confidence 0.66 · active · 1 source · when: for increasing speed
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p49:3` — “» There can only be one thread running at any given time in a python process. » Multiprocessing is parallelism. Multithreading is concurrency. » Multiprocessing is for increasing speed.…”

### Multithreading hiding latency multiprocessing

**Multithreading is for hiding latency. » Multiprocessing is best for computations.**
Confidence 0.70 · active · 1 source · when: for hiding latency
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p49:3` — “» There can only be one thread running at any given time in a python process. » Multiprocessing is parallelism. Multithreading is concurrency. » Multiprocessing is for increasing speed.…”

### Never processes writing time

**Never two processes writing at the same time.**
Confidence 0.72 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p24:16` — “Many readers OR one writer. Never two processes writing at the same time.”

### Others wait oven i o

**The others can wait for the oven (I/O), but they can't chop in parallel. » Multiprocessing means opening more kitchens.**
Confidence 0.91 · active · 2 sources · when: for the oven (I/O)
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p12:3` — “» A process is a kitchen. It has its own fridge (memory), its own stove and its own recipes (code). What's in one kitchen's fridge can't be seen from another kitchen. » A thread is a cook…”

### Pip install users ports

**Install, users, ports – but many writers at once. pip install, no server – but one writing process.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p23:13` — “Install, users, ports – but many writers at once. pip install, no server – but one writing process.”

### Scaling experiment

**Run the query on 1, 2, 4, … months.**
Confidence 0.63 · active · 1 source
Evidence: `session-01/01_do_you_need_a_cluster.ipynb#cell-18:2` — “Run the query on 1, 2, 4, … months. Where does pandas break down on your machine? pandas is skipped automatically once it would run out of memory – a crash would kill the whole kernel.”

### Spark backbone data processing

**» Backbone of data processing in Spark » Distributed, fault-tolerant, and parallelizable data structure » Efficiently process large data-sets across a cluster » Key Characteristics: immutable, distributed, resilient, lazily evaluated, fault- tolerant.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p117:3` — “» Backbone of data processing in Spark » Distributed, fault-tolerant, and parallelizable data structure » Efficiently process large data-sets across a cluster » Key Characteristics:…”

### Spark job writers process

**Writers 1 process 1 at a time many many jobs.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p25:14` — “Writers 1 process 1 at a time many many jobs”

### Spark task map

**» Map Task » Converts input data into key-value pairs. » Processes each record independently. » Reduce Task » Takes the mapped output and consolidates values with the same key. » Produces the final output.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p79:3` — “» Map Task » Converts input data into key-value pairs. » Processes each record independently. » Reduce Task » Takes the mapped output and consolidates values with the same key. » Produces…”

### Spark task multiple independent

**» Multiple independent processes » Best for: CPU-bound tasks e.g. mathematical computations, large data processing » Processes have separate memory spaces » Advantage: Bypasses the GIL for true parallelism.**
Confidence 0.85 · active · 2 sources · when: for true parallelism
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p10:3` — “» Multiple independent processes » Best for: CPU-bound tasks e.g. mathematical computations, large data processing » Processes have separate memory spaces » Advantage: Bypasses the GIL for…”

### Spark task multithreading best

**Multithreading is best for IO. » If you have CPU heavy tasks, use multiprocessing with n_process = n_cores and never more.**
Confidence 0.77 · active · 1 source · when: If you have CPU heavy tasks
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p49:3` — “» There can only be one thread running at any given time in a python process. » Multiprocessing is parallelism. Multithreading is concurrency. » Multiprocessing is for increasing speed.…”

### Spark task never io

**Never! » If you have IO heavy tasks, use multithreading with n_threads = m * n_cores with m a number bigger than 1 that you can tweak on your own. » Try many values and choose the one with the best speedup because there isn't a general rule.**
Confidence 0.77 · active · 1 source · when: If you have IO heavy tasks
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p49:3` — “» There can only be one thread running at any given time in a python process. » Multiprocessing is parallelism. Multithreading is concurrency. » Multiprocessing is for increasing speed.…”

### Stream processing allows companies

**» Stream processing allows companies to process data as it's generated and not hours after the fact as is common with batch processing.**
Confidence 0.70 · active · 1 source · when: after the fact as is common with batch processing
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p21:3` — “» Stream processing allows companies to process data as it's generated and not hours after the fact as is common with batch processing.”

### Thread running given time

**» There can only be one thread running at any given time in a python process. » Multiprocessing is parallelism.**
Confidence 0.77 · active · 1 source
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p49:3` — “» There can only be one thread running at any given time in a python process. » Multiprocessing is parallelism. Multithreading is concurrency. » Multiprocessing is for increasing speed.…”

### Waiting downloads files databases

**Good for waiting: downloads, files, databases (I/O) computing: CPU-bound Python code.**
Confidence 0.70 · active · 1 source · when: for waiting : downloads
Evidence: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p48:18` — “Good for waiting: downloads, files, databases (I/O) computing: CPU-bound Python code”

## Contested

These claims received observations that pull in the opposite direction. They are not settled.

- **In the warm-up we saw that threads bring no speed-up for CPU-bound Python code, because of the Global Interpreter Lock (GIL).** Confidence 0.53, status disputed.
  - against: `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf#p31:1` — “Global Interpreter Lock (GIL)”
  - against: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p81:1` — “Global Interpreter Lock (GIL)”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |
| `session-01/01_do_you_need_a_cluster.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 4 | 2026-11-25 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 9 | 2026-11-25 |
| `session-04/03_duckdb_database.ipynb` | notebook | 0.86 | 1 | 2026-10-28 |
| `raw/20260926-FH-Kufstein-Big Data-Processing-2.pdf` | lecture_note | 0.92 | 19 | 2026-11-25 |
| `session-01/02_bonus_python_without_gil.ipynb` | notebook | 0.86 | 11 | 2026-10-28 |
| `04_mock_exam-gitdiff.md` | exam | 0.95 | 1 | 2026-11-25 |
| `raw/04_mock_exam.md` | exam | 0.95 | 1 | 2026-11-25 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |
| `session-01/00_warmup_threads_vs_processes.ipynb` | notebook | 0.86 | 9 | 2026-10-28 |

## Related Pages

- [[engines-single_machine|Single-Machine Engines]] (31 shared entities)
- [[data-formats|File Formats]] (16 shared entities)
- [[unfiled|Unfiled Observations]] (14 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (11 shared entities)
- [[course-dataset|NYC Yellow Taxi Dataset]] (11 shared entities)
- [[spark-architecture|Spark Architecture]] (11 shared entities)

## Open Questions

11 prompts from the material are collected in [[questions/python-execution|Questions: Python Execution Model]].
- A4 (2 P) What is the Global Interpreter Lock (GIL) in CPython, and what does it prevent?
- A5 (2 P) Threads or processes? Give one word and a half-sentence reason for each: (a) downloading 200 files from an API, (b) a pure-Python…
- 1 · Chores 2 · CPU-bound 3 · I/O-bound Waiting tasks: single thread, threads, Why do threads bring no speed-up?

## Timeline

- 2026-11-25: new_claim on `claim_fa6e3524`
- 2026-11-25: new_claim on `claim_5001acbe`
- 2026-11-25: new_claim on `claim_e5d27670`
- 2026-11-25: new_claim on `claim_adf70625`
- 2026-11-25: new_claim on `claim_5dee5fee`
- 2026-11-25: support_update on `claim_5dee5fee` (0.83 → 0.96)
- 2026-11-25: new_claim on `claim_b6fec17a`
- 2026-11-25: new_claim on `claim_61490bda`
