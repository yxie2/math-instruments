---
id: openai-math-218
record_type: family
title: Environment-preserving couplings and summable scale weights
source_family: '218'
source_collection: openai/math
batch_id: B078
subject: Probability and statistical mechanics
source_paper_ids:
- P-000490
instrument_ids:
- MI-000726
- MI-000727
headline: The family claims conformal universality for weakly perturbed and random-bond planar Ising models.
central_instrument: Preserve a comparison marginal in every environment and exploit geometrically weighted
  vanishing errors without requiring their unweighted summability.
novelty_assessment: Classical finite mechanisms are separated from the source headline claims. Exhaustive
  priority is not established.
formalization_summary: BufferedIsing states a finite-graph likelihood-ratio comparison after buffered
  modifications, with arbitrary fields and common pins. It does not state an SLE convergence theorem.
  The full scope document and named Comparator were read. Other linked Comparators were not inspected.
  Target declarations contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: The finite gluing statement has deterministic reference event probability bounded
  below. The scale comparison additionally assumes the actual local trajectory, conditional implementations
  and independent primitive environments required by the source.
dependencies: Finite stochastic-order couplings, conditional total variation, the source step-mismatch
  estimates and terminal deletion estimates.
antecedents: Maximal coupling, finite stochastic order, and the elementary uniformly summable-kernel argument.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Environment-preserving couplings and summable scale weights

## Source manuscripts and claim

- [Quenched SLE₃ limits for general weak random-bond Ising models](../papers/P-000490.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Quenched SLE₃ Universality for the Weak Random-Bond Ising Model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Quenched-SLE3-Universality-for-the-Weak-Random-Bond-Ising-Model-October-5-2026)
- [Logarithmic Relative Fluctuations in the Weakly Disordered Planar Ising Model](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026)
- [Conformal universality of bulk Ising correlations under weak interactions](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026)
- [SLE3 universality for weak finite-range Ising interactions](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/SLE3-universality-for-weak-finite-range-Ising-interactions-September-23-2026)
- [Buffered comparison and stopping-band resolution in critical Ising](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026)

The family claims conformal universality for weakly perturbed and random-bond planar Ising models.

## Extracted instruments

- [MI-000726: Glue conditional order couplings without changing the quenched reference marginal](../instruments/MI-000726.md)
- [MI-000727: Sum geometrically weighted scale errors without assuming a summable perturbation](../instruments/MI-000727.md)

## Dependencies and antecedents

Finite stochastic-order couplings, conditional total variation, the source step-mismatch estimates and terminal deletion estimates.

Maximal coupling, finite stochastic order, and the elementary uniformly summable-kernel argument.

## Review and formalization scope

Read the complete conditional gluing proof, weighted-decay argument and torus finite-test comparison proof. Five companions are inventory-only. The local estimates needed for the interface limit are not certified.

BufferedIsing states a finite-graph likelihood-ratio comparison after buffered modifications, with arbitrary fields and common pins. It does not state an SLE convergence theorem. The full scope document and named Comparator were read. Other linked Comparators were not inspected. Target declarations contain sorry; no separate solution or Lean build was checked.

The finite gluing statement has deterministic reference event probability bounded below. The scale comparison additionally assumes the actual local trajectory, conditional implementations and independent primitive environments required by the source.

[Batch record](../../batches/B078/README.md)
