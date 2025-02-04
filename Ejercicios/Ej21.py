# Convertir un número binario a decimal.
# Escribe una función que convierta un número binario en su equivalente decimal

def binario(num):
    dec = 0
    for i in range(len(num)):
        dec += int(num[i]) * (2 ** (len(num) - i - 1))
    return dec

num = input("Escribe el número binario: ")
dec = binario(num)
print("El número decimal es:", dec)