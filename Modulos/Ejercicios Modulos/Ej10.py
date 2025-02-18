# Crea un array compuesto por 36 números pares. Muestra el array por
# pantalla. Redimensiona el array anterior a un array bidimensional cuya
# longitud de sus elementos sea de 6. Muestra el array bidimensional por
# pantalla. Redimensiona el primer array en un array tridimensional cuya
# longitud de la última dimensión siga siendo de 6.

import numpy as np

num = np.array([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70])


print(num)
print(num.reshape(-1,6))
print(num.reshape(-1,2,3))