def calcular_factorial(numero):
    factorial = numero
    sumando = 1
    while numero > sumando:
        factorial *= sumando
        print(sumando)
        sumando += 1
    print("El factorial de {0} es {1}".format(numero,factorial))


print("Ingrese numero a calcular: ")
calcular_factorial(int(input()))
