# Verificar si un número es un número Armstrong.
# Crea una función que verifique si un número es un número Armstrong (por ejemplo, 153).

def es_armstrong(num):
    suma = 0
    for i in range(len(str(num))):
        suma += int(str(num)[i]) ** len(str(num))
    if suma == num:
        return True
    else:
        return False
    
num = int(input("Escribe un número: "))
if es_armstrong(num):
    print("El número", num, "es un número Armstrong")
else:
    print("El número", num, "no es un número Armstrong")    
