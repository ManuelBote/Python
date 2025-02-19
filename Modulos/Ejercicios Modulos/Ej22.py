# Crea un array de 2 dimensiones que contenga 5 edades de 5 personas en 2
# poblaciones diferentes. Seguidamente, ordena respecto a cada población las
# edades de las personas de menor a mayor y muéstralo por pantalla. Crea
# otro array de 2 dimensiones que contenga 5 nombres de 5 personas en 2
# poblaciones diferentes. A continuación, ordena alfabéticamente respecto a
# cada población los nombres de las personas

import numpy as np

edades = np.array([[25, 24, 23, 22, 21], [15, 14, 13, 12, 11]])

print(edades)
edades[0].sort()
edades[1].sort()
print(edades)

nombres = np.array([['Juan', 'Pedro', 'Carlos', 'Luis', 'Fernando'], ['Marcos', 'Diego', 'Daniel', 'Jose', 'Juan']])

print(nombres)
nombres[0].sort()
nombres[1].sort()
print(nombres)