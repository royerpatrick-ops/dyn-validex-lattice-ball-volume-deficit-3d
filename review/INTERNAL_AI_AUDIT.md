# Audit mathématique interne assisté par IA — analyse 3D

> **Nature de ce document.** Cet audit a été produit dans le même environnement
> d’intégration ChatGPT/Codex que la consolidation de la preuve. Le projet a
> également comporté des consultations plus ponctuelles de Claude AI, DeepSeek,
> Z.ai et Kimi. Aucun de ces systèmes ne constitue un relecteur humain. Cet
> audit n’est ni une expertise indépendante ni une revue par les pairs ; il est
> publié pour rendre les contrôles internes inspectables et orienter une
> relecture externe critique. ROYER Patrick — Projet Dynagénèse en assume la
> responsabilité humaine.

## Verdict exécutif

La chaîne proposée pour le déficit volumique de la boule est **mathématiquement refermable et ne présente plus de lacune bloquante** après insertion des lemmes consignés dans la note formelle jointe.

Le bon niveau de revendication est toutefois :

> preuve de travail auditée en interne, prête pour une relecture mathématique externe ; pas encore un résultat publié ou certifié par les pairs.

Le résultat soutenu par l’audit est

\[
R^{3/2}\delta_V(R,\xi)
\longrightarrow
C_V=3\,\mathbb E_{\mathrm{Haar}}H,
\qquad 0<C_V<\infty,
\]

pour toute translation fixe \(\xi\). L’audit ne certifie ni une valeur numérique précise de \(C_V\), ni un taux de convergence, ni l’analogue surfacique.

## Périmètre repris

Le dossier transmis a été traité comme un corpus de livraison : notes PDF, archives de calcul, figures et transcriptions ODT. Les six archives munies de manifestes ont été contrôlées auparavant sans anomalie d’intégrité. L’audit présent porte sur la dernière preuve candidate de la limite volumique, et non sur une reconstruction exhaustive de chaque calcul numérique historique.

Trois volets ont été contrôlés séparément :

1. réduction radiale et queue uniforme ;
2. équidistribution linéaire puis affine ;
3. localisation du fonctionnel de paraboloïde et passage aux espérances.

## Matrice de conclusions

| Élément | Verdict | Observation essentielle |
|---|---|---|
| Inclusion \(B_{R-\sqrt3}\subset Q_{R,\xi}\subset B_R\) | Valide | Uniforme en \(\xi\); garantit \(0\le h\le\sqrt3\). |
| Identité radiale du volume | Valide | Donne \(R^{3/2}\delta_V=3\mathbb EZ_R+O(R^{-1/2})\). |
| Échelle \(Z_R=\sqrt R\,h_R\) | Valide | C’est la seule normalisation cohérente avec le modèle parabolique. |
| Queue \(\Pr(Z_R>s)\le K/s^2\) | Valide après explicitation | Séparation stricte, ellipsoïde, platitude et comptage doivent être écrits avec leurs quantificateurs. |
| Équidistribution linéaire | Valide | Application du corollaire 5.9 de Marklof–Strömbergsson après dualité et permutation. |
| Équidistribution affine | Valide, mais non fournie par la citation seule | Nécessite le flot affine limite, Moore, Ratner et l’argument de crochet. |
| Identité avec le domaine local | Corrigée | L’identité exacte est \(Z_R=H_{P_R}(\Lambda_R)\), pas \(H_P(\Lambda_R)\). |
| Localisation de \(H\) | Valide après ajout d’un lemme | Trois témoins et une fenêtre compacte commune suffisent. |
| Continuité \(H_{P_R}\to H_P\) | Valide presque sûrement | Il faut exclure les réseaux rencontrant \(\partial P\), événement Haar-nul. |
| Passage convergence en loi → moyennes | Valide | La queue \(s^{-2}\) donne l’intégrabilité uniforme. |
| Finitude et positivité de \(C_V\) | Valide | \(H>0\) presque sûrement et \(H\in L^1\). |
| Valeur numérique de \(C_V\) | Non certifiée | Les ajustements à rayon fini restent indicatifs. |
| Déficit de surface | Hors preuve actuelle | Demande un fonctionnel et des contrôles supplémentaires. |

## Corrections indispensables apportées

### 1. Distinguer le domaine fini du domaine limite

Avec

\[
P_R=\{(y,z):2z\ge |y|^2+R^{-3/2}z^2\},
\qquad
P=\{(y,z):z\ge |y|^2/2\},
\]

la géométrie exacte donne

\[
\sqrt R\,h_{R,\xi}(u)=H_{P_R}(\Lambda_{R,\xi}).
\]

Le fonctionnel \(H_P\) n’intervient qu’après le lemme séquentiel

\[
R_n\to\infty,\quad
\Lambda_n\to\Lambda,\quad
\Lambda\cap\partial P=\varnothing
\Longrightarrow
H_{P_{R_n}}(\Lambda_n)\to H_P(\Lambda).
\]

Cette correction est matérielle : sans elle, une identité limite était présentée comme exacte à rayon fini.

### 2. Ne pas attribuer l’équidistribution affine au corollaire linéaire

Le corollaire 5.9 de Marklof–Strömbergsson établit l’équidistribution dans l’espace des réseaux **linéaires**. Il ne suffit pas, à lui seul, pour une translation arbitraire \(\xi\), notamment rationnelle ou nulle.

Le complément nécessaire est désormais explicité :

