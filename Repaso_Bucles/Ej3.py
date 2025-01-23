# Dada una lista de números, escribe un programa que devuelva el número más grande.

def mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

lista = [20, 40, 15, 3, 10]

print("El numero mayor de la lista es", mayor(lista))