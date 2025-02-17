# Escribe un programa que reciba un número del 1 al 7 y determine qué día de
# la semana corresponde (lunes, martes, etc.).

dia = int(input("Ingrese el número del día: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("El número no es correcto")