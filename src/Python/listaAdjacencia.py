# Lista de adjacência com um grafo ponderado K5

from collections import defaultdict

class Grafo:
    def __init__(self, peso):
        self.lista_adj = defaultdict(list)
        self.peso = peso
        self.tipo = None
        self.length = 0

    def adicionarAresta(self, a, b):
        self.lista_adj[a].append(b)

    def percorrerGrafo(self):
        for u in self.lista_adj.items():
            print(u)

    def carregarGrafo(self, path):
        # Lendo o arquivo no qual todos os dados do grafo estão contidos!
        file = open(path, 'r')
        listaVertices = file.readlines()

        # Tratando informações importantes, como por exemplo, se o grafo é direcionado ou não e quantidade de vertices
        self.tipo = listaVertices[0].split()[2]
        self.length = int(listaVertices[0].split()[0])

        for i in range(len(listaVertices)):
            verticesAtuais = listaVertices[i].split()
            if self.tipo == 'D':
                if i == 0:
                    pass
                else:
                    if self.peso == False:
                        self.adicionarAresta(
                            int(verticesAtuais[0]), 
                            int(verticesAtuais[1])
                        )
                    else:
                        self.adicionarAresta(
                            int(verticesAtuais[0]), 
                            {"Vertice": int(verticesAtuais[1]), "Peso": float(verticesAtuais[2])}
                        )
            else:
                if i == 0:
                    pass
                else:
                    if self.peso == False:
                        self.adicionarAresta(
                            int(verticesAtuais[0]), 
                            int(verticesAtuais[1])
                        )
                        self.adicionarAresta(
                            int(verticesAtuais[1]), 
                            int(verticesAtuais[0])
                        )
                    else:
                        self.adicionarAresta(
                            int(verticesAtuais[0]),
                            {"Vertice": int(verticesAtuais[1]), "Peso": float(
                                verticesAtuais[2])}
                        )
                        self.adicionarAresta(
                            int(verticesAtuais[1]),
                            {"Vertice": int(verticesAtuais[0]), "Peso": float(
                                verticesAtuais[2])}
                        )
        file.close()
