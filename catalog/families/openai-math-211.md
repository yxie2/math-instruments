---
id: openai-math-211
record_type: family
title: Attempt clocks and deterministic spatial normalization
source_family: '211'
source_collection: openai/math
batch_id: B076
subject: Probability and statistical mechanics
source_paper_ids:
- P-000483
instrument_ids:
- MI-000716
- MI-000717
headline: The family claims geometric limits, diffusion limits and spectral convergence for several regimes
  of random planar maps.
central_instrument: Count every transition attempt to preserve the generator, and use a bounded monotone
  location functional to fix a deterministic spatial scale.
novelty_assessment: Established mechanisms are credited explicitly. Selected source-specific formulations
  are extracted without an exhaustive priority claim.
formalization_summary: The scope and FKCRT Comparator concern the Brownian CRT limit for q>4 through all
  positive edge sizes, with normalized degree measure. They do not state the q=2 diffusion or spectral
  conclusions of the extracted manuscript. The complete scope and Comparator were read. The inspected
  target contains sorry; no separate solution or Lean build was checked.
statement_faithfulness: Clock comparison assumes vanishing cable-edge lengths and a continuous limiting
  path law in a common ambient space. Spatial normalization assumes a finite strictly positive limiting
  diameter.
dependencies: Reversible Markov chains, martingale maximal inequalities, path moduli, weak convergence
  and bounded monotone tests.
antecedents: Classical Poissonization, Dirichlet-form normalization and continuous location functionals.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Attempt clocks and deterministic spatial normalization

## Source manuscripts and claim

- [Random Walks on Critical FK–Ising Maps and Liouville Brownian Motion](../papers/P-000483.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Spectral convergence for critical FK–Ising planar maps](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Spectral-convergence-for-critical-FK-Ising-planar-maps-October-5-2026)
- [A Linear Clock for Random Walk on Tree-Weighted Planar Maps](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026)
- [Canonical conformal limits of subcritical FK planar maps](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Canonical-conformal-limits-of-subcritical-FK-planar-maps-September-24-2026)
- [The critical Liouville quantum sphere and geometric limits of FK maps at q=4](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026)
- [Metric-measure limits of subcritical FK and spanning-tree planar maps](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026)
- [Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026)

The family claims geometric limits, diffusion limits and spectral convergence for several regimes of random planar maps.

## Extracted instruments

- [MI-000716: Keep loop attempts when matching discrete and continuous clocks](../instruments/MI-000716.md)
- [MI-000717: Fix a deterministic scale with a bounded monotone center](../instruments/MI-000717.md)

## Dependencies and antecedents

Reversible Markov chains, martingale maximal inequalities, path moduli, weak convergence and bounded monotone tests.

Classical Poissonization, Dirichlet-form normalization and continuous location functionals.

## Review and formalization scope

Read complete graph-energy, attempt-clock and spatial-normalization proofs in the FK-Ising random-walk manuscript. Six companion manuscripts are inventory-only. Their geometric, Green-kernel, recovery and spectral inputs are not certified.

The scope and FKCRT Comparator concern the Brownian CRT limit for q>4 through all positive edge sizes, with normalized degree measure. They do not state the q=2 diffusion or spectral conclusions of the extracted manuscript. The complete scope and Comparator were read. The inspected target contains sorry; no separate solution or Lean build was checked.

Clock comparison assumes vanishing cable-edge lengths and a continuous limiting path law in a common ambient space. Spatial normalization assumes a finite strictly positive limiting diameter.

[Batch record](../../batches/B076/README.md)
