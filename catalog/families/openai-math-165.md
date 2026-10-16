---
id: openai-math-165
record_type: family
title: Order-sensitive polynomial pairings and total subspace intersections
source_family: '165'
source_collection: openai/math
batch_id: B058
subject: Combinatorics
source_paper_ids:
- P-000333
- P-000334
instrument_ids:
- MI-000564
- MI-000565
headline: The sources claim the Harary-Hill and Zarankiewicz formulas for complete and complete bipartite
  graph crossing numbers.
central_instrument: Two triangular evaluation patterns diagonalize an order-dependent pairing. A polynomial
  filtration bounds all cross-intersection dimensions when each paired intersection is zero.
novelty_assessment: Lagrange annihilation and determinant multiplicity are classical. The exact arbitrary-pair
  subspace inequality is distinct from the structured subspace-design theorem inspected here, but targeted
  searches do not establish its earliest priority. No crossing-number theorem is certified.
formalization_summary: CompleteCrossing states equality of the infimum of crossing counts with the Hill
  expression for n>=3; its target does not separately assert a two-page construction. BipartiteCrossing
  explicitly states an attaining admissible drawing and a universal lower bound for positive m,n. Both
  definitions count spatial intersection points of continuous simple paths with finite proper crossings
  and no triple crossings. Every linked Comparator and the scope document were read in full. The headline
  Comparator proof bodies contain sorry; this does not describe the separate solution files. No solution
  or Lean project was built.
statement_faithfulness: All interpolation nodes are distinct real numbers with an arbitrary prescribed
  order. The subspace theorem assumes only U_i intersect V_i=0 and bounds the ordered double sum, with
  a sharp constant.
dependencies: Lagrange interpolation, polynomial evaluation filtrations, rank loss, determinant divisibility
  and graphs of linear maps.
antecedents: Classical interpolation; Guruswami-Kopparty, Explicit Subspace Designs, for the related conversion
  of intersection dimension into determinant root multiplicity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Order-sensitive polynomial pairings and total subspace intersections

## Source manuscripts and claim

- [The crossing number of complete graphs](../papers/P-000333.md): selected passages extracted.
- [The crossing number of complete bipartite graphs](../papers/P-000334.md): selected passages extracted.

The sources claim the Harary-Hill and Zarankiewicz formulas for complete and complete bipartite graph crossing numbers.

## Extracted instruments

- [MI-000564: Diagonalize an arbitrary node-order pairing on two triangles](../instruments/MI-000564.md)
- [MI-000565: Charge paired-subspace intersections to polynomial root multiplicity](../instruments/MI-000565.md)

## Dependencies and antecedents

Lagrange interpolation, polynomial evaluation filtrations, rank loss, determinant divisibility and graphs of linear maps.

Classical interpolation; Guruswami-Kopparty, Explicit Subspace Designs, for the related conversion of intersection dimension into determinant root multiplicity.

## Review and formalization scope

Read the complete even-node interpolation and detector proofs, and the complete paired-subspace inequality, equality construction and rank-sum corollary. The topological cycle identities and full crossing-count reduction are not audited.

CompleteCrossing states equality of the infimum of crossing counts with the Hill expression for n>=3; its target does not separately assert a two-page construction. BipartiteCrossing explicitly states an attaining admissible drawing and a universal lower bound for positive m,n. Both definitions count spatial intersection points of continuous simple paths with finite proper crossings and no triple crossings. Every linked Comparator and the scope document were read in full. The headline Comparator proof bodies contain sorry; this does not describe the separate solution files. No solution or Lean project was built.

All interpolation nodes are distinct real numbers with an arbitrary prescribed order. The subspace theorem assumes only U_i intersect V_i=0 and bounds the ordered double sum, with a sharp constant.

[Batch record](../../batches/B058/README.md)
