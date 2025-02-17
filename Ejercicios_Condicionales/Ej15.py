# Escribe un programa que determine si un número es múltiplo de 3 o 5

num = int(input("Ingrese un número: "))

if num % 3 == 0 or num % 5 == 0:
    print("El número es múltiplo de 3 o 5")
else:    
    print("El número no es múltiplo de 3 o 5")