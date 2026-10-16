---
id: openai-math-278
record_type: family
title: Angle orbitals and an unrestricted ensemble kinetic certificate
source_family: '278'
source_collection: openai/math
batch_id: B016
subject: Mathematical physics
source_paper_ids:
- P-000135
instrument_ids:
- MI-000230
- MI-000231
headline: The source claims a three-electron, two-nucleus Coulomb ground-state density that no noninteracting
  ground-state ensemble reproduces with a real spin-independent potential in L^(3/2)(R^3)+L^infinity(R^3).
  The positive integer nuclear charge is specified by a finite nonnumerical formula.
central_instrument: An angle splits a density into orthogonal orbitals with one common formal potential;
  a weighted gap and the Pauli bound then certify a constrained-search minimum over every fermionic ensemble.
novelty_assessment: Polar-coordinate calculus, ground-state transforms and the Pauli bound are established.
  The extracted contribution is their domain-aware use for a formal potential that need not define an
  ordinary global Hamiltonian. The full Coulomb nonrepresentability theorem was not audited.
formalization_summary: No family-specific Lean scope document was listed in the pinned inventory. No Lean
  proof was certified for these extracted tools.
statement_faithfulness: The angle equation, regularity and weighted gap are hypotheses here. Local integrability
  of the formal potential is not membership in the ordinary potential class. No rank, reality or spin-diagonality
  restriction is imposed on the competing ensemble.
dependencies: Sobolev chain rules, weighted Poincare inequality, positive ground-state representation,
  cutoff approximation and fermionic one-body occupation bounds.
antecedents: The source credits Frank-Seiringer for the ground-state representation and Levy-Lieb for
  the constrained-search framework. The occupation bound is the usual Pauli principle.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Angle orbitals and an unrestricted ensemble kinetic certificate

## Source manuscript and claim

[A Coulomb ground-state density without Kohn-Sham ensemble representation](../papers/P-000135.md), by OpenAI, September 25, 2026.

The source claims a three-electron, two-nucleus Coulomb ground-state density that no noninteracting ground-state ensemble reproduces with a real spin-independent potential in L^(3/2)(R^3)+L^infinity(R^3). The positive integer nuclear charge is specified by a finite nonnumerical formula.

## Extracted instruments

- [MI-000230: A density angle gives orthogonal orbitals with a common formal potential](../instruments/MI-000230.md)
- [MI-000231: A weighted gap and Pauli occupation bound certify every mixed fermionic state](../instruments/MI-000231.md)

## Dependencies and antecedents

Sobolev chain rules, weighted Poincare inequality, positive ground-state representation, cutoff approximation and fermionic one-body occupation bounds.

The source credits Frank-Seiringer for the ground-state representation and Levy-Lieb for the constrained-search framework. The occupation bound is the usual Pauli principle. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the orbital calculation and the complete ensemble-certificate proof. The channel analysis, proof of the weighted gap, finite charge selection and nodal-plane contradiction were not audited.

No family-specific Lean scope document was listed in the pinned inventory. No Lean proof was certified for these extracted tools.

The angle equation, regularity and weighted gap are hypotheses here. Local integrability of the formal potential is not membership in the ordinary potential class. No rank, reality or spin-diagonality restriction is imposed on the competing ensemble.

[Batch record](../../batches/B016/README.md)
