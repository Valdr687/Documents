# Algorithmique et programmation

## Introduction

Installer une bibliothèque avec pip

1. Ouvrir un terminal
1. ```pip install Nom```

## Variables

### Opérations

| Maths            | Python |
| ---------------- | ------ |
| Addition         | +      |
| Soustraction     | -      |
| Multiplication   | \*     |
| Exposant         | \*\*   |
| Division         | /      |
| Division entière | //     |
| Modulo           | %      |

## Boucles

Une boucle est une **structure répétitive** ou **itératives**.

### Boucles tant que (_while_)

Les boucles TantQue permettent de faire une boucle pour un nombre d'_itérations_ inconnu à priori à l'avance (contrôle d'une saisie, long fichier...).

```pseudo code
Début
    Tant que test
        Opération se répétant tant que le test est vrai
    FinTantQue
Fin
```

En Python :

```python
while test:
    print("Opération se répétant") #print est un example, on peut mettre n'importe quelle instruction
```

### Boucler en comptant

Les boucles Pour sont utilisés quand on connait à l'avance le nombre d'_itérations_ (nombre de passages) ou que l'on souhaite utiliser une variable dont la valeur varie d'un _pas_ fixe.

```pseudo code
Début
    Pour Compteur <-- Initial à Final Pas ValeurduPas faire
        Instructions
    FinTantQue
Fin
```

En Python :

```python
for i in range(start,stop,step):
    print("Opération se répétant") #print est un example, on peut mettre n'importe quelle instruction
#Structure plus compactes
for i in range(start,stop): #step = 1
    print("Opération se répétant")
for i in range(stop): #stop = 0 et step = 1
    print("Opération se répétant")
```
