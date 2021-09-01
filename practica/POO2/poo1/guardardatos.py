import shelve
from personap.personam import Persona
from gerentep.gerentem import Gerente

juan = Persona("Juan Garcia", 42)
susana = Persona("Susana Gomez", 45, 40000)
tom = Gerente("Tom Perez", 42, 50000)

db = shelve.open("persona")
db["juan"] = juan
db["susana"] = susana
db["tom"] = tom
db.close()
