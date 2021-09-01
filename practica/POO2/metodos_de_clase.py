# Pueden ser invocados sin necesitar la instancia de un obj previa
# NombreDeClase.metodo


class Persona(object):
    @classmethod
    def imprimir(cls, parametro1):
        print(parametro1)


Persona.imprimir("Este es el parametro 1")
