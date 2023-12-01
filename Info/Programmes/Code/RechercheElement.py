# Recherche d’un élément. Renvoie le rang de l'élément cherché

from random import randint
# Liste générée aléatoirement au préalable
liste = [ randint(0,10) for i in range(10)]
valeur = 7  # Valeur cherchée

rang = 0
drapeau = 1  # Flag
while drapeau:
    for i in liste:
        if i == valeur:
            print(f"{valeur} est le {rang+1}ème élément de la liste")
            drapeau = 0
        rang += 1

# Recherche du maximum. Renvoie le rang de l'élément cherché

liste = [randint(0, 9) for i in range(10)]  # Liste générée aléatoirement

mx = liste[0]
for i in liste:
    if i > mx:
        mx = i
print(f"{mx} est le maximum de {liste}")

# Recherche du second maximum. Renvoie le rang de l'élément cherché

liste = [randint(0, 9) for i in range(10)]  # Liste générée aléatoirement

mx = max(liste[0], liste[1])
second_max = min(liste[0], liste[1])
for i in range(2, len(liste)):
    if liste[i] > mx:  # liste[i] supérieur au maximum
        second_max = mx
        mx = liste[i]
    elif liste[i] > second_max:  # liste[i] inférieur au maximum et supérieur au second maximum
        second_max = liste[i]
print(f"{second_max} est le second maximum de {liste}")

# Comptage des éléments avec un dictionnaire

liste = [randint(0, 9) for i in range(10)]  # Liste générée aléatoirement

compteur = {}
clés = []
for i in liste:
    if i in clés:
        compteur[i] += 1
    else:
        clés.append(i)
        compteur[i] = 1
print("Il y a", end="")
for j in compteur:
    print(f' {compteur[j]} : {j},', end="")
