# Crea un array que contenga el número de expulsiones que se han producido
# durante la primera evaluación en los cursos A y B de 1º y 2º de ESO del
# instituto Augustóbriga. Seguidamente, representa los datos anteriores en un
# diagrama de barras para observar de una mejor forma la diferencia entre los
# valores de los distintos cursos del centro.

import matplotlib.pyplot as plt
import numpy as np

expulsiones = np.array([3, 5, 2, 6])
cursos = ['1ºA', '1ºB', '2ºA', '2ºB']


plt.bar(cursos, expulsiones, color='red')
plt.title('Diferencia en expulsiones entre cursos A y B')
plt.show()