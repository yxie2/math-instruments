---
id: openai-math-257
record_type: family
title: Normalize combinatorial counts and test dependent vectors in CAT(0) cones
source_family: '257'
source_collection: openai/math
batch_id: B031
subject: Group theory
source_paper_ids:
- P-000196
instrument_ids:
- MI-000354
- MI-000355
headline: The source claims a word-hyperbolic group with no geometric CAT(0) action, built from finite
  random presentation data.
central_instrument: Small summed count error gives total-variation control after normalization. A coupling
  with repeated common data and almost-independent leaves bounds action-dependent tests using inductive
  cone means.
novelty_assessment: Count normalization is elementary. The inductive-mean estimate is explicitly Sturm
  2003, Theorem 4.7, proof (a). The source packages these tools into a conditional-test interface; global
  non-CAT action is not certified.
formalization_summary: 'Read HyperbolicObstruction.lean and its scope: a finite aspherical model with
  linear filling, word-hyperbolic fundamental group, no geometric action on a nonempty proper complete
  CAT(0) space, and no homotopy-equivalent finite model with a locally CAT(-1) metric. Its target contains
  sorry; no build was performed.'
statement_faithfulness: The Comparator does not assert a two-dimensional witness or exclude every locally
  CAT(0) finite model. In the conditional test, the bounded common vector may depend on all table data;
  no independence from leaves is assumed. Limits are taken first in instance size, then in the fixed number
  of leaves.
dependencies: Summed conditional count deviations, Markov inequality, total variation, CAT(0) cone geometry,
  barycenter variance and inductive means.
antecedents: Sturm 2003, Definition 4.6 and Theorem 4.7, proof (a); elementary normalization and sampling
  without replacement.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Normalize combinatorial counts and test dependent vectors in CAT(0) cones

## Source manuscript and claim

[A hyperbolic group with no geometric CAT(0) action](../papers/P-000196.md), by OpenAI, September 25, 2026.

The source claims a word-hyperbolic group with no geometric CAT(0) action, built from finite random presentation data.

## Extracted instruments

- [MI-000354: Turn summed extension-count errors into a normalized coupling law](../instruments/MI-000354.md)
- [MI-000355: Bound dependent conditional tests through inductive means in a CAT(0) cone](../instruments/MI-000355.md)

## Dependencies and antecedents

Summed conditional count deviations, Markov inequality, total variation, CAT(0) cone geometry, barycenter variance and inductive means.

Sturm 2003, Definition 4.6 and Theorem 4.7, proof (a); elementary normalization and sampling without replacement. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full count-to-coupling proof, cone-mean lemma and uniform conditional-test proof. Random-table concentration, diagram estimates and final geometric obstruction were not audited.

Read HyperbolicObstruction.lean and its scope: a finite aspherical model with linear filling, word-hyperbolic fundamental group, no geometric action on a nonempty proper complete CAT(0) space, and no homotopy-equivalent finite model with a locally CAT(-1) metric. Its target contains sorry; no build was performed.

The Comparator does not assert a two-dimensional witness or exclude every locally CAT(0) finite model. In the conditional test, the bounded common vector may depend on all table data; no independence from leaves is assumed. Limits are taken first in instance size, then in the fixed number of leaves.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/257.md) · [Batch record](../../batches/B031/README.md)
