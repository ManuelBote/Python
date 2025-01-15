# Crea un array mediante el módulo NumPy que contenga 12 elementos numéricos para designar los meses del año. 
# Crea otro array cuyos elementos sean los números de días correspondientes a cada mes del año (considerar año bisiesto). 
# Representa mediante el módulo Matplotlib los meses del año 2024 y su número de días.

import numpy as np
import matplotlib.pyplot as plt

meses = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
dias = np.array([31,28,31,30,31,30,31,31,30,31,30,31])

plt.plot(meses, dias)
plt.show()