#include <stdio.h>
#include <stdlib.h>

#define N 3

// Seja G = <V, E> um grafo simples (sem paralelas e laços) e A = [a]ij a matriz que representará nosso grafo G

// Matriz de adjacência é uma das formas de se representar computacionalmente um grafo.
// A ideia é basicamente criar uma matriz n por n, onde n = |V|

/*
 * (1) em um grafo simples, se i == j, [aij] = 0
 * (2) caso exista uma aresta entre os vertices de G, [aij] = 1
*/

int** criarMatriz(int linha, int coluna) {
  int** Matriz = malloc(sizeof(int) * linha);
  for (int i = 0; i < linha; i++) {
    Matriz[i] = malloc(sizeof(int) * coluna);
  }
  return Matriz;
}

void preencherMatriz(int **matriz, int linha, int coluna) {
  for (int i = 0; i < linha; i++) {
    for (int j = 0; j < coluna; j++) {
      if (i != j) {
        printf("Ha uma aresta entre o vertice %d e %d: ", i+1, j+1);
        scanf("%d", &matriz[i][j]);
      } else {
        matriz[i][j] = 0;
      }
    }
  }
}

void percorrerMatriz(int **matriz, int linha, int coluna) {
  for (int i = 0; i < linha; i++) {
    printf("|");
    for (int j = 0; j < coluna; j++) {
      printf(" %d ", matriz[i][j]);
    }
    printf("|\n");
  }
}

int main(int argc, char *argv[]) {
  // Utilizaremos um K3 (grafo completo com 3 vertices) como exemplo

  int** A = criarMatriz(N, N);
  preencherMatriz(A, N, N);
  percorrerMatriz(A, N, N);
  return 0;
}
