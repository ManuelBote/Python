from cuentaBancaria import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        return "Cuenta Joven \n " + "Titular: " + self.titular.mostrar() + " - Cantidad: " + str(self.cantidad) + " - Bonificacion: " + str(self.bonificacion)
    
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self, cantidad):
        if not self.esTitularValido():
            print("No puedes retirar el dinero. Titular no valido")
        elif cantidad > 0:
            super().retirar(cantidad)