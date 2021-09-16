def printer(mensaje):
    return mensaje


a = printer("\nHola mundo!\n")
print(a)


a = 5 #Variable global


def sumar_cinco(b):
    c = a + b  # Variables locales
    return  c


print(sumar_cinco(5), end="\n\n")


a = 10
b = 4


def nopisa():
    a = 1
    print("El valor de a en funcion es", a, end="\n\n")
    print("El vlaor de b dentro de la funcion es", b, end="\n\n")


nopisa()


print("El valor fuera de la funcion es", a, end="\n\n")

# Una variable no puede ser usada como global y local en una misma funcion
# Hay que usar la palabra global para asignar a una variable global un valor

variable_global = 5


def cambio_valor_variable_global():
    global variable_global
    variable_global = 10  # Reasigno valor a variable global
    print("El valor de variable_global", variable_global, end="\n\n")


cambio_valor_variable_global()

print("El valor de la variable fuera de la funcion es: ", variable_global, end="\n\n")
