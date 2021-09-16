"""# Defino listas
juan = ["Juan Garcia", 24, 5000, "Pintor"]
susana = ["Susana Gomez", 25, 6000, "Empleada"]
print(juan[0])

# Definir lista como base de datos

personas = [juan, susana]

# Imprimo lista de personas con un for

for x in personas:
    print(x)

# Imprimo los apellidos

for x in personas:
    print((x[0].split()[-1]))
    x[2] *= 1.20

for x in personas:
    print(x)

personas.append(["Pedro Gutierrez", 20, 12000, "Diseñador"])

for x in personas:
    print(x)
    print("---------")

nueva_lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]

print(nueva_lista)
print('', end="\n#####################\n")

for a in nueva_lista:
    print(a)
    print('', end="\n#####################\n")
"""
nueva_lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]
"""
for a in nueva_lista:
    for b in a:
        print(b)
        print('', end="\n#####################\n")
"""
for a in nueva_lista:
    if isinstance(a, nueva_lista):
        for b in a:
            if isinstance(b, nueva_lista):
                for c in b:
                    print(c)
            else:
                print(b)
    else:
        print(a)