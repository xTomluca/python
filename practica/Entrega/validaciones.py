import re

FALSE = 0
TRUE = 1


def validar_nombre_apellido(dato):

    cantidad_caracteres = len(dato)
    secuencia = "[a-zA-Z]{" + str(cantidad_caracteres) + "}"
    patron = re.compile(secuencia)
    if patron.match(dato):
        return TRUE
    return FALSE


def validar_dni(dni):
    secuencia = "[0-9]{1,2}[.]{1}[0-9]{3}[.]{1}[0-9]{3}"
    patron = re.compile(secuencia)
    if patron.fullmatch(dni):
        return TRUE
    return FALSE


def validar_dia(dia):
    secuencia = "[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}"
    patron = re.compile(secuencia)
    if patron.fullmatch(dia):
        return TRUE
    return FALSE


def validar_horario(horario):
    secuencia = "[0-9]{2}[:]{1}[0-9]{2}"
    patron = re.compile(secuencia)
    if patron.fullmatch(horario):
        return TRUE
    return FALSE


def validar_turno(int_hora, int_minuto, fecha, micursor):
    micursor.execute("select dia, hora, minuto from paciente")
    n_dato = 0
    global flag_dia
    global flag_hora
    global flag_minuto
    flag_dia = FALSE
    flag_hora = FALSE
    flag_minuto = FALSE
    for paciente in micursor:
        for dato in paciente:
            if n_dato == 0:
                if dato == fecha.date():
                    flag_dia = TRUE
                else:
                    flag_dia = FALSE
            elif n_dato == 1:
                if dato == int_hora:
                    flag_hora = TRUE
                else:
                    flag_hora = FALSE
            else:
                if dato == int_minuto:
                    flag_minuto = TRUE
                else:
                    flag_minuto = FALSE
            if flag_dia == TRUE and flag_hora == TRUE and flag_minuto == TRUE:

                return FALSE
            n_dato += 1
        n_dato = 0
    return TRUE


def dni_existente(micursor, dni):
    dato = (dni,)
    sentencia = "select dni from paciente where dni = %s"
    micursor.execute(sentencia, dato)
    for x in micursor:
        return TRUE
    return FALSE
