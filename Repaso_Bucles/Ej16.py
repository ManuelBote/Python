# Dado un diccionario con valores numéricos, escribe un programa que cuente cuántos valores son mayores que un número dado.

def mayores(diccionario, num):
    cont = 0
    for i in diccionario:
        if diccionario[i] > num:
            cont +=1
    return cont

diccionario = {'a': 10, 'b': 12, 'c': 3, 'd': 20, 'e': 25}
num = int(input("Escribe un numero: "))

print("En el diccionario hay", mayores(diccionario, num), "valores mayores a", num)
