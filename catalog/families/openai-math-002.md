---
id: openai-math-002
record_type: family
title: Full BSD formula from low Selmer corank
source_family: '002'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Number theory and arithmetic geometry
source_paper_ids:
- P-000033
- P-000064
- P-000072
instrument_ids:
- MI-000053
- MI-000054
- MI-000055
headline: Full BSD formula in Selmer corank 0 and 1
central_instrument: '“Tame variables”: ultrafilter limits of cyclic characters at auxiliary primes used as extra Iwasawa variables to force integrality with no residual-image hypothesis; a “theta implication” comparing Artin lengths from a holomorphic theta family on U(3,1) with a nilpotent parameter replaces Eisenstein congruences.'
novelty_assessment: new construction; rest combination
formalization_summary: 'no'
statement_faithfulness: —
dependencies: 'yes: Selmer converse, two-primary BSD, Goldfeld (→ Smith 2025 preprint)'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized new construction three-paper chain plus an unpublished preprint
map_formalization_summary: 'no'
---

# Full BSD formula from low Selmer corank

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000033](../papers/P-000033.md)
- [P-000064](../papers/P-000064.md)
- [P-000072](../papers/P-000072.md)

## Family description

Source status as recorded in the direction paper: not formalized new construction three-paper chain plus an unpublished preprint

If the q-power Selmer group of $`E/\mathbb{Q}`$ has corank 0 or 1 at some prime q, then rank equals analytic rank equals that corank, Sha is finite, and the exact BSD leading-term formula holds with no hypotheses on reduction, torsion, isogenies, CM or residual image. The main paper’s own contribution is the exact valuation at every odd prime; rank and finiteness come from the companion “Selmer converse”, the 2-adic part from the “two-primary” companion, and the auxiliary quadratic fields from family 006, which rests on Smith’s 2025 preprint.

## Extracted instruments.

- [MI-000053: Tame variables, finite models and residual concentration](../instruments/MI-000053.md)

- [MI-000054: Integral character-division test and codimension-two divisor removal](../instruments/MI-000054.md)

- [MI-000055: Theta implication with a retained nilpotent tame parameter](../instruments/MI-000055.md)

## Reused.

Gross–Zagier and Kolyvagin; Kato’s zeta elements; Kolyvagin derivatives with Mazur–Rubin switches; BDP measures; Cassels and Milne isogeny invariance; Burungale–Flach for CM rank 0; Chai–Hida rigidity; Poitou–Tate.

## Caveats.

Proposition 5.14 asserts Kato’s divisibility at every odd prime including Eisenstein primes, stronger than the statements found in the initial comparison, and is a principal step to check. The foundational steps require attention (ultrafilter limits of cochains, “no $`\mathrm{lim}^{1}`$ term”). The companion’s appendix cites an undated 185-page author-hosted draft, apparently not load-bearing.

## Recorded assessment

- Novelty: new construction; rest combination
- Formalization: no
- Statement coverage: —
- Dependencies: yes: Selmer converse, two-primary BSD, Goldfeld (→ Smith 2025 preprint)
- Antecedents: —
