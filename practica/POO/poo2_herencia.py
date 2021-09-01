class ClasePadre1:
    atributo1 = 2
    # nombre = "SINNOMBRE"


class ClasePadre2:
    atributo2 = 3


class ClaseHija(ClasePadre1, ClasePadre2):  # HERENCIA
    atributo3 = 4

    def imprimir(self, nombre):
        self.nombre = nombre
        print(self.nombre)


objeto = ClaseHija()
print(objeto.atributo1)
print(objeto.atributo2)
print(objeto.atributo3)
objeto.imprimir("PEDRO")
objeto.atributo3 = 0
print(objeto.atributo3)
