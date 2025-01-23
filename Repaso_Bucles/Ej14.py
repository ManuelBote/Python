# Dada una lista de claves y una lista de valores, escribe un programa que cree un diccionario usando los elementos de ambas listas.

def crear_dic(clave, valor):
    diccionario = {}
    for i in range(len(clave)):
        diccionario[clave[i]] = valor[i]
    return diccionario

clave = ["a", "b", "c", "d", "e"]
valor = [1, 2, 3, 4, 5]

print(crear_dic(clave, valor))