# Establece la matriz de adyacencia para un grafo cuadricular de 4 elementos,
# donde las relaciones entre ambos son equivalentes. A partir de la matriz de
# adyacencia, determina el número de componentes conexas del grafo
# empleando una matriz CSR.

import numpy as np
from scipy.sparse import csr_matrix

matriz = np.array([ [1, 1, 0, 1],
                    [0, 0, 1, 0],
                    [0, 1, 0, 1],
                    [1, 1, 1, 1]])

print(csr_matrix(matriz))
print(csr_matrix(matriz).sum(axis=1))    