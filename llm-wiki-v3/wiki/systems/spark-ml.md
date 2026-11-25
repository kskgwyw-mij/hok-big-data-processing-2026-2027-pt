---
title: Spark ML
type: systems
topic: spark.ml
entity_ids:
  - ent_estimator
  - ent_rmse
  - ent_spark
  - ent_transformer
  - ent_crossvalidator
  - ent_csv
  - ent_scikit_learn
  - ent_spark_ml
  - ent_vectorassembler
  - ent_ansi
  - ent_automatic_sorting
  - ent_batch_processing
claim_ids:
  - claim_aed304ab
  - claim_1dedc141
  - claim_f5dbba71
  - claim_57806f5d
  - claim_c7089dbd
  - claim_9b577afc
  - claim_fd59cbd1
  - claim_44546246
  - claim_32f26968
  - claim_6b23e9e7
  - claim_e48070b2
  - claim_ec3966df
  - claim_67656973
  - claim_5b788979
  - claim_05d87fd6
  - claim_fbb6eaf3
  - claim_4167573d
  - claim_8f0e589a
  - claim_bcfa37d1
  - claim_a7647619
confidence: 0.703
status: active
last_rendered: 2026-11-25T12:17:11Z
sources:
  - src_1cebb3bb
  - src_47132aab
  - src_59b6ded4
  - src_68fcf2b9
  - src_fc0bfe80
review_required: false
---

# Spark ML

Rendered from 20 claims and 5 sources. Median confidence 0.70; 19 active, 0 disputed, 0 superseded.

## Current Understanding

### Hyper parameter tuning crossvalidator

**Your turn (5 min): evaluate the best model (cv_model.bestModel) on the test set with three metrics: RMSE, MAE and R².**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-49:1` — “Your turn (5 min): evaluate the best model (cv_model.bestModel) on the test set with three metrics: RMSE, MAE and R². Hint: rmse.evaluate(pred, {rmse.metricName: "mae"}) overrides the…”

**TODO: compute rmse, mae and r2 with the evaluator rmse and its metricName parameter.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-50` — “TODO: compute rmse, mae and r2 with the evaluator rmse and its metricName parameter”

### Spark ml four words

**Spark ML wants all features in one vector column (VectorAssembler).**
Confidence 0.81 · active · 2 sources
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p36:14` — “You know this from scikit-learn: fit = Estimator, transform = Transformer. New: all features must sit in one vector column.”

**Concept: Transformer — What it does: .transform(df) → new DataFrame with extra column(s); scikit-learn analogue: transform().**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-43:6` — “Pipeline | chain of stages; itself an Estimator | sklearn.pipeline.Pipeline”

### Crossvalidator m trips cleaned

**12.7 M trips, cleaned Pipeline to saved model CSV vs. Parquet · data quality in one pass · ANSI mode · Baseline · Pipeline · CrossValidator · gradient-boosted trees · features save().**
Confidence 0.74 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p39:7` — “12.7 M trips, cleaned Pipeline to saved model CSV vs. Parquet · data quality in one pass · ANSI mode · Baseline · Pipeline · CrossValidator · gradient-boosted trees · features save()”

### Data leakage information future

**Using information from the future = target leakage: great test score, useless in practice.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p38:17` — “Using information from the future = target leakage: great test score, useless in practice.”

### Data modelling level sql

**» Level 1: SQL & Python & Data Modelling & Data Pipeline.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p23:3` — “» Level 1: SQL & Python & Data Modelling & Data Pipeline”

### Decouples applications immutable data

**This decouples applications from each other » Immutable data provides pipeline repeatability.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p35:3` — “» Faster calculations on windowed data (real-time) » More scalable due to distributed nature of data stores » Decouples how data is used from how it is produced. This decouples…”

### Kafka uber uses

**» Uber uses Kafka extensively in their real-time pricing pipeline.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf#p49:3` — “» Uber uses Kafka extensively in their real-time pricing pipeline.”

### Key features

**» Key Features: » Scalability » Fault tolerance » Distributed storage.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p54:8` — “» Key Features: » Scalability » Fault tolerance » Distributed storage”

### Level talk stakeholders writing

**» Level 4: Talk to Stakeholders before writing pipelines (communication).**
Confidence 0.70 · active · 1 source · when: before writing pipelines (communication)
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p23:10` — “» Level 4: Talk to Stakeholders before writing pipelines (communication)”

### Linearregression estimator transformer

**Estimator Estimator Transformer Estimator StringIndexer OneHotEncoder VectorAssembler LinearRegression hour → index index → 0/1 vector all → "features" learns weights.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p40:3` — “» read.csv returned instantly, count() took much longer. Explain with transformation, action and lazy evaluation. » Narrow or wide: filter, withColumn, groupBy().agg(), orderBy, select.…”

### Monitoring automatic alerts health

**» Monitoring: automatic alerts about the health of the data and the pipeline, needed for proactive response to potential business risks.**
Confidence 0.70 · active · 1 source · when: for proactive response to potential business risks
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p27:12` — “» Monitoring: automatic alerts about the health of the data and the pipeline, needed for proactive response to potential business risks.”

