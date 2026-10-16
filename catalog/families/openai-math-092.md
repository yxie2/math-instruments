---
id: openai-math-092
record_type: family
title: Uniform subset-sum sampling and exact covering periodization
source_family: 092
source_collection: openai/math
batch_id: B048
subject: Convex and metric geometry
source_paper_ids:
- P-000263
- P-000264
instrument_ids:
- MI-000484
- MI-000485
headline: The principal source claims an order n log n single-lattice covering bound; the companion claims
  the matching order for extremal covering densities.
central_instrument: A squared exponential potential upgrades a small bad fraction to control at every
  group point. A buffered finite window transfers arbitrary coverings to periodic ones with vanishing
  density loss.
novelty_assessment: The potential-square core is explicit in Li-Liu Theorem 4.1; periodization is classical
  Rogers theory, as stated by Prosanov. No new covering-order theorem is certified.
formalization_summary: The supplied targets concern an exact single-lattice cover in all n>=2 and matching
  asymptotic upper/lower orders of translative and lattice density suprema. The scope document and linked
  Comparator definitions and target statements were read. The inspected targets contain sorry; no solution
  or Lean project was built.
statement_faithfulness: Subset-sum bit labels retain multiplicity. Conditioning precedes each fresh uniform
  shift. Periodization equates infima over coverings, not different density statistics for one covering.
dependencies: Finite abelian translation bijections, a second moment, conditional Markov inequality, nonnegative
  weights, bounded convex bodies, local finiteness and boundary buffers.
antecedents: Li-Liu, Two-stage binary correction for nearly linear lattice coverings, Theorem 4.1; Prosanov
  Theorem 2.1, attributed to Rogers.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform subset-sum sampling and exact covering periodization

## Source manuscripts and claim

- [A single-lattice covering bound of order n log n](../papers/P-000263.md): selected passages extracted.
- [Translative covering densities of order n log n](../papers/P-000264.md): selected passages extracted.

The principal source claims an order n log n single-lattice covering bound; the companion claims the matching order for extremal covering densities.

## Extracted instruments

- [MI-000484: Upgrade a small bad fraction to a uniform subset-sum lower bound](../instruments/MI-000484.md)
- [MI-000485: Periodize a buffered covering window without losing boundary coverage](../instruments/MI-000485.md)

## Dependencies and antecedents

Finite abelian translation bijections, a second moment, conditional Markov inequality, nonnegative weights, bounded convex bodies, local finiteness and boundary buffers.

Li-Liu, Two-stage binary correction for nearly linear lattice coverings, Theorem 4.1; Prosanov Theorem 2.1, attributed to Rogers.

## Review and formalization scope

Read both complete selected source proofs. Read the cited Li-Liu robust binary translation proof and Prosanov periodization statement directly. Lattice geometry, random body construction and the global upper/lower covering bounds were not audited.

The supplied targets concern an exact single-lattice cover in all n>=2 and matching asymptotic upper/lower orders of translative and lattice density suprema. The scope document and linked Comparator definitions and target statements were read. The inspected targets contain sorry; no solution or Lean project was built.

Subset-sum bit labels retain multiplicity. Conditioning precedes each fresh uniform shift. Periodization equates infima over coverings, not different density statistics for one covering.

[Batch record](../../batches/B048/README.md)
