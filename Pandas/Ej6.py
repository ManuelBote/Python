# Crea un dataframe mediante el paquete Pandas que contenga el número de
# aprobados y suspensos en 20 asignaturas de ESO y FP. Los índices de cada
# fila del dataframe deben ser los nombres de las asignaturas cuyos aprobados
# y suspensos se muestran. Muestra el dataframe completo y, después, las 3
# asignaturas con mayor número de suspensos y las 2 asignaturas con el
# mayor número de aprobados.

import pandas as pd

diccionario = {"asignaturas" : ["Matemáticas", "Lengua", "Ciencias Sociales", "Inglés", "Física", "Química", "Tecnología", "Biología", "Geografía", "Historia", "Educación Física", "Informática", "Música", "Plástica", "Religión", "Tutores", "Economía", "Educación Cívica", "Álgebra", "Programación"],
               "aprobados" : [10, 8, 5, 3, 20, 1, 6, 8, 9, 10, 11, 22, 13, 4, 15, 6, 7, 18, 9, 10],
               "suspensos" : [10, 14, 7, 20, 1, 22, 3, 5, 6, 0, 1, 4, 3, 1, 8, 4, 7, 1, 9, 11]}

dataframe = pd.DataFrame(diccionario)
print(dataframe)

print("Las 3 asignaturas con mayor número de suspensos son:")
print(dataframe.sort_values(by = "suspensos", ascending=False).head(3))

print("Las 2 asignaturas con mayor número de aprobados son:")
print(dataframe.sort_values(by = "aprobados", ascending=False).head(2))