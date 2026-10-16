---
id: openai-math-039
record_type: family
title: Universal interpolation profiles and jet degeneration
source_family: 039
source_collection: openai/math
batch_id: B068
subject: Algebraic and complex geometry
source_paper_ids:
- P-000419
- P-000420
instrument_ids:
- MI-000650
- MI-000651
headline: The family claims Nagata inequalities and maximal multipoint Seshadri constants.
central_instrument: Countable determinantal loci turn a very-general counterexample into a universal interpolation
  profile; weighted initial terms transfer jet surjectivity.
novelty_assessment: Classical mechanisms and source interfaces are separated. These extractions neither
  certify the source headline theorems nor establish priority for the selected formulations.
formalization_summary: The scope and both Comparators were read in full. Nagata targets the strict inequality
  for all r>=10 outside one nonempty very-general locus, including reducible curves, repetitions and unequal
  multiplicities. MaximalSeshadriConstants targets eventual maximal constants on each smooth polarized
  complex surface, with a surface-dependent threshold, not an explicit uniform threshold or higher-dimensional/positive-characteristic
  statements. The target declarations have sorry bodies; helper declarations do not constitute a separate
  solution. No Lean solution was built.
statement_faithfulness: The first tool is only a conditional reduction from a counterexample. The second
  can move the evaluation tuple under scaling and keeps Laurent directions in the jet matrix.
dependencies: Taylor matrices, countable exceptional loci, cyclic products, monomial valuations and continuity
  of nonzero minors.
antecedents: Classical very-general specialization and Ito Proposition 5.7 on degeneration of jet separation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Universal interpolation profiles and jet degeneration

## Source manuscripts and claim

- [Nagata's conjecture for plane curves](../papers/P-000419.md): selected passages extracted.
- [Maximal Multipoint Seshadri Constants in Higher Dimensions](../papers/P-000420.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Maximal Seshadri constants on arbitrary polarized surfaces](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026)
- [Maximal multipoint Seshadri constants in positive characteristic](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026)

The family claims Nagata inequalities and maximal multipoint Seshadri constants.

## Extracted instruments

- [MI-000650: Convert a very-general violation into a universal equal-multiplicity profile](../instruments/MI-000650.md)
- [MI-000651: Transfer jet surjectivity from weighted initial terms](../instruments/MI-000651.md)

## Dependencies and antecedents

Taylor matrices, countable exceptional loci, cyclic products, monomial valuations and continuity of nonzero minors.

Classical very-general specialization and Ito Proposition 5.7 on degeneration of jet separation.

## Review and formalization scope

Read the full universal-profile proof and the row-valuation, weighted-limit and rank-transfer arguments. Two of four manuscripts receive extractions; surface and positive-characteristic companions remain inventory-only. Nagata and asymptotic maximality are not certified.

The scope and both Comparators were read in full. Nagata targets the strict inequality for all r>=10 outside one nonempty very-general locus, including reducible curves, repetitions and unequal multiplicities. MaximalSeshadriConstants targets eventual maximal constants on each smooth polarized complex surface, with a surface-dependent threshold, not an explicit uniform threshold or higher-dimensional/positive-characteristic statements. The target declarations have sorry bodies; helper declarations do not constitute a separate solution. No Lean solution was built.

The first tool is only a conditional reduction from a counterexample. The second can move the evaluation tuple under scaling and keeps Laurent directions in the jet matrix.

[Batch record](../../batches/B068/README.md)
