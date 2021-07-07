# Lista de adjacência com um grafo ponderado K5

from collections import defaultdict

class Grafo:
    def __init__(self, tipo):
        self.grafo = defaultdict(list)
        self.tipo = tipo
        self.length = 0

    def adicionarAresta(self, a, b):
        self.grafo[a].append(b)

    def percorrerGrafo(self):
        for u in self.grafo.items():
            print(u)

    def carregarGrafo(self, path):
        file = open(path, 'r')
        listaVertices = file.readlines()
        for i in range(len(listaVertices)):
            verticesAtuais = listaVertices[i].split()
            if i == 0:
                self.length = int(verticesAtuais[0])
            else:
                if self.tipo != 'w':
                    self.adicionarAresta(int(verticesAtuais[0]), int(verticesAtuais[1]))
                    self.adicionarAresta(int(verticesAtuais[1]), int(verticesAtuais[0]))
                else:
                    self.adicionarAresta(
                        int(verticesAtuais[0]), 
                        {"Vertice": int(verticesAtuais[1]), "Peso": float(verticesAtuais[2])}
                    )
                    self.adicionarAresta(
                        int(verticesAtuais[1]), 
                        {"Vertice": int(verticesAtuais[0]), "Peso": float(verticesAtuais[2])}
                    )
        file.close()
