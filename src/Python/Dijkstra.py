from listaAdjacencia import Grafo
import sys
from queue import PriorityQueue

def Dijkstra(G, s):
    
    graphInfo = {
        "DIST": [sys.maxsize] * G.length,
        "PI": [None] * G.length
    }

    graphInfo["DIST"][s] = 0
    
    Q = PriorityQueue()
    Q.put(s, 0)

    while not Q.empty():
        u = Q.get()
        for v in list(G.lista_adj[u]):
            if graphInfo["DIST"][v] > graphInfo["DIST"][u] + G.dist(u, v):
                graphInfo["DIST"][v] = graphInfo["DIST"][u] + G.dist(u, v)
                graphInfo["PI"][v] = u
                Q.put(v, graphInfo["DIST"][v])

    return graphInfo