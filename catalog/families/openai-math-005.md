---
id: openai-math-005
record_type: family
title: Matched endpoint damping and moment-square upper certificates
source_family: '005'
source_collection: openai/math
batch_id: B042
subject: Number theory
source_paper_ids:
- P-000240
instrument_ids:
- MI-000442
- MI-000443
headline: The source claims irrationality of Catalan s constant.
central_instrument: Matched damping keeps pure and mixed logarithmic moments compatible. Negative moment
  squares admit trial-coefficient upper bounds reduced to one-variable suprema.
novelty_assessment: Chebyshev logarithmic-kernel expansions and tangent upper bounds are classical. The
  source particular damping/certificate architecture is extracted without certifying the irrationality
  proof.
formalization_summary: Read Catalan.lean in full. Its catalan_irrational target contains sorry. No Lean
  build or numerical irrationality-certificate audit.
statement_faithfulness: Regularization must match the same moments in pure and cross terms. Endpoint diagonal
  corrections are retained before taking suprema; n tends to infinity before damping tends to zero.
dependencies: Chebyshev expansions, endpoint-scaled damping, negative quadratic completion, geometric
  trial coefficients and uniform coercivity.
antecedents: Haagerup logarithmic-kernel identity in Garoufalidis-Popescu Lemma 3.1; classical quadratic
  duality.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Matched endpoint damping and moment-square upper certificates

## Source manuscript and claim

[Catalan's constant is irrational](../papers/P-000240.md), by OpenAI, September 24, 2026.

The source claims irrationality of Catalan s constant.

## Extracted instruments

- [MI-000442: Match logarithmic-kernel damping to the singular endpoint scales](../instruments/MI-000442.md)
- [MI-000443: Turn negative moment squares into one-variable upper certificates](../instruments/MI-000443.md)

## Dependencies and antecedents

Chebyshev expansions, endpoint-scaled damping, negative quadratic completion, geometric trial coefficients and uniform coercivity.

Haagerup logarithmic-kernel identity in Garoufalidis-Popescu Lemma 3.1; classical quadratic duality. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete energy-reduction proof. The majorant construction, nonvanishing, finite-place estimates and final rational certificate were not audited.

Read Catalan.lean in full. Its catalan_irrational target contains sorry. No Lean build or numerical irrationality-certificate audit.

Regularization must match the same moments in pure and cross terms. Endpoint diagonal corrections are retained before taking suprema; n tends to infinity before damping tends to zero.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/005.md) · [Batch record](../../batches/B042/README.md)
