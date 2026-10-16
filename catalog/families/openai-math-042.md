---
id: openai-math-042
record_type: family
title: Thin parameter collars and quantitative holomorphic gluing
source_family: '042'
source_collection: openai/math
batch_id: B033
subject: Algebraic and complex geometry
source_paper_ids:
- P-000203
instrument_ids:
- MI-000368
- MI-000369
headline: The source claims that every complex K3 surface is Oka.
central_instrument: Endpoint jet matching makes a real-parameter family compatible across thin complex
  collars; a quadratic splitting recurrence pays for shrinking base domains.
novelty_assessment: Polynomial approximation, Cartan splitting and Newton iteration are classical. The
  extraction records the order of choices and the explicit loss bookkeeping; no priority or K3 theorem
  certification.
formalization_summary: No formalization scope document is listed for this family in the pinned release
  inventory. No Lean build was performed.
statement_faithfulness: The complex neighborhood may depend on the approximant. Target approximation requires
  one fixed spray or a uniform fiber modulus; arbitrary moving sprays do not supply that estimate.
dependencies: Local graph sprays, Banach-valued polynomial approximation with endpoint jets, linear dbar
  solutions, Cauchy estimates and contraction mappings.
antecedents: Classical Cartan splitting and holomorphic spray gluing; Forstneric 2013, Section 3.3, gives
  a directly comparable additive splitting construction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Thin parameter collars and quantitative holomorphic gluing

## Source manuscript and claim

[Every complex K3 surface is Oka](../papers/P-000203.md), by OpenAI, September 23, 2026.

The source claims that every complex K3 surface is Oka.

## Extracted instruments

- [MI-000368: Match endpoint jets before choosing a thin complex parameter collar](../instruments/MI-000368.md)
- [MI-000369: Pay for shrinking domains with a quadratic holomorphic splitting recurrence](../instruments/MI-000369.md)

## Dependencies and antecedents

Local graph sprays, Banach-valued polynomial approximation with endpoint jets, linear dbar solutions, Cauchy estimates and contraction mappings.

Classical Cartan splitting and holomorphic spray gluing; Forstneric 2013, Section 3.3, gives a directly comparable additive splitting construction. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete interval-complexification and quantitative open-gluing arguments. The K3 degeneration and global flexibility argument were not audited.

No formalization scope document is listed for this family in the pinned release inventory. No Lean build was performed.

The complex neighborhood may depend on the approximant. Target approximation requires one fixed spray or a uniform fiber modulus; arbitrary moving sprays do not supply that estimate.

[Batch record](../../batches/B033/README.md)
