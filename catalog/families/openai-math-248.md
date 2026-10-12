---
id: openai-math-248
record_type: family
title: Thompson’s group F is not amenable
source_family: '248'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Algebra and operator algebras
source_paper_ids:
- P-000073
instrument_ids:
- MI-000047
- MI-000048
- MI-000049
headline: Thompson’s group F is not amenable
central_instrument: Color each element of a Følner set by a Hilbert-ball vector via the recursion “color = f(average of child colors)”, with f a Benyamini–Sternfeld Lipschitz map having no approximate fixed point; pair transports force the averages to agree, an impossibility.
novelty_assessment: new use; leaning new
formalization_summary: yes, F from scratch
statement_faithfulness: 'yes'
dependencies: corollaries only
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, conceptual, F defined from scratch new use, leaning new
map_formalization_summary: 'yes'
---

# Thompson’s group F is not amenable

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000073](../papers/P-000073.md)

## Family description

Source status as recorded in the direction paper: Lean, conceptual, F defined from scratch new use, leaning new

F admits no positive normalized left-invariant mean, settling Geoghegan’s 1979 question in five pages. The formal statement defines F as dyadic piecewise-linear homeomorphisms and the invariant mean on $`\ell^\infty(F)`$; it gives no finite certificate, and the constants are existential.

## Extracted instruments.

- [MI-000047: Recursive Hilbert-ball-valued coloring of dyadic partitions](../instruments/MI-000047.md)

- [MI-000048: Benyamini–Sternfeld displacement map as an amenability obstruction](../instruments/MI-000048.md)

- [MI-000049: Correlation comparison via pair transport](../instruments/MI-000049.md)

## Reused.

Følner’s criterion (formalized forward direction); Cannon–Floyd–Parry partition model; Benyamini–Sternfeld; convexity of the square norm.

## Caveats.

The five-page argument addresses Geoghegan’s amenability question. The pointwise and averaged estimates above were compared with the source; this check does not certify the full proof. A direct invariant-mean argument can fail because a fixed partition level may have measure zero. The source instead chooses a finite averaging set A first and selects the level afterwards. Other OpenAI preprints are used only for corollaries.

## Recorded assessment

- Novelty: new use; leaning new
- Formalization: yes, F from scratch
- Statement coverage: yes
- Dependencies: corollaries only
- Antecedents: —
