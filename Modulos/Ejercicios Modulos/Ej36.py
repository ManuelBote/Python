# Crea un array que contenga la deuda en el casino de una persona ludópata
# para cada mes de 2024. A partir del array anterior, elabora un array que
# contenga la deuda acumulada que presenta esta persona en cada mes del
# año 2024

import numpy as np

deuda = np.array([10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500])

deuda_acumulada = np.cumsum(deuda)

print(deuda_acumulada)  