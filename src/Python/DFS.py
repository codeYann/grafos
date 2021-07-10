from listaAdjacencia import Grafo

def DFS_VISIT(grafo, vertice, setVertices):
    setVertices.add(vertice)
    print("Vertices visitados: {}".format(vertice))
    for v in grafo[vertice]:
        if v not in setVertices:
            DFS_VISIT(grafo, v, setVertices)

def DFS(G):
    verticesVizitados = set()
    for vertices in G.grafo.keys():
        if vertices not in verticesVizitados:
            DFS_VISIT(G.grafo, vertices, verticesVizitados)
    return verticesVizitados
