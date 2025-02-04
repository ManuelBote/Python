# Imprimir una tabla de multiplicar con números del 1 al 10.
# Crea una función que imprima una tabla de multiplicar para los números del 1 al 10

def tabla():
    for i in range(1, 11):
        print("Tabla del", i)
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)
        print()

tabla()

