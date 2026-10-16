---
id: openai-math-274
record_type: family
title: Integer filters with coefficient budgets and state-dependent gate pruning
source_family: '274'
source_collection: openai/math
batch_id: B055
subject: Mathematical physics
source_paper_ids:
- P-000309
- P-000310
instrument_ids:
- MI-000540
- MI-000541
headline: The sources claim bounded-error parity lower bounds for constant-depth quantum circuits with
  polynomially many zero-initialized ancillary qubits.
central_instrument: A root polynomial times a normalized Chebyshev filter controls both integer-grid error
  and weighted coefficients. Deleting rare reflections on the actual pruned-prefix state admits a direct
  error telescope.
novelty_assessment: Exact-root Chebyshev approximation and telescoping gate deletion have explicit earlier
  antecedents. The source adds a coefficient budget and a conditional regularity argument for state-dependent
  retention.
formalization_summary: The inspected QACParity Comparator states the measured-output positive-advantage
  lower bound, and RegularParity states its below-two-thirds specialization. Both use zero ancillas and
  allow arbitrary final garbage; both target proofs contain sorry. Although the scope document also describes
  localization, neither inspected Comparator contains a separate localization or regular-trajectory theorem.
  The scope document and every linked Comparator were read in full. No solution or Lean project was built.
statement_faithfulness: The filter is small on positive integers, not throughout the interval adjacent
  to zero. Pruning uses probabilities in the current pruned state and commuting gates within each layer;
  regularity also needs the source uniform overlap-tail hypothesis.
dependencies: Chebyshev growth, coefficient convolution, Markov and counting bounds, commuting projectors,
  unitary telescoping and state-dependent product tests.
antecedents: Sherstov exact-root approximate inclusion-exclusion; Nadimpalli-Parham-Vasconcelos-Yuen wide-gate
  deletion.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Integer filters with coefficient budgets and state-dependent gate pruning

## Source manuscripts and claim

- [Product-projection localization and the QAC0 parity lower bound](../papers/P-000309.md): selected passages extracted.
- [Regular trajectories, pruning and quantum parity](../papers/P-000310.md): selected passages extracted.

The sources claim bounded-error parity lower bounds for constant-depth quantum circuits with polynomially many zero-initialized ancillary qubits.

## Extracted instruments

- [MI-000540: Combine exact integer roots with a Chebyshev filter while budgeting coefficients](../instruments/MI-000540.md)
- [MI-000541: Prune commuting reflections using probabilities in the current pruned state](../instruments/MI-000541.md)

## Dependencies and antecedents

Chebyshev growth, coefficient convolution, Markov and counting bounds, commuting projectors, unitary telescoping and state-dependent product tests.

Sherstov exact-root approximate inclusion-exclusion; Nadimpalli-Parham-Vasconcelos-Yuen wide-gate deletion.

## Review and formalization scope

Read the complete polynomial construction and the full projection-insertion, retained-layer and pruning proofs. The preceding tail-transport and localization induction are not certified.

The inspected QACParity Comparator states the measured-output positive-advantage lower bound, and RegularParity states its below-two-thirds specialization. Both use zero ancillas and allow arbitrary final garbage; both target proofs contain sorry. Although the scope document also describes localization, neither inspected Comparator contains a separate localization or regular-trajectory theorem. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

The filter is small on positive integers, not throughout the interval adjacent to zero. Pruning uses probabilities in the current pruned state and commuting gates within each layer; regularity also needs the source uniform overlap-tail hypothesis.

[Batch record](../../batches/B055/README.md)
