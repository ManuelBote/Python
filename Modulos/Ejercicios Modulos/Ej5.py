# Representa en un gráfico el sueldo que ha cobrado un trabajador de una empresa en cada uno de los meses de 2024 
# (si en alguno de esos meses el trabajador ha estado en paro, el sueldo será nulo). 
# Haz los cambios pertinentes para que la representación sea a través de puntos únicamente.

import matplotlib.pyplot as plt

meses = ([1,2,3,4,5,6,7,8,9,10,11,12])
sueldo = ([1000,2000,1500,1200,1000,0,0,1250,1490,1780,2100,2400])

plt.plot(meses,sueldo)
plt.show()
