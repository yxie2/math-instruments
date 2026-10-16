---
id: openai-math-229
record_type: family
title: Posterior product laws, nonlinear flow conversion and informative rounding
source_family: '229'
source_collection: openai/math
batch_id: B054
subject: Probability and statistical mechanics
source_paper_ids:
- P-000301
- P-000302
- P-000303
instrument_ids:
- MI-000532
- MI-000533
- MI-000534
headline: The three sources claim sharp Potts reconstruction thresholds and a four-state capacity criterion
  on bounded-degree trees.
central_instrument: Bayes reweighting gives the correct unconditional law of combined posteriors. A cubic
  change of information variable yields a telescoping capacity flow. Barycentric posterior spreading has
  an explicit reverse garbling.
novelty_assessment: The posterior product and survey principles have direct Mezard-Montanari and Bhatnagar-Maneva
  antecedents. The nonlinear flow recursion is the p=3 case of Pemantle-Peres; the cubic renormalization
  is a source interface conditional on its moment-saving input.
formalization_summary: 'Both linked Comparators state only three-state supercritical Kesten-Stigum reconstruction:
  b lambda^2>1 on regular trees and d lambda^2>1 on Poisson trees, with lambda in [-1/2,1]. They use a
  positive limiting expected total-variation advantage, with unordered observations and the offspring
  tree observed; the Poisson statement averages over trees and spins. Their target proofs contain sorry.
  They do not state four-state thresholds, nonreconstruction, equality cases, the capacity criterion or
  stochastic-block-model conclusions. The scope document and every linked Comparator were read in full.
  No solution or Lean project was built.'
statement_faithfulness: Experiments are conditionally independent given the root, not independent under
  the actual marginal law. Capacity conversion requires 0<r<1, bounded branching and a cubic saving. Posterior
  grid refinement preserves labeled observations.
dependencies: Bayes formula, posterior barycenters, conditional products, cubic inequalities, conserved
  flows and Blackwell garbling.
antecedents: Mezard-Montanari posterior distribution recursion; Pemantle-Peres nonlinear capacity; Bhatnagar-Maneva
  surveys and convex domination.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Posterior product laws, nonlinear flow conversion and informative rounding

## Source manuscripts and claim

- [The Reconstruction Threshold for the Ferromagnetic Four-State Potts Model](../papers/P-000301.md): selected passages extracted.
- [A Capacity Criterion for Four-State Potts Reconstruction on Trees](../papers/P-000302.md): selected passages extracted.
- [The exact reconstruction threshold for the three-state symmetric channel](../papers/P-000303.md): selected passages extracted.

The three sources claim sharp Potts reconstruction thresholds and a four-state capacity criterion on bounded-degree trees.

## Extracted instruments

- [MI-000532: Combine posterior experiments with their exact Bayes reweighting](../instruments/MI-000532.md)
- [MI-000533: Convert cubic information savings into a flow of bounded nonlinear potential](../instruments/MI-000533.md)
- [MI-000534: Round posterior laws by a barycentric refinement with an explicit reverse garbling](../instruments/MI-000534.md)

## Dependencies and antecedents

Bayes formula, posterior barycenters, conditional products, cubic inequalities, conserved flows and Blackwell garbling.

Mezard-Montanari posterior distribution recursion; Pemantle-Peres nonlinear capacity; Bhatnagar-Maneva surveys and convex domination.

## Review and formalization scope

Read the selected posterior identities, the full cubic renormalization and flow proofs, and the barycentric refinement and pure-completion proofs. The polynomial certificates and claimed threshold or capacity equivalences are not certified.

Both linked Comparators state only three-state supercritical Kesten-Stigum reconstruction: b lambda^2>1 on regular trees and d lambda^2>1 on Poisson trees, with lambda in [-1/2,1]. They use a positive limiting expected total-variation advantage, with unordered observations and the offspring tree observed; the Poisson statement averages over trees and spins. Their target proofs contain sorry. They do not state four-state thresholds, nonreconstruction, equality cases, the capacity criterion or stochastic-block-model conclusions. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

Experiments are conditionally independent given the root, not independent under the actual marginal law. Capacity conversion requires 0<r<1, bounded branching and a cubic saving. Posterior grid refinement preserves labeled observations.

[Batch record](../../batches/B054/README.md)
