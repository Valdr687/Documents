from Graphes_1e_serie import *
from collections import deque

def distance(G, s):
    """ graphe non pondéré, distance depuis l'origine s. On utilise une structure de
    file fournie par deque """
    n = len(G)
    inf = float('inf')
    dist = [inf] * n
    dist[s] = 0

    F = deque()
    F.append(s)

    while len(F) > 0:
        x = F.popleft()
        for y in G[x]:
            if dist[y] == inf:
                dist[y] = dist[x] + 1
                F.append(y)
    
    return dist

def parcours_profondeur(G, s):
    n = len(G)
    deja_vus = [False] * n
    parcours = []
    a_traiter = [s]

    while len(a_traiter) != 0:
        x = a_traiter.pop()
        if not deja_vus[x]:
            deja_vus[x] = True
            parcours.append(x)
            for v in G[x]:
                if not deja_vus[v]:
                    a_traiter.append(v)
    
    return parcours

# Exercice 1

def distance_et_parcours(G,s,t):
    n = len(G)
    inf = float('inf')
    dist = [inf] * n
    dist[s] = 0

    F = deque()
    F.append(s)

    while len(F) > 0:
        x = F.popleft()
        for y in G[x]:
            if dist[y] == inf:
                dist[y] = dist[x] + 1
                F.append(y)
    
    return dist[t-1], 

G=Graphe(10,5)
print(G)
print(distance(ListeAdjacence(G),2))

tracer_graphe(G)
