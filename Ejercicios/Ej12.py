# Suma de dígitos de un número. Escribe una función que reciba un número y devuelva la suma de sus dígitos

def suma(num):
    suma = 0
    for i in range(len(str(num))):
        suma += int(str(num)[i])
    return suma

num = int(input("Ingrese un número: "))
print(suma(num))