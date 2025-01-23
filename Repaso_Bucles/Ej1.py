# Dada una lista de números, escribe un programa que calcule la suma de todos los elementos.

def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

lista = [20, 40, 15, 3, 10]

print(suma(lista))