# Crea una serie mediante el paquete Pandas que contenga las profesiones de 20 personas de una cierta población. 
# Modifica las etiquetas de los elementos de la serie para que sean los nombres de las personas que poseen dichas profesiones. 
# Muestra la serie completa por pantalla y, después, la profesión de dos personas al azar de la población

import pandas as pd

profesiones = [
    "Abogado", "Arquitecto", "Ingeniero", "Médico", "Profesor",
    "Psicólogo", "Diseñador gráfico", "Programador", "Chef", "Enfermero",
    "Científico", "Periodista", "Electricista", "Abogado", "Contador",
    "Actor", "Cocinero", "Carpintero", "Farmacéutico", "Fisioterapeuta"
]

nombres = [
    "Ana", "Luis", "Carlos", "María", "José", "Laura", "Pedro", "Isabel", "Juan", "Elena",
    "David", "Sofía", "Antonio", "Carmen", "Marta", "Raúl", "Patricia", "Javier", "Beatriz", "Alberto"
]

serie = pd.Series(profesiones, index=nombres)

print(serie)

print(serie.sample(2))