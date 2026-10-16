---
id: openai-math-108
record_type: family
title: Signed equality gadgets and linear-size coefficient selection
source_family: '108'
source_collection: openai/math
batch_id: B040
subject: Theoretical computer science
source_paper_ids:
- P-000233
instrument_ids:
- MI-000428
- MI-000429
headline: The source claims a cubic lower bound for border determinantal complexity of the permanent.
central_instrument: A signed three-by-three gadget enforces equality of edge choices by cancellation.
  Two cardinality gates select a diagonal-shift coefficient with linear permanent-size overhead.
novelty_assessment: Signed permanent gadgets have explicit Valiant and Dell-Husfeldt-Marx-Taslaman-Wahlen
  antecedents. The source specific count/scalar interface is extracted without a priority certification.
formalization_summary: Read PermanentCubic.lean and SmoothInitialForm.lean in full. Both main target proofs
  contain sorry. No Lean build; neither the cubic nor smooth-initial-form lower bound is certified here.
statement_faithfulness: Cancellation concerns sums of completions, not absence of individual matchings.
  The scalar must be nonzero; the complex projection does not transfer unchanged to characteristic two.
dependencies: Weighted perfect matchings, signed boundary tables, count gates and fixed affine substitution.
antecedents: Valiant permanent projections; Dell-Husfeldt-Marx-Taslaman-Wahlen Section 3 and Figure 2.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Signed equality gadgets and linear-size coefficient selection

## Source manuscript and claim

[A cubic lower bound for border determinantal complexity of the permanent](../papers/P-000233.md), by OpenAI, September 24, 2026.

The source claims a cubic lower bound for border determinantal complexity of the permanent.

## Extracted instruments

- [MI-000428: Enforce equality of two matching-edge choices by signed cancellation](../instruments/MI-000428.md)
- [MI-000429: Select two prescribed diagonal-shift exponents with linear permanent overhead](../instruments/MI-000429.md)

## Dependencies and antecedents

Weighted perfect matchings, signed boundary tables, count gates and fixed affine substitution.

Valiant permanent projections; Dell-Husfeldt-Marx-Taslaman-Wahlen Section 3 and Figure 2. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete selector proof, including every boundary state and shared-vertex factorization, and the border-model/affine-substitution proofs. The gradient/conductor lower-bound argument was not audited.

Read PermanentCubic.lean and SmoothInitialForm.lean in full. Both main target proofs contain sorry. No Lean build; neither the cubic nor smooth-initial-form lower bound is certified here.

Cancellation concerns sums of completions, not absence of individual matchings. The scalar must be nonzero; the complex projection does not transfer unchanged to characteristic two.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/108.md) · [Batch record](../../batches/B040/README.md)
