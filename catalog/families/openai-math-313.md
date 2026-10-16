---
id: openai-math-313
record_type: family
title: Dense inverse limits and compact derived Nakayama
source_family: '313'
source_collection: openai/math
batch_id: B037
subject: Topology
source_paper_ids:
- P-000221
instrument_ids:
- MI-000404
- MI-000405
headline: The source claims finite generation over Z_p of every homotopy group of the K(n)-local sphere
  for all positive heights and primes.
central_instrument: A small-correction construction kills lim-one for dense countable Banach towers. Derived
  completeness and finite mod-p homotopy produce compact modules to which a digit-by-digit Nakayama argument
  applies.
novelty_assessment: These are established inverse-limit and completion mechanisms. The source cites Le
  Bras for the dense-tower criterion. The difficult chromatic finiteness inputs are outside this extraction.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build was performed.
statement_faithfulness: Dense maps need not be onto. Derived completeness is a spectrum-level assumption;
  ordinary completeness of individual homotopy groups is derived, not assumed. Finite mod-p cofiber groups
  need not themselves be killed by p.
dependencies: Complete nonarchimedean spaces, finite clopen approximations, the countable product model
  of derived inverse limit, finite p-groups and compact Nakayama.
antecedents: Le Bras 2018, Proposition 3.5; classical Milnor exact sequences and topological Nakayama
  arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Dense inverse limits and compact derived Nakayama

## Source manuscript and claim

[Finite generation for the K(n)-local sphere](../papers/P-000221.md), by OpenAI, September 24, 2026.

The source claims finite generation over Z_p of every homotopy group of the K(n)-local sphere for all positive heights and primes.

## Extracted instruments

- [MI-000404: Kill lim-one by uniformly small corrections in a dense Banach tower](../instruments/MI-000404.md)
- [MI-000405: Derive finite generation from finite mod-p homotopy and derived completeness](../instruments/MI-000405.md)

## Dependencies and antecedents

Complete nonarchimedean spaces, finite clopen approximations, the countable product model of derived inverse limit, finite p-groups and compact Nakayama.

Le Bras 2018, Proposition 3.5; classical Milnor exact sequences and topological Nakayama arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete countable Banach inverse-limit lemma and the derived-completion finite-generation lemma. The marking towers, transfer stabilization and mod-p chromatic finiteness theorem were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build was performed.

Dense maps need not be onto. Derived completeness is a spectrum-level assumption; ordinary completeness of individual homotopy groups is derived, not assumed. Finite mod-p cofiber groups need not themselves be killed by p.

[Batch record](../../batches/B037/README.md)
