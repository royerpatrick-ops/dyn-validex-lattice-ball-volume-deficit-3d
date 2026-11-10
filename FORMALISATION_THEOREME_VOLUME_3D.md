# Déficit volumique de l’enveloppe convexe d’un réseau translaté dans une boule

**Auteur humain :** ROYER Patrick — Projet Dynagénèse  
**ORCID :** [0009-0009-4149-2834](https://orcid.org/0009-0009-4149-2834)

## Statut et portée

Cette note formalise la preuve candidate apparue dans les échanges de développement 3D. Après reprise des calculs et trois audits internes assistés par IA — queue uniforme, dynamique homogène, localisation parabolique — aucun obstacle mathématique bloquant n’a été trouvé dans cet environnement de travail. Cette appréciation n’est ni indépendante ni équivalente à une revue par les pairs. La preuve ci-dessous est soumise à une relecture mathématique humaine externe avant toute revendication comme théorème établi.

Le résultat porte uniquement sur le déficit **volumique** pour une boule et une translation fixe du réseau. Il ne donne ni valeur fermée de la constante limite, ni taux de convergence, ni analogue automatique pour l’aire de surface.

## 1. Énoncé

Pour \(R>0\), \(\xi\in\mathbb R^3\), posons

\[
L_\xi=\mathbb Z^3+\xi,
\qquad
Q_{R,\xi}=\operatorname{conv}(L_\xi\cap B_R),
\]

où \(B_R\) est la boule euclidienne fermée de rayon \(R\), centrée en l’origine. Le déficit volumique relatif est

\[
\delta_V(R,\xi)
=\frac{\operatorname{Vol}(B_R)-\operatorname{Vol}(Q_{R,\xi})}
{\operatorname{Vol}(B_R)}.
\]

Soit

\[
X_{\mathrm{aff}}
=\operatorname{ASL}_3(\mathbb R)/
  \operatorname{ASL}_3(\mathbb Z)
\]

l’espace des réseaux affines unimodulaires en convention colonne, muni de sa probabilité de Haar \(\mu_{\mathrm{aff}}\). L’identification par inversion \(g\Gamma\mapsto\Gamma g^{-1}\) le relie au quotient à gauche employé dans les sources et préserve Haar. Écrivons un point de \(\mathbb R^3\) sous la forme \((y,z)\in\mathbb R^2\times\mathbb R\) et définissons le paraboloïde

\[
P=\{(y,z):z\ge \tfrac12|y|^2\}.
\]

Pour un réseau affine plein \(\Lambda\), posons

\[
H(\Lambda)
=\inf\{z:(0,z)\in\operatorname{conv}(\Lambda\cap P)\}.
\]

La quantité est finie pour tout \(\Lambda\), et elle admet la formule duale

\[
H(\Lambda)
=\max_{b\in\mathbb R^2}
  \min_{(y,z)\in\Lambda\cap P}(z-b\cdot y).
\tag{1}
\]

**Théorème.** Il existe une constante universelle

\[
C_V=3\int_{X_{\mathrm{aff}}}H(\Lambda)\,d\mu_{\mathrm{aff}}(\Lambda),
\qquad 0<C_V<\infty,
\tag{2}
\]

telle que, pour toute translation fixe \(\xi\in\mathbb R^3\),

\[
\boxed{
\lim_{R\to\infty}R^{3/2}\delta_V(R,\xi)=C_V.}
\tag{3}
\]

La constante ne dépend donc pas de \(\xi\), y compris lorsque \(\xi\) est rationnelle ou nulle.

## 2. Réduction radiale

Chaque point \(x\in\mathbb R^3\) appartient à une cellule unitaire du pavage associé à \(L_\xi\), dont les huit sommets sont à distance au plus \(\sqrt3\) du point \(x\). Si \(|x|\le R-\sqrt3\), chacun de ces sommets \(p\) vérifie \(|p|\le|x|+|p-x|\le R\), et \(x\) est leur combinaison convexe. Par conséquent,

\[
B_{R-\sqrt3}\subset Q_{R,\xi}\subset B_R
\qquad (R>\sqrt3),
\tag{4}
\]

uniformément en \(\xi\). En particulier, \(0\) est intérieur à \(Q_{R,\xi}\).

Pour \(u\in S^2\), définissons la fonction radiale

\[
\rho_{R,\xi}(u)
=\max\{t\ge0:tu\in Q_{R,\xi}\},
\]

de sorte que \(R-\sqrt3\le\rho_{R,\xi}(u)\le R\), et posons

\[
h_{R,\xi}(u)=R-\rho_{R,\xi}(u).
\]

Alors \(0\le h_{R,\xi}(u)\le\sqrt3\). Si \(\sigma\) désigne la probabilité uniforme sur \(S^2\), la formule polaire donne

\[
\delta_V(R,\xi)
=\mathbb E_\sigma\!\left[1-\left(1-\frac{h_{R,\xi}}R\right)^3\right].
\]

Avec

\[
Z_{R,\xi}(u)=\sqrt R\,h_{R,\xi}(u),
\]

on obtient l’identité

\[
R^{3/2}\delta_V(R,\xi)
=3\,\mathbb E_\sigma[Z_{R,\xi}]
-3R^{-1/2}\mathbb E_\sigma[h_{R,\xi}^2]
+R^{-3/2}\mathbb E_\sigma[h_{R,\xi}^3]
=3\,\mathbb E_\sigma[Z_{R,\xi}]+O(R^{-1/2}),
\tag{5}
\]

où le reste est uniforme en \(\xi\), puisque \(0\le h_{R,\xi}\le\sqrt3\). Il suffit donc d’identifier la limite de \(\mathbb E Z_{R,\xi}\).

## 3. Modèle local parabolique exact

Prenons \(k\) selon Haar sur \(SO(3)\) et posons

\[
u=-k^{-1}e_3,
\qquad
D_R=\operatorname{diag}(R^{-1/4},R^{-1/4},R^{1/2}),
\]

\[
\Lambda_{R,\xi}(k)
=D_R\bigl(k(L_\xi)+Re_3\bigr).
\tag{6}
\]

La direction \(u\) est uniforme. Le roulis tangent supplémentaire contenu dans \(k\) ne change pas la profondeur radiale.

L’image de la boule par ce changement de coordonnées est

\[
P_R
=\{(y,z):2z\ge |y|^2+R^{-3/2}z^2\}.
\tag{7}
\]

On a \(P_R\subset P\), et tout compact de \(\operatorname{int}P\) est inclus dans \(P_R\) pour \(R\) assez grand.

Pour un domaine \(D\), lorsque l’axe vertical rencontre \(\operatorname{conv}(\Lambda\cap D)\), notons

\[
H_D(\Lambda)
=\inf\{z:(0,z)\in\operatorname{conv}(\Lambda\cap D)\}.
\]

On peut poser \(H_D=+\infty\) lorsque cette intersection est vide. Dans le cas de \(P_R\), l’inclusion (4) garantit qu’elle est non vide dès que \(R>\sqrt3\).

Le changement d’échelle donne l’identité exacte

\[
\boxed{
Z_{R,\xi}(u)=H_{P_R}(\Lambda_{R,\xi}(k))\qquad(R>\sqrt3).}
\tag{8}
\]

Il est important de ne pas remplacer \(P_R\) par \(P\) dans cette identité : \(H_P\) est seulement le fonctionnel limite.

## 4. Équidistribution du réseau affine local

### Proposition 1

Pour toute translation fixe \(\xi\), la loi de \(\Lambda_{R,\xi}(k)\), avec \(k\) Haar sur \(SO(3)\), converge vers \(\mu_{\mathrm{aff}}\) lorsque \(R\to\infty\).

### Preuve

Projetons d’abord sur l’espace linéaire

\[
X_{\mathrm{lin}}
=\operatorname{SL}_3(\mathbb R)/\operatorname{SL}_3(\mathbb Z).
\]

La projection de \(\Lambda_{R,\xi}(k)\) est \(L_R=D_Rk\mathbb Z^3\). Son réseau dual est \(L_R^*=D_R^{-1}k\mathbb Z^3\). En convention ligne, choisissons une permutation orthogonale \(P\) envoyant l’axe distingué sur le premier axe. Avec \(t=\frac14\log R\), posons

\[
\Phi_t=\operatorname{diag}(e^{-2t},e^t,e^t).
\]

on a explicitement

\[
(L_R^*)^T
=\mathbb Z^3k^TD_R^{-1}
=\mathbb Z^3(k^TP)
  \Phi_tP^{-1}.
\]

Le corollaire 5.9 de Marklof–Strömbergsson donne alors l’équidistribution vers Haar sur \(X_{\mathrm{lin}}\), après l’identification par inversion entre leurs quotients-lignes à gauche et les quotients-colonnes ci-dessus. Le facteur fixe \(P^{-1}\) s’absorbe dans la fonction test. Pour passer de leurs cartes sphériques à l’intégrale sur \(SO(3)\), on désintègre Haar au-dessus de \(S^2\); sur une partition finie en cartes, les sections locales et les mesures obtenues satisfont l’hypothèse de jacobien non singulier presque partout, tandis que la fibre \(SO(2)\) commute avec la diagonale. La convergence dominée recolle les cartes. Dualité, transposition et permutation fixe préservent Haar.

Cette citation ne fournit que l’équidistribution **linéaire**. L’extension affine se démontre comme suit.

La projection

\[
\pi:X_{\mathrm{aff}}\longrightarrow X_{\mathrm{lin}}
\]

est un fibré torique propre. L’équidistribution linéaire entraîne donc la tension des lois affines. Considérons une limite faible sous-séquentielle \(\nu\).

Pour \(a\in\mathbb R\), posons \(\theta=aR^{-3/4}\) et

\[
q_\theta=
\begin{pmatrix}
\cos\theta&0&-\sin\theta\\
0&1&0\\
\sin\theta&0&\cos\theta
\end{pmatrix}.
\]

La loi de \(k\) est invariante par \(k\mapsto q_\theta k\). Si

\[
g_R(x)=D_R(x+Re_3),
\]

la loi de \(\Lambda_{R,\xi}\) est donc invariante sous

\[
S_{R,a}=g_Rq_\theta g_R^{-1}.
\]

Un calcul direct donne, uniformément sur les compacts,

\[
S_{R,a}\longrightarrow T_a,
\qquad
T_a(y_1,y_2,z)
=(y_1+a,y_2,z+ay_1+\tfrac12a^2).
\tag{9}
\]

La tension et l’invariance exacte sous \(S_{R,a}\) impliquent que \(\nu\) est invariante sous le flot unipotent \(U=\{T_a:a\in\mathbb R\}\). En effet, pour \(f\in C_c\), la convergence de \(S_{R,a}\) vers \(T_a\), uniforme sur les compacts, et la tension permettent de remplacer \(f\circ S_{R,a}\) par \(f\circ T_a\) dans l’intégrale avant de passer à la limite. La projection de \(\nu\) est Haar sur \(X_{\mathrm{lin}}\).

Décomposons \(\nu\) en composantes \(U\)-ergodiques. La projection de chaque composante est ergodique pour le flot linéaire

\[
\bar U=\{\exp(aE_{31})\}.
\]

Le groupe \(\operatorname{SL}_3(\mathbb R)\) est connexe et simple à centre fini, \(\operatorname{SL}_3(\mathbb Z)\) est un réseau, et \(\bar U\) est fermé et non compact. Le théorème d’ergodicité de Moore affirme donc que Haar linéaire est \(\bar U\)-ergodique. Par unicité de la décomposition ergodique, presque toute composante se projette exactement sur Haar linéaire.

Le groupe \(\operatorname{ASL}_3(\mathbb Z)\) est un réseau dans \(\operatorname{ASL}_3(\mathbb R)\), ses fibres au-dessus de l’espace linéaire étant des tores compacts. Dans l’immersion affine dans \(\operatorname{SL}_4\),

\[
T_a=\exp(aN),
\qquad
N=
\begin{pmatrix}E_{31}&e_1\\0&0\end{pmatrix},
\qquad N^3=0.
\]

Ainsi \(U\) est Ad-unipotent et le théorème de classification de Ratner s’applique. Il rend presque toute composante homogène sur une orbite \(Hx\subset X_{\mathrm{aff}}\), où l’on peut prendre \(H\) connexe et contenant \(U\). Si la projection de l’algèbre de Lie \(\mathfrak h\) vers \(\mathfrak{sl}_3\) avait une dimension strictement inférieure à huit, la restriction lisse de \(\pi\) à \(Hx\), couverte par un nombre dénombrable de cartes, aurait partout un rang inférieur à huit. La formule de l’aire, ou le théorème de Sard carte par carte, rendrait son image Haar-négligeable, même si elle était dense. Cela contredirait le fait que la mesure projetée est Haar. Ainsi

\[
p(\mathfrak h)=\mathfrak{sl}_3.
\tag{10}
\]

Posons

\[
V=\{v\in\mathbb R^3:(0,v)\in\mathfrak h\}.
\]

Si \(v\in V\) et \(X\in\mathfrak{sl}_3\), choisissons un relèvement \((X,w_X)\in\mathfrak h\). Alors

\[
[(X,w_X),(0,v)]=(0,Xv),
\]

donc, par (10), \(V\) est invariant sous la représentation standard de \(\mathfrak{sl}_3\). Ainsi \(V=\{0\}\) ou \(V=\mathbb R^3\). Le générateur de \(U\) est \((E_{31},e_1)\). Avec

\[
D=\operatorname{diag}(1,-2,1),
\]

prenons un relèvement \((D,w)\in\mathfrak h\). Pour la convention

\[
[(X,u),(Y,v)]=([X,Y],Xv-Yu),
\]

on a

\[
[(D,w),(E_{31},e_1)]
=(0,e_1-w_1e_3)\ne0.
\tag{11}
\]

Ainsi \(V\ne0\), puis \(V=\mathbb R^3\). Pour tout \((X,w)\in\mathfrak h\), on peut alors soustraire \((0,w)\in\mathfrak h\), ce qui donne \((X,0)\in\mathfrak h\). Avec (10), cela entraîne

\[
\mathfrak h=\mathfrak{asl}_3.
\]

Comme \(\operatorname{ASL}_3(\mathbb R)\) est connexe, on a \(H=\operatorname{ASL}_3(\mathbb R)\). Presque toute composante est donc Haar affine, puis \(\nu=\mu_{\mathrm{aff}}\). Toute limite sous-séquentielle étant la même, la proposition est démontrée. ∎

## 5. Localisation et continuité du fonctionnel

### Lemme 2

Si \(R_n\to\infty\), \(\Lambda_n\to\Lambda\) dans \(X_{\mathrm{aff}}\), et

\[
\Lambda\cap\partial P=\varnothing,
\]

alors

\[
H_{P_{R_n}}(\Lambda_n)\longrightarrow H_P(\Lambda).
\tag{12}
\]

### Preuve

Tout réseau affine plein possède un rayon de recouvrement fini \(c\). Choisissons trois cibles dont les projections horizontales, de norme \(A\), forment un grand triangle autour de l’origine et sont séparées de plus de \(2c\). Prenons leur hauteur commune \(Z\) telle que

\[
Z-c>\tfrac12(A+c)^2.
\]

Les points de \(\Lambda\) situés à distance au plus \(c\) de ces cibles sont distincts, appartiennent strictement à \(P\), et leurs projections entourent encore l’origine si \(A\) est assez grand. On obtient ainsi trois points \((y_i,z_i)\in\Lambda\cap\operatorname{int}P\) et des constantes \(r,M>0\) tels que

\[
B_r(0)\subset\operatorname{conv}(y_1,y_2,y_3),
\qquad z_i\le M.
\tag{13}
\]

Pour

\[
\phi_\Lambda(b)
=\min_{(y,z)\in\Lambda\cap P}(z-b\cdot y),
\]

les témoins (13) donnent

\[
\phi_\Lambda(b)\le M-r|b|.
\]

Comme \(\phi_\Lambda(0)\ge0\), seules les pentes \(|b|\le B=M/r\) peuvent maximiser \(\phi_\Lambda\). Pour ces pentes et pour \((y,z)\in P\),

\[
z-b\cdot y\ge\tfrac12|y|^2-B|y|.
\]

Choisissons \(Y,Z_0\) tels que

\[
\tfrac12Y^2-BY>M,
\qquad
Z_0-BY>M.
\]

Les points pouvant réaliser le minimum sont donc contenus dans la même fenêtre compacte

\[
W=\{|y|\le Y,\ 0\le z\le Z_0\}.
\tag{14}
\]

Fixons \(0<r'<r\) et \(M'>M\). En choisissant des représentants compatibles de \(\Lambda_n\to\Lambda\), les trois témoins persistent pour \(\Lambda_n\), appartiennent à \(P_{R_n}\) pour \(n\) assez grand, et satisfont les versions uniformes de (13) avec \(r',M'\). Les mêmes bornes localisent tous les fonctionnels dans une fenêtre commune. On choisit ses paramètres \(Y,Z_0\) avec une petite marge, de sorte que \(\partial W\cap\Lambda=\varnothing\). Dans cette fenêtre, il n’y a qu’un nombre fini de points et ceux de \(\Lambda_n\) leur correspondent bijectivement pour \(n\) assez grand.

Si un point limite vérifie \(2z-|y|^2>0\), alors ses correspondants satisfont finalement

\[
2z_n-|y_n|^2>R_n^{-3/2}z_n^2
\]

et appartiennent à \(P_{R_n}\). S’il vérifie \(2z-|y|^2<0\), ses correspondants restent hors de \(P_{R_n}\), puisque \(P_{R_n}\subset P\). L’hypothèse \(\Lambda\cap\partial P=\varnothing\) couvre tous les points de la fenêtre. Les configurations finies et les fonctions affines correspondantes convergent donc uniformément sur la boule de pentes commune. Leurs maxima convergent, ce qui prouve (12).

Pour compléter la dualité (1), la localisation réduit \(\phi_\Lambda\) au minimum d’un nombre fini de fonctions affines sur la boule compacte \(|b|\le B\); son maximum est donc atteint en un point \(b_*\). À ce maximum, l’origine appartient à l’enveloppe convexe des vecteurs \(-y_i\) actifs. Il existe ainsi des poids \(t_i\ge0\), de somme un, tels que \(\sum_i t_i y_i=0\). Pour chaque point actif,

\[
z_i-b_*\cdot y_i=\phi_\Lambda(b_*),
\]

d’où \(\sum_i t_i z_i=\phi_\Lambda(b_*)\). Le point \((0,\phi_\Lambda(b_*))\) appartient donc à \(\operatorname{conv}(\Lambda\cap P)\). Réciproquement, toute combinaison convexe de projection horizontale nulle a une hauteur au moins \(\phi_\Lambda(b)\), pour tout \(b\). Les deux inégalités donnent (1). ∎

Sous Haar affine,

\[
\mu_{\mathrm{aff}}\{\Lambda:\Lambda\cap\partial P\ne\varnothing\}=0,
\tag{15}
\]

car \(\partial P\) a mesure de Lebesgue tridimensionnelle nulle; on applique la formule affine de Siegel à une exhaustion bornée.

Ce fait est aussi contenu dans le mécanisme du lemme 6.2(vi) de Marklof–Strömbergsson.

Les propositions 1, (8), (12) et (15), puis la version séquentielle du théorème de l’application continue pour les fonctionnels variables \(H_{P_R}\), donnent donc

\[
Z_{R,\xi}\ \Longrightarrow\ H(\Lambda_{\mathrm{Haar}}).
\tag{16}
\]

## 6. Queue uniforme

### Lemme 3

Il existe des constantes absolues \(K,R_0\) telles que, pour tout \(R\ge R_0\), tout \(\xi\in\mathbb R^3\) et tout \(s\ge1\),

\[
\mathbb P_\sigma(Z_{R,\xi}>s)\le\frac K{s^2}.
\tag{17}
\]

### Preuve

Posons \(d=s/\sqrt R\). Si \(d\ge\sqrt3\), l’événement est vide par (4). Supposons donc \(d<\sqrt3\). Si \(h_{R,\xi}(u)>d\), le point \(x=(R-d)u\) est extérieur au compact convexe \(Q_{R,\xi}\). Il existe un vecteur unitaire \(n\) tel que

\[
n\cdot x>\sup_{q\in Q_{R,\xi}}n\cdot q.
\]

Le demi-espace fermé \(\{y:n\cdot(y-x)\ge0\}\), plan frontière compris, ne contient donc aucun point de \(L_\xi\cap B_R\).

Considérons l’ellipsoïde

\[
E=\left\{x+tu+w:
w\perp u,\
\left(\frac{t}{d/4}\right)^2
+\left(\frac{|w|}{\sqrt{Rd}/4}\right)^2\le1
\right\}.
\]

Pour \(R\ge3\), tout point de \(E\) vérifie

\[
|x+tu+w|^2
\le(R-3d/4)^2+Rd/16
=R^2-\frac{23}{16}Rd+\frac9{16}d^2
\le R^2.
\]

Ainsi \(E\subset B_R\). Le plan séparateur passe par le centre de \(E\). Après l’application affine envoyant \(E\) sur la boule unité, son demi-ellipsoïde extérieur devient une demi-boule centrale; celle-ci contient une boule translatée de rayon \(1/4\). L’image inverse est donc un ellipsoïde \(E'\), translaté et homothétique de \(E\) par un facteur \(1/4\), sans point de \(L_\xi\). Ses demi-axes sont

\[
a=d/16,
\qquad b=\sqrt{Rd}/16.
\]

Translater \(E'\) par \(-\xi\) le rend sans point de \(\mathbb Z^3\), sans changer ses largeurs. Notons \(w_v(K)=\max_{p\in K}v\cdot p-\min_{p\in K}v\cdot p\). Si \(F_3\) est une constante de platitude en dimension trois, il existe \(v\in\mathbb Z^3\setminus\{0\}\) tel que

\[
w_v(E')
=\frac18\sqrt{d^2(v\cdot u)^2
+Rd\,|\operatorname{proj}_{u^\perp}v|^2}
\le F_3.
\]

Par conséquent,

\[
|v\cdot u|\le\frac{8F_3}{d},
\qquad
|\operatorname{proj}_{u^\perp}v|
\le\frac{8F_3}{\sqrt{Rd}},
\qquad
|v|\le\frac{8\sqrt2F_3}{d},
\tag{18}
\]

où la dernière borne utilise \(d\le R\), vrai ici pour \(R\ge3\).

Pour un \(v\) fixé, la seconde inégalité impose

\[
\sin\angle(u,\pm v)
\le\frac{8F_3}{|v|\sqrt{Rd}}.
\]

Comme \(s\ge1\), on a \(Rd=s\sqrt R\ge\sqrt R\). En choisissant une fois pour toutes \(R_0\) assez grand en fonction de \(F_3\), le membre de droite est au plus \(1/2\) pour tout \(v\ne0\). La mesure sphérique normalisée des deux calottes correspondantes est alors au plus

\[
\frac C{Rd\,|v|^2},
\]

avec \(C\) absolue. Une union sur les vecteurs satisfaisant la dernière borne de (18), puis le comptage par coquilles

\[
\sum_{0<|v|\le L}|v|^{-2}=O(1+L),
\]

donnent

\[
\mathbb P(h_{R,\xi}>d)
\le\frac C{Rd}\left(1+\frac{8\sqrt2F_3}{d}\right)
\le\frac K{Rd^2}
=\frac K{s^2}.
\]

Dans la seconde inégalité, on utilise \(d<\sqrt3\). Les constantes \(K,R_0\) sont indépendantes de \(R,s,\xi\). Cela prouve (17). ∎

## 7. Passage aux espérances et conclusion

La borne (17) entraîne, pour \(T\ge1\),

\[
\sup_{R\ge R_0,\xi}
\mathbb E[(Z_{R,\xi}-T)_+]
\le\int_T^\infty\frac K{s^2}\,ds
=\frac KT.
\tag{19}
\]

En particulier,

\[
\sup_{R\ge R_0,\xi}
\mathbb E\!\left[
Z_{R,\xi}\mathbf1_{\{Z_{R,\xi}>2T\}}
\right]
\le\frac{2K}{T},
\]

donc la famille est uniformément intégrable. De plus, (16), (17) et le théorème de Portmanteau donnent

\[
\mathbb P(H>s)\le\frac K{s^2},
\qquad
\mathbb E[(H-T)_+]\le\frac KT.
\]

La convergence des espérances se voit alors directement par

\[
\left|\mathbb EZ_{R,\xi}-\mathbb EH\right|
\le
\left|\mathbb E(Z_{R,\xi}\wedge T)-\mathbb E(H\wedge T)\right|
+\frac{2K}{T}.
\]

Le premier terme tend vers zéro pour \(T\) fixé par (16), puis \(T\to\infty\). On obtient

\[
\mathbb E Z_{R,\xi}\longrightarrow
\mathbb E_{\mu_{\mathrm{aff}}}H,
\qquad
\mathbb E_{\mu_{\mathrm{aff}}}H<\infty.
\tag{20}
\]

Enfin \(H>0\) presque sûrement. En effet, \(\Lambda\cap P\) est non vide et le minimum de \(z\) sur cet ensemble est atteint; s’il était nul, \(\Lambda\) contiendrait le sommet \((0,0)\), événement de mesure de Haar affine nulle. Par la formule duale avec \(b=0\),

\[
H(\Lambda)\ge\min_{(y,z)\in\Lambda\cap P}z>0
\]

presque sûrement. Ainsi

\[
0<\mathbb E_{\mu_{\mathrm{aff}}}H<\infty.
\]

En combinant (5) et (20), on obtient (2)–(3). ∎

## 8. Ce que cette preuve ne démontre pas

- Elle ne calcule pas explicitement \(C_V\).
- Elle ne transforme pas les ajustements numériques à rayon fini en estimation rigoureuse de \(C_V\).
- Elle ne fournit pas de vitesse dans (3).
- Elle ne prouve pas l’asymptotique analogue pour le déficit de surface.
- L’équidistribution est démontrée avec une direction uniforme et un roulis tangent indépendant. Cela suffit ici, car la profondeur radiale est invariante sous ce roulis; aucune conclusion n’est revendiquée pour un repère tangent déterministe arbitraire.

## 9. Sources primaires utilisées

1. J. Marklof et A. Strömbergsson, *The distribution of free path lengths in the periodic Lorentz gas and related lattice point problems*, Annals of Mathematics 172 (2010), notamment corollaire 5.9 et lemme 6.2 : [article officiel](https://annals.math.princeton.edu/2010/172-3/p12), [PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n3-p12-p.pdf).
2. M. Ratner, *On Raghunathan’s measure conjecture*, Annals of Mathematics 134 (1991), 545–607 : [article officiel](https://annals.math.princeton.edu/1991/134-3/p02).
3. C. C. Moore, *Ergodicity of flows on homogeneous spaces*, American Journal of Mathematics 88 (1966), 154–178 : [DOI](https://doi.org/10.2307/2373052).
4. R. Kannan et L. Lovász, *Covering minima and lattice-point-free convex bodies*, Annals of Mathematics 128 (1988), 577–602 : [article officiel](https://annals.math.princeton.edu/1988/128-3/p06).
5. W. Banaszczyk, A. Litvak, A. Pajor et S. Szarek, *The Flatness Theorem for Nonsymmetric Convex Bodies via the Local Theory of Banach Spaces*, Mathematics of Operations Research 24 (1999), 728–750 : [DOI](https://doi.org/10.1287/moor.24.3.728).
