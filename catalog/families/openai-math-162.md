---
id: openai-math-162
record_type: family
title: Affine moments and a nonlinear change of covering coordinates
source_family: '162'
source_collection: openai/math
batch_id: B058
subject: Combinatorics
source_paper_ids:
- P-000331
- P-000332
instrument_ids:
- MI-000562
- MI-000563
headline: The sources claim balanced counterexamples to Ryser covering at sufficiently large prime orders
  and counterexamples at prime-power ranks.
central_instrument: Exact point-line moments give a uniform variance budget. Cubing one coordinate turns
  deleted lines into bounded-intersection curves, while a conditional missing-line argument forces a complete
  parallel class.
novelty_assessment: The affine identity is explicitly present in Murphy-Petridis. The coordinate map and
  conditional cover argument use elementary finite-field geometry; their assembly is recorded without
  certifying the probabilistic construction or asserting priority.
formalization_summary: BalancedRyser states eventual balanced counterexamples for all sufficiently large
  primes. RyserCovering states one fixed prime congruent to two modulo three and all sufficiently large
  prime extension degrees; RyserOddExtensions states eventual odd-degree failures for every sufficiently
  large such prime and infinitely many ranks. Every linked Comparator and the scope document were read
  in full. The headline Comparator proof bodies contain sorry; this does not describe the separate solution
  files. No solution or Lean project was built.
statement_faithfulness: The first identity holds over every finite field and for arbitrary subsets. The
  cubic map uses primes congruent to two modulo three. The mixed-cover conclusion is conditional on both
  line density and a separate almost-pencil theorem.
dependencies: Affine incidence counting, finite-field permutation monomials, polynomial root bounds and
  elementary covering budgets.
antecedents: Murphy-Petridis, A Point-Line Incidence Identity in Finite Fields, and Applications, Lemma
  1; elementary polynomial root counting.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Affine moments and a nonlinear change of covering coordinates

## Source manuscripts and claim

- [Balanced counterexamples to Ryser's conjecture at prime orders](../papers/P-000331.md): selected passages extracted.
- [A counterexample to Ryser's covering conjecture](../papers/P-000332.md): selected passages extracted.

The sources claim balanced counterexamples to Ryser covering at sufficiently large prime orders and counterexamples at prime-power ranks.

## Extracted instruments

- [MI-000562: Use the exact affine incidence variance before any random selection](../instruments/MI-000562.md)
- [MI-000563: Turn deletion lines into curves and complete an almost-pencil cover](../instruments/MI-000563.md)

## Dependencies and antecedents

Affine incidence counting, finite-field permutation monomials, polynomial root bounds and elementary covering budgets.

Murphy-Petridis, A Point-Line Incidence Identity in Finite Fields, and Applications, Lemma 1; elementary polynomial root counting.

## Review and formalization scope

Read the entire elementary-estimates appendix of the balanced manuscript and the entire two-coordinatization gadget proof in its companion. The imported deletion/near-pencil theorem and the remaining hypergraph construction are not certified.

BalancedRyser states eventual balanced counterexamples for all sufficiently large primes. RyserCovering states one fixed prime congruent to two modulo three and all sufficiently large prime extension degrees; RyserOddExtensions states eventual odd-degree failures for every sufficiently large such prime and infinitely many ranks. Every linked Comparator and the scope document were read in full. The headline Comparator proof bodies contain sorry; this does not describe the separate solution files. No solution or Lean project was built.

The first identity holds over every finite field and for arbitrary subsets. The cubic map uses primes congruent to two modulo three. The mixed-cover conclusion is conditional on both line density and a separate almost-pencil theorem.

[Batch record](../../batches/B058/README.md)
