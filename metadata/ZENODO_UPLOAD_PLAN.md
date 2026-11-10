# Zenodo upload plan — v0.1-review

This is a local publication checklist. A Zenodo draft with reserved DOI
10.5281/zenodo.24112798 exists; no public record exists until publication.

## Record type and scope

- Resource type: **Publication / Preprint**.
- Access: **Open**.
- Main licence: **CC BY 4.0** for the preprint and original numerical data.
- The source archive also contains original utility code under the MIT licence,
  as described in `LICENSE`.
- Version: **v0.1-review**.
- Review status: **candidate proof; no independent human review received**.

## Files to upload

### Core publication files

1. `DYN-Preprint-Volume-Deficit-3D-v0.1-review.pdf`
2. `dyn-validex-lattice-ball-volume-deficit-3d-v0.1-review-source.zip`

### Frozen numerical supplement

3. `DYN-Analyse_Asymptotique_3D_v0_1.zip`
4. `DYN-Cinf_3D_R192_R256_v0_1.zip`
5. `DYN-Doublement_3D_R512.zip`
6. `DYN-Extension_Statique_3D_R48_R64_v0_1.zip`
7. `DYN-Extension_Statique_3D_R96_R128_v0_1.zip`
8. `DYN-Modele_Statique_3D_v0_1.zip`
9. `SHA256SUMS-ZENODO.txt` (manifest of the preceding eight files)

The expected hashes of the six supplement archives are recorded in
`ZENODO_NUMERICAL_SUPPLEMENT_SHA256.txt`. The source-archive hash is generated
outside the repository in `dist/SOURCE_ARCHIVE_SHA256.txt`. The final upload
manifest is generated outside the repository by
`tools/generate_zenodo_upload_manifest.py`.

## Pre-publication gates

- [x] Public creator, project wording and ORCID confirmed by ROYER Patrick.
- [x] GitHub owner royerpatrick-ops and repository name confirmed.
- [x] Publication requested with the proposed CC BY 4.0 / MIT licence split.
- [x] DOI reserved and inserted into the frozen repository files.
- [x] `python tools/verify_release.py` succeeds after the final manifest build.
- [x] The eight upload files match their recorded SHA-256 hashes.
- [x] GitHub release URL added as a related identifier.
- [ ] Zenodo preview reviewed by the creator.
- [x] Explicit authorization received to perform the public deposits.
