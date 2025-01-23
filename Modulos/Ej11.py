# Representa gráficamente la variación que experimenta la población de un municipio determinado a lo largo de un año. 
# Establece la línea del gráfico con estilo punteado, de color verde y de grosor relativamente visible. 
# Representa conjuntamente en el mismo gráfico la variación de otra población vecina

import numpy as np
import matplotlib.pyplot as plt

meses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
poblacion = np.array([1100, 1200, 1230, 1240, 1300, 1560, 1670, 2080, 1790, 1800, 1600, 1820])
poblacion2 = np.array([2100, 2200, 2130, 2000, 1900, 1870, 1790, 1580, 1950, 2000, 2300, 2100])

plt.plot(meses, poblacion, color='green', linestyle='dotted', linewidth=5)
plt.plot(meses, poblacion2, color='red', linestyle='dotted', linewidth=5)
plt.show()