# Verificar si un número es primo. Crea una función que reciba un número y devuelva si es primo o no

def primo(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

num = int(input("Introduce un numero: "))
if primo(num):
    print("El numero",num,"es primo")
else:
    print("El numero",num,"no es primo")