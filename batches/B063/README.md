# B063: Geometric reductions, measure changes and holomorphic filters

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000606: Rule out an open zero-height region using finite-radius frequency control](../../catalog/instruments/MI-000606.md) | 346 |
| [MI-000607: Compare projected mass with integer counts using determinant and tilt errors](../../catalog/instruments/MI-000607.md) | 346 |
| [MI-000608: Separate the affine maximal equation with a square-root graph ansatz](../../catalog/instruments/MI-000608.md) | 353 |
| [MI-000609: Derive an inverse-Hessian cap identity from affine stationarity](../../catalog/instruments/MI-000609.md) | 353 |
| [MI-000610: Flatten model distance while keeping its upper Hessian bound](../../catalog/instruments/MI-000610.md) | 356 |
| [MI-000611: Obtain weighted-generator regularity from the original heat resolvent](../../catalog/instruments/MI-000611.md) | 356 |
| [MI-000612: Turn bounded Hartogs coordinates into a forbidden holomorphic real-part bound](../../catalog/instruments/MI-000612.md) | 359 |
| [MI-000613: Extract one Taylor residue class with a root-of-unity filter](../../catalog/instruments/MI-000613.md) | 359 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B063.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from four families and all eight associated manuscripts. Complete selected arguments were read. Primary comparisons include Simon's area formula, Wang's affine-maximal survey and Brena-Gigli's weighted regularity discussion. All three available scope documents and all three linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: frequency identities, projection determinants, separated affine Hessians, cap integrals, model-distance cutoffs, drift resolvents, Hartogs determinant bounds and root-of-unity filters.

The records distinguish classical tools from source-specific interfaces and retain all conditional inputs. No source singular-set, global affine Bernstein, RCD curvature, every-geodesic, negative-curvature or Liouville headline is certified. Finite Fourier models do not prove infinite-dimensional generator regularity. No Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
