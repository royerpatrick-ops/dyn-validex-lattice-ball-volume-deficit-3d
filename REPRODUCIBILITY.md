# Reproducibility status

## Scope

The candidate theorem is qualitative. Its proof does not depend on accepting a
finite-radius numerical fit. Historical calculations are supplied as a separate
frozen supplement so that their integrity and provenance can be checked without
conflating them with the proof.

## What has been checked

- Six numerical archives contain 868 files and about 180.57 MiB in total.
- Each archive includes code, plans, seeds or translation identifiers, saved
  data, outputs and checks.
- All six internal SHA-256 manifests were recomputed successfully: no file was
  missing, unlisted or divergent.
- The recorded numerical chain covers 640 hull computations and radii from 16
  to 512.
- The saved checks explicitly state that they were performed in the same
  AI-assisted collaborative environment and are not an external audit. The
  roles of the systems used are documented in [AI_ASSISTANCE.md](AI_ASSISTANCE.md).

## Reproduction strength

- **Strong:** file integrity and reanalysis of saved outputs.
- **Moderate:** complete recomputation from source.
- **Not established:** independent reproduction by another person or team.

The recorded environment was Linux with Python 3.12.14. Cross-platform
compatibility is described but has not been demonstrated by continuous
integration. Some dependency files use lower bounds rather than exact pins, and
the historical batches do not yet have one root command that recomputes the full
chain.

## Publication layout

The GitHub repository intentionally remains lightweight. The six unchanged ZIP
archives are planned for Zenodo and are identified by
`metadata/ZENODO_NUMERICAL_SUPPLEMENT_SHA256.txt`. Loose historical PDFs,
PNGs, ODT development documents and LibreOffice lock files are excluded because
they are duplicated, non-canonical or may contain irrelevant office metadata.

## Claims not supported by the numerical supplement

The supplement does not certify an explicit value of \(C_V\), a correction of
the form \(A/\sqrt R\), a convergence rate, or a surface-area asymptotic. The
panel of 16 translations used in several batches is fixed rather than an
independent random sample.
