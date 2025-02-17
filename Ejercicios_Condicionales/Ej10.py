# Escribe un programa que lea dos números y un operador (+, -, *, /) y realice la
# operación correspondiente.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador: ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2

print("El resultado es:", resultado)