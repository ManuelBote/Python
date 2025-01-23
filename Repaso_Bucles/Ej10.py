# Dada una lista de números, escribe un programa que cree una nueva lista con los cuadrados de esos números

def cuadrados(lista):
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    return lista2

lista = [2, 1, 20, 31, 4, 11, 15, 22, 3, 10, 5, 6]

print(cuadrados(lista))