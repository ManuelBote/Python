# Realiza un programa que recoja por teclado la cantidad total a pagar y la cantidad que se a entregado. La aplicacion debe calcular
# El cambio correspondiente con el menor numero de monedas o billetes posibles

cambios = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

def devolver(total, pagado, cambios):
    if total > pagado:
       return "No se ha entregado la cantidad requerida"
    elif total == pagado:
        return "Se ha entregado la cantidad justa, por lo que no hay cambio"
    else:
        resto = pagado - total
        devolucion = []
        for i in cambios:
            while resto != 0:
                if resto >= i:
                    resto = resto - i
                    devolucion.append(i)
                else:
                    break
        return devolucion
    

total = float(input("Indique el total a pagar: "))
pagado = float(input("Indica el dinero entregado: "))

devolucion = devolver(total, pagado, cambios)

print(devolucion)
    