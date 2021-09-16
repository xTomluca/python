print("\nIntroduzca fecha en el siguiente formato: 04/12/1973 ")
fecha = input()
fecha_ordenada = ""

if len(fecha) == 10:
    fecha_ordenada += "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(fecha[6], fecha[7], fecha[8], fecha[9], fecha[2],
    fecha[3], fecha[4], fecha[5], fecha[0], fecha[1])
    print("\nFecha ordenada: {0}".format(fecha_ordenada))
else:
    print("\nError al introducir fecha {0}, respete el formato".format(fecha))