# Crear un programa que calcule el promedio de una lista de números.
# Escribe una función que calcule el promedio de los números en una lista.

import random

def promedio(lista):
    total = 0
    for i in lista:
        total += i
    return total / len(lista)

lista = []
for i in range (10):
    lista.append(random.randint(1, 100))
print(lista)
print("El promedio es:", promedio(lista))