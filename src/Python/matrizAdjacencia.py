import numpy as np

class MatrizAdj:
    def __init__(self):
        self.matriz = []
    
    def __len__(self):
        return int(len(self.matriz))

    def carregarGrafo(self, path):
        arquivo = open(path, 'r')
        lista = arquivo.readlines()

        for i in range(len(lista)):
            linhaAtual = lista[i].split()
            if i == 0:
                n = int(linhaAtual[0])
                self.matriz = np.zeros((n, n), dtype = np.int64)
            else:
                self.matriz[int(linhaAtual[0])][int(linhaAtual[1])] = 1
                self.matriz[int(linhaAtual[1])][int(linhaAtual[0])] = 1
        arquivo.close()

    def percorrerMatriz(self):
        if self.matriz.__len__() == 0:
            raise Exception("A matriz é nula. Portanto, você deve carregar um grafo")
        else:
            for i in range((self.matriz.__len__())):
                for j in range((self.matriz.__len__())):
                    print(self.matriz[i][j], end=" ")
                print()
