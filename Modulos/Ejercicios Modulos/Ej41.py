#  ¿A qué número hay que elevar 2 para que resulte 20? ¿A qué número hay
# que elevar 2 para que resulte 46? ¿A qué número hay que elevar 2 para que
# resulte 180? Realiza las acciones debidas para poder resumir todas las
# respuestas anteriores en un único array

import numpy as np

numeros = np.array([20, 46, 180])

resultado = np.log2(numeros)

print(resultado)    