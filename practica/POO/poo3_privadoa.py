class AccesoPrivado(object):
    def __privado(self):
        print("Mensaje Privado")

    def getPrivado(self):
        self.__privado()


objeto = AccesoPrivado()
objeto._AccesoPrivado__privado()
objeto.getPrivado()
