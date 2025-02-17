# Crea una clase Figura con un método area que calcule el área. Luego, crea
# las subclases Círculo y Rectángulo que sobrescriban el método area para
# calcular el área según la fórmula correspondiente.

class Figura:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, lado):
        super().__init__(lado)
    
    def area(self):
        return 3.14 * ((self.lado/2) ** 2)

class Rectángulo(Figura):
    def __init__(self, lado, alto):
        super().__init__(lado)
        self.alto = alto
    
    def area(self):
        return self.lado * self.alto


c1 = Circulo(5)
r1 = Rectángulo(5, 10)

print("Área del círculo:", c1.area())
print("Área del rectángulo:", r1.area())    