def ordenar(num1, num2):
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1
    
def calcularMCD(num1, num2):
    n1, n2 = ordenar(num1, num2)
    resto = n1%n2
    if resto == 0:
        return n2
    else:
        return calcularMCD(n2, resto)


num1 = int(input("Di un numero: "))
num2 = int(input("Di otro numero: "))

maxcd = calcularMCD(num1, num2)
print("El maximo comun divisor es:",maxcd)