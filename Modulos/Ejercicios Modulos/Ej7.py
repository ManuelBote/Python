# Crea un array formado por 20 números comprendidos entre el 140 y el 190.
# Muestra por pantalla del primer al octavo elemento y, por otro lado, del
# elemento 14 al 19. Crea otro array formado por 40 elementos comprendidos
# entre el 140 y el 180. Muestra por pantalla desde el último elemento hasta el
# antepenúltimo y, por otro lado, los 20 primeros elementos de 2 en 2. Crea un
# array bidimensional con 15 números del 200 al 250. Muestra por pantalla de
# cada subarray los 3 primeros elementos y del último subarray los 2 primeros
# elementos.

import numpy as np

num = np.array([])

for i in range(20):
    num = np.append(num, np.random.randint(140, 190))

print(num)
print("Primeros 8 elementos: ", num[0:8])
print("Elementos del 14 al 19: ", num[14:19])

print("==============================================")
num2 = np.array([140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180])

print(num2)
print("Ultimos 3 elementos: ", num2[-1:-4:-1])
print("Primeros 20 elementos de 2 en 2: ", num2[0:20:2])

print("==============================================")

num3 = np.array([[201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215],
                 [216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]])
print(num3)
print("Primeros 3 elementos de cada subarray:",num3[0:3, 0:3])
print("Ultimos elementos del subarray2: ", num3[-1:, -2:])



