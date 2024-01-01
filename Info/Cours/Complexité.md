# Notion de complexité d'un algorithme

## Introduction

En plus d'être correct, un algorithme doit être efficace. On mesure cette efficacité par la :

- complexité en temps : temps d'exécution
- complexité en mémoire : ressources nécessaires à son exécution

On s'intéresse à la **complexité en temps**.

## Calcul de la complexité

On définit une fonction $T(n)$ qui représente le temps d'unité de temps ou d'opérations de temps en fonction de $n$, la taille de l'entrée.

On considère les opérations élémentaires :

- déclaration, affectations, et retour d'une variable
- incrémentation d'une variable
  -gestion de la variable dans une boucle "Pour" `For i in range()`
- tests élémentaires, boucle "Tant que" et structures conditionnelles "Si"

**Par hypothèse les couts sont identiques et de valeur $1$**

On s'intéresse à $\Theta$ qui correspond à l'ordre de grandeur de $T$ :

- $T(2n + 2)$ correspond à $\Theta(n)$, à l'infini on considère que $2n+2 \approx n$

### Les différentes classes de complexité

| Notation                  | Classe                       |
| ------------------------- | ---------------------------- |
| $\Theta(1)$               | Complexité constante         |
| $\Theta(\ln(n))$          | Complexité logarithmique     |
| $\Theta(n)$               | Complexité linéaire          |
| $\Theta(n \times \ln(n))$ | Complexité quasi-linéaire    |
| $\Theta(n^2)$             | Complexité quadratique       |
| $\Theta(n^{p})$           | Complexité polynomiale       |
| $\Theta(n^{\ln(n)})$      | Complexité quasi-polynomiale |
| $\Theta(2^n)$             | Complexité exponentielle     |

### Les différents types de complexité

- Complexité dans le pire des cas $C_{max}$ : majorant du temps d'exécution
- Complexité en moyenne $C_{moy}$ : moyenne du temps d'exécution, correspond au comportement moyen d'un algorithme
- Complexité dans le meilleur des cas $C_{min}$ : minorant du temps d'exécution, peu utile
