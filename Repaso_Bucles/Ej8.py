# Dada una lista de números, escribe un programa que imprima todos los números impares.

def impares(lista):
    lista2 = []
    for i in lista:
        if i % 2 != 0:
            lista2.append(i)
    return lista2

lista = [2, 1, 20, 31, 4, 11, 15, 22, 3, 10, 5, 6]

print(impares(lista))