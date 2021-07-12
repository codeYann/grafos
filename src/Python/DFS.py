from listaAdjacencia import Grafo

def DFS_VISIT(lista_adj, vertice, setVertices):
    setVertices.add(vertice)
    print("Vertices visitados: {}".format(vertice))
    for v in lista_adj[vertice]:
        if v not in setVertices:
            DFS_VISIT(lista_adj, v, setVertices)

def DFS(G):
    verticesVizitados = set()
    for vertices in G.lista_adj.keys():
        if vertices not in verticesVizitados:
            DFS_VISIT(G.lista_adj, vertices, verticesVizitados)
    return verticesVizitados
