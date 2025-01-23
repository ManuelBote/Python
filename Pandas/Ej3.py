# Crea una serie a partir de un diccionario de Python y empleando el paquete Pandas. 
# La serie debe contener los números de alumnos asociados a 20 asignaturas de ESO o FP. 
# Muestra la serie completa por pantalla y, después, el número de alumnos en la asignatura de Tecnología y en la asignatura de Biología. 
# Realiza los cambios necesarios para que otra serie creada a partir del diccionario contenga sólo las 10 primeras asignaturas. 
# Muestra esta última serie por pantalla.

import pandas as pd

asignaturas = {
    "Matemáticas": 30,
    "Lengua": 28,
    "Ciencias Sociales": 25,
    "Inglés": 35,
    "Física": 22,
    "Química": 20,
    "Tecnología": 18,
    "Biología": 24,
    "Geografía": 27,
    "Historia": 29,
    "Educación Física": 40,
    "Informática": 30,
    "Música": 18,
    "Plástica": 25,
    "Religión": 15,
    "Tutores": 30,
    "Economía": 20,
    "Educación Cívica": 22,
    "Álgebra": 33,
    "Programación": 19
}

serie = pd.Series(asignaturas)

print(serie)

print(serie[["Tecnología", "Biología"]])

print(serie.head(10))
