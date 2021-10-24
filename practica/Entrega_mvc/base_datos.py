from peewee import *
import datetime

try:
    db = SqliteDatabase("nivel_avanzado.db")

    class BaseModel(Model):
        class Meta:
            database = db

    class Paciente(BaseModel):
        nombre = CharField()
        apellido = CharField()
        dni = TextField()
        fecha = DateField()
        hora = IntegerField()
        minuto = IntegerField()

    db.connect()
    db.create_tables([Paciente])

    """
    nuevoPaciente = Paciente()
    print("Inserte nombre: ")
    nuevoPaciente.nombre = input()
    print("Inserte apellido: ")
    nuevoPaciente.apellido = input()
    print("Inserte dni: ")
    nuevoPaciente.dni = input()
    print("Inserte hora: ")
    nuevoPaciente.hora = int(input())
    print("Inserte minuto: ")
    nuevoPaciente.minuto = int(input())
    nuevoPaciente.fecha = datetime.date(1995, 8, 11)
    nuevoPaciente.save()
    """


#### QUE NECESITO?
####
except Exception:
    print("Error")
