# Dado un diccionario con valores numéricos, escribe un programa que sume todos los valores.

def suma(diccionario):
    suma = 0
    for i in diccionario:
        suma += diccionario[i]
    return suma

diccionario = {'a': 10, 'b': 12, 'c': 3, 'd': 20, 'e': 25}

print("La suma de los numeros es:", suma(diccionario))