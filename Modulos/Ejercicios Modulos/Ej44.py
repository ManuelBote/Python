# ¿Cuál es el máximo común divisor de los números 20, 24 y 32? Calcula el
# resultado a partir de un array constituido por dichos números y empleando las
# funciones de NumPy adecuadas.

import numpy as np

numeros = np.array([20, 24, 32])

resultado = np.lcm.reduce(numeros)

print(resultado)