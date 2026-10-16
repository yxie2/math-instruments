# B023: Finite bookkeeping for analytic hierarchies

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000288: Fractional cell variance preserves second moments on moving measures](../../catalog/instruments/MI-000288.md) | 081 |
| [MI-000289: Charge overlapping descendant seeds through disjoint generation intervals](../../catalog/instruments/MI-000289.md) | 081 |
| [MI-000290: Exponential-clock thinning cancels its own inverse-probability cost](../../catalog/instruments/MI-000290.md) | 083 |
| [MI-000291: A small lower deficit prevents a fixed loss when changing probabilities](../../catalog/instruments/MI-000291.md) | 083 |
| [MI-000292: Proportional cancellation gives exact reconstruction on a refinement graph](../../catalog/instruments/MI-000292.md) | 085 |
| [MI-000293: Fill refinement capacities with particles that retain their birth levels](../../catalog/instruments/MI-000293.md) | 085 |
| [MI-000294: Binary blocks control row-selected products of noncommuting nested projections](../../catalog/instruments/MI-000294.md) | 086 |
| [MI-000295: Group a multilinear expansion by its two earliest increments and retain the remainder](../../catalog/instruments/MI-000295.md) | 086 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B023.json).

Eight instruments are extracted from four analysis families. The selected proofs were read in full, with primary comparisons to Kuwae-Shioya varying Hilbert spaces, classical local-minimum independent-set selection and the Mikhailets-Murach presentation of the Rademacher-Menshov estimate. Four Comparator target files were inspected. These comparisons do not certify novelty or the headline analytic claims.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give eight check groups.

- Family 081: 12 atomic cell-variance models and 150 weighted trees with 9,600 leafwise charging checks. Atomic grids test finite identities, not continuum AD hypotheses. The source energy, flat-limit and excess-propagation inputs remain unaudited.
- Family 083: 6,960 exact clock orders on 32 graphs, compensated Hilbert models and 500 probability mixtures, including sharp two-point transfer examples. Retention is explicitly dependent. The higher-p Fourier, snapshot and path-product estimates remain inputs.
- Family 085: 540 exact signed-measure reconstruction identities on 45 shared-descendant models, and 8,320 birth-filtered prefix occupancies on 80 vector-refinement models. Zero-mass cancellation and pre-birth history are retained. These are not disk-maximal endpoint checks.
- Family 086: 108 noncommuting projection operator-norm models and 90 exact four-tensor expansions with 2,625 grouped terms. Nonnested projections and dropped terminal remainders fail the corresponding conclusions. The continuous inverse theorem, compression and scale summation were not audited.

The four Comparator files contain target statements, not a Lean proof build performed here. Family 086 has no listed family-specific scope document. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
