# B056: Finite algebra certificates and representation-theory reductions

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000546: Check a sparse Hochschild class by a full polynomial certificate](../../catalog/instruments/MI-000546.md) | 199 |
| [MI-000547: Transfer two-sided cohomology vanishing through a trivial extension](../../catalog/instruments/MI-000547.md) | 199 |
| [MI-000548: Filter Koszul positions by exponent plus exterior support](../../catalog/instruments/MI-000548.md) | 200 |
| [MI-000549: Use commuting forms and right multiplication to extract one monomial ideal](../../catalog/instruments/MI-000549.md) | 200 |
| [MI-000550: Bound coordinate inversion by integral exterior volume](../../catalog/instruments/MI-000550.md) | 203 |
| [MI-000551: Separate principal units before restricting cohomology to a Sylow subgroup](../../catalog/instruments/MI-000551.md) | 203 |
| [MI-000552: Track repeated cycles in a character-square recurrence](../../catalog/instruments/MI-000552.md) | 205 |
| [MI-000553: Construct a horizontal-strip chain from dominance](../../catalog/instruments/MI-000553.md) | 205 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B056.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from four algebra and representation-theory families and all eight associated manuscripts. Complete selected source arguments were read. Targeted primary comparisons include Cibils-Marcos-Redondo-Solotar, Mermin-Murai, Stacks Tag 00N6, Eisele and Law lectures recorded by Tomczak. Both available scope documents and all four linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) provide eight groups of checks. The cocycle certificate is checked over F_2[q] on all 104976 radical four-words and all 324 boundary input pairs. Other groups test transfer duality, filtered Koszul homology, noncentral ordered bases, integral coordinate projections, principal-unit restriction, a tensor-square recurrence and constructive dominance chains.

The character recurrence is independently checked only through degree 8, not the manuscript reported range through 64. Infinite Ext vanishings, general triangular-identity existence, Donovan finiteness, universal tensor squares and Saxl remain unverified. Inspected Comparator targets contain sorry; this does not describe or invalidate the separate solution files, which were not built. No source headline theorem is certified, and the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
