# Crea una clase base Animal con el atributo nombre y un método descripción que imprima una descripción del animal.
# Crea una subclase Gato que herede de Animal y añada un método maullar.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def descripcion(self):
        print("Nombre del animal: " + self.nombre)

class Gato(Animal):
    def maullar(self):
        print("Gato maullando")

g1 = Gato(input("Nombre del gato: "))
g1.descripcion()
g1.maullar()    