### Pickle pipeline fit return parameter

**What does Pipeline.fit() return? » 3 × 2 parameter grid, numFolds = 5: how many models are trained? » Your teammate wants to pickle.dump() the Spark PipelineModel.**
Confidence 0.76 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p40:3` — “» read.csv returned instantly, count() took much longer. Explain with transformation, action and lazy evaluation. » Narrow or wide: filter, withColumn, groupBy().agg(), orderBy, select.…”

### Scikit learn know fit

**You know this from scikit-learn: fit = Estimator, transform = Transformer.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p36:14` — “You know this from scikit-learn: fit = Estimator, transform = Transformer. New: all features must sit in one vector column.”

### Spark feature x

**Feature Spark 1.x Spark 2.x.**
Confidence 0.66 · active · 1 source
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p120:6` — “Feature Spark 1.x Spark 2.x”

### Spark fully supported backward

**» Fully supported for backward » Recommended entry point since compatibility Spark 2.0 » Use in specific scenarios or with » Provides a higher-level API and libraries/APIs reliant on it better integration with latest Spark features.**
Confidence 0.70 · active · 1 source · when: for backward » Recommended entry point since compatibility Spark 2
Evidence: `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf#p114:5` — “» Fully supported for backward » Recommended entry point since compatibility Spark 2.0 » Use in specific scenarios or with » Provides a higher-level API and libraries/APIs reliant on it…”

### Spark kaggle fundamentals ml

**Part: 2 · Spark ML — What you do: data quality, features, Pipeline, CrossValidator, saving models; Data: NYC taxi January 2015, CSV (~12.7 M trips).**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:9` — “2 · Spark ML | data quality, features, Pipeline, CrossValidator, saving models | NYC taxi January 2015, CSV (~12.7 M trips)”

### Spark task problems numerous

**» Problems: » Numerous Nodes » Complex Data Pipelines » Hardware Failures » Network Outages » Data Errors » Fault-Tolerance: » Redundant data storage » Automatic task restarts » Recovery Mechanisms.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf#p69:3` — “» Problems: » Numerous Nodes » Complex Data Pipelines » Hardware Failures » Network Outages » Data Errors » Fault-Tolerance: » Redundant data storage » Automatic task restarts » Recovery…”

### Todo haversine km

**TODO: haversine_km TODO: RMSE, MAE and R² on the test set.**
Confidence 0.70 · active · 1 source
Evidence: `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf#p39:11` — “TODO: haversine_km TODO: RMSE, MAE and R² on the test set”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `raw/20260925-FH-Kufstein-Big Data-Processing-1.pdf` | lecture_note | 0.92 | 3 | 2026-11-25 |
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-4.pdf` | lecture_note | 0.92 | 7 | 2026-11-25 |
| `raw/20261016-FH-Kufstein-Big Data-Processing-3.pdf` | lecture_note | 0.92 | 4 | 2026-11-25 |
| `raw/20261031-FH-Kufstein-Big Data-Processing-5.pdf` | lecture_note | 0.92 | 2 | 2026-11-25 |

## Related Pages

- [[data-formats|File Formats]] (13 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (12 shared entities)
- [[unfiled|Unfiled Observations]] (10 shared entities)
- [[bigdata-foundations|Big Data Foundations]] (8 shared entities)
- [[data-duckdb|DuckDB]] (7 shared entities)
- [[course-exam|Exam]] (6 shared entities)

## Open Questions

5 prompts from the material are collected in [[questions/spark-ml|Questions: Spark ML]].
- D3 (2 P) Transformer or Estimator: StringIndexer, VectorAssembler, LinearRegression. What type of object does Pipeline.fit() return?
- D4 (1 P) CrossValidator with a parameter grid of 3 × 2 values and numFolds=5. How many model fits in total, including the final refit?
- Transformer or Estimator: StringIndexer, OneHotEncoder, VectorAssembler, LinearRegression? What does Pipeline.fit() return?

## Timeline

- 2026-11-25: new_claim on `claim_5b788979`
- 2026-11-25: new_claim on `claim_05d87fd6`
- 2026-11-25: new_claim on `claim_fbb6eaf3`
- 2026-11-25: new_claim on `claim_4167573d`
- 2026-11-25: new_claim on `claim_8f0e589a`
- 2026-11-25: evidence_attached on `claim_8f0e589a` (0.70 → 0.70)
- 2026-11-25: new_claim on `claim_bcfa37d1`
- 2026-11-25: new_claim on `claim_a7647619`
