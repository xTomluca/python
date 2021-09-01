class Auto:
    color = "Azul"


objeto = Auto()
print(objeto.color)
print(dir(Auto))  # Imprimimos los metodos de clase
# Vemos cual es su clase padre
print(Auto.__class__.__base__)
# Vemos si es un objeto de alguna clase
print(Auto.__class__)
input()
