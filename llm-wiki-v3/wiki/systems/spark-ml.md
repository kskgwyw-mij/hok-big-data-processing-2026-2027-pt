---
title: Spark ML
type: systems
topic: spark.ml
entity_ids:
  - ent_rmse
  - ent_spark_ml
  - ent_crossvalidator
  - ent_csv
  - ent_estimator
  - ent_scikit_learn
  - ent_spark_stage
  - ent_transformer
  - ent_vectorassembler
claim_ids:
  - claim_aed304ab
  - claim_1dedc141
  - claim_f5dbba71
  - claim_57806f5d
  - claim_c7089dbd
confidence: 0.629
status: active
last_rendered: 2026-11-25T09:51:47Z
sources:
  - src_47132aab
review_required: false
---

# Spark ML

Rendered from 5 claims and 1 sources. Median confidence 0.63; 4 active, 0 disputed, 0 superseded.

## Current Understanding

### Hyper parameter tuning crossvalidator

**Your turn (5 min): evaluate the best model (cv_model.bestModel) on the test set with three metrics: RMSE, MAE and R².**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-49:1` — “Your turn (5 min): evaluate the best model (cv_model.bestModel) on the test set with three metrics: RMSE, MAE and R². Hint: rmse.evaluate(pred, {rmse.metricName: "mae"}) overrides the…”

**TODO: compute rmse, mae and r2 with the evaluator rmse and its metricName parameter.**
Confidence 0.55 · candidate · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-50` — “TODO: compute rmse, mae and r2 with the evaluator rmse and its metricName parameter”

### Spark ml four words

**Concept: Transformer — What it does: .transform(df) → new DataFrame with extra column(s); scikit-learn analogue: transform().**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-43:6` — “Pipeline | chain of stages; itself an Estimator | sklearn.pipeline.Pipeline”

**Spark ML wants all features in one vector column (VectorAssembler).**
Confidence 0.63 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-43:9` — “Spark ML wants all features in one vector column (VectorAssembler). First, split and set a baseline: always predict the average duration of the training set.”

### Spark kaggle fundamentals ml

**Part: 2 · Spark ML — What you do: data quality, features, Pipeline, CrossValidator, saving models; Data: NYC taxi January 2015, CSV (~12.7 M trips).**
Confidence 0.69 · active · 1 source
Evidence: `session-04/04_spark_fundamentals_and_ml.ipynb#cell-0:9` — “2 · Spark ML | data quality, features, Pipeline, CrossValidator, saving models | NYC taxi January 2015, CSV (~12.7 M trips)”

## Sources

| Source | Type | Authority | Claims | Date |
|---|---|---|---|---|
| `session-04/04_spark_fundamentals_and_ml.ipynb` | notebook | 0.86 | 5 | 2026-10-28 |

## Related Pages

- [[data-formats|File Formats]] (4 shared entities)
- [[course-exam|Exam]] (2 shared entities)
- [[course-setup|Course Setup]] (2 shared entities)
- [[engines-single_machine|Single-Machine Engines]] (2 shared entities)
- [[tooling-kaggle|Kaggle Labs]] (2 shared entities)
- [[spark-architecture|Spark Architecture]] (1 shared entities)

## Open Questions

5 prompts from the material are collected in [[questions/spark-ml|Questions: Spark ML]].
- Transformer or Estimator: StringIndexer, OneHotEncoder, VectorAssembler, LinearRegression? What does Pipeline.fit() return?
- A CrossValidator with 3 × 2 parameter values and numFolds=5: how many models are trained? Why did we tune on a sample?
- 5.3 (4 P) (a) Transformer or Estimator: StringIndexer, VectorAssembler, LinearRegression. (b) A CrossValidator with a 3 × 2 parameter grid…

## Timeline

- 2026-11-25: new_claim on `claim_aed304ab`
- 2026-11-25: new_claim on `claim_1dedc141`
- 2026-11-25: evidence_attached on `claim_1dedc141` (0.69 → 0.69)
- 2026-11-25: evidence_attached on `claim_1dedc141` (0.69 → 0.69)
- 2026-11-25: evidence_attached on `claim_1dedc141` (0.69 → 0.69)
- 2026-11-25: new_claim on `claim_f5dbba71`
- 2026-11-25: new_claim on `claim_57806f5d`
- 2026-11-25: new_claim on `claim_c7089dbd`
