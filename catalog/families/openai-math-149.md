---
id: openai-math-149
record_type: family
title: Affine plateaux and ordered-cut flux
source_family: '149'
source_collection: openai/math
batch_id: B075
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000477
- P-000478
instrument_ids:
- MI-000708
- MI-000709
headline: The family claims boundedness, persistence and classwise uniform permanence for weakly reversible
  mass-action systems.
central_instrument: Active slopes control finite affine minima, while return paths make ordered-cut flux
  nonnegative under sufficiently strong weight separation.
novelty_assessment: Selected local mechanisms are distinguished from the manuscripts headline claims.
  Primary comparisons identify established antecedents; exhaustive priority is not established.
formalization_summary: Read the scope and complete MassAction Comparator. It targets global existence
  and bounds away from zero and infinity for every positive initial state of a weakly reversible network
  with positive constant rates. Its bound may depend on that initial state; it does not state the newer
  classwise uniform absorbing-set result. Inspected theorem targets contain sorry; no separate solution
  or Lean build was checked.
statement_faithfulness: The trapping conclusion assumes a compact plateau inside the control region and
  a uniform positive active-slope bound below it. The flux lemma requires all-pairs weight ordering, including
  across components.
dependencies: Finite affine minima, right derivatives, compact ODE continuation and directed return paths.
antecedents: Classical nonsmooth Lyapunov arguments and ordered reaction-flux decompositions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Affine plateaux and ordered-cut flux

## Source manuscripts and claim

- [Uniform Permanence in Weakly Reversible Mass-Action Systems](../papers/P-000477.md): selected passages extracted.
- [Boundedness and persistence of weakly reversible mass-action systems](../papers/P-000478.md): selected passages extracted.

The family claims boundedness, persistence and classwise uniform permanence for weakly reversible mass-action systems.

## Extracted instruments

- [MI-000708: Trap trajectories on a compact maximum plateau of a finite affine minimum](../instruments/MI-000708.md)
- [MI-000709: Regroup weighted directed edges into nonnegative level-cut fluxes](../instruments/MI-000709.md)

## Dependencies and antecedents

Finite affine minima, right derivatives, compact ODE continuation and directed return paths.

Classical nonsmooth Lyapunov arguments and ordered reaction-flux decompositions.

## Review and formalization scope

Read the compact-plateau proof, the active-increase statement and complete trapping proof, and the full finite cut-flux proof and its application. Both manuscripts receive extractions. The affine-label construction and the uniform active-increase proof are not certified.

Read the scope and complete MassAction Comparator. It targets global existence and bounds away from zero and infinity for every positive initial state of a weakly reversible network with positive constant rates. Its bound may depend on that initial state; it does not state the newer classwise uniform absorbing-set result. Inspected theorem targets contain sorry; no separate solution or Lean build was checked.

The trapping conclusion assumes a compact plateau inside the control region and a uniform positive active-slope bound below it. The flux lemma requires all-pairs weight ordering, including across components.

[Batch record](../../batches/B075/README.md)
