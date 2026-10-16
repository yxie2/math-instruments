---
id: openai-math-020
record_type: family
title: Adaptive prime deletion and weighted Hilbert counts
source_family: '020'
source_collection: openai/math
batch_id: B007
subject: Number theory
source_paper_ids:
- P-000101
instrument_ids:
- MI-000158
- MI-000159
headline: The source claims positive-density (d-2)-free values for every irreducible integer polynomial
  of degree d>=4 with no fixed prime (d-2)-power divisor. Its new large-prime analysis concerns degrees
  four through eight; higher degrees use earlier results.
central_instrument: Keeping full evaluation kernels produces a monotone finite rank record for adaptive
  prime deletion. Selected conjugate pairs yield a weighted complete intersection with an explicit leading
  Hilbert coefficient.
novelty_assessment: Determinant methods, Hilbert series and function-field dimension arguments are established.
  The adaptive deletion construction and the explicit paired-coordinate Hilbert calculation are candidate
  source-specific packages. The global power-free theorem and priority are not certified.
formalization_summary: PowerFreeValues.lean states convergence to a positive Euler-product density for
  irreducible polynomials over Q of degree at least four, with k=d-2 and the local admissibility hypothesis.
  The scope document and Comparator declarations were compared, but no Lean solution was built or kernel-checked.
  The extracted auxiliary mechanisms are not separate Comparator statements.
statement_faithfulness: The formalized statement allows nonmonic and nonprimitive integer polynomials,
  negative values and positive integer inputs; zero is not power-free. The source uses a separate content-transfer
  argument. Simultaneous polynomial conditions use unions of bad residues, not the product of individual
  density constants.
dependencies: Deterministic patch selection; full bounded-degree evaluation kernels; polynomial-size nonzero
  minors; random subsets of large auxiliary primes; weighted homogenization, complete intersections and
  bounded-degree projection estimates.
antecedents: Heath-Brown, Salberger, Browning and Xiao supply the determinant-method and power-free background.
  The source explicitly separates its low-degree analysis from Browning and Xiao results already sufficient
  in degree at least nine.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive prime deletion and weighted Hilbert counts

## Source manuscript and claim

[Squarefree values of quartics and power-free values of polynomials](../papers/P-000101.md), by OpenAI, None.

The source claims positive-density (d-2)-free values for every irreducible integer polynomial of degree d>=4 with no fixed prime (d-2)-power divisor. Its new large-prime analysis concerns degrees four through eight; higher degrees use earlier results.

## Extracted instruments

- [MI-000158: A monotone rank record controls bad primes chosen adaptively](../instruments/MI-000158.md)
- [MI-000159: Selected coordinate pairs give a uniform weighted Hilbert coefficient](../instruments/MI-000159.md)

## Dependencies and antecedents

Deterministic patch selection; full bounded-degree evaluation kernels; polynomial-size nonzero minors; random subsets of large auxiliary primes; weighted homogenization, complete intersections and bounded-degree projection estimates.

Heath-Brown, Salberger, Browning and Xiao supply the determinant-method and power-free background. The source explicitly separates its low-degree analysis from Browning and Xiao results already sufficient in degree at least nine. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the adaptive-path construction and deletion proof, and the weighted-Hilbert proposition with its affine and infinity boundary arguments. The full counting theorem, quartic exceptional curves and finite parameter certificate were not independently audited.

PowerFreeValues.lean states convergence to a positive Euler-product density for irreducible polynomials over Q of degree at least four, with k=d-2 and the local admissibility hypothesis. The scope document and Comparator declarations were compared, but no Lean solution was built or kernel-checked. The extracted auxiliary mechanisms are not separate Comparator statements.

The formalized statement allows nonmonic and nonprimitive integer polynomials, negative values and positive integer inputs; zero is not power-free. The source uses a separate content-transfer argument. Simultaneous polynomial conditions use unions of bad residues, not the product of individual density constants.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/020.md) · [Batch record](../../batches/B007/README.md)
