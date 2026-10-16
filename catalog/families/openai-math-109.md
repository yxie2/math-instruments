---
id: openai-math-109
record_type: family
title: Rank-counted shears and retained-order synthetic Fourier transforms
source_family: '109'
source_collection: openai/math
batch_id: B035
subject: Theoretical computer science
source_paper_ids:
- P-000211
instrument_ids:
- MI-000384
- MI-000385
headline: The source claims exact integer multiplication in O(n (log n)^(1-kappa)) time on one fixed finite-tape
  Turing machine, with kappa=2^(-182).
central_instrument: Lower-triangular Bruhat factors make a rational shear cost one expensive interchange
  per rank. Synthetic Fourier transforms use signed coefficient permutations and consume their retained
  bit-reversed order directly.
novelty_assessment: Bruhat elimination and Nussbaumer polynomial transforms are classical. The source-specific
  interfaces are extracted without certifying the claimed sub-n-log-n algorithm.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build was performed.
statement_faithfulness: The matrix family and dimension are fixed before choosing the odd prime and input
  field width. Both Fourier signs are normalized by 1/t, so their composite is I/t, not I.
dependencies: Rational elimination, unit denominators modulo prime powers, ordered field updates, negacyclic
  coefficient rotations and radix-two transforms.
antecedents: Classical Bruhat decomposition and Nussbaumer transforms; Harvey-van der Hoeven 2021 provides
  the established multiplication framework cited by the source.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rank-counted shears and retained-order synthetic Fourier transforms

## Source manuscript and claim

[Integer multiplication below n log n](../papers/P-000211.md), by OpenAI, September 23, 2026.

The source claims exact integer multiplication in O(n (log n)^(1-kappa)) time on one fixed finite-tape Turing machine, with kappa=2^(-182).

## Extracted instruments

- [MI-000384: Implement a rational matrix shear with one interchange per rank](../instruments/MI-000384.md)
- [MI-000385: Cancel synthetic characters without division and retain the FFT output order](../instruments/MI-000385.md)

## Dependencies and antecedents

Rational elimination, unit denominators modulo prime powers, ordered field updates, negacyclic coefficient rotations and radix-two transforms.

Classical Bruhat decomposition and Nussbaumer transforms; Harvey-van der Hoeven 2021 provides the established multiplication framework cited by the source. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete lower-triangular factorization, matrix-shear, synthetic character cancellation and stored-order transform arguments. The finite motifs, simultaneous-layer algorithm and final complexity assembly were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build was performed.

The matrix family and dimension are fixed before choosing the odd prime and input field width. Both Fourier signs are normalized by 1/t, so their composite is I/t, not I.

[Batch record](../../batches/B035/README.md)
