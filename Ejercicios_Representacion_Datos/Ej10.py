# Crea un array que contenga el número de títulos de Grand Slam que posee
# Rafael Nadal, Roger Federer, Novak Djokovic y Andy Murray. Seguidamente,
# representa los datos anteriores en un diagrama de barras vertical para
# apreciar mejor la legendaria rivalidad del Big Four de la ATP. Además,
# modifica el color y la anchura vertical de las barras del gráfico

import matplotlib.pyplot as plt
import numpy as np

jugadores = ['Rafael Nadal', 'Roger Federer', 'Novak Djokovic', 'Andy Murray']
titulos = np.array([22, 20, 24, 3])

plt.bar(jugadores, titulos, color='blue', width=0.5)
plt.title('Grand Slam de la ATP')
plt.show()