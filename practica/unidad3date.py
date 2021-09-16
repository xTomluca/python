import datetime
import calendar

datetime.datetime.now()
print(datetime.datetime.utcnow(), end="\n\n")
print(datetime.datetime.now(), end="\n\n")
print(datetime.datetime.now().day, end="\n\n")
print(datetime.datetime.now().month, end="\n\n")
print(datetime.datetime.now().minute, end="\n\n")
print(datetime.datetime.now().second, end="\n\n")
print(datetime.datetime.now().microsecond, end="\n\n")

#Simplificar formato

print(datetime.datetime.today().strftime("%H:%M:%S--%d/%m/%y"), end="\n\n")

""""
%a - Nombre del día de la semana
%A - Nombre del día completo
%b - Nombre abreviado del mes
%B - Nombre completo del mes
%c - Fecha y hora actual
%d - Día del mes
%H - Hora (formato 24 horas)
%I - Hora (formato 12 horas)
%j - Día del año
%m - Mes en número
%M- Minutos
%p - Equivalente de AM o PM
%S - Segundos
"""

"""
%U - Semana del año (domingo como primer día de la semana)
%w - Día de la semana
%W - Semana del año (lunes como primer día de la semana)
%x - Fecha actual
%X - Hora actual
%y - Número de año (14)
%Y - Número de año entero (2014)
%Z - Zona horaria
"""
# Diferencia de fechas 1
actual = datetime.datetime.now()
anterior = datetime.datetime(2021, 6, 4, 0, 0, 0)
print(actual-anterior, end="\n\n")

# Diferencia de fechas 2
hoy = datetime.date.today()
hace5 = datetime.timedelta(days=5)
print(hoy, end="\n\n")
print(hace5, end="\n\n")
print(hoy-hace5, end="\n\n")
