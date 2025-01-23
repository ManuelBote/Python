# Verificar si un número es perfecto.
# Implementa una función que determine si un número es perfecto (la suma de sus divisores propios es igual al número)

def perfecto(num):
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i
    if total == num:
        return True
    else:
        return False

num = int(input("Escribe un numero: "))

if perfecto(num):
    print("El número", num, "es perfecto")
else:
    print("El número", num, "no es perfecto")