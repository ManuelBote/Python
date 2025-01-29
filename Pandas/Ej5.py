# Crea un dataframe mediante el paquete Pandas que contenga la altura y el
# peso de 20 personas pertenecientes a una cierta población. Modifica los
# índices del dataframe para que sean los nombres de las personas cuya altura
# y peso se muestra en cada fila. Muestra el dataframe completo y, después,
# las 3 personas con más altura y las 2 personas con más peso.

import pandas as pd

diccionario = {"alturas" : [1.80, 1.75, 1.70, 1.65, 1.60, 1.55, 1.50, 1.45, 1.40, 1.50, 1.79, 1.82, 1.94, 1.56, 1.64, 1.78, 1.60, 1.85, 1.47, 1.66],
               "pesos" : [80, 70, 55, 90, 100, 89, 60, 64, 74, 93, 86, 79, 72, 80, 85, 70, 74, 99, 103, 88]}

nombres = ["Ana", "Luis", "Carlos", "María", "José", "Laura", "Pedro", "Isabel", "Juan", "Elena",
           "David", "Sofía", "Antonio", "Carmen", "Marta", "Raúl", "Patricia", "Javier", "Beatriz", "Alberto"]

dataFrame = pd.DataFrame(diccionario, index = nombres)
print(dataFrame)

print("Las 3 personas con más altura son:")
print(dataFrame.sort_values(by = "alturas", ascending=False).head(3))

print("Las 2 personas con más peso son:")
print(dataFrame.sort_values(by = "pesos", ascending=False).head(2))
