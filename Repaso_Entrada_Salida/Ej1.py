# Pide al usuario ingresar las notas de los estudiantes en una lista. Calcula el
# promedio de las notas e imprime el resultado.

lista = []

while True:
    nota = int(input("Ingrese una nota o ingrese -1 para terminar: "))
    if nota == -1:
        break
    lista.append(nota)

promedio = sum(lista) / len(lista)
print("El promedio es:", promedio)