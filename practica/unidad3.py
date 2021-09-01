import pprint
juan = {'identificacion': {'nombre': 'Juan', 'apellido': 'Garcia'},
'edad': 24, 'sueldo': 5000, 'profesion': 'Pintor'}
susana = {'identificacion': {'nombre': 'Susana', 'apellido': 'Gomez'},
'edad': 25, 'sueldo': 6000, 'profesion': 'Empleada'}
db = {}
db['juan'] = juan
db['susana'] = susana
print("-------\n")
print(db)
print("-------\n")
pprint.pprint(db)
