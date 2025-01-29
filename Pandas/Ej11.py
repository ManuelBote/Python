# Crea un archivo json (de extensión json) que contenga el número de faltas de
# alumnos, alumnas, profesores y profesoras a lo largo de los 31 días de enero.
# Mediante el paquete de Pandas, convierte el contenido del archivo json a un
# dataframe y muéstralo por pantalla. Muestra además la información referente
# a los 10 primeros días y, por otra parte, la información referente a los 9
# últimos días

import pandas as pd

archivo = pd.read_json("Python\Pandas\Ej11.json")
dataframe = pd.DataFrame(archivo)
print(dataframe)

print("Los 10 primeros días son:")
print(dataframe.head(10))

print("Los 9 últimos días son:")
print(dataframe.tail(9))

