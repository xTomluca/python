a = 1
b = 2
c = 3

print("spam " * 3)
if a == 1 and b == 2 and c == 3:
    print("REPETIR " * 3)

if (a == 1 and
    b == 2 and
    c ==3):
    print("Repetir " * 3)

# ELIF

if a == 2:
    print("A", a)
elif b == 4:
    print("B", b)
else:
    print("C", c)


nombre = "Juan"
if "an" in nombre:
    print("Contiene an")
    if nombre.endswith("n"):
        nombre *= 2
        print(nombre)
