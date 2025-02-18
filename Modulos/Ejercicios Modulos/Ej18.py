#  Crea un array de 2 dimensiones que contenga los 12 primeros números
# pares. Seguidamente crea un array separando el primero en 4 partes iguales
# y muéstralo por pantalla. A continuación, crea otro array separando el primero
# por columnas y en 4 partes iguales (mostrándolo por pantalla

import numpy as np

pares = np.array([[2,4,6,8,10,12],[14,16,18,20,22,24]])

p4 = pares.reshape(-1, 3)
print(p4)

print("==============================================")

subarrays_columnas = np.array_split(pares, 4, axis=1)
print(subarrays_columnas)