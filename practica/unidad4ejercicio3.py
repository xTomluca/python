print("Ingrese numero :")
numero = int(input())
lista_dec = [numero]
lista_asc = [0]
desc = ""
asc = ""


def descendente(numero):
    global desc
    while numero > 0:
        lista_dec.append(numero-1)
        numero -= 1

    for x in lista_dec:
        if x != 0:
            desc += ("{0}, ".format(str(x)))
        else:
            desc += ("{0}".format(str(x)))


def ascendente(numero):
    global asc
    sumador = 1
    while numero >= sumador:
        lista_asc.append(sumador)
        sumador += 1

    for x in lista_asc:
        if x != numero:
            asc += ("{0}, ".format(str(x)))
        else:
            asc += ("{0}".format(str(x)))


descendente(numero)
ascendente(numero)
print("Lista descendente:")
print(desc, end="\n\n")
print("Lista ascendente:")
print(asc, end="\n\n")
