# Modifica la clase Animal para que cada subclase (Perro, Gato) tenga un
# método hacer_sonido que imprima un sonido diferente según el tipo de
# animal. Llama al método en un objeto de cada clase.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def descripcion(self):
        print("Nombre del animal: " + self.nombre)

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")


p1 = Perro(input("Nombre del perro: "))
p1.descripcion()
p1.hacer_sonido()

g1 = Gato(input("Nombre del gato: "))
g1.descripcion()
g1.hacer_sonido()