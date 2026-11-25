---
title: GIL
type: entity
entity_id: ent_gil
entity_type: concept
claim_ids:
  - claim_af9a5b8d
  - claim_1a0fc8d5
  - claim_5b33ee68
  - claim_8d7591e3
  - claim_b0affde9
  - claim_573e711b
  - claim_ae291429
  - claim_875dccdd
  - claim_52d2f069
  - claim_fbfe301b
  - claim_3ed72880
  - claim_fc2762ef
confidence: 0.692
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_46087206
  - src_9e752903
  - src_b3356305
  - src_c65c80a3
  - src_ffd1cdcc
---

# GIL

Type: concept. Mentioned in 12 claims across 3 topics.
Aliases: Global Interpreter Lock, global interpreter lock.

## Claims

- **Part: A — Topic: Foundations: Big Data, scaling, GIL, threads vs. processes; Points: 12.** Confidence 0.83 · [[course-exam|Exam]]
- **Run: 1 — Python: 3.12, normal build (our kernel); GIL: always on.** Confidence 0.75 · [[python-execution|Python Execution Model]]
- **Folder: session-01/ — Topic: Do you really need a cluster? Threads vs. processes, pandas vs. Polars vs. DuckDB, Parquet vs. CSV, bonus: Python without the GIL; Runs on: laptop.** Confidence 0.73 · [[engines-single_machine|Single-Machine Engines]]
- **Work type: CPU-bound Python code — Use: processes; Why: each process has its own GIL – but no shared memory.** Confidence 0.69 · [[python-execution|Python Execution Model]]
- **Work type: waiting / I/O — Use: threads; Why: the GIL is released while waiting.** Confidence 0.69 · [[python-execution|Python Execution Model]]
- **Before we compare big-data engines, we need one fact about Python: the Global Interpreter Lock (GIL) lets only one thread execute Python code at a time.** Confidence 0.69 · [[python-execution|Python Execution Model]]
- **You cannot switch the GIL off in the normal build – you need that separate build.** Confidence 0.69 · [[python-execution|Python Execution Model]]
- **Why are Polars and DuckDB faster even on the same single machine? (Think: GIL, cores, columnar layout, lazy plans.).** Confidence 0.67 · [[engines-single_machine|Single-Machine Engines]]
- **In the warm-up we saw that threads bring no speed-up for CPU-bound Python code, because of the Global Interpreter Lock (GIL).** Confidence 0.63 · [[python-execution|Python Execution Model]]
- **Outlook: Python 3.13+ offers an experimental free-threaded build without the GIL (PEP 703).** Confidence 0.63 · [[python-execution|Python Execution Model]]
- **Polars (Rust) and DuckDB (C++) run their work outside the GIL on all cores – no multiprocessing tricks needed.** Confidence 0.63 · [[python-execution|Python Execution Model]]
- **Not every library is ready yet. If you import a C extension that is not marked as free-threading-safe, Python switches the GIL back on and prints a warning.** Confidence 0.61 · [[python-execution|Python Execution Model]]

## Related Entities

- [[duckdb|DuckDB]] (3)
- [[polars|Polars]] (3)
- [[topic|topic]] (2)
- [[big_data|Big Data]] (1)
- [[csv|CSV]] (1)
- [[jupyter|Jupyter]] (1)
- [[parquet|Parquet]] (1)
- [[pandas|pandas]] (1)
