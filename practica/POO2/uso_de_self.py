class Persona(object):
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        print(self.nombre)

    def datos(self, salario):
        print(
            "Nombre de la persona: "
            + self.nombre
            + "\n"
            + "Salario en $: "
            + str(salario)
        )


objeto = Persona("Juan", 39, "Masculino")
objeto.datos(100)
