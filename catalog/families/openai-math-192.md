---
id: openai-math-192
record_type: family
title: Reporting by cancellation and amplification of retained variance per degree
source_family: '192'
source_collection: openai/math
batch_id: B011
subject: Combinatorics
source_paper_ids:
- P-000118
instrument_ids:
- MI-000194
- MI-000195
headline: The source claims Boolean functions whose signed singleton Fourier sum exceeds any prescribed
  constant times the square root of real multilinear degree.
central_instrument: An exceptional report depends on all coordinates but has an indicator decomposing
  into terms that each omit one coordinate. A positive variance gain for this reporting rule can be amplified
  through finite averages and read out as a Boolean Fourier correlation.
novelty_assessment: Conditional-expectation projection, degree subadditivity, the central limit theorem
  and uniform integrability are established. The selected candidate combination is the reporting cancellation
  with a rare Gaussian gain and its iterative degree-to-variance conversion.
formalization_summary: SquareRootDegree.lean states both unbounded signed violations and unbounded absolute
  singleton-sum-to-square-root-degree ratios for positive-degree Boolean functions on finite sign cubes.
  Scope documents and Comparator statements were compared. No Lean solution was built or kernel-checked,
  and the extracted auxiliary results are not separately certified Comparator targets.
statement_faithfulness: Cell indicators have bounded real multilinear degree; they need not be subcubes
  or depend on a fixed small coordinate set. The singleton coefficients are summed, not squared. Every
  stage is finite, but useful dimension bounds are not provided.
dependencies: Finite observation partitions; conditional scores; output-indicator degree bounds; a cancellation
  identity; independent variance-one inputs; Gaussian interval estimates; finite-stage normal approximation
  and a sign readout.
antecedents: O’Donnell-Servedio and Blais-Tan-Wan use conditional coordinate sums for decision-tree inequalities.
  Standard probability supplies the score projection, central limit theorem and moment transfer. The source
  distinguishes these query-depth settings from general low-degree cells.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Reporting by cancellation and amplification of retained variance per degree

## Source manuscript and claim

[Unbounded Violations of the Square-Root Degree Bound](../papers/P-000118.md), by OpenAI, September 26, 2026.

The source claims Boolean functions whose signed singleton Fourier sum exceeds any prescribed constant times the square root of real multilinear degree.

## Extracted instruments

- [MI-000194: A cancellation report saves degree while retaining more than the revealed-coordinate variance](../instruments/MI-000194.md)
- [MI-000195: Finite observation scores amplify a variance-to-degree advantage into Boolean correlation](../instruments/MI-000195.md)

## Dependencies and antecedents

Finite observation partitions; conditional scores; output-indicator degree bounds; a cancellation identity; independent variance-one inputs; Gaussian interval estimates; finite-stage normal approximation and a sign readout.

O’Donnell-Servedio and Blais-Tan-Wan use conditional coordinate sums for decision-tree inequalities. Standard probability supplies the score projection, central limit theorem and moment transfer. The source distinguishes these query-depth settings from general low-degree cells. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the finite-observation calculus, amplification criterion, reporting rule, Gaussian interval construction and finite-input transfer. Later mean-cost, weighted-mixture and small-width variants were not audited.

SquareRootDegree.lean states both unbounded signed violations and unbounded absolute singleton-sum-to-square-root-degree ratios for positive-degree Boolean functions on finite sign cubes. Scope documents and Comparator statements were compared. No Lean solution was built or kernel-checked, and the extracted auxiliary results are not separately certified Comparator targets.

Cell indicators have bounded real multilinear degree; they need not be subcubes or depend on a fixed small coordinate set. The singleton coefficients are summed, not squared. Every stage is finite, but useful dimension bounds are not provided.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/192.md) · [Batch record](../../batches/B011/README.md)
