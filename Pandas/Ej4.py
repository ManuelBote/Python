# Crea un dataframe mediante el paquete Pandas que contenga el número de homicidios causados por hombres 
# y por mujeres en los primeros 20 días de un mes. 
# Muestra el dataframe completo por pantalla y, después, muestra un dataframe con los 5 días donde más homicidios se han producido.

import pandas as pd

homicidios = {"Homicidios de hombres" : [3, 4, 5, 1, 2, 0, 0, 3, 2, 6, 1, 10, 0, 2, 1, 3, 4, 5, 6, 7],
              "homicidios de mujeres" : [2, 3, 4, 1, 2, 0, 0, 2, 1, 5, 1, 9, 0, 2, 1, 3, 4, 5, 6, 7]}

dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

dataFrame = pd.DataFrame(homicidios, index = dias)
print(dataFrame)

dataFrame["Total"] = dataFrame["Homicidios de hombres"] + dataFrame["homicidios de mujeres"]

max5dias = dataFrame.sort_values(by = "Total", ascending=False).head(5)
print("Los 5 dias con mas homicidios son:")
print(max5dias)


