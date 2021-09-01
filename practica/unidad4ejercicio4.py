print("\nIngrese texto para contar sus vocales:\n")
palabra = input()
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
letras_contenidas = ""

for letra in palabra:
    if letra == "a" or letra == "A":
        contador_a += 1
    elif letra == "e" or letra == "E":
        contador_e += 1
    elif letra == "i" or letra == "I":
        contador_i += 1
    elif letra == "o" or letra == "O":
        contador_o += 1
    elif letra == "u" or letra == "U":
        contador_u += 1

if (contador_a != 0 or contador_e != 0 or contador_i != 0 or contador_o != 0 
or contador_u != 0):
    letras_contenidas += "El texto {0} ingresado contiene ".format(palabra)
    if contador_a > 1:
        letras_contenidas += "{0} vocales: A ".format(contador_a)
    elif contador_a == 1:
        letras_contenidas += "{0} vocal: A ".format(contador_a)
    if contador_e > 1:
        letras_contenidas += "{0} vocales: E ".format(contador_e)
    elif contador_e == 1:
        letras_contenidas += "{0} vocal: E ".format(contador_e)
    if contador_i > 1:
        letras_contenidas += "{0} vocales: I ".format(contador_i)
    elif contador_i == 1:
        letras_contenidas += "{0} vocal: I ".format(contador_i)
    if contador_o > 1:
        letras_contenidas += "{0} vocales: O ".format(contador_o)
    elif contador_o == 1:
        letras_contenidas += "{0} vocal: O ".format(contador_o)
    if contador_u > 1:
        letras_contenidas += "{0} vocales: U ".format(contador_u)
    elif contador_u == 1:
        letras_contenidas += "{0} vocal U ".format(contador_u)
    print(letras_contenidas)