# Pide al usuario que ingrese las edades de varios niños (en formato de tupla) y
# calcula la edad promedio.


def calcular_edad_promedio(edades):
    if len(edades) == 0:
        return 0
    return sum(edades) / len(edades)

edades_input = input("Ingresa las edades separadas por coma: ")
edades = tuple(map(int, edades_input.split(',')))

edad_promedio = calcular_edad_promedio(edades)
print(f"La edad promedio de los niños es: {edad_promedio}")
