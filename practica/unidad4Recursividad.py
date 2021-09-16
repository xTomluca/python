lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]
# imprimimos la lista


def recorrer_lista(item):
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x)
        else:
            print("Entro al else ", x)


recorrer_lista(lista)

print("--------------------------")


def recorrer_lista_nueva(item, nivel):
    for x in item:
        if isinstance(x, list):
            recorrer_lista_nueva(x, nivel + 1)
        else:
            for y in range(nivel):
                print((""))
            print(x)


recorrer_lista_nueva(lista, 0)


print("------------------------------->>>")


def recorrer_lista_nueva_2(item, nivel=0):
    for x in item:
        if isinstance(x, list):
            recorrer_lista_nueva_2(x, nivel + 1)
        else:
            for y in range(nivel):
                print("\t", end="")
            print(x)


recorrer_lista_nueva_2(lista)


def contador_yield1(max):
    n = 0
    while n < max:
        yield n
        n += 1

d = contador_yield1(8)


print(d)
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))
print('', end="\n################\n")
print(next(d))

ingreso = 0

def nuevo_ingreso():
    global ingreso
    ingreso += 1
    print("Se ha realizado un nuevo ingreso",ingreso)

nuevo_ingreso()
nuevo_ingreso()
nuevo_ingreso()
print(ingreso)

# ANIDAMIENTO Y NIVELES - GLOBAL VS NONLOCAL

nivel0 = 0


def f1():
    nivel1 = 1

    def f2():
        nivel2 = 2
        print(nivel0, nivel1, nivel2)

    f2()
    print(nivel0, nivel1)


f1()
print(nivel0)
print("\n\n----------------------")

nivel0 = 0

# USO NONLOCAL PARA ASIGNAR VALOR A UNA VARIABLE LOCAL ANIDADA
def f11():
    nivel1 = 1

    def f2():
        nonlocal nivel1 
        nivel1 = 16
        nivel2 = 2
        print(nivel0, nivel1, nivel2)

    f2()
    print(nivel0, nivel1)


f11()
print(nivel0)

