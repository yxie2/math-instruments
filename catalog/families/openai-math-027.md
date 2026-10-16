---
id: openai-math-027
record_type: family
title: Uniform integral parameters and compatible two-flag reconstruction
source_family: '027'
source_collection: openai/math
batch_id: B022
subject: Number theory
source_paper_ids:
- P-000160
instrument_ids:
- MI-000282
- MI-000283
headline: The source claims Zariski density of integral points on every relevant component of rank-r SL_r
  character varieties of curves with prescribed quasi-unipotent boundary classes, over one finite extension
  independent of the point and component.
central_instrument: Cyclotomic eigenvalues have unit pairwise differences, and finite generation of the
  unit group puts all determinant-normalizing roots into one fixed number field. Two flags and their identified
  quotients are reconstructed by compatible lower-block matrices.
novelty_assessment: Cyclotomic units, Dirichlet finite generation and simultaneous flag splittings are
  established ingredients. Their uniform arithmetic and quotient-compatibility bookkeeping is isolated
  here; the complete character-variety density theorem is not independently certified.
formalization_summary: Read CharacterVarietiesAllSeamsSupport.lean. It asks for ProducedMarkedSeamEquations
  under its properness, maximality, positive-genus, puncture and existing-solution hypotheses. It does
  not state the full integral-point density theorem; the imported equation definitions were not audited
  in full. The inspected Comparator files contain target statements with sorry placeholders; no Lean solution
  was built or kernel-checked.
statement_faithfulness: The field extension is fixed before varying points. Integrality is in the ambient
  character scheme, with exact complex boundary classes; it does not require preservation of the same
  Jordan class at every finite prime. Integral spectral projectors give projective summands, not automatically
  free ones; the source separately supplies free graded pieces. All sewn quotient identifications remain
  required.
dependencies: Cyclotomic norm identities, finite generation of number-field units, integral roots of units,
  split exact sequences with free quotients, two-flag block decomposition and compatible triangular matrices.
antecedents: Dirichlet unit theorem; classical cyclotomic units and simultaneous splittings of two flags;
  the source relates its flag operations to Mellit and Su stratifications.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform integral parameters and compatible two-flag reconstruction

## Source manuscript and claim

[Integral points on character varieties of curves](../papers/P-000160.md), by OpenAI, September 25, 2026.

The source claims Zariski density of integral points on every relevant component of rank-r SL_r character varieties of curves with prescribed quasi-unipotent boundary classes, over one finite extension independent of the point and component.

## Extracted instruments

- [MI-000282: One finite field supplies unit-separated spectra and all unit determinant roots](../instruments/MI-000282.md)
- [MI-000283: Two flags reconstruct through a once-crossing gallery with compatible graded maps](../instruments/MI-000283.md)

## Dependencies and antecedents

Cyclotomic norm identities, finite generation of number-field units, integral roots of units, split exact sequences with free quotients, two-flag block decomposition and compatible triangular matrices.

Dirichlet unit theorem; classical cyclotomic units and simultaneous splittings of two flags; the source relates its flag operations to Mellit and Su stratifications. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete arithmetic-parameter section and two-flag reconstruction proof. The seam induction and full density deduction were not audited.

Read CharacterVarietiesAllSeamsSupport.lean. It asks for ProducedMarkedSeamEquations under its properness, maximality, positive-genus, puncture and existing-solution hypotheses. It does not state the full integral-point density theorem; the imported equation definitions were not audited in full. The inspected Comparator files contain target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The field extension is fixed before varying points. Integrality is in the ambient character scheme, with exact complex boundary classes; it does not require preservation of the same Jordan class at every finite prime. Integral spectral projectors give projective summands, not automatically free ones; the source separately supplies free graded pieces. All sewn quotient identifications remain required.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/027.md) · [Batch record](../../batches/B022/README.md)
