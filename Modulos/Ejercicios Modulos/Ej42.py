# ¿A qué número hay que elevar 10 para que resulte 150? ¿ A qué número hay
# que elevar 10 para que resulte 1000? ¿A qué número hay que elevar 10 para
# que resulte 777? Realiza las acciones debidas para poder resumir todas las
# respuestas anteriores en un único array.

import numpy as np

numeros = np.array([150, 1000, 777])

resultado = np.log10(numeros)

print(resultado)