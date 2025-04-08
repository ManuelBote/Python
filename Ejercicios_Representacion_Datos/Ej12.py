# Crea un array que contenga el número de hijos al preguntar a 50 personas en
# una encuesta realizada en la Rambla de Barcelona. Seguidamente,
# representa los datos anteriores en un histograma para observar cuál es el
# valor más frecuente y repetido dentro del muestreo llevado a cabo en dicha
# encuesta.

import matplotlib.pyplot as plt
import numpy as np

mascotas = np.random.choice([0, 1, 2, 3, 4, 5], size=50)

plt.hist(mascotas, bins=6, color='red')
plt.show()