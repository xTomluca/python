import shelve

db = shelve.open("persona")
for key in db:
    print(key, "->\n", db[key].nombre, db[key].sueldo)

juan = db["juan"]
print(juan.apellido())
print(db["susana"].apellido())
db.close()
