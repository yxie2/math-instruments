# B055: Matrix trace defects, quantum pruning and rational coercivity

Extraction date: 2026-10-16. This batch adds 4 families, 9 source manuscripts and 9 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000537: Fix matrix channels before choosing a regular auxiliary coefficient](../../catalog/instruments/MI-000537.md) | 262 |
| [MI-000538: Retain a noncommutative square in integrated trace duality](../../catalog/instruments/MI-000538.md) | 262 |
| [MI-000539: Recognize an integrated divided-difference kernel as random unitary conjugation](../../catalog/instruments/MI-000539.md) | 262 |
| [MI-000540: Combine exact integer roots with a Chebyshev filter while budgeting coefficients](../../catalog/instruments/MI-000540.md) | 274 |
| [MI-000541: Prune commuting reflections using probabilities in the current pruned state](../../catalog/instruments/MI-000541.md) | 274 |
| [MI-000542: Solve contact-length variations by separating row, column and height coordinates](../../catalog/instruments/MI-000542.md) | 275 |
| [MI-000543: Eliminate high modes using coercivity in a form norm](../../catalog/instruments/MI-000543.md) | 275 |
| [MI-000544: Approximate a finite odd Gaussian formula from its output toward its leaves](../../catalog/instruments/MI-000544.md) | 281 |
| [MI-000545: Prove an expectation inequality with an exact positive certificate modulo a derivative](../../catalog/instruments/MI-000545.md) | 281 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B055.json) records hashes, exact labels and manuscript coverage.

Nine selected instruments from four families and all nine associated manuscripts. Complete selected arguments were read, with targeted primary comparisons to Benguria-Loss, Hiai, Sherstov, Nadimpalli-Parham-Vasconcelos-Yuen and Fantuzzi-Goluskin-Huang-Chernyshenko. All four scope documents and six distinct Comparators were inspected in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check fixed matrix channels, trace squares, Gaussian conjugation averages, integer filters, adaptive pruning, contact geometry, form-level energy elimination, odd formula approximation and an exact rational coercivity certificate.

The formal targets are narrower than some scope descriptions: the Lieb-Thirring target is scalar; the inspected parity Comparators contain no separate localization theorem; SKValue contains no QAOA convergence claim. Target proofs contain sorry, and no Lean solution was built. The rational polynomial identity is checked exactly, but its PDE sign and boundary hypotheses remain unverified. No source headline theorem is certified. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
