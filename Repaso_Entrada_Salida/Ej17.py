# Pide al usuario ingresar los nombres de varias asignaturas y las notas
# correspondientes a cada una. Luego, calcula y muestra el promedio de las
# notas

diccionario = {}

while True:
    nombre = input("Ingrese el nombre de una asignatura: ")
    if nombre == "-1":
        break
    nota = float(input("Ingrese la nota de la asignatura: "))
    diccionario[nombre] = nota

lista = []

for i in diccionario:
    lista.append(diccionario[i])

promedio = sum(lista) / len(lista)
print("El promedio de las notas es:", promedio)