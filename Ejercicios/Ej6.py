# Verificar si un número es par o impar. Implementa una función que reciba un número y determine si es par o impar.

def verificar(num):
    if num % 2 == 0:
        return "El numero",num,"es par"
    else:
        return "El numero",num,"es impar"

num = int(input("Introduce un numero: "))
print(verificar(num)) 