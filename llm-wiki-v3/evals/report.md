# Eval report

Generated 2026-11-25T12:17:18Z

## Retrieval (evidence span -> claim)

| Metric | Value |
|---|---|
| queries | 80 |
| recall_at_1 | 0.525 |
| recall_at_5 | 0.838 |
| recall_at_10 | 0.85 |
| mrr | 0.648 |

## State update cases

| Case | Pass | Detail |
|---|---|---|
| support raises a new claim above the prior | pass | probability=0.8151 |
| independent support accumulates | pass | 0.82 -> 0.95 |
| same-source evidence does not double count | pass | 0.95 -> 0.95 |
| contradiction lowers probability | pass | 0.95 -> 0.82 |
| contradiction opens a conflict | pass | conflicts=1 |
| contradicted claim is disputed | pass | status=disputed |
| supersession keeps the old claim | pass | superseded=1 |
| supersession links old and new | pass | superseded_by set |
| superseded claim loses probability | pass | p=0.25 |
| decay lowers an unconfirmed claim | pass | 0.95 -> 0.73, freshness 0.2567 |
| transitions are written | pass | transitions=3 |

## Faithfulness

- pass — every claim id on a page exists in state (unknown=0 [])
- pass — rendered claims contain their text (mismatch=0 [])
- pass — evidence entries are attached to their claim (orphan evidence=0)
- pass — superseded claims are not presented as current (violations=0)

Pages checked: 120 · claims checked: 2048

## Governance

- pass — audit log is written (events=1)
- pass — every transition has an actor and an operation (invalid=0)
- pass — every claim has provenance (claims without source=0)
- pass — raw copies match their recorded hash (mismatches=0)
- pass — no private-only text appears in a rendered page (private claims=89 leaks=0)
- pass — private claims are stored apart from public claims (mixed=0)

Failures: 0
