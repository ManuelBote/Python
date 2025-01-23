# Dada una lista de números y un valor x, escribe un programa que cree una nueva lista con los números menores a x.

def menores(lista, num):
    lista2= []
    for i in lista:
        if i < num:
            lista2.append(i)
    return lista2

lista = [2, 1, 20, 31, 4, 11, 15, 22, 3, 10, 5, 6]
num = int(input("Escribe un numero: "))

print(menores(lista, num))