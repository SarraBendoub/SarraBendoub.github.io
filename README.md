# Portfolio de Sarra Ben Doub

Site personnel : Data Scientist & AI Engineer, données financières, risque et IA.
`index.html` est la version française (page par défaut), `index-en.html` la version anglaise.

Site statique en HTML, CSS et JavaScript. Pas de build, pas de dépendance.

## Contenu

```
index.html, index-en.html   les deux pages du site
styles.css, script.js       mise en forme et menu mobile
favicon.svg
assets/                     photo de profil, image d'aperçu au partage (1200 x 630)
cv/                         CV en PDF (FR, EN) et leurs sources HTML
projects/NN-nom/media/      démos vidéo et captures de chaque projet
projects/NN-nom/docs/       lettres de recommandation
```

## Mettre à jour le CV

Modifier `cv/cv-fr.html` ou `cv/cv-en.html`, puis :

```
python cv/build-cv.py
```

Le script utilise Chrome en mode headless et signale un CV qui déborde sur deux pages.
Fermer le PDF dans le lecteur avant de relancer, sinon il n'est pas réécrit.

## Avant de publier une modification

- Reporter le changement dans les deux pages, française et anglaise.
- Après une modification de `styles.css` ou `script.js`, changer la date `?v=AAAAMMJJ` dans les
  deux pages, sinon les visiteurs gardent l'ancienne version en cache.
- Vérifier qu'aucun lien local n'est cassé :

```bash
for p in index.html index-en.html; do grep -oE '(src|href|poster)="[^"]+"' $p | sed 's/.*="//;s/"$//;s/?.*//' | grep -v '^#\|^http\|^mailto\|^tel' | sort -u | while read -r f; do [ -e "$f" ] || echo "MANQUANT ($p): $f"; done; done
```

Tout fichier présent dans ce dossier est public une fois le site en ligne. Les rapports de stage
et documents internes sont conservés ailleurs.
