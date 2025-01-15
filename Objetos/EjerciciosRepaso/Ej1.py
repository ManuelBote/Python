#Crea una clase llamada Perro con los atributos nombre y edad. Define un método que imprima un saludo con el nombre del perro

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola " + self.nombre)


p1 = Perro(input("Nombre: "), int(input("Edad: ")))
p1.saludar()