#  Crea un array que contenga el color favorito de 20 personas (fruto de otra
# encuesta). Al preguntar a otras 20 personas más, se ha obtenido otro array
# de 20 elementos. Elabora, a partir de los dos arrays anteriores, un conjunto
# único con los colores favoritos en la totalidad de la encuesta (ya que es muy
# probable que algunas respuestas se repitan en el muestreo).

import numpy as np

colores = np.array(["rojo", "azul", "verde", "rosa", "naranja", "rojo", "naranja", "verde", "azul", "azul", "negro", "negro", "morado", "rojo", "rosa", "rojo", "azul", "verde", "blanco", "marron"])

colores2 = np.array(["marron", "celeste", "verde", "blanco", "blanco", "rojo", "verde", "verde", "amarillo", "negro", "morado", "azul", "verde", "amarillo", "rojo", "rojo", "azul", "verde", "amarillo", "magenta"])

conjunto = np.concatenate((colores, colores2))
conjunto2 = np.unique(conjunto)

print(conjunto2)