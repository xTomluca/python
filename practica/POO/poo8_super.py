class Vehiculo(object):
    def tipo(self):
        print("Dos ruedas")


class Material(object):
    def tipo(self):
        print("Plastico")


class Moto(Vehiculo, Material):
    def modelo(self):
        print("Modelo 1")
        super(Moto, self).tipo()
        super().tipo()
        Material.tipo(self)
        Vehiculo.tipo(self)


class Bicicleta(
    Material, Vehiculo
):  # Lee superclase de izq a derecha utilizando metodos de la primera en caso de estar repetidos
    def modelo(self):
        print("Modelo 2")
        super(
            Bicicleta, self
        ).tipo()  # Utiliza el metodo de clase madre - Herencia multiple, el primero de la izq
        super().tipo()
        Material.tipo(self)
        Vehiculo.tipo(self)


print("----PRIORIDAD DE CLASES---------")
print(Moto.__mro__)
print(Bicicleta.__mro__)
print("-------Para objeto 1----------")
objeto1 = Moto()
objeto1.modelo()
objeto1.tipo()
print("----------Para objeto 2-------")
objeto2 = Bicicleta()
objeto2.modelo()
objeto2.tipo()  # Accede a la primera clase madre de izq a derecha q tenga este metodo
