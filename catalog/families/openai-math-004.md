---
id: openai-math-004
record_type: family
title: Hilbert’s tenth problem over ℚ
source_family: '004'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Number theory and arithmetic geometry
source_paper_ids:
- P-000019
- P-000042
instrument_ids:
- MI-000004
- MI-000005
- MI-000006
headline: Hilbert’s tenth problem over $`\mathbb{Q}`$ undecidable
central_instrument: The reduction does not construct a Diophantine definition of $`\mathbb{Z}`$. A Turing reduction dovetails integer-root enumeration with finite rational-oracle tests. Compactness and elliptic height bounds show that some finite test fails if no integer root exists. Every terminating run makes finitely many queries, with no uniform bound asserted.
novelty_assessment: new
formalization_summary: 'no'
statement_faithfulness: —
dependencies: 'yes: FM modularity at 2; pointwise 2-converse'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized new architecture depends on two other OpenAI papers
map_formalization_summary: 'no'
---

# Hilbert’s tenth problem over ℚ

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000019](../papers/P-000019.md)
- [P-000042](../papers/P-000042.md)

## Family description

Source status as recorded in the direction paper: not formalized new architecture depends on two other OpenAI papers

No algorithm decides whether an integer polynomial has a rational zero; the problem has Turing degree $`0'`$, already for degree $`\le 4`$. The paper explicitly gives no existential definition of $`\mathbb{Z}`$ in $`\mathbb{Q}`$ and no Diophantine model, so this route does not conflict with Mazur’s conjecture.

## Extracted instruments.

- [MI-000004: Finite rational tests with compactness](../instruments/MI-000004.md)

- [MI-000005: Five-point height estimate](../instruments/MI-000005.md)

- [MI-000006: Pole-parity existential formula](../instruments/MI-000006.md)

## Reused.

DPRM; Poonen 2002 index reading; Cassels–Tate; Deligne canonical models; Darmon–Granville; Green–Tao–Ziegler with Selberg sieve; compactness.

## Caveats.

The argument depends on two other unverified OpenAI manuscripts: “Fontaine–Mazur modularity at the prime 2” and “A pointwise 2-converse for elliptic curves with rational two-torsion”. The second is needed as written to eliminate Sha\[2\]. The proof of termination uses a non-constructive compactness argument.

## Recorded assessment

- Novelty: new
- Formalization: no
- Statement coverage: —
- Dependencies: yes: FM modularity at 2; pointwise 2-converse
- Antecedents: —
