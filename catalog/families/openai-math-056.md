---
id: openai-math-056
record_type: family
title: Cycle-rank descent and branch rounding deficits
source_family: '056'
source_collection: openai/math
batch_id: B070
subject: Algebraic and complex geometry
source_paper_ids:
- P-000431
- P-000432
instrument_ids:
- MI-000662
- MI-000663
headline: The family claims termination of projective and Kahler fourfold minimal model programs.
central_instrument: Borel-Moore localization detects strict cycle-rank losses. A first blowup and distinct
  monomial valuations pay all but a controlled branch rounding error.
novelty_assessment: The selected tools use established mechanisms. Exact source-specific rounding and
  lattice interfaces have not received exhaustive priority checks. No headline theorem is certified.
formalization_summary: No Lean scope document is supplied for this family in the pinned inventory. No
  formal solution was built.
statement_faithfulness: Cycle loss requires the target exceptional set to have dimension below the cycle
  dimension. The local difficulty estimate needs a terminal pair, effective boundary and integral scaled
  fixed coefficients.
dependencies: Analytic fundamental classes, Kahler positivity, localization, codimension-two regularity,
  normalization multiplicity and ceiling arithmetic.
antecedents: Classical cycle-rank arguments and the Alexeev-Hacon-Kawamata weighted difficulty framework.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Cycle-rank descent and branch rounding deficits

## Source manuscripts and claim

- [Termination of generalized log canonical flips on compact Kähler fourfolds](../papers/P-000431.md): selected passages extracted.
- [Termination for projective log canonical fourfolds with rational boundary](../papers/P-000432.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Termination of generalized-canonical flips on compact Kähler fourfolds](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026)
- [Finite ordinary minimal model programs on compact Kähler fourfolds](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026)
- [Finite ordinary minimal model programs on compact Kähler fourfolds](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-September-24-2026)

The family claims termination of projective and Kahler fourfold minimal model programs.

## Extracted instruments

- [MI-000662: Count birational contractions by losses of analytic cycle classes](../instruments/MI-000662.md)
- [MI-000663: Bound a local difficulty deficit by the number of varying branches](../instruments/MI-000663.md)

## Dependencies and antecedents

Analytic fundamental classes, Kahler positivity, localization, codimension-two regularity, normalization multiplicity and ceiling arithmetic.

Classical cycle-rank arguments and the Alexeev-Hacon-Kawamata weighted difficulty framework.

## Review and formalization scope

Read the complete cycle-loss proof and complete ceiling-error proof with weight/default definitions. Two of five manuscripts receive extractions; three companions remain inventory-only. Global branch inequalities, boundedness of the difficulty and termination are not certified.

No Lean scope document is supplied for this family in the pinned inventory. No formal solution was built.

Cycle loss requires the target exceptional set to have dimension below the cycle dimension. The local difficulty estimate needs a terminal pair, effective boundary and integral scaled fixed coefficients.

[Batch record](../../batches/B070/README.md)
