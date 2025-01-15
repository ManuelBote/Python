# Diseña una funcion que calcule el area y el perimetro de una circunferencia.
# Utiliza dicha funcion en un programa principal que lea el radio de una circunferencia y muestre su area y perimetro.

import math

def circulo(radio):
    area = math.pi * (radio**2)
    perimetro = 2 * math.pi * radio
    print("La area es: %.2f" % area)
    print("El perimetro es: %.2f" % perimetro)

radio = float(input("Ingrese el radio de la circunferencia: "))
circulo(radio)