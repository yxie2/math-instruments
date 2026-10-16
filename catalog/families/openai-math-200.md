---
id: openai-math-200
record_type: family
title: Coefficient-space filtrations and ordered bases over a division algebra
source_family: '200'
source_collection: openai/math
batch_id: B056
subject: Algebra
source_paper_ids:
- P-000317
- P-000318
instrument_ids:
- MI-000548
- MI-000549
headline: The manuscripts claim the Artinian Lex-Plus-Powers Betti theorem and the Artinian Eisenbud-Green-Harris
  theorem over the complex numbers.
central_instrument: Filter Koszul terms by exponent plus exterior support to preserve internal degree.
  Separately, commuting linear forms in a division-coefficient polynomial algebra yield an ordered basis
  and a monomial ideal once triangular identities are available.
novelty_assessment: Initial-degeneration Betti bounds and Cohen-Macaulay parameter regularity are classical.
  The useful source interface retains vector-valued coefficients and distinguishes commuting forms from
  potentially noncommuting coefficients. The triangular-identity existence argument is not certified.
formalization_summary: Only the selected manuscript arguments are reviewed. No scope document or Comparator
  is listed for this family in the pinned inventory. No Lean solution was built.
statement_faithfulness: The first comparison applies to finite coefficient spaces in degree zero. The
  second is conditional on all the source commuting and triangular identities; it does not assert that
  arbitrary division-valued linear forms work.
dependencies: Graded Koszul homology, finite filtered complexes, leading coefficient subspaces, Cohen-Macaulay
  modules, regular parameters and elimination over a division algebra.
antecedents: Classical initial-ideal Hilbert and Betti comparison, recorded by Mermin-Murai; Stacks Project
  Tag 00N6 for regular systems of parameters.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Coefficient-space filtrations and ordered bases over a division algebra

## Source manuscripts and claim

- [The Artinian Lex-Plus-Powers Betti Theorem](../papers/P-000317.md): selected passages extracted.
- [Commuting Division-Coefficient Forms and the Artinian Eisenbud--Green--Harris Conjecture](../papers/P-000318.md): selected passages extracted.

The manuscripts claim the Artinian Lex-Plus-Powers Betti theorem and the Artinian Eisenbud-Green-Harris theorem over the complex numbers.

## Extracted instruments

- [MI-000548: Filter Koszul positions by exponent plus exterior support](../instruments/MI-000548.md)
- [MI-000549: Use commuting forms and right multiplication to extract one monomial ideal](../instruments/MI-000549.md)

## Dependencies and antecedents

Graded Koszul homology, finite filtered complexes, leading coefficient subspaces, Cohen-Macaulay modules, regular parameters and elimination over a division algebra.

Classical initial-ideal Hilbert and Betti comparison, recorded by Mermin-Murai; Stacks Project Tag 00N6 for regular systems of parameters.

## Review and formalization scope

Read the full filtered-module and Koszul comparison section and the complete ordered-basis and monomial-extraction proofs. The construction of the required triangular identities and the remaining headline proof are not audited.

Only the selected manuscript arguments are reviewed. No scope document or Comparator is listed for this family in the pinned inventory. No Lean solution was built.

The first comparison applies to finite coefficient spaces in degree zero. The second is conditional on all the source commuting and triangular identities; it does not assert that arbitrary division-valued linear forms work.

[Batch record](../../batches/B056/README.md)
