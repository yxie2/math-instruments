---
id: openai-math-122
record_type: family
title: Damping products and hiding fixed-count labels
source_family: '122'
source_collection: openai/math
batch_id: B074
subject: Theoretical computer science
source_paper_ids:
- P-000465
- P-000466
instrument_ids:
- MI-000696
- MI-000697
headline: The family claims quantitative trace-reconstruction lower bounds and newer quasipolynomial upper
  bounds.
central_instrument: Mixed linear/quadratic damping survives multiplication; a common component hides enough
  labels to smooth adjacent fixed-count schedules.
novelty_assessment: Established mechanisms and directly checked antecedents are identified below. No exhaustive
  novelty determination or source headline certification is claimed.
formalization_summary: Read the scope and complete TraceReconstruction Comparator. It targets superpolynomial
  worst-case sample lower bounds at every fixed positive success probability, one-trace indistinguishability,
  and a quantitative bound along varying deletion rates. It does not state the newer upper-bound decoder
  theorems. The inspected theorem targets contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: The damping budget counts factors with multiplicity. The overlap amplification
  assumes a positive overlap input and sufficiently large parameters; no asymptotic source reconstruction
  guarantee is certified.
dependencies: Cayley transforms, Cauchy-Schwarz, common sublaws, hypergeometric distributions and total
  variation.
antecedents: Classical disk-to-half-plane estimates, common-part couplings and smoothing of fixed-count
  samples.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Damping products and hiding fixed-count labels

## Source manuscripts and claim

- [Uniform quasipolynomial-time trace reconstruction](../papers/P-000465.md): selected passages extracted.
- [Quantitative lower bounds for trace reconstruction](../papers/P-000466.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [A latest-anchor induction with spectrally compact masks for worst-case trace reconstruction](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026)

The family claims quantitative trace-reconstruction lower bounds and newer quasipolynomial upper bounds.

## Extracted instruments

- [MI-000696: Keep a product uniformly inside the Cayley half-plane](../instruments/MI-000696.md)
- [MI-000697: Amplify adjacent-power overlap by hiding labels in a fixed-count schedule](../instruments/MI-000697.md)

## Dependencies and antecedents

Cayley transforms, Cauchy-Schwarz, common sublaws, hypergeometric distributions and total variation.

Classical disk-to-half-plane estimates, common-part couplings and smoothing of fixed-count samples.

## Review and formalization scope

Read the complete controlled-product lemma and its factor-count context, and the complete adjacent-power overlap proof and paired-hiding discussion. Two of three manuscripts receive extractions; the latest-anchor upper-bound manuscript remains inventory-only. Multiscale analytic continuation, score induction and decoder complexity are not certified.

Read the scope and complete TraceReconstruction Comparator. It targets superpolynomial worst-case sample lower bounds at every fixed positive success probability, one-trace indistinguishability, and a quantitative bound along varying deletion rates. It does not state the newer upper-bound decoder theorems. The inspected theorem targets contain sorry; no separate solution or Lean build was checked.

The damping budget counts factors with multiplicity. The overlap amplification assumes a positive overlap input and sufficiently large parameters; no asymptotic source reconstruction guarantee is certified.

[Batch record](../../batches/B074/README.md)
