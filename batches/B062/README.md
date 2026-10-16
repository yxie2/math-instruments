# B062: Absorption, operator obstructions and state-norm recovery

Extraction date: 2026-10-16. This batch adds 4 families, 9 source manuscripts and 9 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000597: Absorb a projective representation by multiplying the regular cocycle](../../catalog/instruments/MI-000597.md) | 286 |
| [MI-000598: Use ICC to recover a full commensuration-germ stabilizer](../../catalog/instruments/MI-000598.md) | 286 |
| [MI-000599: Extract a nearby unitary intertwiner from the off-diagonal block of an almost-flip](../../catalog/instruments/MI-000599.md) | 289 |
| [MI-000600: Detect a persistent obstruction in almost-commuting clock and shift matrices](../../catalog/instruments/MI-000600.md) | 289 |
| [MI-000601: Bound a sum of free generators by splitting cancellation prefixes](../../catalog/instruments/MI-000601.md) | 289 |
| [MI-000602: Obtain two GNS multiplication isometries from scalar conditional expectations](../../catalog/instruments/MI-000602.md) | 290 |
| [MI-000603: Turn fourth-moment control into a bounded spectrally filtered witness](../../catalog/instruments/MI-000603.md) | 290 |
| [MI-000604: Recover a maximal-abelian expectation by refining centralizer pinches](../../catalog/instruments/MI-000604.md) | 300 |
| [MI-000605: Control functional calculus with a class of state-continuous right multipliers](../../catalog/instruments/MI-000605.md) | 300 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B062.json) records hashes, exact labels and manuscript coverage.

Nine selected instruments from four families and all nine associated manuscripts. Complete selected source arguments were read. Primary comparisons include Vaes and Haagerup-Musat; Exel-Loring was checked only at abstract/introduction level because full PDF retrieval failed. Both available Lean scope documents and both linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) cover twisted absorption, free-word germ controls, polar intertwiners, the clock-and-shift index, free-prefix norm bounds, conditional GNS products, fourth moments and clipping, centralizer pinching, and right-multiplier controls.

The finite checks have explicit boundaries. They do not compute completely bounded distances, certify arbitrary ICC germs, realize scalar centralizers in nontrivial finite matrix algebras, or prove the source global classification, stability, bicentralizer and paving headlines. Classical mechanisms are identified as such. No Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
