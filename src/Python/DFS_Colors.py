from listaAdjacencia import Grafo

def vetoresDeEstado(length):
    return [0] * length

def DFS_VISIT(lista_adj, vertice, vetorCores):
    vetorCores[vertice] = "G"
    print("Vertices visitados: {}".format(vertice))
    for v in lista_adj[vertice]:
        if vetorCores[v] == "W":
            DFS_VISIT(lista_adj, v, vetorCores)
    vetorCores[vertice] = "B"

def DFS(Grafo):
    cores = ["W" for _ in range(Grafo.length)] 
    for vertice in list(Grafo.list_adj.keys()):
        if cores[vertice] == "W":
            DFS_VISIT(Grafo.list_adj, vertice, cores)
    return cores
