# Mémo info PTSI/PT

## Table des matières

1. [Python](#python)
1. [Méthode de résolutions analytique](#méthodes-de-résolutions-analytique)
1. [Traitement de données](#traitements-de-données)
1. [SQL](#sql)

===

## Python

### Lecture dans un fichier

with open(chemin,"r",encoding="utf8") as f:
texte = f.read()
 Lecture ligne par ligne
with open(chemin,"r",encoding="utf8") as f:
lignes = f.readlines()
(Nettoyage éventuel des débuts et fins de lignes)
lignes = [c.strip() for c in lignes]
 Écriture dans un fichier
with open(chemin,"w",encoding="utf8") as f:
f.write(début)…
⁝
f.write(suite)…
⁝
f.write(fin)

## Méthodes de résolutions analytique

### Méthode de Newton

### Intégration numérique

## Traitements de données

### Dichotomie

### Tris

### Manipulations sur les listes

## SQL
