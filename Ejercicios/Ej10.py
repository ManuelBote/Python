# Invertir una cadena de texto. Implementa una función que reciba una cadena y devuelva la misma cadena pero invertida.

def invertir(cadena):
    for i in range(len(cadena)):
        print(cadena[len(cadena)-i-1],end="")

cadena = input("Ingrese una cadena: ")
invertir(cadena)    