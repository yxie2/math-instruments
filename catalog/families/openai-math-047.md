---
id: openai-math-047
record_type: family
title: Polynomial cylinder certificates and filtered derivation control
source_family: '047'
source_collection: openai/math
batch_id: B026
subject: Algebraic and complex geometry
source_paper_ids:
- P-000176
instrument_ids:
- MI-000314
- MI-000315
headline: The source claims an explicit complex four-dimensional affine domain A with A[w] polynomial
  in five variables while A itself is not polynomial in four variables.
central_instrument: A finite exponential changes the equation, after which an explicit ideal-membership
  certificate removes a localized coordinate denominator. Degree-exact representatives let a locally nilpotent
  derivation pass to the associated graded algebra.
novelty_assessment: Residual-coordinate stabilization and homogenization of locally nilpotent derivations
  have established antecedents. The explicit cylinder arithmetic is checked here; the claimed obstruction
  to A being polynomial is not certified.
formalization_summary: Read ComplexCancellation.lean and the family scope. The target gives the explicit
  quotient polynomial, finite type, domain, Krull dimension four, a polynomial cylinder and non-isomorphism
  to a four-variable polynomial algebra. Stable-coordinate and general line-bundle lifting consequences
  are excluded. These are inspected target statements with sorry placeholders; no Lean solution was built
  or kernel-checked.
statement_faithfulness: Localization alone does not provide a coordinate at p=0. The certificate is polynomial
  before localization. The filtered derivation argument requires exact weighted representatives, and LND
  order additivity requires a characteristic-zero domain.
dependencies: Locally nilpotent exponential maps, unimodular linear substitutions, polynomial ideal certificates,
  cancellation by a nonzero divisor, adapted filtrations and iterated Leibniz.
antecedents: El Kahoui-Ouali and Dutta-Lahiri on residual and stable coordinates; Kaliman-Makar-Limanov
  filtered derivations; classical factorial closure of LND kernels.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Polynomial cylinder certificates and filtered derivation control

## Source manuscript and claim

[An explicit failure of complex affine-space cancellation](../papers/P-000176.md), by OpenAI, September 23, 2026.

The source claims an explicit complex four-dimensional affine domain A with A[w] polynomial in five variables while A itself is not polynomial in four variables.

## Extracted instruments

- [MI-000314: A polynomial certificate removes the denominator from a cylinder coordinate](../instruments/MI-000314.md)
- [MI-000315: Use an adapted filtration to preserve locally nilpotent derivations and their invariants](../instruments/MI-000315.md)

## Dependencies and antecedents

Locally nilpotent exponential maps, unimodular linear substitutions, polynomial ideal certificates, cancellation by a nonzero divisor, adapted filtrations and iterated Leibniz.

El Kahoui-Ouali and Dutta-Lahiri on residual and stable coordinates; Kaliman-Makar-Limanov filtered derivations; classical factorial closure of LND kernels. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete construction and stabilization section, the induced-LND proof and the LND-order lemma. The exact associated-graded presentation, lifted additive actions and rigidity obstruction were not audited.

Read ComplexCancellation.lean and the family scope. The target gives the explicit quotient polynomial, finite type, domain, Krull dimension four, a polynomial cylinder and non-isomorphism to a four-variable polynomial algebra. Stable-coordinate and general line-bundle lifting consequences are excluded. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

Localization alone does not provide a coordinate at p=0. The certificate is polynomial before localization. The filtered derivation argument requires exact weighted representatives, and LND order additivity requires a characteristic-zero domain.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/047.md) · [Batch record](../../batches/B026/README.md)
