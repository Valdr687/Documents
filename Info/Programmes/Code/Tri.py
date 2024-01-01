# Tri par sélection

def recherche_max(L):
    maxi = L[0]  # n'importe quelle valeur de L aurait convenu
    for e in L:
        if e > maxi:
            maxi = e
    return maxi


def reverse(L):
    liste = []
    n = len(L)
    for i in range(n, 0, -1):
        liste.append(L[i-1])
    return liste


def tri_selec(L):  # tri par recherches du maximum
    n = len(L)
    liste = []
    for i in range(n):
        m = recherche_max(L)
        liste.append(m)
        L.remove(m)  # attention L sera vidée de ses éléments à la fin !
    return reverse(liste)

# Tri à bulle

def tri_bulle(nombres: list) -> list:
    n = len(nombres)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if nombres[j] > nombres[j+1]:
                # nombres[j] et nombre[j + 1] à échanger
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
    return nombres
