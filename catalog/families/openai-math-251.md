---
id: openai-math-251
record_type: family
title: Indexed-edge operator bounds and protected metric transfers
source_family: '251'
source_collection: openai/math
batch_id: B059
subject: Group theory
source_paper_ids:
- P-000345
- P-000346
instrument_ids:
- MI-000576
- MI-000577
headline: The sources claim that unitarizability is equivalent to amenability and that strong Ulam stability
  characterizes amenability.
central_instrument: A factorization through separately indexed edges bounds masked rank-one operators
  even with repeated group labels. Schur complements construct metric isometries preserving a designated
  subspace, and polar correction makes an approximately fixed subspace exact.
novelty_assessment: Frame factorization, Schur-complement whitening and polar decomposition are classical.
  The retained-label and protected-subspace interfaces are explicit source implementations. No equivalence
  with amenability is certified.
formalization_summary: DixmierAllDiscrete states amenability/unitarizability equivalence for all discrete
  groups and nonunitarizable witnesses bounded by 1+epsilon, with separability for countable groups. Dixmier
  separately states a separable witness bounded by 101 for countable nonamenable groups. There is no linked
  strong-Ulam-stability Comparator. The scope document and all linked Comparators were read in full. Their
  headline targets have sorry proof bodies; some supporting definitions contain explicit proofs. No separate
  solution or Lean project was built.
statement_faithfulness: Both row and incoming-column sparsity are required. The transfer projection commutes
  with the reference metric and has small compressed perturbation; preservation means mapping the subspace
  onto itself, not preserving its original orthogonal complement.
dependencies: Synthesis/analysis operators, Hilbert direct sums, positive square roots, Schur complements,
  spectral calculus and polar decomposition.
antecedents: Classical frame bounds and block Gaussian elimination; Higham, Computing the Polar Decomposition
  with Applications, elementary polar formulas.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Indexed-edge operator bounds and protected metric transfers

## Source manuscripts and claim

- [Unitarizability implies amenability for discrete groups](../papers/P-000345.md): selected passages extracted.
- [Strong Ulam Stability Characterizes Amenability](../papers/P-000346.md): selected passages extracted.

The sources claim that unitarizability is equivalent to amenability and that strong Ulam stability characterizes amenability.

## Extracted instruments

- [MI-000576: Factor a sparse masked operator through edges with their labels retained](../instruments/MI-000576.md)
- [MI-000577: Transfer nearby metrics while protecting a prescribed subspace](../instruments/MI-000577.md)

## Dependencies and antecedents

Synthesis/analysis operators, Hilbert direct sums, positive square roots, Schur complements, spectral calculus and polar decomposition.

Classical frame bounds and block Gaussian elimination; Higham, Computing the Polar Decomposition with Applications, elementary polar formulas.

## Review and formalization scope

Read the complete indexed-mask proof and the full prescribed-subspace transfer and exact-fixing lemmas. Boundary actions, sparse flags, circuit comparisons and nonunitarizability obstructions remain unaudited.

DixmierAllDiscrete states amenability/unitarizability equivalence for all discrete groups and nonunitarizable witnesses bounded by 1+epsilon, with separability for countable groups. Dixmier separately states a separable witness bounded by 101 for countable nonamenable groups. There is no linked strong-Ulam-stability Comparator. The scope document and all linked Comparators were read in full. Their headline targets have sorry proof bodies; some supporting definitions contain explicit proofs. No separate solution or Lean project was built.

Both row and incoming-column sparsity are required. The transfer projection commutes with the reference metric and has small compressed perturbation; preservation means mapping the subspace onto itself, not preserving its original orthogonal complement.

[Batch record](../../batches/B059/README.md)
