# Crear un programa que muestre los primeros N cuadrados perfectos.
# Escribe una función que imprima los primeros N números que son cuadrados
# perfectos

import math

def cuadrados(num):
    for i in range(1, num + 1):
        if math.sqrt(i).is_integer():
            print(i, end=" ")

num = int(input("Escribe el número de cuadrados: "))
cuadrados(num)