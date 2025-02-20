# Crea un array que contenga 10 números decimales aleatorios entre el 10 y el
# 20. A partir de ese array, obtén otro array redondeando a 2 decimales los
# elementos del primero

import numpy as np

numeros = np.random.uniform(10, 20, 10)

redondeados = np.around(numeros, decimals=2)

print(numeros)
print(redondeados)