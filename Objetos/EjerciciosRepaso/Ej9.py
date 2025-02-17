# Crea una clase Empleado con un método calcular_bonus que calcule el bono
# anual de un empleado. Luego, crea una subclase Vendedor que modifique el
# método para calcular el bono según las ventas realizadas.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_bonus(self):
        return self.salario * 0.1

class Vendedor(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas
    
    def calcular_bonus(self):
        bono_basico = super().calcular_bonus()
        bono_ventas = self.ventas * 0.05
        return bono_basico + bono_ventas


empleado = Empleado("Juan", 50000)
vendedor = Vendedor("Ana", 50000, 100000)

print("Bono de", empleado.nombre, ":", empleado.calcular_bonus())
print("Bono de", vendedor.nombre, ":", vendedor.calcular_bonus())