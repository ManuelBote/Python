from Persona import *


class Cuenta:
    def __init__(self, Persona, dinero):
        self.Persona = Persona
        self._dinero = dinero

    @property
    def Persona(self):
        return self._Persona

    @Persona.setter
    def Persona(self, value):
        self._Persona = value

    @property
    def dinero(self):
        return self.dinero

    @dinero.setter
    def apellido(self, value):
        self._apellido = value

    def mostrar(self):
        return (
            "Cuenta \n"
            + "Titular:"
            + self.Persona.mostrar()
            + "\n"
            + "Dinero:"
            + str(self.dinero)
        )

    def ingresar(self, dinero):
        if dinero > 0:
            self._dinero = self._dinero + dinero
            return self.dinero

    def sacar(self, dinero):
        if dinero > 0:
            self._dinero = self._dinero - dinero
            return self.dinero
