from listaAdjacencia import Grafo
import sys

def BellmanFord(G, s):
    graphInfo = {
        "DIST":[sys.maxsize] * G.length,
        "PI": [None] * G.length
    }
    graphInfo["DIST"][s] = 0

    for _ in range(G.length - 1):
        for edges in G.edges:
            i, j = edges
            if graphInfo["DIST"][j] > graphInfo["DIST"][i] + G.dist(i, j):
                graphInfo["DIST"][j] = graphInfo["DIST"][i] + G.dist(i, j)
                graphInfo["PI"][j] = i
    return graphInfo

G = Grafo(True)
G.carregarGrafo("../grafos/grafo.txt")

c = BellmanFord(G, 7)

print(c)