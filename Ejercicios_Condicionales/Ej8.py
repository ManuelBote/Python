# Escribe un programa que clasifique a una persona en una categoría según su
# edad: niño (0-12), adolescente (13-17), adulto (18-64), o adulto mayor (65+).

edad = int(input("Ingrese la edad: "))

if edad <=12:
    print("Niño")
elif edad >= 13 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 65:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")