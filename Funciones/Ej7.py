# realiza un programa que pregunte aleatoriamente una multiplicacion. El programa debe indicar si la respuesta a sido correcta o no 
# (en caso de que la respuesta sea incorrecta el programa debe indicar cual es la correcta). 
# El programa preguntara 10 multiplicacion y al finalizar mostrara el numero de aciertos

import random

cont = 0

for i in range (10):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)

    print("Cuanto es",n1,"x",n2,": ", end="")
    resultado = int(input())

    if resultado == n1*n2:
        print("Correcto")
        cont += 1
    else:
        print("Incorrecto, el resultado es",(n1*n2))
    print("=======================================")

print("El numero de aciertos es:",cont)

