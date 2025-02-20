# Crea un array que contenga 10 números decimales aleatorios entre el 40 y el
# 50. A partir de ese array, obtén otro array redondeando hacia el número
# entero superior los elementos del primero.

import numpy as np

numeros = np.random.uniform(40, 50, 10)

redondeados = np.ceil(numeros)

print(numeros)
print(redondeados)