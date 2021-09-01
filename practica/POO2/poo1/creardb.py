if __name__ == "__main__":
    from personap.personam import Persona
    from gerentep.gerentem import Gerente

    juan = Persona("Jugan Garcia", 42)
    susana = Persona("Susana Gomez", 45, 40000)
    tom = Gerente("Tom Perez", 50, 50000)
    db = [juan, susana, tom]

    for persona in db:
        print(persona.nombre, persona.sueldo)
    print("------------------")

    for objeto in db:
        objeto.dar_aumento(0.10)
    for objeto in db:
        print(objeto.nombre, "->", objeto.sueldo)
    print("------------------")
    for objeto in db:
        print(objeto.apellido(), "->", objeto.sueldo)
    print("------------------")

    print("---------__str__--------")
    print(juan)
    print(susana)
    print(tom)
    print("------------------")
    """
    personas = [juan, susana]
    for persona in personas:
        print(persona.nombre, persona.sueldo)
    print("----------------")

    #########################
    ##### POR COMPRENSION
    ############################

    x = [(persona.nombre, persona.sueldo) for persona in personas]
    print(x)
    print("--------------")

    y = [
        (persona.edad ** 2 if persona.edad >= 7 else persona.edad)
        for persona in personas
    ]
    print(y)
    """
