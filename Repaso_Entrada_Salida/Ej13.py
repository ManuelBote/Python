# Pide al usuario ingresar las edades de varias personas y clasifícalas en tres
# categorías: menores de 18, de 18 a 40, y mayores de 40. Usa un diccionario
# para contar cuántas personas hay en cada categoría.

diccionario = {"Menores de 18": 0, "De 18 a 40": 0, "Mayores de 40": 0}

while True:
    edad = int(input("Ingrese la edad de una persona: "))
    if edad == -1:
        break
    else:
        if edad < 18:
            diccionario["Menores de 18"] += 1
        elif edad <= 40:
            diccionario["De 18 a 40"] += 1
        else:
            diccionario["Mayores de 40"] += 1

for i in diccionario:
    print(i, ":", diccionario[i])
