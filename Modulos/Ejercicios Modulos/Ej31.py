# Crea un array que contenga 10 números decimales aleatorios. A partir de ese
# array, obtén otro array fruto de truncar la parte decimal de los elementos del
# primero

import numpy as np

numeros = np.random.rand(10)

truncados = np.trunc(numeros)

print(numeros)
print(truncados)