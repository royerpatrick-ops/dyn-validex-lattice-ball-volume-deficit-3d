# Déficit volumique des enveloppes de réseaux translatés en dimension trois

> **Statut : manuscrit de travail non relu par les pairs.**  
> Ce dépôt est préparé afin de solliciter une relecture mathématique humaine,
> indépendante et critique. Le résultat principal ne doit pas encore être cité
> comme un théorème établi.

[English README](README.md) · [Guide de relecture](REVIEWING.md) ·
[Demande de relecture](review/REQUEST_FOR_HUMAN_REVIEW.md) ·
[Audit interne assisté par IA](review/INTERNAL_AI_AUDIT.md)

**Auteur humain et déposant :** ROYER Patrick — Projet Dynagénèse  
**ORCID :** [0009-0009-4149-2834](https://orcid.org/0009-0009-4149-2834)

## Proposition principale soumise à vérification

Pour

\[
Q_{R,\xi}=\operatorname{conv}\bigl((\mathbb Z^3+\xi)\cap B_R\bigr),
\]

la preuve candidate affirme que, pour toute translation fixe
\(\xi\in\mathbb R^3\),

\[
\lim_{R\to\infty}R^{3/2}\delta_V(R,\xi)
=C_V
=3\int H\,d\mu_{\mathrm{aff}},
\qquad 0<C_V<\infty,
\]

avec une constante indépendante de \(\xi\).

La preuve complète se trouve dans
[`FORMALISATION_THEOREME_VOLUME_3D.md`](FORMALISATION_THEOREME_VOLUME_3D.md).
Le [PDF canonique](output/pdf/DYN-Preprint-Volume-Deficit-3D-v0.1-review.pdf)
est inclus dans le dépôt et sera joint à la release GitHub et à Zenodo.

## Relectures prioritaires

Les relectures partielles sont bienvenues, en particulier sur :

1. l’équidistribution affine et l’argument Moore-Ratner ;
2. la queue uniforme issue de la platitude ;
3. la localisation parabolique et la convergence \(H_{P_R}\to H_P\) ;
4. le passage de la convergence en loi aux espérances.

Les objections, contre-exemples, hypothèses manquantes et preuves alternatives
sont aussi utiles que les confirmations. Chaque rapport doit identifier la
version, le document, la section et l’équation examinés.

## Limites déclarées

- aucune relecture mathématique humaine indépendante n’a encore été reçue ;
- la constante \(C_V\) n’est pas calculée explicitement ;
- les estimations numériques à rayon fini sont exploratoires ;
- aucun taux de convergence n’est établi ;
- l’analogue pour le déficit de surface n’est pas démontré ;
- les calculs historiques n’ont pas encore été reproduits par une équipe
  indépendante.

## Transparence sur l’assistance par IA

Le travail a reposé sur une assistance substantielle et intégrée de ChatGPT et
Codex pour l’exploration mathématique, la rédaction, les vérifications, la
consolidation, la programmation et la critique interne. Claude AI, DeepSeek,
Z.ai et Kimi ont été consultés plus ponctuellement à des fins d’exploration ou
de contre-vérification. Ces contrôles assistés par IA ne constituent ni une
expertise humaine indépendante ni une revue par les pairs. Aucun système d’IA
n’est présenté comme auteur. ROYER Patrick — Projet Dynagénèse assume seul la
responsabilité des affirmations et des fichiers déposés. Voir
[AI_ASSISTANCE.md](AI_ASSISTANCE.md).

## Archives numériques, citation et licences

Les six archives numériques gelées, d’environ 181 Mio, sont destinées au
supplément Zenodo plutôt qu’à l’historique Git. Les métadonnées de citation sont
dans [`CITATION.cff`](CITATION.cff). Les documents et données originales sont
placés sous CC BY 4.0, et le code original sous licence MIT. DOI Zenodo de la
version : [10.5281/zenodo.24112798](https://doi.org/10.5281/zenodo.24112798).

Le statut exact des contrôles d’intégrité et de reproductibilité est détaillé
dans [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).
