#  Seja G = <V, E> um grafo simples (sem paralelas e laços) e A = [a]ij a matriz que representará nosso grafo G

#  Matriz de adjacência é uma das formas de se representar computacionalmente um grafo.
#  A ideia é basicamente criar uma matriz n por n, onde n = |V|

#  (1) em um grafo simples, se i == j, [aij] = 0
#  (2) caso exista uma aresta entre os vertices de G, [aij] = 1

SIZE = 3


def criarMatriz(N):
    G = []
    for i in range(N):
        linhas = []
        for j in range(N):
            if i == j:
                linhas.append(0)
            else:
                linhas.append(int(input("Entre com o elemento [{}]:[{}]: ".format(i, j))))
        G.append(linhas)
    return G

def percorrerMatriz(matriz, N):
    for i in range(N):
        print("| ", end="")
        for j in range(N):
            print(matriz[i][j], end = " ")
        print("|")


def main():
    G = criarMatriz(SIZE)
    percorrerMatriz(G, 3)

main()

