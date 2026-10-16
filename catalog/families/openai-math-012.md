---
id: openai-math-012
record_type: family
title: Adaptive cut comparison through column sampling
source_family: '012'
source_collection: openai/math
batch_id: B007
subject: Number theory
source_paper_ids:
- P-000099
instrument_ids:
- MI-000154
- MI-000155
headline: The source claims the joint Dickman law for consecutive integers in ordinary natural density,
  and density one half for each ordering of their largest prime factors. This extraction selects the sampling
  argument that permits tests depending on the entire arithmetic configuration.
central_instrument: A deterministic column sample approximates an optimizing cut; degree control, a Lipschitz
  extension and uniform integrability then upgrade single-site comparisons to adaptive cut-norm comparisons.
novelty_assessment: Small-sample cut approximation, Lipschitz extension and bounded differences are established.
  The source-specific package allows unbounded, position-dependent kernels with integrated rather than
  conditional row-second-moment control. Priority is not certified.
formalization_summary: JointDickman.lean states natural density for both thresholds based at n, for fixed
  0<a,b<1, and both strict ordering densities. The scope document and Comparator declarations were compared,
  but no Lean solution was built or kernel-checked. The extracted auxiliary mechanisms are not separate
  Comparator statements.
statement_faithfulness: The main claim is ordinary, not logarithmic, density. Arithmetic scale x tends
  to infinity for each fixed B before B tends to infinity. Uniformity in a fixed auxiliary position parameter
  is a uniform expectation bound, not a simultaneous event over its continuum of values.
dependencies: Independent finite site types; symmetric zero-diagonal kernels; an every-type expected degree
  bound; integrated row second moments; a comparison uniform over bounded single-site tests; a small column
  sample and concentration after extension from one common degree event.
antecedents: The source credits Alon, Fernandez de la Vega, Kannan and Karpinski and Borgs, Chayes, Lovasz,
  Sos and Vesztergombi for sampling optimizing cuts. McShane extension and McDiarmid concentration are
  established inputs. The arithmetic comparison uses additional divisor-channel and multiplicative-function
  arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Adaptive cut comparison through column sampling

## Source manuscript and claim

[The joint Dickman law for consecutive integers](../papers/P-000099.md), by OpenAI, September 24, 2026.

The source claims the joint Dickman law for consecutive integers in ordinary natural density, and density one half for each ordering of their largest prime factors. This extraction selects the sampling argument that permits tests depending on the entire arithmetic configuration.

## Extracted instruments

- [MI-000154: A small column sample approximates a cut using total squared mass](../instruments/MI-000154.md)
- [MI-000155: A common degree event transfers single-site tests to adaptive cut norms](../instruments/MI-000155.md)

## Dependencies and antecedents

Independent finite site types; symmetric zero-diagonal kernels; an every-type expected degree bound; integrated row second moments; a comparison uniform over bounded single-site tests; a small column sample and concentration after extension from one common degree event.

The source credits Alon, Fernandez de la Vega, Kannan and Karpinski and Borgs, Chayes, Lovasz, Sos and Vesztergombi for sampling optimizing cuts. McShane extension and McDiarmid concentration are established inputs. The arithmetic comparison uses additional divisor-channel and multiplicative-function arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete sampling section and the introduction, and compared the formalization scope with the challenge statements. The divisor amplifier, residue smoothing channels and multiplicative short-interval inputs were not fully audited.

JointDickman.lean states natural density for both thresholds based at n, for fixed 0<a,b<1, and both strict ordering densities. The scope document and Comparator declarations were compared, but no Lean solution was built or kernel-checked. The extracted auxiliary mechanisms are not separate Comparator statements.

The main claim is ordinary, not logarithmic, density. Arithmetic scale x tends to infinity for each fixed B before B tends to infinity. Uniformity in a fixed auxiliary position parameter is a uniform expectation bound, not a simultaneous event over its continuum of values.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/012.md) · [Batch record](../../batches/B007/README.md)
