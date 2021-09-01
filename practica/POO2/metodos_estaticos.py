# No es posible acceder desde ellos a una variable de instancia


class Persona(object):
    @staticmethod
    def imprimir(parametro1):
        print(parametro1)


objeto = Persona()
objeto.imprimir("Valor del parametro 1")
