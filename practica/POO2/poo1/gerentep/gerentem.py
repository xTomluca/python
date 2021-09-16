from personap.personam import Persona


class Gerente(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad, sueldo, "Gerente")

    def dar_aumento(self, porcentaje, premio=0.1):
        self.sueldo *= 1.0 + porcentaje + premio

    def __str__(self):
        return "%s, %s" % (Persona.__str__(self), self.trabajo)


if __name__ == "__main__":
    Tom = Gerente("Tom Perez", 42, 50000, "Software")
    print(Tom.nombre)
    Tom.dar_aumento(0.10, 0.40)
    print(Tom.sueldo)
