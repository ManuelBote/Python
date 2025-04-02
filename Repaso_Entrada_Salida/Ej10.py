# Pide al usuario ingresar los nombres y salarios de varios empleados en un
# diccionario. Luego, muestra el nombre del empleado con el salario más alto

diccionario = {}

while True:
    nombre = input("Ingrese el nombre del empleado: ")
    if nombre == "-1":
        break
    salario = float(input("Ingrese el salario del empleado: "))
    diccionario[nombre] = salario

print("El empleado con el salario más alto es:", max(diccionario, key=diccionario.get))