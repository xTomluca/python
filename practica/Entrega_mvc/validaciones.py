import re
from datetime import datetime
from tkinter.messagebox import showerror


def validar_nombre(window, nombre):

    cantidad_caracteres = len(nombre)
    secuencia = "[a-zA-Z- ]{" + str(cantidad_caracteres) + "}"
    patron = re.compile(secuencia)
    if patron.match(nombre):
        return True
    window.m_ventana.nombre_entrada.delete(0, "end")
    showerror("Error formato", "Formato nombre erroneo")
    return False


def validar_apellido(window, apellido):

    cantidad_caracteres = len(apellido)
    secuencia = "[a-zA-Z- ]{" + str(cantidad_caracteres) + "}"
    patron = re.compile(secuencia)
    if patron.match(apellido):
        return True
    window.m_ventana.apellido_entrada.delete(0, "end")
    showerror("Error formato", "Formato apellido erroneo")
    return True


def validar_dni(window, dni):
    secuencia = "[0-9]{1,2}[.]{1}[0-9]{3}[.]{1}[0-9]{3}"
    patron = re.compile(secuencia)
    if patron.fullmatch(dni):
        return True

    window.m_ventana.dni_entrada.delete(0, "end")
    showerror("Error formato", "Fomato correcto DNI= 31.540.089")
    return False


def validar_dia(window, dia):
    secuencia = "[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}"
    patron = re.compile(secuencia)
    if patron.fullmatch(dia):
        str_dia = dia[0] + dia[1]
        str_mes = dia[3] + dia[4]
        str_an = dia[6] + dia[7] + dia[8] + dia[9]
        int_dia = int(str_dia)
        int_mes = int(str_mes)
        int_an = int(str_an)
        try:
            return datetime(int_an, int_mes, int_dia)
        except Exception:
            print("entro a exception")
            showerror("Error fecha", "Corregir fecha")
            window.m_ventana.dia_entrada.delete(0, "end")
            return False
    showerror(
        "Error formato",
        "Fomato correcto DIA= 20/06/2021",
    )
    window.m_ventana.dia_entrada.delete(0, "end")
    return False


def validar_horario(window, horario):
    secuencia = "[0-9]{2}[:]{1}[0-9]{2}"
    patron = re.compile(secuencia)
    if patron.fullmatch(horario):
        return True
    showerror("Error formato", "Fomato correcto HORARIO= 12:20")
    window.m_ventana.horario_entrada.delete(0, "end")
    return False


def validar_turno(window, int_hora, int_minuto, fecha, micursor):
    micursor.execute("select dia, hora, minuto from paciente")
    n_dato = 0
    global flag_dia
    global flag_hora
    global flag_minuto
    flag_dia = False
    flag_hora = False
    flag_minuto = False
    for paciente in micursor:
        for dato in paciente:
            if n_dato == 0:
                if dato == fecha.date():
                    flag_dia = True
                else:
                    flag_dia = False
            elif n_dato == 1:
                if dato == int_hora:
                    flag_hora = True
                else:
                    flag_hora = False
            else:
                if dato == int_minuto:
                    flag_minuto = True
                else:
                    flag_minuto = False
            if flag_dia == True and flag_hora == True and flag_minuto == True:
                showerror("Error", "El turno se encuentra ocupado")
                window.m_ventana.horario_entrada.delete(0, "end")
                return False
            n_dato += 1
        n_dato = 0
    print("OKKKKKKKKKK")
    return True


def dni_existente(micursor, dni):
    dato = (dni,)
    sentencia = "select dni from paciente where dni = %s"
    micursor.execute(sentencia, dato)
    for x in micursor:
        showerror(
            "Error",
            "El paciente ya se encuentra en el sistema, debe modificar el turno",
        )
        return True
    return False
