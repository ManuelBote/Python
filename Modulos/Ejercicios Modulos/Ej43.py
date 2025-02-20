# ¿Cuál es el mínimo común múltiplo de los números 18,12 y 42? Calcula el
# resultado a partir de un array constituido por dichos números y empleando las
# funciones de NumPy adecuadas.

import numpy as np

numeros = np.array([18, 12, 42])

resultado = np.gcd.reduce(numeros)

print(resultado)