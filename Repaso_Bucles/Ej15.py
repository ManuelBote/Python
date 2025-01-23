# Escribe un programa que sume los números del 1 al n usando un bucle while.

num = int(input("Escribe el numero hasta donde desea contar: "))

cont = 1
while True:
    print(cont)
    if cont == num:
        break
    else:
        cont += 1