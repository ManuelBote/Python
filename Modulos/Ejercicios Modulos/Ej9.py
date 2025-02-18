# Crea un array indicando en qué mes del año cumplen años tus padres y tus tíos. 
# A partir del array anterior elabora una matriz CSR en la que sólo aparezcan los términos no nulos. 
# Muestra la matriz por pantalla, así como los datos de forma condensada y el número de elementos que no son nulos.

import numpy as np 
from scipy.sparse import csr_matrix

meses = np.array([1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1])

print(csr_matrix(meses))
print(csr_matrix(meses).count_nonzero())
print(csr_matrix(meses).data)

