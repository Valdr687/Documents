# Python : Boite à outils

## Numpy

```python
import numpy as np
```

### Tableaux pré-définis

| Objectif                                      | Code Python                                            |
|-|-|
|Tableau à 1D de n zéros| `t= np.zeros(n)`|
| Tableau à 2D de n lignes et m colonnes         | `t = np.zeros((n, m))`                                 |
| Tableau à 1D de n valeurs régulièrement espacées, entre a (inclus) et b (inclus) | `t = np.linspace(a, b, n)`                              |
| Tableau à 1D de valeurs régulièrement espacées, entre a (inclus) et b (exclus) par pas de p | `t = np.arange(a, b, p)`                               |

### Opérations sur les tableaux

| Objectif                                       | Code Python                                               |
|------------------------------------------------|-----------------------------------------------------------|
| Récupérer l’élément de rang i d’un tableau 1D     | `t[i]`                                                    |
| Récupérer les éléments entre les rangs a (inclus) et b (exclus) d’un tableau 1D | `t[a:b]`                                             |
| Récupérer les éléments à partir du rang a (inclus) d’un tableau 1D | `t[a:]`                                               |
| Récupérer les éléments jusqu’au rang b (exclus) d’un tableau 1D | `t[:b]`                                               |
| Récupérer les éléments entre les rangs a (inclus) et b (exclus) par pas p d’un tableau 1D | `t[a:b:p]`                                       |
| Récupérer l’élément de la ligne i et colonne j d’un tableau 2D | `t[i, j]` ou `t[i][j]`                                 |
| Récupérer la ligne i d’un tableau 2D             | `t[i, :]`                                               |
| Récupérer la colonne j d’un tableau 2D          | `t[:, j]`                                               |

### Fonctions statistiques utiles

| Objectif                                   | Code Python                                    |
|--------------------------------------------|------------------------------------------------|
| Valeur minimale                            | `np.min(t)`                                    |
| Valeur maximale                            | `np.max(t)`                                    |
| Somme des éléments                        | `np.sum(t)`                                    |
| Moyenne                                    | `np.mean(t)`                                   |
| Écart-type expérimental $\sqrt{\frac{1}{N-1}\sum_{i=0}^{N-1}(x_i-\overline{x})^2}$                  | `np.std(t, ddof=1)`                            |

## Graphique

```python
import matplotlib . pyplot as plt # Pour tracer des graphiques
```

## Tracé d’un graphe

Entrée des données expérimentales dans un tableau array, grâce à la bibliothèque numpy on crée un
np.array pour chacune des grandeurs (abscisses et ordonnées).
Il est important de rentrer le même nombre de valeurs de x et de y et dans le même ordre.

```python
x = np. array ([ rentrer les valeurs de x séparées par des virgules ])
# contient les valeurs x auxquelles ont été mesurées celles de y
y = np. array ([ rentrer les valeurs de y séparées par des virgules ])
# ce sont les valeurs de y correspondantes
```

## Options

- couleur : première lettre anglaise de la couleur (b, g, y, c, r, m, w ou k pour le noir)
- style_point :

| Paramètre | x   | X            | +   | P          | .   | o   | *   | d       |
|-----------|-----|--------------|-----|------------|-----|-----|-----|---------|
| Marqueur  | croix | Croix plein | plus | Plus plein | pixel | rond | étoile | carreau |

- Style_trait

| Paramètre      | -   | -  | .   | P   | _   | ,   | v   |
|----------------|-----|---|-----|-----|-----|-----|-----|
| Marqueur       | trait pointillé | Ligne continue | Point | tiret | Plus plein | Ligne de tirets | pixel | triangle |
