mark = 0

def DFS_VISIT(lista_adj, v, grafoInfo, arestas):
    global mark 
    mark = mark + 1
    grafoInfo["D"][v] = mark
    grafoInfo["cores"][v] = "C"
    for u in lista_adj[v]:
        if grafoInfo["cores"][u] == "B" and grafoInfo["cores"][v] == "C":
            arestas["arvore"].append((v, u))
        elif grafoInfo["cores"][u] == "C" and grafoInfo["cores"][v] == "C":
            arestas["retorno"].append((v, u))
        else:
            if grafoInfo["D"][v] < grafoInfo["D"][u]:
                arestas["avanco"].append((v, u))
            else:
                arestas["cruzamento"].append((v, u))
        if grafoInfo["cores"][v] == "B":
            DFS_VISIT(lista_adj, u, grafoInfo, arestas)
    mark = mark + 1
    grafoInfo["F"][v] = mark
    grafoInfo["cores"][v] == "P"

def DFS(G, lista_adj, lista_vertice):
    global mark
    mark = 0

    grafoInfo = {
        "cores": ["B"] * G.length,
        "D": [0] * G.length, # Momento em que o grafo é vizitado
        "F": [0] * G.length # Momento em que o grafo não possui nenhum vizinho para se vizitar
    }

    # Nomenclatura das arestas
    arestas = {
        "arvore": [],
        "retorno": [],
        "cruzamento": [],
        "avanco": []
    }

    for v in lista_vertice:
        if grafoInfo["cores"][v] == "B":
            DFS_VISIT(lista_adj, v, grafoInfo, arestas)
    return grafoInfo, arestas
