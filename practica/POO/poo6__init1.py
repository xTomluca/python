class Comentario:
    def imprimir(self):
        print(self.texto)


objeto = Comentario()
objeto.texto = "Esto es una variable de instancia"
objeto.imprimir()
