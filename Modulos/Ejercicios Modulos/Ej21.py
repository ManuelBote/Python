# Crea un array de 1 dimensión que contenga 15 edades de 15 personas
# diferentes. Seguidamente, ordena el array anterior de personas de menor
# edad a personas de mayor edad y muéstralo por pantalla. Crea otro array de
# 1 dimensión que contenga 15 nombres de 15 personas diferentes. A
# continuación, ordena el array anterior de manera que los nombres aparezcan
# alfabéticamente ordenados (mostrándolo también por pantalla).

import numpy as np

edades = np.array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])

print(edades)
edades.sort()
print(edades)

nombres = np.array(['Juan', 'Pedro', 'Carlos', 'Luis', 'Fernando', 'Marcos', 'Diego', 'Daniel', 'Jose', 'Juan', 'Pedro', 'Carlos', 'Luis', 'Fernando', 'Marcos', 'Diego'])

print(nombres)
nombres.sort()
print(nombres)