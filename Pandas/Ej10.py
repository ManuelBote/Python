# Crea un archivo json (de extensión .json) que contenga la altura que tiene un
# balón al ser golpeado en la Tierra y en 4 planetas más a lo largo de 50
# segundos. Mediante el paquete Pandas, convierte el contenido del archivo
# json a un dataframe y muéstralo por pantalla. Muestra además la información
# referente a los 20 primeros segundos y, por otra parte, la información
# referente a los 10 últimos segundos.

import pandas as pd

archivo = pd.read_json("Python\Pandas\Ej10.json")
dataframe = pd.DataFrame(archivo)
print(dataframe)

print("Los 20 primeros segundos son:")
print(archivo.head(20))

print("Los 10 últimos segundos son:")
print(archivo.tail(10))