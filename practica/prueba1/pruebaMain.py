# import prueba1


def recorrerLista(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrerLista(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)


lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]
recorrerLista(lista)

# prueba1.recorrerLista(lista)
