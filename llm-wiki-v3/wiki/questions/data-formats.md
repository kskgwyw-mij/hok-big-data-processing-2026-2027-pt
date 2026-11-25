---
title: Questions: File Formats
type: questions
topic: data.formats
question_count: 22
last_rendered: 2026-11-25T12:17:11Z
---

# Questions: File Formats

Prompts extracted from the material. No answers are stored: the state holds claims, not solutions, so these stay open until someone writes a claim with evidence.

## Big Data Processing – Mock exam / Part A – Foundations

- A6 (4 P) Your team has an 8 GB Parquet dataset (one year of trips) and laptops with 16 GB RAM and 8 cores. A colleague wants to rent a Spark cluster for the weekly report. Argue for or against it: name a single-machine tool you would try first and why it can work, two reasons why distributed systems are harder, and one situation in which the cluster would be justified.
  - `raw/04_mock_exam.md:33` · exam_prompt

## Big Data Processing – Mock exam / Part C – Python environments, file formats, DuckDB

- C1 (1 P) Which of these formats are columnar: CSV, JSON, Avro, Parquet, ORC?
  - `raw/04_mock_exam.md:64` · exam_prompt
- C2 (1 P) Which row-oriented binary format with an embedded schema is commonly used for Kafka events?
  - `raw/04_mock_exam.md:66` · exam_prompt
- C5 (2 P) Why is it dangerous to load a pickle file from an unknown source?
  - `raw/04_mock_exam.md:72` · exam_prompt

## General

- » Name three disadvantages of CSV you measured in Lab B, each with your number. » Which of CSV, pickle and Parquet keep category and nullable-integer dtypes?
  - `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p21:3` · open_question

## Session 2 – Apache Spark Fundamentals / Exit Ticket – Individual, no AI

- Does this mean Spark only read 10 rows from the Parquet file?
  - `session-02/02_spark_fundamentals.ipynb#cell-43:48` · open_question

## Session 2 – Apache Spark Fundamentals / Part 2 – Reading data: from Parquet to DataFrame / Predict before you run

- Q2 – When you call spark.read.parquet(...), does Spark immediately read all the data into memory?
  - `session-02/02_spark_fundamentals.ipynb#cell-6:14` · open_question

## Session 4 · Lab B – Saving data and models: CSV vs. pickle vs. Parquet / Smaller dtypes – and who remembers them?

- From now on, every format gets the same test: write, read, size – and do the dtypes survive?
  - `session-04/02_file_formats_and_pickle.ipynb#cell-13:1` · open_question

## Session 4 · Lab B – Saving data and models: CSV vs. pickle vs. Parquet / Where pickle shines: Python objects such as trained models

- How much smaller is the file, and does loading still give identical predictions?
  - `session-04/02_file_formats_and_pickle.ipynb#cell-25:1` · open_question

## Session 4 · Lab B – Saving data and models: CSV vs. pickle vs. Parquet / Exam-style questions

- A student downloads best_model.pkl from a forum and runs pickle.load. Explain the risk in two sentences.
  - `session-04/02_file_formats_and_pickle.ipynb#cell-33:10` · exam_prompt
- True or false, with justification: "pickle is the best format for large datasets because it is fastest to read."
  - `session-04/02_file_formats_and_pickle.ipynb#cell-33:11` · exam_prompt
- A colleague stores the monthly taxi extract as CSV "because everybody can open it". Give three concrete disadvantages you observed in this lab, each with the measured effect on your machine.
  - `session-04/02_file_formats_and_pickle.ipynb#cell-33:2` · exam_prompt
- Your pandas DataFrame has a category column and nullable integers. Which of CSV, pickle and Parquet keep these types after a round trip? Explain why CSV cannot.
  - `session-04/02_file_formats_and_pickle.ipynb#cell-33:4` · exam_prompt
- On small data, loading a pickle can be as fast as reading Parquet. Why does Parquet still scale better when you only need 3 of 19 columns of a 50 GB dataset? Use the words columnar and row group statistics.
  - `session-04/02_file_formats_and_pickle.ipynb#cell-33:6` · exam_prompt
- Scenario: you trained a scikit-learn model on your laptop; the model will be used by a batch job on a server in six months. Which format do you save it in, and which two pieces of information do you store with it?
  - `session-04/02_file_formats_and_pickle.ipynb#cell-33:8` · exam_prompt

## Session 4 · Lab B – Saving data and models: CSV vs. pickle vs. Parquet / The data: one million real taxi trips

- Then think: would you want to write this for 50 columns?
  - `session-04/02_file_formats_and_pickle.ipynb#cell-9:4` · open_question

## Part 1 · Spark fundamentals / Reading Parquet into a DataFrame

- Predict before you run: does spark.read.parquet(...) read all the data into memory?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-10:6` · open_question

## Part 2 · Spark ML: how long will my taxi ride take? / Exam-style questions

- Your teammate wants to pickle.dump() the Spark PipelineModel. What do you tell them?
  - `session-04/04_spark_fundamentals_and_ml.ipynb#cell-57:23` · exam_prompt

## Session 6 · Block 2 – Kafka from Python: producers, consumers, consumer groups / Exam-style questions

- (2 P) What does a serializer do in a Kafka producer, and why does Kafka itself not care whether you send JSON, Avro or CSV?
  - `session-06/02_kafka_python.ipynb#cell-23:49` · exam_prompt

## Block 3 – Exam circuit / Station 2 – File formats and engines

- 2.1 (2 P) Sort into row-oriented and column-oriented: CSV, JSON, Avro, Parquet, ORC. Which one is typical for writing events record by record to Kafka?
  - `session-06/03_exam_circuit.md:33` · exam_prompt

## Block 3 – Exam circuit / Station 4 – Spark execution and joins: read the plan

- 4.3 (3 P) A 2 GB CSV file, spark.sql.files.maxPartitionBytes = 128 MB, a machine with 4 cores. About how many partitions and tasks, and how many "waves" of tasks? What happens if the data had only 2 partitions?
  - `03_exam_circuit-gitdiff.md:178` · exam_prompt

## gitdiff / Station 4 – Spark execution: lazy evaluation and shuffles

- 4.3 (3 P) A 2 GB CSV file, spark.sql.files.maxPartitionBytes = 128 MB, a machine with 4 cores. About @@ -0,0 +1,127 @@
  - `03_exam_circuit-gitdiff.md:301` · exam_prompt
