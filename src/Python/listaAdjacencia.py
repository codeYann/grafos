# Lista de adjacência com um grafo ponderado K5

class ListaAdj:
    def __init__(self):
        self.lista_adj = []

    def carregarLista(self, path):
        arquivo = open(path, 'r')
        lista = arquivo.readlines()

        for i in range(len(lista)):
            linhaAtual = lista[i].split()
            if i == 0:
                n = int(linhaAtual[0])
                self.lista_adj = [[] for _ in range(n)]
            else:
                self.lista_adj[int(linhaAtual[0])].append({"Vertice": int(linhaAtual[1]), "Peso": float(linhaAtual[2])})
                self.lista_adj[int(linhaAtual[1])].append({"Vertice": int(linhaAtual[0]), "Peso": float(linhaAtual[2])})
        
        arquivo.close()

    def imprimirLista(self, n):
        for i in range(n):
            print("Vertice ", i, ":", self.lista_adj[i])
            print()
