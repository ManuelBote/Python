# Dada una lista con elementos duplicados, escribe un programa que elimine los duplicados sin usar el método set().

def eliminar_duplicados(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2


lista = [10, 10, 3, 23, 43, 23, 10, 5, 2, 20, 50, 3]

print(lista)
print(eliminar_duplicados(lista))
