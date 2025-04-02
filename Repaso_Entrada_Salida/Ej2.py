# Crea un programa que reciba una lista de palabras e indique cuántas veces
# aparece una palabra específica (ingresada por el usuario)

var = input("Ingrese un texto: ")

lista = var.split()

palabra = input("Ingrese la palabra a buscar: ")

cont = 0
for i in lista:
    if i == palabra and cont == 0:
        print(palabra, "aparece", lista.count(palabra), "veces")
        cont+=1