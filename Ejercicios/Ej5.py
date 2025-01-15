# Generar la tabla de multiplicar de un número. Escribe una función que genere la tabla de multiplicar de un número (por ejemplo, tabla del 3)

def tabla(num):
    tabla = []
    for i in range(1,11):
        tabla.append(str(num)+"*"+str(i)+"="+str(num*i))    
    return tabla

num = int(input("Introduce un numero: "))
tabla = tabla(num)

for i in tabla:
    print(i)
 