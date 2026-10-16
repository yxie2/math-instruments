---
id: openai-math-233
record_type: family
title: Conditional projection and local-kernel transfer for planar Gaussian fields
source_family: '233'
source_collection: openai/math
batch_id: B006
subject: Probability and statistical mechanics
source_paper_ids:
- P-000098
instrument_ids:
- MI-000152
- MI-000153
headline: The source claims a joint critical-line limit of Ashkin-Teller heights and complete primal and
  dual current supports, including the Potts endpoint. The selected instruments concern auxiliary Gaussian
  tests used in the random-domain identification.
central_instrument: Convergence of conditional Gaussian projection norms preserves locality of arbitrary
  bounded tests; Cameron-Martin comparison transfers one selected local kernel across domains and conditional
  random environments.
novelty_assessment: Gaussian projection, domain Markov decomposition and Cameron-Martin comparison are
  established. The candidate contribution is their precise combination for discontinuous cable tests with
  fixed buffers and a common subsequence. The global current-cluster theorem and historical priority are
  not certified.
formalization_summary: No family-specific formalization scope document is listed in the pinned release
  inventory. No Comparator comparison or Lean proof build is claimed.
statement_faithfulness: Auxiliary cable mesh and current mesh are distinct. Tests use the whole cable
  field, including bridges, with the specified ambient harmonic extension. Random-domain conclusions require
  the stated conditional GFF law and admissible approximations; equality of field marginals is not an
  identification of two fields path by path.
dependencies: Metric-graph GFF convergence and local sets; Gaussian Hilbert-space projections and residual
  covariances; Cameron-Martin likelihoods and Pinsker; interior harmonic estimates; conditional mixed-expectation
  limits.
antecedents: Aru, Lupu and Sepulveda supply metric-graph convergence and first-passage-set machinery.
  Established double-current results and the conjectural critical-line extension of Alcalde Lopez, Heeney
  and Lis motivate the source. Classical Gaussian change of measure remains an input.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Conditional projection and local-kernel transfer for planar Gaussian fields

## Source manuscript and claim

[The joint scaling limit of critical Ashkin-Teller currents](../papers/P-000098.md), by OpenAI, None.

The source claims a joint critical-line limit of Ashkin-Teller heights and complete primal and dual current supports, including the Potts endpoint. The selected instruments concern auxiliary Gaussian tests used in the random-domain identification.

## Extracted instruments

- [MI-000152: Converging conditional Gaussian projection norms preserve locality of bounded tests](../instruments/MI-000152.md)
- [MI-000153: Cameron-Martin comparison transfers one local test kernel across domains](../instruments/MI-000153.md)

## Dependencies and antecedents

Metric-graph GFF convergence and local sets; Gaussian Hilbert-space projections and residual covariances; Cameron-Martin likelihoods and Pinsker; interior harmonic estimates; conditional mixed-expectation limits.

Aru, Lupu and Sepulveda supply metric-graph convergence and first-passage-set machinery. Established double-current results and the conjectural critical-line extension of Alcalde Lopez, Heeney and Lis motivate the source. Classical Gaussian change of measure remains an input. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the reverse-buffer proof, common-kernel proof and interior-exhaustion corollary, preserving the exact whole-cable extension and random-parameter conditions. The finite current coupling, screening, Gaussian collision arguments and no-crossing/cluster identification were not fully audited.

No family-specific formalization scope document is listed in the pinned release inventory. No Comparator comparison or Lean proof build is claimed.

Auxiliary cable mesh and current mesh are distinct. Tests use the whole cable field, including bridges, with the specified ambient harmonic extension. Random-domain conclusions require the stated conditional GFF law and admissible approximations; equality of field marginals is not an identification of two fields path by path.

[Batch record](../../batches/B006/README.md)
