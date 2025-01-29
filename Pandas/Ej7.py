# Crea un archivo csv (de extensión .csv) que contenga temperatura media,
# temperatura máxima, temperatura mínima, probabilidad de precipitación y
# porcentaje de humedad de los 31 días del mes de enero. Mediante el
# paquete Pandas, convierte el contenido del archivo csv a un dataframe y
# muéstralo por pantalla. Muestra además la información referente a los 12
# primeros días y, por otra parte, la información referente a los 4 últimos días.

import pandas as pd

archivo = pd.read_csv("Python\Pandas\Ej7.csv")
print(archivo)

print("Los 12 primeros días son:")
print(archivo.head(12))

print("Los 4 últimos días son:")
print(archivo.tail(4))