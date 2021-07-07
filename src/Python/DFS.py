from listaAdjacencia import Grafo

def DFS_VISIT(grafo, vertice, setVertices):
    setVertices.add(vertice)
    print(vertice)
    for v in grafo[vertice]:
        if v not in setVertices:
            DFS_VISIT(grafo, v, setVertices)

def DFS(grafo):
    verticesVizitados = set()
    for vertices in grafo.keys():
        if vertices not in verticesVizitados:
            DFS_VISIT(grafo, vertices, verticesVizitados)
