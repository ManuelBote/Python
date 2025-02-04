# Contar la frecuencia de cada letra en una cadena de texto.
# Implementa una función que devuelva un diccionario con la frecuencia de aparición
# de cada letra en una cadena.

def contar(cadena):
    diccionario = {}
    for i in cadena:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario

cadena = input("Escribe la cadena de texto: ")
print(contar(cadena))