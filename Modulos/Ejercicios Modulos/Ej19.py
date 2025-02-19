#  Crea un array de 1 dimensión que contenga el número de días que tiene
# cada mes del año. Seguidamente busca los meses en los que el número de
# días es 30. Crea otro array de 1 dimensión con 10 números aleatorios. A
# continuación, busca las posiciones de los números que sean múltiplos de 3.

import random
import numpy as np

meses = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

print(meses)
print(meses[meses == 30])

num = np.array([])
for i in range(10):
    num = np.append(num, random.randint(1, 100))

print(num)
print(num[num % 3 == 0])