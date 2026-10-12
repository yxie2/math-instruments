---
id: openai-math-112
record_type: family
title: Depth-three circuits beyond the square root
source_family: '112'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Combinatorics, geometry and complexity
source_paper_ids:
- P-000026
instrument_ids:
- MI-000083
- MI-000084
- MI-000085
headline: Explicit depth-3 circuit lower bound $`2^{\omega(\sqrt{n})}`$
central_instrument: '“Restriction bound independent of clause count”: a restricted width-k CNF written as a signed combination of width-b CNFs with bounded expected mass, with a suitable testing width for any fixed $`pk`$; the standard switching bound $`(5pk)^s`$ gives decay in $`s`$ when $`pk<1/5`$.'
novelty_assessment: new
formalization_summary: files
statement_faithfulness: yes, Σ₃ gate count, exact computation
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 179 files new
map_formalization_summary: 'yes'
---

# Depth-three circuits beyond the square root

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000026](../papers/P-000026.md)

## Family description

Source status as recorded in the direction paper: Lean, 179 files new

The source gives a fixed language in P such that for every real constant $`A>0`$, $`\Sigma_{3}`$ circuits (unbounded fan-in, no bottom fan-in restriction, size = gate count) computing its n-bit slice need more than $`2^{A\sqrt n}`$ gates for large n: the explicit $`2^{\omega(\sqrt n)}`$ problem of Håstad–Jukna–Pudlák 1995 and Gurumukhani et al. 2024, record $`2^{1.282\sqrt n}`$ (Paturi–Pudlák–Saks–Zane 2005). The growth rate is an inverse tower in log n; this is weaker than $`2^{n^{1/2+\varepsilon}}`$, as the paper says.

## Extracted instruments.

- [MI-000083: Restriction bound independent of clause count](../instruments/MI-000083.md)

- [MI-000084: Sparse partition](../instruments/MI-000084.md)

- [MI-000085: Slice language](../instruments/MI-000085.md)

## Reused.

Håstad-style restrictions and wide-clause truncation; Razborov’s reverse encoding; sunflower lemma; universal hashing; t-th moment bounds.

## Caveats.

The argument does not depend on other OpenAI manuscripts. The mathematical review checked selected identities in Lemma 3.1 and the arithmetic in §6. A separate literature comparison for the marker-mixture device remains incomplete.

## Recorded assessment

- Novelty: new
- Formalization: files
- Statement coverage: yes, Σ₃ gate count, exact computation
- Dependencies: no
- Antecedents: —
