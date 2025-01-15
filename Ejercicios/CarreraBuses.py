import random
import time
import os

# Definir los autobuses usando cadenas de símbolos
bus1 = [
    "   ____",
    " /|_||_\\`.__",
    "(   _pito_ _\\",
    "=`-(_)--(_)-'"
]
bus2 = [
    "   ____",
    " /|_||_\\`.__",
    "(   _puta_ _\\",
    "=`-(_)--(_)-'"
]

# Definir la línea de meta
finish_line = 100

# Posiciones iniciales de los autobuses
pos_bus1 = 0
pos_bus2 = 0

# Función para imprimir la carrera
def imprimir_carrera(pos1, pos2):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    print("Línea de salida")
    print("-" * finish_line)
    for linea in bus1:
        print(" " * pos1 + linea)
    print()
    for linea in bus2:
        print(" " * pos2 + linea)
    print("-" * finish_line)
    print("Línea de meta")

# Carrera
while pos_bus1 < finish_line and pos_bus2 < finish_line:
    time.sleep(0.5)  # Pausa de medio segundo para animación
    pos_bus1 += random.randint(1, 3)  # Avance aleatorio entre 1 y 3 posiciones
    pos_bus2 += random.randint(1, 3)
    imprimir_carrera(pos_bus1, pos_bus2)

# Determinar el ganador
if pos_bus1 >= finish_line and pos_bus2 >= finish_line:
    print("¡Es un empate!")
elif pos_bus1 >= finish_line:
    print("¡El autobús 1 gana!")
else:
    print("¡El autobús 2 gana!")
