# Crea un array de 1 dimensión que contenga los 10 primeros números
# múltiplos de 3. Seguidamente, aplica un filtro con un array booleano de
# manera que obtengas un array con los números 3, 15 y 30, mostrándolo por
# pantalla. Crea otro array de 1 dimensión que contenga los 50 primeros
# números. A continuación, aplica un filtro de modo que obtengas un array
# formado por los números múltiplos de 6 entre el 0 y el 50

import numpy as np

num = np.arange(3, 31, 3)

filtro = (num == 3) | (num == 15) | (num == 30)
print(num[filtro])

num50 = np.arange(51)
filtro2 = num50 % 6 == 0
print(num50[filtro2])