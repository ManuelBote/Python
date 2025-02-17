# Escribe un programa que reciba una calificación (número) y determine si la
# calificación es aprobada (superior o igual a 5) o suspensa

calificacion = int(input("Ingrese la calificación: "))

if calificacion >= 5:
    print("Aprobado")
else:
    print("Suspenso")