# Crea un array de 1 dimensión que contenga los 10 primeros términos de la
# serie de Fibonacci. Seguidamente, busca la posición que ocupa en la serie el
# número 13. Crea otro array de 1 dimensión que contenga los 10 primeros
# números múltiplos de 7. A continuación, busca la posición que ocupa en la
# serie el número 49.

import numpy as np

fibonacci = np.array([1,2,3,5,8,13,21,34,55,89])

print(fibonacci)
print(np.where(fibonacci == 13))

num = np.array([])
for i in range(10):
    num = np.append(num, (i+1) * 7)

print(num)
print(np.where(num == 49))