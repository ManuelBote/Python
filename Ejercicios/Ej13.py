# Contar cuántas veces aparece una subcadena en una cadena. Implementa una función que cuente las veces que una subcadena aparece dentrode una caden

def contar(cadena,subcadena):
    cont = 0
    for i in range(len(cadena)):
        if cadena.find(subcadena,i, i+len(subcadena)) != -1:
            cont += 1
    return cont

cadena = input("Ingrese una cadena: ")
subcadena = input("Ingrese una subcadena: ")
print(contar(cadena,subcadena))