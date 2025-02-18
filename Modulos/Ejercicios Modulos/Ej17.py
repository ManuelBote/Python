# Crea un array de 1 dimensión que contenga los 6 primeros números pares.
# Seguidamente muestra por pantalla un array fruto de separar el anterior en 3
# partes y otro array fruto de separar el primero en 2 partes. Partiendo del array
# obtenido al separar en 3 partes, muestra por pantalla el segundo subarray.

import numpy as np

pares = np.array([2,4,6,8,10,12])

p3 = pares.reshape(-1, 2)
p2 = pares.reshape(-1, 3)

print(p3)
print(p2)

print(p3[1])