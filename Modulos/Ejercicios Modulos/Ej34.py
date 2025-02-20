# Crea un array que contenga 10 números decimales aleatorios entre el 60 y el
# 80. A partir de ese array, obtén otro array redondeando hacia el número
# entero inferior los elementos del primero

import numpy as np

numeros = np.random.uniform(60, 80, 10)

redondeados = np.floor(numeros)

print(numeros)
print(redondeados)