# Escribe un programa que lea tres números y determine cuál es el mayor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El mayor numero es:", num1)
elif num2 > num1 and num2 > num3:
    print("El mayor numero es:", num2)
elif num3 > num1 and num3 > num2:
    print("El mayor numero es:", num3)
else:
    print("Los números son iguales")
