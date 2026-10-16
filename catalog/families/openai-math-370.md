---
id: openai-math-370
record_type: family
title: Keep weights and midpoint displacement in localized potential estimates
source_family: '370'
source_collection: openai/math
batch_id: B027
subject: Partial differential equations
source_paper_ids:
- P-000181
instrument_ids:
- MI-000324
- MI-000325
headline: The source claims nonexistence of positive entire subcritical Henon-Lane-Emden pairs in every
  dimension n>=2, with arbitrary real weights and positive exponents under its stated regularity.
central_instrument: A paired potential identity retains spatial weights under a compact cutoff. An interval-overlap
  comparison controls endpoint defects even when interval midpoints do not coincide.
novelty_assessment: Rellich-Pohozaev identities and one-dimensional integration by parts are established
  methods. These selected weighted formulations are inspected without certifying the source global nonexistence
  theorem or claiming a first discovery.
formalization_summary: Read HenonEmden.lean and its scope. Solutions are continuous globally and C2 off
  the origin; equations are required away from zero, p and q are individually positive, and the strict
  weighted subcritical inequality excludes equality. The inspected Comparator ends in sorry. It is a target
  statement, not a Lean proof built or kernel-checked here.
statement_faithfulness: The extracted virial identity uses n>=3, weights A,B>-2 and exact Newtonian potentials
  after the source reductions. The interval comparison retains midpoint displacement and defines zero-weight
  unbounded endpoint terms without subtracting infinities.
dependencies: Tonelli and Fubini under established convergence, weighted integration by parts, Newton-kernel
  homogeneity, interval overlap and odd-function pairing.
antecedents: Classical Rellich-Pohozaev identities; source references weighted identities of Phan and
  system identities of Mitidieri and Souplet. Their full primary proofs were not separately audited in
  this batch.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Keep weights and midpoint displacement in localized potential estimates

## Source manuscript and claim

[The Subcritical Hénon–Lane–Emden Conjecture](../papers/P-000181.md), by OpenAI, September 24, 2026.

The source claims nonexistence of positive entire subcritical Henon-Lane-Emden pairs in every dimension n>=2, with arbitrary real weights and positive exponents under its stated regularity.

## Extracted instruments

- [MI-000324: Pair two potential gradients before estimating a localized virial term](../instruments/MI-000324.md)
- [MI-000325: Control interval endpoint defects using the sign of midpoint displacement](../instruments/MI-000325.md)

## Dependencies and antecedents

Tonelli and Fubini under established convergence, weighted integration by parts, Newton-kernel homogeneity, interval overlap and odd-function pairing.

Classical Rellich-Pohozaev identities; source references weighted identities of Phan and system identities of Mitidieri and Souplet. Their full primary proofs were not separately audited in this batch. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete localized virial and interval-pair proofs and the parameter definitions. Initial reductions, exact potential representation, pressure estimates and final uniform energy bound were not audited.

Read HenonEmden.lean and its scope. Solutions are continuous globally and C2 off the origin; equations are required away from zero, p and q are individually positive, and the strict weighted subcritical inequality excludes equality. The inspected Comparator ends in sorry. It is a target statement, not a Lean proof built or kernel-checked here.

The extracted virial identity uses n>=3, weights A,B>-2 and exact Newtonian potentials after the source reductions. The interval comparison retains midpoint displacement and defines zero-weight unbounded endpoint terms without subtracting infinities.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/370.md) · [Batch record](../../batches/B027/README.md)
