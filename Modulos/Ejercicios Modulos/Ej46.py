#  Crea un array que contenga el color favorito de 20 personas (fruto de otra
# encuesta). Al preguntar a otras 20 personas más, se ha obtenido otro array
# de 20 elementos. Elabora, a partir de los dos arrays anteriores, un conjunto
# único con los colores favoritos en la totalidad de la encuesta (ya que es muy
# probable que algunas respuestas se repitan en el muestreo).

import numpy as np

colores = np.array(["rojo", "azul", "verde", "amarillo", "naranja", "rojo", "azul", "verde", "amarillo", "naranja", "rojo", "azul", "verde", "amarillo", "naranja", "rojo", "azul", "verde", "amarillo", "naranja"])

colores2 = np.array(["rojo", "azul", "verde", "amarillo", "naranja", "rojo", "azul", "verde", "amarillo", "naranja", "rojo", "azul", "verde", "amarillo", "naranja", "rojo", "azul", "verde", "amarillo", "naranja"])

conjunto = np.concatenate((colores, colores2))
conjunto2 = np.unique(conjunto)

print(conjunto2)