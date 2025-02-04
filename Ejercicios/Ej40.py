# Crear un programa que calcule la suma de los números de una matriz (2D).
# Crea una función que reciba una matriz de números (lista de listas) y devuelva la
# suma de todos sus elementos

import random

def suma(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
    return suma

matriz = []
for i in range (5):
    matriz.append([])
    for j in range (5):
        matriz[i].append(random.randint(1, 10))

print(matriz)
print("La suma de los elementos de la matriz es:", suma(matriz))