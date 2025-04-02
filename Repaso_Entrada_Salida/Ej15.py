# Pide al usuario un nombre y una nueva edad. Si el nombre está en el
# diccionario de personas, actualiza la edad, de lo contrario, agrega el nombre
# con la edad.

diccionario = {}

while True:
    nombre = input("Ingrese un nombre: ")
    if nombre == "-1":
        break
    edad = int(input("Ingrese la edad: "))
    diccionario[nombre] = edad

print(diccionario)