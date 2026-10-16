---
id: openai-math-168
record_type: family
title: Height-one lattice recovery and regular kernel reduction
source_family: '168'
source_collection: openai/math
batch_id: B036
subject: Combinatorics
source_paper_ids:
- P-000218
instrument_ids:
- MI-000398
- MI-000399
headline: The source claims combinatorial invariance of equal-parameter Kazhdan-Lusztig polynomials for
  arbitrary Coxeter systems.
central_instrument: Free full-rank lattices are recovered from height-one localizations. Nonproportional
  edge labels make reduction of a restriction kernel saturated and preserve its generic rank.
novelty_assessment: Both are classical commutative-algebra mechanisms. They are extracted independently
  of the source more substantial rank-two edge-image comparison.
formalization_summary: 'Read KLInvariance.lean: strong Bruhat order, normalized R/P families and the interval-order-isomorphism
  target. The final target contains sorry; no Lean build.'
statement_faithfulness: Freeness is an essential input to the chosen lattice statement. Kernel reduction
  requires injectivity of the reducing label on every target and freeness of the original kernel; arbitrary
  partial sheaf kernels are not assumed free.
dependencies: Unique factorization, rational basis coordinates, nonzerodivisors on quotient modules, kernel
  saturation and product annihilators.
antecedents: Classical height-one recovery over polynomial rings and elementary regular-element base change;
  Braden-MacPherson/Fiebig sheaves provide the source setting.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Height-one lattice recovery and regular kernel reduction

## Source manuscript and claim

[Combinatorial invariance of Kazhdan–Lusztig polynomials](../papers/P-000218.md), by OpenAI, September 24, 2026.

The source claims combinatorial invariance of equal-parameter Kazhdan-Lusztig polynomials for arbitrary Coxeter systems.

## Extracted instruments

- [MI-000398: Recover a free full-rank lattice from height-one localizations](../instruments/MI-000398.md)
- [MI-000399: Reduce a restriction kernel modulo a regular transverse label](../instruments/MI-000399.md)

## Dependencies and antecedents

Unique factorization, rational basis coordinates, nonzerodivisors on quotient modules, kernel saturation and product annihilators.

Classical height-one recovery over polynomial rings and elementary regular-element base change; Braden-MacPherson/Fiebig sheaves provide the source setting. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete lattice lemma, moment-graph module assumptions and the saturation/generic-rank paragraph of the edge-image proof. The rest of the edge-image bound and global invariance argument were not audited.

Read KLInvariance.lean: strong Bruhat order, normalized R/P families and the interval-order-isomorphism target. The final target contains sorry; no Lean build.

Freeness is an essential input to the chosen lattice statement. Kernel reduction requires injectivity of the reducing label on every target and freeness of the original kernel; arbitrary partial sheaf kernels are not assumed free.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/168.md) · [Batch record](../../batches/B036/README.md)
