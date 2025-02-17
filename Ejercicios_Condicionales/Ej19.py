# Escribe un programa que reciba tres longitudes de lados y determine si es un
# triángulo válido (la suma de dos lados debe ser mayor que el tercer lado)

lado1 = float(input("Ingrese el largo de lado 1: "))
lado2 = float(input("Ingrese el largo de lado 2: "))
lado3 = float(input("Ingrese el largo de lado 3: "))

if lado1 + lado2 > lado3:
    print("El triángulo es válido")
else:
    print("El triángulo no es válido")