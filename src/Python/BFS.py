from listaAdjacencia import Grafo
from collections import deque

def BFS(G, vertice):
    structures = {
        "COR": ["B"] * G.length,
        "D": [float('inf')] * G.length,
        "PI": [None] * G.length
    }
    structures["COR"][vertice] = "C"
    structures["D"][vertice] = 0
    structures["PI"][vertice] = None

    Q = deque()
    Q.append(vertice)
    
    while len(Q) != 0:
        u = Q.pop()

        for v in list(G.lista_adj[u]):
            if structures["COR"][v] == "B":
                structures["COR"][v] = "C"
                structures["PI"][v] = u
                structures["D"][v] = structures["D"][u] + 1
                Q.append(v)

        structures["COR"][u] = "P"

    return structures
