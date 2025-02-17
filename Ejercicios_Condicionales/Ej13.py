# Escribe un programa que reciba una calificación numérica (de 0 a 10) y
# determine la calificación textual (por ejemplo, "A", "B", "C", "D", "F").

calificacion = int(input("Ingrese la calificación: "))

if calificacion >= 0 and calificacion <= 10:
    if calificacion >= 0 and calificacion <= 3:
        calificacion = "D"
    elif calificacion >= 4 and calificacion <= 6:
        calificacion = "C"
    elif calificacion >= 7 and calificacion <= 9:
        calificacion = "B"
    else:
        calificacion = "A"
elif calificacion >= 10:
    calificacion = "F"

print("La calificación es:", calificacion)