# B014: Spectral normalization, dependent cancellation and conditional entropy gains

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000213: Separated integer frequencies reproduce a finite collection of phase averages](../../catalog/instruments/MI-000213.md) | 144 |
| [MI-000214: Spectral whitening fills zero-density sets without an inverse lower bound](../../catalog/instruments/MI-000214.md) | 144 |
| [MI-000215: Sublinear word entropy forces cancellation against dissociated characters under arbitrary coupling](../../catalog/instruments/MI-000215.md) | 145 |
| [MI-000216: Triple independence fixes positive squares and preserves an operator rectangle under polar normalization](../../catalog/instruments/MI-000216.md) | 145 |
| [MI-000217: A sumset bound converts hidden grid entropy into fair-pair capacity at finer scales](../../catalog/instruments/MI-000217.md) | 148 |
| [MI-000218: Two-point entropy gains survive future averaging when the pair is fixed by the past](../../catalog/instruments/MI-000218.md) | 148 |
| [MI-000219: A decoding-capacity contradiction forces measure overlap between the two first-bit branches](../../catalog/instruments/MI-000219.md) | 153 |
| [MI-000220: Singular concentration and common branch mass produce many nearby opposite prefixes](../../catalog/instruments/MI-000220.md) | 153 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B014.json).

Selection covers eight mechanisms from four manuscripts: finite phase substitution, spectral whitening at zero density, entropy cancellation under arbitrary coupling, fixed operator squares, sumset-controlled pair capacity, conditional two-point entropy gain, first-bit measure overlap and cross-prefix neighbor extraction. The selected source arguments were read. Four listed Comparator files were compared with the scope documents for families 144, 145 and 148; family 153 had no listed scope document. Primary comparisons include Green's dissociated exponential estimate, Taylor's spectral representation, Varju's fair-pair decomposition and entropy gain, and Garsia's entropy/singularity work. The records distinguish these established ingredients from source-specific combinations.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups. Checks include 77,700 exact monomial integrals, 120 spectral-fiber models with zeros and multiplicity, 27 dependent codebook models, 160 operator rectangles with three-wise independent parameters, 324 finite-law capacity inequalities, 16 observed-sum entropy models, 100 two-point entropy gains, 60 future mixtures, 24 finite-prefix entropy models and 35 bin-mass models with 77,137 word-pair distances. Negative controls distinguish finite from adaptive phase tests, flatness from cyclicity, orthogonality from dissociation, full spans from partial isometries, and finite truncations from limiting branch overlap. Only two of the bin-mass examples give a positive lower bound; the other cases still check the incidence and distance mechanism.

Run `python batches/B014/verification/check_instruments.py` from the repository root with NumPy and SciPy from the shared verification requirements. Integer and rational operations handle frequencies, prefix geometry and shift breakpoints; matrix operations, linear programs and entropy logarithms use floating point. The finite cancellation bound is often numerically loose.

The smooth simple-spectrum construction, multiple-mixing implication, uniform nonsaturation and global dimension formula, and arithmetic singularity classification were not independently certified. No Lean solution was built. Targeted comparisons do not establish historical priority.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
