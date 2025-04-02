# Pide al usuario ingresar las coordenadas X e Y de varios puntos. Crea una
# tupla con esos valores y luego calcula la distancia entre los puntos.

def calcular_distancia(coordenadas):
    distancia = 0
    for i in range(len(coordenadas)):
        distancia += abs(coordenadas[i][0] - coordenadas[i+1][0]) + abs(coordenadas[i][1] - coordenadas[i+1][1])
    return distancia

coordenadas = []

while True:
    coordenada = input("Ingrese las coordenadas separadas por espacio: ")
    if coordenada == "-1":
        break
    coordenadas.append(tuple(map(int, coordenada.split())))

distancia = calcular_distancia(coordenadas)     