---
id: openai-math-330
record_type: family
title: Signed tests and metric wedges for approximation obstructions
source_family: '330'
source_collection: openai/math
batch_id: B009
subject: Functional analysis
source_paper_ids:
- P-000109
instrument_ids:
- MI-000174
- MI-000175
headline: The source claims a countable uniformly discrete, unbounded and nonproper metric space whose
  real Lipschitz-free space has AP but no BAP. Its bounded blocks also yield equivalent norms on real
  ell1 with prescribed failures of bounded approximation.
central_instrument: Continuation records discard at most one direction per support state, allowing opposite
  scalar tests whose signed-measure errors average by degree. Pointed metric wedges transfer arbitrarily
  large block obstructions while preserving ordinary approximation.
novelty_assessment: Free-space linearization, McShane extension, signed dual representations and direct-sum
  approximation are classical. The support-state continuation and anchor construction are candidate source-specific
  ingredients. The complete block construction and global result are not certified here.
formalization_summary: DiscreteLipschitzFree.lean states the bounded-block anchor obstruction and the
  AP-without-BAP endpoint. RealL1Renorming.lean states equivalent complete real ell1 norms with 2B_p-BAP
  but not p-BAP, B_p=300p^2+150p+5, preserving the original vector-space operations. The family scope
  and Comparator declarations were compared. No Lean solution was built or kernel-checked; the auxiliary
  cards are not separate Comparator targets.
statement_faithfulness: A bounded uniformly discrete free space is isomorphic to ell1 and has a diameter-dependent
  BAP. The final example must be unbounded; it is not proper. A finite-rank range need not have finite
  evaluation support until it is perturbed. Signed measures, not necessarily probabilities, are required.
dependencies: Finite-rank support perturbation; affine mass-one signed measures; bounded total variation;
  rare nonbacktracking matches after fixing the support; strict continuation maxima; clipped scalar extension;
  reversal-invariant incidence averaging; contractive pointed retractions.
antecedents: Kalton gives AP for uniformly discrete free spaces and posed the BAP issue. Godefroy-Kalton
  develop linearization; the coefficient ell1 equivalence is established. Naor uses signed representations
  in almost extension. Ben-David and coauthors use a related continuation-length consistency argument
  in graph algorithms.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Signed tests and metric wedges for approximation obstructions

## Source manuscript and claim

[A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces](../papers/P-000109.md), by OpenAI, September 26, 2026.

The source claims a countable uniformly discrete, unbounded and nonproper metric space whose real Lipschitz-free space has AP but no BAP. Its bounded blocks also yield equivalent norms on real ell1 with prescribed failures of bounded approximation.

## Extracted instruments

- [MI-000174: Continuation records permit signed opposing tests with degree-averaged loss](../instruments/MI-000174.md)
- [MI-000175: Pointed wedges preserve AP while accumulating unbounded approximation constants](../instruments/MI-000175.md)

## Dependencies and antecedents

Finite-rank support perturbation; affine mass-one signed measures; bounded total variation; rare nonbacktracking matches after fixing the support; strict continuation maxima; clipped scalar extension; reversal-invariant incidence averaging; contractive pointed retractions.

Kalton gives AP for uniformly discrete free spaces and posed the BAP issue. Godefroy-Kalton develop linearization; the coefficient ell1 equivalence is established. Naor uses signed representations in almost extension. Ben-David and coauthors use a related continuation-length consistency argument in graph algorithms. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the finite-support and signed-measure reductions, rare-walk quantifier order, continuation lemma, scalar tests and wedge reduction. The complete deterministic colored-graph sequence and all block geometry estimates were not audited.

DiscreteLipschitzFree.lean states the bounded-block anchor obstruction and the AP-without-BAP endpoint. RealL1Renorming.lean states equivalent complete real ell1 norms with 2B_p-BAP but not p-BAP, B_p=300p^2+150p+5, preserving the original vector-space operations. The family scope and Comparator declarations were compared. No Lean solution was built or kernel-checked; the auxiliary cards are not separate Comparator targets.

A bounded uniformly discrete free space is isomorphic to ell1 and has a diameter-dependent BAP. The final example must be unbounded; it is not proper. A finite-rank range need not have finite evaluation support until it is perturbed. Signed measures, not necessarily probabilities, are required.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/330.md) · [Batch record](../../batches/B009/README.md)
