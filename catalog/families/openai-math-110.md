---
id: openai-math-110
record_type: family
title: Compact policies and finite rational online tables
source_family: '110'
source_collection: openai/math
batch_id: B073
subject: Theoretical computer science
source_paper_ids:
- P-000461
- P-000462
instrument_ids:
- MI-000692
- MI-000693
headline: The family claims a squared-logarithmic randomized k-server bound on arbitrary metrics and a
  uniform efficient implementation on rational finite metrics.
central_instrument: Finite-family feasibility extends by compactness to one policy; a rational causal
  flow table can be rounded to bounded random bits with an additive diameter loss.
novelty_assessment: Directly checked antecedents are identified below. No exhaustive novelty determination
  or certification of a source headline is claimed.
formalization_summary: Read the scope and both complete Comparators. KServer targets a squared-logarithmic
  expected bound on arbitrary metrics, with zero additive term for distinct initial servers. UniformKServer
  additionally targets polynomial computation per request on rational finite metrics; its additive constant
  is not polynomially bounded in the statement. Inspected Comparator target bodies contain sorry; no separate
  solution or Lean build was checked.
statement_faithfulness: Compactness assumes feasibility for every finite family of words and gives no
  effective algorithm. Table construction is finite but may be enormous; polynomial per-request scheduling
  is a separate unverified step.
dependencies: Product compactness, finite expected-cost polynomials, rational linear programming, conditional
  probabilities and coupling.
antecedents: Tychonoff compactness, finite-horizon online strategy linear programs and dyadic probability
  rounding.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Compact policies and finite rational online tables

## Source manuscripts and claim

- [Squared-logarithmic randomized k-server on arbitrary metrics](../papers/P-000461.md): selected passages extracted.
- [Uniform computation of the squared-logarithmic k-server bound](../papers/P-000462.md): selected passages extracted.

The family claims a squared-logarithmic randomized k-server bound on arbitrary metrics and a uniform efficient implementation on rational finite metrics.

## Extracted instruments

- [MI-000692: Extend finite-word policy constraints by compactness](../instruments/MI-000692.md)
- [MI-000693: Extract causal rational flow tables and round them with a diameter budget](../instruments/MI-000693.md)

## Dependencies and antecedents

Product compactness, finite expected-cost polynomials, rational linear programming, conditional probabilities and coupling.

Tychonoff compactness, finite-horizon online strategy linear programs and dyadic probability rounding.

## Review and formalization scope

Read the complete compact-policy proof and finite-table proposition, including singular probability rows and coupling after first disagreement. Both manuscripts receive extractions. The finite-family minimax bound, squared-logarithmic existence theorem and uniform scheduling construction are not certified.

Read the scope and both complete Comparators. KServer targets a squared-logarithmic expected bound on arbitrary metrics, with zero additive term for distinct initial servers. UniformKServer additionally targets polynomial computation per request on rational finite metrics; its additive constant is not polynomially bounded in the statement. Inspected Comparator target bodies contain sorry; no separate solution or Lean build was checked.

Compactness assumes feasibility for every finite family of words and gives no effective algorithm. Table construction is finite but may be enormous; polynomial per-request scheduling is a separate unverified step.

[Batch record](../../batches/B073/README.md)
