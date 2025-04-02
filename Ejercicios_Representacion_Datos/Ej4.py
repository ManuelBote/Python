# Crea un array que contenga el número de litros por metro cuadrado que
# cayeron en las localidades de Valencia afectadas por la DANA.
# Seguidamente, representa los datos anteriores para observar la variación de
# precipitaciones experimentada a lo largo del fatídico día. Además, establece
# una rejilla horizontal para apreciar de una mejor manera en qué momento de
# la tarde los valores de lluvia comienzan a ser anormales.

import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt


horas = np.arange(24) 
precipitaciones = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 30, 50, 70, 100, 120, 150, 180, 200, 180, 120, 90, 60, 30, 10])  # Precipitaciones por hora


plt.plot(horas, precipitaciones, marker='o', linestyle='-', color='b', label='Precipitación (litros/m²)')
plt.title('Variación de Precipitaciones en Valencia')
plt.xlabel('Hora del Día')
plt.ylabel('Precipitación')
plt.show()
