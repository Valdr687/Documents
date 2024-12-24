from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def tracer_graphe(G):
    graph = nx.Graph()

    for node, edges in G.items():
        for edge in edges:
            graph.add_edge(node, edge)

    nx.draw(graph, with_labels=True, node_color='lightblue',
            edge_color='gray', node_size=500, font_size=10)
    plt.show()


def Graphe(Ordre, DegreMax):
    G = {0: []}

    for Sommet in range(Ordre+1):
        Arretes = []
        for SommetPrecedent in range(Sommet):
            if Sommet in G[SommetPrecedent]:
                Arretes.append(SommetPrecedent)

        DegreMaxLocal = randint(0, DegreMax)

        while len(Arretes) < DegreMaxLocal and Sommet != Ordre:

            n = randint(Sommet, Ordre)

            if n not in Arretes and n != Sommet:
                Arretes.append(n)
        G[Sommet] = Arretes

    return G


def ListeAdjacence(G):

    return [i[1] for i in G.items()]

# Exercice 2


def DegreMaxGraphe(G):
    Deg = 0
    for i in G.items():
        if len(i[1]) > Deg:
            Deg = len(i[1])
    return Deg


def DegreMoyenGraphe(G):
    Deg = 0
    for i in G.items():
        Deg += len(i[1])
    return Deg/len(G.items())

# Exercice 3


def Distribution(G):
    d = {}

    degre_max = DegreMaxGraphe(G)

    for i in range(degre_max+1):
        l = []
        for j in G.items():
            if len(j[1]) <= i:
                l.append(j[0])

        d[i] = l

    return d


# Exercice 4

def liste_à_matrice(L):
    n = len(L)
    M = np.zeros((n, n))

    for i in range(len(L)):
        for j in L[i]:
            M[i][j] = 1

    return M

# Exercice 5


def matrice_à_liste(M):
    n = len(M[0])
    L = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                L[j].append(i)

    return L

# Exercice 6


def graphe_alea(n):
    M = np.zeros((n, n))

    for i in range(1, n):

        for j in range(randint(0, n)):

            M[i][randint(0, n-1)] = 1
    return M


# Exemple d'utilisation
