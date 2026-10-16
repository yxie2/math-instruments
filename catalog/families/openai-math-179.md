---
id: openai-math-179
record_type: family
title: First-order principal units and a conditional binary-character obstruction
source_family: '179'
source_collection: openai/math
batch_id: B020
subject: Combinatorics
source_paper_ids:
- P-000153
instrument_ids:
- MI-000267
- MI-000268
headline: The source claims that positive orders of real circulant Hadamard matrices are exactly 1 and
  4, with the corresponding exclusion of even Barker lengths other than 2 and 4.
central_instrument: Two different small parameters at a prime over 2 yield additive first-order character
  sums. A binary coefficient identity makes their sum nonzero when supplied alternating products are odd-order
  roots of unity.
novelty_assessment: Principal-unit linearization and prime-to-residue-characteristic torsion reduction
  are elementary established facts. The extracted obstruction isolates the source binary identity but
  retains the difficult global odd-order product input as an unverified assumption.
formalization_summary: Read the scope document and CirculantHadamard.lean and EvenBarker.lean definitions
  and targets. They assert the unrestricted positive-order classification and the positive even Barker
  classification, respectively. These files specify targets with sorry placeholders; no Lean solution
  was built or kernel-checked.
statement_faithfulness: The local ring is a domain, the small parameter is nonzero, and torsion order
  must be coprime to the residue characteristic. Residue one alone does not imply equality to one; the
  order-four example demonstrates this.
dependencies: Local domains, first-order principal units, Gaussian integers, character orthogonality and
  a separately supplied global alternating-product theorem.
antecedents: Classical principal-unit quotients, reduction of prime-to-p torsion and character sums. The
  source cites Kronecker for the preceding global root-of-unity criterion.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# First-order principal units and a conditional binary-character obstruction

## Source manuscript and claim

[The circulant Hadamard conjecture](../papers/P-000153.md), by OpenAI, September 23, 2026.

The source claims that positive orders of real circulant Hadamard matrices are exactly 1 and 4, with the corresponding exclusion of even Barker lengths other than 2 and 4.

## Extracted instruments

- [MI-000267: Principal-unit first-order maps and prime-to-residue torsion reduction](../instruments/MI-000267.md)
- [MI-000268: A binary identity couples two first-order character sums](../instruments/MI-000268.md)

## Dependencies and antecedents

Local domains, first-order principal units, Gaussian integers, character orthogonality and a separately supplied global alternating-product theorem.

Classical principal-unit quotients, reduction of prime-to-p torsion and character sums. The source cites Kronecker for the preceding global root-of-unity criterion. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the first-order lemma, torsion reduction proof and complete final binary contradiction. The local comparison and alternating-product proposition needed to supply odd torsion were not audited.

Read the scope document and CirculantHadamard.lean and EvenBarker.lean definitions and targets. They assert the unrestricted positive-order classification and the positive even Barker classification, respectively. These files specify targets with sorry placeholders; no Lean solution was built or kernel-checked.

The local ring is a domain, the small parameter is nonzero, and torsion order must be coprime to the residue characteristic. Residue one alone does not imply equality to one; the order-four example demonstrates this.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/179.md) · [Batch record](../../batches/B020/README.md)
