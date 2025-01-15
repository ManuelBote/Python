# Crea una clase Estudiante con los atributos nombre, edad y nota_media. Añade un método que imprima si el estudiante 
# ha aprobado o suspendido según su nota_media.

class Estudiante:
    def __init__(self, nombre, edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media
        
    def aprobar(self):
        if self.nota_media >= 5.0:
            print(self.nombre + " ha aprobado")
        else:
            print(self.nombre + " ha suspendido")

e1 = Estudiante(input("Nombre del estudiante: "), int(input("Edad: ")), float(input("Nota media: ")))
e1.aprobar()