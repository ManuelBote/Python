# Escribe un programa que compare dos números y determine si son iguales,
# el primero es mayor o el segundo es mayor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número es mayor")
elif num1 < num2:
    print("El segundo número es mayor")
else:
    print("Los números son iguales")