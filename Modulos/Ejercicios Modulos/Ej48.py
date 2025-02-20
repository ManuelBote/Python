# Crea un array que contenga las aficiones/hobbies de 20 personas (fruto de
# otra encuesta). Al preguntar a otras 20 personas más, se ha obtenido otro
# array de 20 elementos. Elabora, a partir de los dos arrays anteriores, un
# conjunto formado por las aficiones de la primera encuesta que no están
# presentes en las respuestas de las 20 últimas personas

import numpy as np

aficiones1 = np.array(['leer', 'viajar', 'deporte', 'cine', 'música', 'arte', 'teatro', 'naturaleza', 'fotografía', 'videojuegos',
                                'pintura', 'senderismo', 'cocina', 'jardinería', 'escribir', 'música', 'bailar', 'escuchar música', 'ciclismo', 'pesca'])

aficiones2 = np.array(['cocina', 'deporte', 'música', 'viajar', 'arte', 'senderismo', 'cine', 'videojuegos', 'bailar', 'teatro',
                                'lectura', 'ciclismo', 'escuchar música', 'fotografía', 'escribir', 'pintura', 'pesca', 'jardinería', 'bailar', 'naturaleza'])

aficiones_unicas = np.setdiff1d(aficiones1, aficiones2)

print(aficiones_unicas)