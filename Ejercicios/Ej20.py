# Generar un número aleatorio entre un rango dado.
# Crea una función que genere un número aleatorio entre un mínimo y un máximo dados.

import random

def numero(min, max):
    num = random.randint(min, max)
    return num

min = int(input("Escribe el mínimo: "))
max = int(input("Escribe el máximo: "))

num = numero(min, max)
print("El número aleatorio es:", num)