---
id: openai-math-159
record_type: family
title: Erdős’s reciprocal-sum conjecture
source_family: '159'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Combinatorics and theoretical computer science
source_paper_ids:
- P-000050
instrument_ids:
- MI-000037
- MI-000038
- MI-000039
headline: Erdős reciprocal-sum conjecture; quasipolynomial Szemerédi
central_instrument: '“Triangular polynomial cells” with descending precision budgets: a density increment that never resets to a sub-progression; the loss at weight i depends only on precisions at higher weights, turning $`\log\log N`$ into $`\log N`$.'
novelty_assessment: new architecture
formalization_summary: 'original: lower-bound companion; headline also linked, unbuilt'
statement_faithfulness: —
dependencies: no load-bearing
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: 'original label: companion only; repository also links a headline development, unbuilt new architecture'
map_formalization_summary: 'original: companion only; see card'
---

# Erdős’s reciprocal-sum conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000050](../papers/P-000050.md)

## Family description

Source status as recorded in the direction paper: original label: companion only; repository also links a headline development, unbuilt new architecture

The source claims $`r_k(N)\le C_kN\exp(-c_k(\log N)^{\varepsilon_k})`$ for each fixed $`k\ge3`$, with $`c_k,\varepsilon_k>0`$, and hence progressions of every finite length in any set with divergent reciprocal sum. The dyadic deduction is valid: for a $`k`$-progression-free set $`A`$,
``` math
\sum_{n\in A\cap[2^j,2^{j+1})}\frac1n
 \le 2^{-j}r_k(2^{j+1})
 \ll_k \exp(-c'_k j^{\varepsilon_k}),
```
and the last expression is summable in $`j`$. By contrast, $`\sum_{m\ge2}\exp(-(\log m)^c)`$ diverges for $`0<c\le1`$ and converges for $`c>1`$. The original discussion of the weaker Leng–Sah–Sawhney log-log bound must be understood in the former range; divergence is not true for every positive $`c`$. The 198-page source uses the LSS inverse theorem as an external input.

## Extracted instruments.

- [MI-000037: Triangular polynomial cells with descending precision budgets](../instruments/MI-000037.md)

- [MI-000038: Shift comparison and positive counting](../instruments/MI-000038.md)

- [MI-000039: Relative lifting with additive rank and exact marked projection](../instruments/MI-000039.md)

## Reused.

LSS inverse theorem; Schoen–Sisask almost-periodicity; Kelley–Meka sifting; Green–Tao polynomial orbits; Leng’s equidistribution; Candela–Sisask densification; CRT prime boxes.

## Caveats.

The quantitative upper bound was not verified here. The repository documentation links a development for the reciprocal-sum consequence, beyond the lower-bound companion noted in the initial extraction; that development was not built here. The paper claims an improvement from log log to log for every k at once. The trace’s Part I never closed (“circularity concern unresolved”) and Part II ends in “claimed/asserted”. The argument has a long chain of dependencies. An appendix extends LSS to product groups of dimension $`(2+p)^A`$ with a step-drop lemma uniform in parameter count, which the model itself flagged as delicate.

## Recorded assessment

- Novelty: new architecture
- Formalization: original: lower-bound companion; headline also linked, unbuilt
- Statement coverage: —
- Dependencies: no load-bearing
- Antecedents: —
