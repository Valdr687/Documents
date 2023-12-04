# Fonction création de matrice

def creer_matrice(n, p, v):
    m = [None] * n
    #Puis on affecte à chacune de ses cases un tableau de taille p différent.
    for i in range(n):
        m[i] = [v] * p
    return m

def dimensions(m):
    #On détermine n comme la longueur du tableau m et on vérifie que n > 0
    n = len(m)
    assert n > 0 #assert retourne une erreur si la condition n’est pas réalisée
    #Détermination de la dimension p et vérification que p>0
    p = len(m[0]) #la première ligne existe car n>0
    assert p > 0
    #on vérifie que toutes les lignes de m ont bien la longueur p
    for r in m:
        assert len(r) == p
    return (n, p) #on renvoie la paire (n,p)

def transpose(m):
    n, p = dimensions(m)
    t = creer_matrice(p, n, None)
    for j in range(p):
        for i in range(n):
            t[j][i] = m[i][j]
    return t

def mult_matrice(a, b):
    n, p = dimensions(a)
    q, r = dimensions(b)
    assert q == p
    c = creer_matrice(n, r, 0)
    for i in range(n):
        for j in range(r):
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]
    return c
