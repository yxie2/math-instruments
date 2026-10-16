---
id: openai-math-116
record_type: family
title: Finite coefficient descent and rational integration jets
source_family: '116'
source_collection: openai/math
batch_id: B074
subject: Theoretical computer science
source_paper_ids:
- P-000463
- P-000464
instrument_ids:
- MI-000694
- MI-000695
headline: The family claims uniform matrix hitting points and lists for noncommutative formulas across
  characteristics.
central_instrument: A regular representation of a truncated coefficient ring preserves bounded-degree
  nonzero numerators; integration jets make an order bound into a nonzero matrix column.
novelty_assessment: Established mechanisms and directly checked antecedents are identified below. No exhaustive
  novelty determination or source headline certification is claimed.
formalization_summary: Read the scope and complete FormulaHitting Comparator. It explicitly defines the
  rational jet matrices and targets universal nonzero evaluation for bounded-size division-free formulas
  over characteristic-zero fields. It does not separately assert construction complexity, rational-inverse
  formulas or the newer positive-characteristic theorem. RationalHitting was not inspected. The inspected
  theorem targets contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: Coefficient descent requires a regular common denominator and a strict numerator
  degree bound. Rational integration jets require characteristic zero and only detect series whose first
  nonzero coefficient survives truncation.
dependencies: Local polynomial rings, regular representations, nilpotent truncation and formal integration.
antecedents: Classical finite algebra representations and formal Taylor truncations.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite coefficient descent and rational integration jets

## Source manuscripts and claim

- [Uniform Matrix Hitting Points in Every Positive Characteristic](../papers/P-000463.md): selected passages extracted.
- [One Rational Matrix Hitting Point for Noncommutative Formulas](../papers/P-000464.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Polynomial Hitting Lists for Noncommutative Rational Formulas](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026)

The family claims uniform matrix hitting points and lists for noncommutative formulas across characteristics.

## Extracted instruments

- [MI-000694: Preserve a nonzero matrix evaluation through a finite coefficient ring](../instruments/MI-000694.md)
- [MI-000695: Convert formal integration coefficients into a nonzero first column](../instruments/MI-000695.md)

## Dependencies and antecedents

Local polynomial rings, regular representations, nilpotent truncation and formal integration.

Classical finite algebra representations and formal Taylor truncations.

## Review and formalization scope

Read the full coefficient-descent proof, the common-denominator argument preceding it and the characteristic-zero jet construction and detection calculation. Two of three manuscripts receive extractions; the rational-formula hitting-list manuscript remains inventory-only. Word-series independence, multiplicity bounds and positive-characteristic shift-system bounds are not certified.

Read the scope and complete FormulaHitting Comparator. It explicitly defines the rational jet matrices and targets universal nonzero evaluation for bounded-size division-free formulas over characteristic-zero fields. It does not separately assert construction complexity, rational-inverse formulas or the newer positive-characteristic theorem. RationalHitting was not inspected. The inspected theorem targets contain sorry; no separate solution or Lean build was checked.

Coefficient descent requires a regular common denominator and a strict numerator degree bound. Rational integration jets require characteristic zero and only detect series whose first nonzero coefficient survives truncation.

[Batch record](../../batches/B074/README.md)
