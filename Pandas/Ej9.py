# Crea un archivo csv (de extensión .csv) que contenga el número de faltas de
# alumnado en 5 asignaturas distintas a lo largo de 50 días lectivos. Mediante
# el paquete Pandas, convierte el contenido del archivo csv a un dataframe y
# muéstralo por pantalla. Muestra además la información referente a los 15
# primeros días y, por otra parte, la información referente a los 20 últimos días.

import pandas as pd

archivo = pd.read_csv("Python\Pandas\Ej9.csv")
print(archivo)

print("Los 15 primeros días son:")
print(archivo.head(15))

print("Los 20 últimos días son:")
print(archivo.tail(20))