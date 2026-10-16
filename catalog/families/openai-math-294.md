---
id: openai-math-294
record_type: family
title: Uniform bundle expansion and continuous determinant normalization
source_family: '294'
source_collection: openai/math
batch_id: B034
subject: Operator algebras
source_paper_ids:
- P-000207
instrument_ids:
- MI-000376
- MI-000377
headline: The source claims a counterexample to Kaplansky quasitrace additivity and failures of tensor-product
  stable finiteness.
central_instrument: An incidence dimension inequality produces bundle maps with no small collective image.
  A strictly geodesically convex determinant potential normalizes expanding maps continuously over the
  base.
novelty_assessment: Incidence avoidance, Sard and operator scaling are established techniques. The source
  records a bundlewise continuous normalization with a strict expansion margin; no novelty certification
  of the global counterexample.
formalization_summary: Inspected the quasitrace target and the stable-finiteness consequence target and
  definitions. They include a uniform 1/144 additivity defect and the tensor-product consequences; target
  proofs contain sorry. No Lean build was performed.
statement_faithfulness: The incidence base has real dimension 2h; the maps are smooth complex bundle maps.
  The normalization assumes expansion by a factor of at least two on every source subspace, uniformly
  over a compact base.
dependencies: Grassmann bundles, surjective evaluation of finitely many smooth sections, Sard, eigenvalue
  monotonicity, determinant expansions and continuous functional calculus.
antecedents: Gurvits operator scaling and Sra-Hosseini geodesic log-determinant convexity; classical transversality.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform bundle expansion and continuous determinant normalization

## Source manuscript and claim

[A counterexample to Kaplansky's quasitrace conjecture and failure of tensor-product stable finiteness](../papers/P-000207.md), by OpenAI, September 23, 2026.

The source claims a counterexample to Kaplansky quasitrace additivity and failures of tensor-product stable finiteness.

## Extracted instruments

- [MI-000376: Avoid small collective images by a Grassmann incidence dimension bound](../instruments/MI-000376.md)
- [MI-000377: Normalize expanding bundle maps through a unique determinant minimizer](../instruments/MI-000377.md)

## Dependencies and antecedents

Grassmann bundles, surjective evaluation of finitely many smooth sections, Sard, eigenvalue monotonicity, determinant expansions and continuous functional calculus.

Gurvits operator scaling and Sra-Hosseini geodesic log-determinant convexity; classical transversality. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read both bundle-map lemmas completely. The Chern obstruction, universal algebra construction and quasitrace-defect proof were not audited.

Inspected the quasitrace target and the stable-finiteness consequence target and definitions. They include a uniform 1/144 additivity defect and the tensor-product consequences; target proofs contain sorry. No Lean build was performed.

The incidence base has real dimension 2h; the maps are smooth complex bundle maps. The normalization assumes expansion by a factor of at least two on every source subspace, uniformly over a compact base.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/294.md) · [Batch record](../../batches/B034/README.md)
