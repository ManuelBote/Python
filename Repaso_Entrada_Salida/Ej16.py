# Recibe una lista de nombres y muestra solo aquellos cuyo nombre tenga más
# de 5 caracteres

lista = []

while True:
    nombre = input("Ingrese un nombre: ")
    if nombre == "-1":
        break
    else:
        lista.append(nombre)

for i in lista:
    if len(i) >= 5:
        print(i)