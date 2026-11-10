# Volume deficit of translated lattice hulls in three dimensions

> **Status: working manuscript, not peer-reviewed.**  
> This repository is published to request an independent, critical human
> mathematical review. No claim here should yet be treated as an established
> theorem.

[Version française](README.fr.md) · [How to review](REVIEWING.md) ·
[Human-review request](review/REQUEST_FOR_HUMAN_REVIEW.md) ·
[Internal AI-assisted audit](review/INTERNAL_AI_AUDIT.md)

**Human author and depositor:** ROYER Patrick — Projet Dynagénèse  
**ORCID:** [0009-0009-4149-2834](https://orcid.org/0009-0009-4149-2834)

## Candidate main result

Let

\[
Q_{R,\xi}=\operatorname{conv}\bigl((\mathbb Z^3+\xi)\cap B_R\bigr)
\]

and let \(\delta_V(R,\xi)\) be its relative volume deficit in the
three-dimensional Euclidean ball \(B_R\). The working manuscript claims that,
for every fixed \(\xi\in\mathbb R^3\),

\[
\lim_{R\to\infty}R^{3/2}\delta_V(R,\xi)
=C_V
=3\int_{X_{\mathrm{aff}}}H(\Lambda)\,d\mu_{\mathrm{aff}}(\Lambda),
\qquad 0<C_V<\infty,
\]

where \(C_V\) is independent of \(\xi\).

The complete candidate proof is in
[`FORMALISATION_THEOREME_VOLUME_3D.md`](FORMALISATION_THEOREME_VOLUME_3D.md).
The [canonical PDF](output/pdf/DYN-Preprint-Volume-Deficit-3D-v0.1-review.pdf)
will also be attached to the GitHub release and Zenodo record.

## Priority review questions

Partial reviews are welcome. The highest-priority points are:

1. **Affine equidistribution.** Does the passage from linear spherical
   equidistribution to affine Haar measure follow rigorously from the limiting
   unipotent flow, Moore ergodicity, Ratner measure classification, the rank
   argument and the Lie-algebra bracket?
2. **Uniform tail estimate.** Is
   \(\Pr(\sqrt R\,h_{R,\xi}>s)\le K s^{-2}\) truly uniform in \(R\) and
   \(\xi\), including the separation, flatness and spherical-cap counting
   steps?
3. **Parabolic localization.** Are the compact localization lemma, the
   variable-domain convergence \(H_{P_R}\to H_P\), and the Haar-null boundary
   argument complete?
4. **Passage to expectations.** Do weak convergence and uniform integrability
   justify the limiting expectation and the positivity and finiteness of
   \(C_V\)?

Corrections, counterexamples, missing hypotheses and alternative proofs are
explicitly welcome. Please use the **Mathematical review report** issue form
and identify the release/tag, document, section and equation reviewed.

## Current limitations

- No independent human mathematical review has yet been received.
- The work does not compute \(C_V\) explicitly.
- Finite-radius numerical estimates are exploratory and are not part of the
  candidate theorem.
- No quantitative convergence rate is proved.
- No analogous surface-area asymptotic is proved.
- Historical numerical archives passed integrity checks, but no independent
  party has reproduced every historical run.

## Numerical supplement

Six frozen numerical archives (about 181 MiB in total) are intentionally kept
out of Git history. They are planned as a Zenodo supplement. Their checksums
and reproduction status are recorded in the release materials. This keeps the
GitHub repository lightweight while Zenodo preserves the complete frozen
artifacts.

The precise integrity and recomputation status is documented in
[`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

## AI-assistance disclosure

The work used sustained, integrated assistance from ChatGPT and Codex for
mathematical exploration, drafting, verification, consolidation, programming
and internal critique. Claude AI, DeepSeek, Z.ai and Kimi were consulted more
occasionally for exploration or cross-checking. These AI-assisted checks do
**not** constitute independent human review or peer review. No AI system is
presented as an author. ROYER Patrick — Projet Dynagénèse remains solely
responsible for the public claims and deposited files. See
[AI_ASSISTANCE.md](AI_ASSISTANCE.md).

## Citation and licence

Citation metadata are in [`CITATION.cff`](CITATION.cff). Documents and original
data are offered under CC BY 4.0; original code is offered under the MIT
License. See [`LICENSE`](LICENSE) for scope. Versioned Zenodo DOI:
[10.5281/zenodo.24112798](https://doi.org/10.5281/zenodo.24112798).
