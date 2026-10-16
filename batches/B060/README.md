# B060: Tree representations, probabilistic covers and Fourier restriction

Extraction date: 2026-10-16. This batch adds 4 families, 9 source manuscripts and 9 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000578: Regularize a determinant potential while preserving every subset rank](../../catalog/instruments/MI-000578.md) | 174 |
| [MI-000579: Separate partition capacity constraints using minimum spanning trees](../../catalog/instruments/MI-000579.md) | 174 |
| [MI-000580: Compress a cover after independent Bernoulli smoothing](../../catalog/instruments/MI-000580.md) | 175 |
| [MI-000581: Use a maximal truncation to bound the strictly heavy set](../../catalog/instruments/MI-000581.md) | 175 |
| [MI-000582: Repair a sampled cover using the quadratic number of pair failures](../../catalog/instruments/MI-000582.md) | 175 |
| [MI-000583: Concentrate a sum by counting how often each independent input is read](../../catalog/instruments/MI-000583.md) | 184 |
| [MI-000584: Couple all probability rows through one rejection stream](../../catalog/instruments/MI-000584.md) | 184 |
| [MI-000585: Capture a hypergraph support by hitting one low-degree vertex](../../catalog/instruments/MI-000585.md) | 186 |
| [MI-000586: Average a Fourier restriction without discarding exterior degree](../../catalog/instruments/MI-000586.md) | 186 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B060.json) records hashes, exact labels and manuscript coverage.

Nine instruments from four families and all nine associated manuscripts. Complete selected arguments were read, with direct primary comparisons to Barthe, Bednorz-Martynek-Meller, Fischer-Person, Gavinsky and coauthors, Angel-Spinka and Kelman and coauthors. All four scopes and all six linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain nine groups: isotropic tree unions, MST separation, smoothed compression, exact cutoffs, sampled-pair covers, read-k tails, exact joint coupling, hypergraph capture and biased Fourier restriction.

The tools include explicitly classical results. Smoothed success is not deterministic containment; simultaneous coupling is not simultaneous pairwise optimality; one captured support vertex need not mean one edge; restricted Fourier degree does not constrain exterior degree. Small cover examples test the mechanism, not the enormous theorem-scale instances. No Lean solution was built and no headline thin-tree, expectation-threshold, coloring or influence theorem is certified. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
