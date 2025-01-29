# Crea un archivo csv (de extensión .csv) que contenga el número de
# habitantes de 5 poblaciones distintas a lo largo de 50 años. Mediante el
# paquete Pandas, convierte el contenido del archivo csv a un dataframe y
# muéstralo por pantalla. Muestra además la información referente a los 22
# primeros años y, por otra parte, la información referente a los 15 últimos
# años.

import pandas as pd

archivo = pd.read_csv("Python\Pandas\Ej8.csv")
print(archivo)

print("Los 22 primeros años son:")
print(archivo.head(22))

print("Los 15 últimos años son:")
print(archivo.tail(15))