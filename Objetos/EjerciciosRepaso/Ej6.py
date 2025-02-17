# Crea una clase Empleado con atributos nombre, puesto y salario. Luego, crea
# una subclase Gerente que añada un atributo departamento y un método
# informar.

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, puesto, salario, departamento):
        super().__init__(nombre, puesto, salario)
        self.departamento = departamento

    def informar(self):
        print("Nombre: " + self.nombre)
        print("Puesto: " + self.puesto)
        print("Salario: " + str(self.salario))
        print("Departamento: " + self.departamento)

g1 = Gerente("Juan", "Director", 10000, "Finanzas")
g1.informar()