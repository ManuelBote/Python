# Crea un archivo json (de extensión json) que contenga el peso, altura, IMC,
# IGC y grupo sanguíneo de 50 personas pertenecientes a una población.
# Mediante el paquete Pandas, convierte el contenido del archivo json a un
# dataframe y muéstralo por pantalla. Muestra además la información referente
# a las 15 primeras personas y, por otra parte, la información referente a las 25
# últimas personas.

import pandas as pd

archivo = pd.read_json("Python\Pandas\Ej12.json")
dataframe = pd.DataFrame(archivo)
print(dataframe)

print("Las 15 primeras personas son:")
print(dataframe.head(15))

print("Las 25 últimas personas son:")
print(dataframe.tail(25))