# Escribe un programa que determine si un año dado es bisiesto. Un año es
# bisiesto si es divisible entre 4, pero no entre 100, a menos que también sea
# divisible entre 400.

año = int(input("Ingrese el año: "))

if año % 4 == 0 and año % 100 != 0 or año % 100 == 0 and año % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")