- les réseaux sont écrits en convention colonne dans les quotients \(G/\Gamma\), avec identification par inversion vers les quotients \(\Gamma\backslash G\) des sources ;
- la projection affine-linéaire est un fibré torique propre, donc les lois affines sont tendues ;
- les petites rotations d’angle \(aR^{-3/4}\) engendrent à la limite

  \[
  T_a(y_1,y_2,z)
  =(y_1+a,y_2,z+ay_1+a^2/2) ;
  \]

- toute limite est invariante sous ce flot unipotent ;
- Moore rend sa projection linéaire ergodique ;
- Ratner homogénéise les composantes affines ;
- un argument de rang force la projection de leur algèbre de Lie à être \(\mathfrak{sl}_3\) ;
- le crochet

  \[
  [(\operatorname{diag}(1,-2,1),w),(E_{31},e_1)]
  =(0,e_1-w_1e_3)\ne0
  \]

  force toutes les translations, donc toute l’algèbre \(\mathfrak{asl}_3\).

Cette partie est la plus profonde de la preuve. Elle est cohérente, mais mérite prioritairement une relecture par un spécialiste de dynamique homogène.

### 3. Formaliser la localisation

Pour chaque réseau affine plein, trois points strictement dans \(P\) peuvent être choisis de façon que leurs projections horizontales entourent l’origine. Ils donnent

\[
\phi(b)\le M-r|b|,
\qquad
\phi(b)=\min_{(y,z)\in\Lambda\cap P}(z-b\cdot y),
\]

donc seuls les \(|b|\le M/r\) comptent. Sur cet ensemble de pentes,

\[
z-b\cdot y\ge |y|^2/2-B|y|
\]

enferme tous les points actifs dans une fenêtre compacte. La continuité devient alors un problème fini.

### 4. Compléter la preuve de queue

La preuve initiale avait la bonne architecture. Les compléments requis sont :

- séparation **stricte** de \((R-d)u\) et de l’enveloppe ;
- définition explicite de l’ellipsoïde de demi-axes \(d/4\) et \(\sqrt{Rd}/4\) ;
- extraction d’un ellipsoïde homothétique dans le demi-ellipsoïde sans point ;
- convention de largeur et citation du théorème de platitude ;
- annonce d’un \(R_0\) absolu avant l’estimation des calottes ;
- comptage correct

  \[
  \sum_{0<|v|\le L}|v|^{-2}=O(1+L),
  \]

  puis utilisation de \(d<\sqrt3\).

Après ces ajouts,

\[
\Pr_u(\sqrt R\,h_{R,\xi}(u)>s)\le K/s^2
\]

est uniforme en \(\xi\), pour \(s\ge1\) et \(R\ge R_0\).

## Points qui restent ouverts

### Valeur de la constante

La preuve identifie

\[
C_V=3\mathbb E_{\mathrm{Haar}}H,
\]

mais ne calcule pas cette espérance. Dans le corpus numérique, le coefficient volumique normalisé vaut \(2{,}835535\) à \(R=512\), tandis qu’un ajustement prospectif de type \(C+A/\sqrt R\) suggère environ \(2{,}903\). Ces nombres sont compatibles avec une constante finie, mais ne constituent pas une certification de sa valeur asymptotique.

Une estimation défendable de \(C_V\) demanderait au minimum :

- une simulation directe du modèle limite Haar/paraboloïde ;
- un budget d’erreur statistique ;
- un contrôle séparé du biais de fenêtre et du biais de rayon fini ;
- idéalement, des bornes rigoureuses ou validées par intervalles.

### Vitesse de convergence

La preuve est qualitative. Aucun \(O(R^{-\alpha})\) n’est établi pour

\[
R^{3/2}\delta_V(R,\xi)-C_V.
\]

Les ajustements empiriques de type \(C+A/\sqrt R\) doivent rester présentés comme modèles numériques prospectifs.

### Surface

Le déficit d’aire ne se déduit pas formellement du déficit volumique. Il faut contrôler l’orientation et les pentes des facettes locales, donc un fonctionnel plus riche que la seule hauteur axiale \(H\). La constante surfacique numérique actuelle ne doit pas être promue au rang de théorème par analogie.

## Niveau de confiance

- **Élevé** : réduction radiale, changement d’échelle, queue uniforme, localisation compacte, troncature.
- **Bon mais à faire relire par un spécialiste** : rigidité affine via Moore–Ratner et argument de rang.
- **Exploratoire** : valeur numérique de la constante, loi des corrections à rayon fini, extension à la surface.

L’audit est interne au même environnement de travail, bien que les trois volets aient été examinés séparément. Il ne remplace donc pas une expertise externe indépendante.

## Document de référence produit

La démonstration consolidée se trouve dans `FORMALISATION_THEOREME_VOLUME_3D.md`. Cette version doit désormais servir de base canonique pour toute révision, traduction en LaTeX ou soumission à un relecteur.

## Sources primaires contrôlées

- J. Marklof et A. Strömbergsson, Annals of Mathematics 172 (2010) : [article](https://annals.math.princeton.edu/2010/172-3/p12).
- M. Ratner, Annals of Mathematics 134 (1991) : [article](https://annals.math.princeton.edu/1991/134-3/p02).
- C. C. Moore, American Journal of Mathematics 88 (1966) : [DOI](https://doi.org/10.2307/2373052).
- R. Kannan et L. Lovász, Annals of Mathematics 128 (1988) : [article](https://annals.math.princeton.edu/1988/128-3/p06).
- W. Banaszczyk, A. Litvak, A. Pajor et S. Szarek, Mathematics of Operations Research 24 (1999) : [DOI](https://doi.org/10.1287/moor.24.3.728).
