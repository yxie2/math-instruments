---
id: openai-math-125
record_type: family
title: Population radii and exact feature-preserving compression
source_family: '125'
source_collection: openai/math
batch_id: B050
subject: Theoretical computer science
source_paper_ids:
- P-000277
- P-000278
instrument_ids:
- MI-000498
- MI-000499
headline: The sources claim single-exponential recovery for metric k-median and a deterministic approximation
  threshold of 1+2/e.
central_instrument: Population-normalized radii amortize expensive guesses across disjoint client balls.
  Affine elimination compresses state distributions while preserving specified statistics exactly.
novelty_assessment: Sampling and dummy centers have a CGLSS antecedent; feature compression is constructive
  Caratheodory. The source population-budget interface is recorded without an exhaustive novelty claim.
formalization_summary: The targets include proxy-assisted exact-budget recovery on bounded integral metrics,
  randomized approximation below two, and deterministic 1+2/e+epsilon approximation with an infimum threshold
  conditional on P not equal NP. The scope document and all linked Comparator definitions and targets
  were read. Their main target proofs contain sorry; no solution or Lean project was built.
statement_faithfulness: The radius budget uses persistent previously added leaves and the total comparison
  cost P. Feature compression preserves listed expectations and statewise properties, not arbitrary subsequent
  adaptive behavior.
dependencies: Metric triangle inequality, distance-to-set Lipschitzness, closed-ball populations, geometric
  menu probabilities; rational nullspaces and affine dependencies.
antecedents: Cohen-Addad-Grandoni-Lee-Schwiegelshohn-Svensson recovery and dummy centers; Bayer-Teichmann
  moment matching and Caratheodory.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Population radii and exact feature-preserving compression

## Source manuscripts and claim

- [Single-exponential recovery and bounded-price strictness for metric k-median](../papers/P-000277.md): selected passages extracted.
- [The approximation threshold for metric k-median](../papers/P-000278.md): selected passages extracted.

The sources claim single-exponential recovery for metric k-median and a deterministic approximation threshold of 1+2/e.

## Extracted instruments

- [MI-000498: Pay for rare radius guesses with disjoint client populations](../instruments/MI-000498.md)
- [MI-000499: Compress a finite distribution while preserving chosen rational features](../instruments/MI-000499.md)

## Dependencies and antecedents

Metric triangle inequality, distance-to-set Lipschitzness, closed-ball populations, geometric menu probabilities; rational nullspaces and affine dependencies.

Cohen-Addad-Grandoni-Lee-Schwiegelshohn-Svensson recovery and dummy centers; Bayer-Teichmann moment matching and Caratheodory.

## Review and formalization scope

Read the full computable-radius, dummy-metric, radius-budget and guided-trajectory arguments, and the companion affine-support-reduction proof. The global recovery and approximation algorithms remain outside these checks.

The targets include proxy-assisted exact-budget recovery on bounded integral metrics, randomized approximation below two, and deterministic 1+2/e+epsilon approximation with an infimum threshold conditional on P not equal NP. The scope document and all linked Comparator definitions and targets were read. Their main target proofs contain sorry; no solution or Lean project was built.

The radius budget uses persistent previously added leaves and the total comparison cost P. Feature compression preserves listed expectations and statewise properties, not arbitrary subsequent adaptive behavior.

[Batch record](../../batches/B050/README.md)
