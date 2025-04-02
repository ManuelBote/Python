#  Crea un diccionario con el nombre de las ciudades como claves y las
# temperaturas de cada ciudad como valores. Pide al usuario ingresar una
# ciudad y muestra su temperatura.

diccionario = {}

while True:
    nombre = input("Ingrese el nombre de una ciudad: ")
    if nombre == "-1":
        break
    temperatura = float(input("Ingrese la temperatura de la ciudad: "))
    diccionario[nombre] = temperatura

nombre = input("Ingrese la ciudad a buscar: ")
print("La temperatura de la ciudad", nombre, "es:", diccionario[nombre])