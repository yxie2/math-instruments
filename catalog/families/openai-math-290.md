---
id: openai-math-290
record_type: family
title: Conditional GNS product isometries and bounded randomization witnesses
source_family: '290'
source_collection: openai/math
batch_id: B062
subject: Operator algebras
source_paper_ids:
- P-000371
- P-000372
instrument_ids:
- MI-000602
- MI-000603
headline: The sources claim expected amenable subalgebras preserving core commutants and a bounded-recovery
  theorem for modular spectral averages.
central_instrument: Scalar conditional expectations make multiplication maps isometric. A fourth-moment
  estimate survives truncation and spectral filtering to produce one bounded witness.
novelty_assessment: The GNS calculation is elementary and conditional. Fourth-moment truncation has an
  explicit Haagerup-Musat antecedent; its modular spectral interface is the selected source specialization.
formalization_summary: BoundedRecovery includes a nondegenerate bounded continuous real spectral calculus,
  a closed Tomita graph and cyclic separating vector, modular conjugation, and scalar centralizer. Its
  hypothesis is a free-ultrafilter limit of integer symmetric averages followed by positive limsup in
  n; its conclusion is a bounded witness on a strict subsequence with doubled spectral half-width. It
  does not state an absolute or relative bicentralizer theorem. Both available scope documents and both
  linked Comparators in this batch were read in full. Target theorems have sorry proof bodies; some supporting
  definitions have explicit proofs. No separate solution or Lean build was checked.
statement_faithfulness: Scalar expectations are hypotheses of the extracted product lemma. The bounded
  witness requires both row and column moments in the indicated nontracial order; finite models do not
  realize the source scalar-centralizer setting.
dependencies: State-preserving expectations, GNS inner products, Steinhaus moments, polar clipping and
  Hilbert-space contraction filters.
antecedents: Conditional-expectation orthogonality; Haagerup-Musat noncommutative Khintchine truncation.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Conditional GNS product isometries and bounded randomization witnesses

## Source manuscripts and claim

- [Expected amenable subalgebras preserving core commutants](../papers/P-000371.md): selected passages extracted.
- [Bounded recovery for modular spectral averages](../papers/P-000372.md): selected passages extracted.

The sources claim expected amenable subalgebras preserving core commutants and a bounded-recovery theorem for modular spectral averages.

## Extracted instruments

- [MI-000602: Obtain two GNS multiplication isometries from scalar conditional expectations](../instruments/MI-000602.md)
- [MI-000603: Turn fourth-moment control into a bounded spectrally filtered witness](../instruments/MI-000603.md)

## Dependencies and antecedents

State-preserving expectations, GNS inner products, Steinhaus moments, polar clipping and Hilbert-space contraction filters.

Conditional-expectation orthogonality; Haagerup-Musat noncommutative Khintchine truncation.

## Review and formalization scope

Read the complete product-isometry proof and bounded-recovery proof. Only the local moment-to-witness implication is extracted; the source modular averaging inputs and bicentralizer conclusions remain unaudited.

BoundedRecovery includes a nondegenerate bounded continuous real spectral calculus, a closed Tomita graph and cyclic separating vector, modular conjugation, and scalar centralizer. Its hypothesis is a free-ultrafilter limit of integer symmetric averages followed by positive limsup in n; its conclusion is a bounded witness on a strict subsequence with doubled spectral half-width. It does not state an absolute or relative bicentralizer theorem. Both available scope documents and both linked Comparators in this batch were read in full. Target theorems have sorry proof bodies; some supporting definitions have explicit proofs. No separate solution or Lean build was checked.

Scalar expectations are hypotheses of the extracted product lemma. The bounded witness requires both row and column moments in the indicated nontracial order; finite models do not realize the source scalar-centralizer setting.

[Batch record](../../batches/B062/README.md)
