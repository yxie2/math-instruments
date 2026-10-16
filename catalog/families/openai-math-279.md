---
id: openai-math-279
record_type: family
title: Dyadic probability completion and filters evaluated after a verified run
source_family: '279'
source_collection: openai/math
batch_id: B016
subject: Mathematical physics
source_paper_ids:
- P-000136
instrument_ids:
- MI-000232
- MI-000233
headline: The source claims uniformly polynomial-time exact integer factoring, with probability one and
  a fixed finite gate set, using verifiable auxiliary factorizations to reconstruct transition probabilities.
central_instrument: A rare uniform-guess branch fills the exact remainder left by downward dyadic rounding.
  Deferred filters give a known product success probability without conditioning on eventual completion.
novelty_assessment: Amplitude amplification and coherent retention of classical records are established.
  The dyadic completion and same-run deferred-filter interface are candidate reusable refinements. Their
  extraction does not certify the order-trial or complete factoring construction.
formalization_summary: The scope document and ExactQuantumFactoring.lean Comparator statement were read.
  The statement specifies a length-uniform generator over a finite gate alphabet, bounded-arity wires
  and Born probability one for canonical prime-factor output. It is a target statement, not a kernel-checked
  solution; no Lean project was built.
statement_faithfulness: Retention appends a flag and never renormalizes the state. Every workspace register
  must remain available for inversion. The verified auxiliary data are generated within the process and
  must determine the true predicates uniquely.
dependencies: Dyadic sampling by Hadamard bits and reversible arithmetic, exact probability reconstruction,
  orthogonal classical histories and ordinary two-reflection amplitude amplification.
antecedents: Brassard-Hoyer-Mosca-Tapp provides the standard amplification framework; the source separately
  uses Miller-Shor factoring reductions and Pratt-style recursive auxiliary data.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Dyadic probability completion and filters evaluated after a verified run

## Source manuscript and claim

[Exact quantum factoring over a fixed finite gate set](../papers/P-000136.md), by OpenAI, September 25, 2026.

The source claims uniformly polynomial-time exact integer factoring, with probability one and a fixed finite gate set, using verifiable auxiliary factorizations to reconstruct transition probabilities.

## Extracted instruments

- [MI-000232: Dyadic rounding plus a rare canonical guess calibrates success exactly](../instruments/MI-000232.md)
- [MI-000233: Deferred filters yield a product success law on the same recorded adaptive run](../instruments/MI-000233.md)

## Dependencies and antecedents

Dyadic sampling by Hadamard bits and reversible arithmetic, exact probability reconstruction, orthogonal classical histories and ordinary two-reflection amplitude amplification.

Brassard-Hoyer-Mosca-Tapp provides the standard amplification framework; the source separately uses Miller-Shor factoring reductions and Pratt-style recursive auxiliary data. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the model, transition interface and complete exactness section, plus the Comparator scope. The order transform, majorant construction, full process proof and primality appendix were not audited.

The scope document and ExactQuantumFactoring.lean Comparator statement were read. The statement specifies a length-uniform generator over a finite gate alphabet, bounded-arity wires and Born probability one for canonical prime-factor output. It is a target statement, not a kernel-checked solution; no Lean project was built.

Retention appends a flag and never renormalizes the state. Every workspace register must remain available for inversion. The verified auxiliary data are generated within the process and must determine the true predicates uniquely.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/279.md) · [Batch record](../../batches/B016/README.md)
