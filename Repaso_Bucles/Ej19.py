# Dada una lista de números, escribe un programa que elimine los números negativos.

def eliminar_negativos(lista):
    lista2 = []
    for i in lista:
        if i >= 0:
            lista2.append(i)
    return lista2

lista = [-1, 0, 12, -20, -4, 43, 7, -9]

print(eliminar_negativos(lista))
