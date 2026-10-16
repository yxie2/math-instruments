# B076: Reflections, oscillation, polynomial coordinates and random-map clocks

Extraction date: 2026-10-16. This batch adds 4 families, 5 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000710: Use affine side relations to remove a plane-wave eigenfunction](../../catalog/instruments/MI-000710.md) | 150 |
| [MI-000711: Turn an invariant product kernel into a finite-dimensional spectral obstruction](../../catalog/instruments/MI-000711.md) | 150 |
| [MI-000712: Extract convergence from sublinear deterministic-block oscillation](../../catalog/instruments/MI-000712.md) | 154 |
| [MI-000713: Keep boundary terms in the finite van der Corput estimate](../../catalog/instruments/MI-000713.md) | 154 |
| [MI-000714: Normalize local root coefficients while retaining progression inheritance](../../catalog/instruments/MI-000714.md) | 182 |
| [MI-000715: Count square constraints before lifting to a two-list operator bound](../../catalog/instruments/MI-000715.md) | 182 |
| [MI-000716: Keep loop attempts when matching discrete and continuous clocks](../../catalog/instruments/MI-000716.md) | 211 |
| [MI-000717: Fix a deterministic scale with a bounded monotone center](../../catalog/instruments/MI-000717.md) | 211 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B076.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and five selected manuscripts. Eleven companion manuscripts remain inventory-only. Complete selected proofs, the three available scopes and all three linked Comparators were read. Primary comparisons identify classical compact spectral obstructions and Lucier auxiliary-polynomial inheritance.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) test reflection phases, compact spectral obstructions, deterministic block witnesses, finite correlation windows, local polynomial coordinates, square-constraint kernels, loop-aware clocks and law-continuous centers.

No billiard weak-mixing theorem, multiple-average convergence theorem, polynomial power saving or random-map scaling limit is certified. No separate Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
