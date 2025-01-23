#Dado un diccionario con valores numéricos, escribe un programa que devuelva el valor más pequeño.

def minimo(diccionario):
    min = list(diccionario.values())[0]
    for i in diccionario:
        if diccionario[i] < min:
            min = diccionario[i]
    return min

diccionario = {'a': 10, 'b': 12, 'c': 3, 'd': 20, 'e': 25}

print("El valor minimo es:", minimo(diccionario))