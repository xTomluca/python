import re
from datetime import date, datetime
from tkinter.messagebox import showerror
from excepciones import (
    ExcepcionValidacionApellido,
    ExcepcionValidacionDia,
    ExcepcionValidacionDni,
    ExcepcionValidacionHorario,
    ExcepcionValidacionNombre,
    Excepcion,
)


def validar_nombre(window, nombre):

    """
    Se encarga de validar que el nombre del paciente contenga caracteres del alfabeto
    En caso de ser nombre compuesto permitir espacios
    Retorna:
    True si el nombre es valido
    False, si es invalido (Excepcion)
    """

    cantidad_caracteres = len(nombre)
    secuencia = "[a-zA-Z- ]{" + str(cantidad_caracteres) + "}"
    patron = re.compile(secuencia)
    if patron.match(nombre):
        return True
    try:
        raise ExcepcionValidacionNombre(
            "Error", "El nombre contiene caracteres invalidos"
        )
    except ExcepcionValidacionNombre as error:
        error.mostrarError()
        window.m_ventana.nombre_entrada.delete(0, "end")
        return False


def validar_apellido(window, apellido):

    """
    Se encarga de validar que el apellido del paciente contenga caracteres del alfabeto
    En caso de ser apellido compuesto permitir espacios
    Retorna:
    True si el apellido es valido
    False, si es invalido (Excepcion)
    """

    cantidad_caracteres = len(apellido)
    secuencia = "[a-zA-Z- ]{" + str(cantidad_caracteres) + "}"
    patron = re.compile(secuencia)
    if patron.match(apellido):
        return True
    try:
        raise ExcepcionValidacionApellido(
            "Error", "El apellido contiene caracteres invalidos"
        )
    except ExcepcionValidacionApellido as error:
        error.mostrarError()
        window.m_ventana.apellido_entrada.delete(0, "end")
        return False


def validar_dni(window, dni):
    """
    Se encarga de validar que el dni tenga entre 7 y 8 caracteres numeros y dos puntos divisores
    Retorna:
    True si el valido es valido
    False, si es invalido (Excepcion)
    """
    secuencia = "[0-9]{1,2}[.]{1}[0-9]{3}[.]{1}[0-9]{3}"
    patron = re.compile(secuencia)
    if patron.fullmatch(dni):
        return True
    try:
        raise ExcepcionValidacionDni(
            "Error DNI", "El formato correcto del DNI es: 39.111.321"
        )
    except ExcepcionValidacionDni as error:
        error.mostrarError()
        window.m_ventana.dni_entrada.delete(0, "end")
        return False


def validar_dia(window, dia):

    """
    Se encarga de validar que el dia respete el siguiente formato: 11/08/2021
    Retorna:
    Datetime si el dia es valido
    False, si es dia (Excepcion)
    """

    if len(dia) == 10:
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
                try:
                    raise ExcepcionValidacionDia(
                        "Error", "Formato correcto: 17/09/2021"
                    )
                except ExcepcionValidacionDia as error:
                    window.m_ventana.dia_entrada.delete(0, "end")
                    error.mostrarError()
                    return False
    try:
        raise ExcepcionValidacionDia("Error", "Formato correcto: 17/09/2021")
    except ExcepcionValidacionDia as error:
        window.m_ventana.dia_entrada.delete(0, "end")
        error.mostrarError()
        return False


def validar_horario(window, horario):
    """
    Se encarga de validar que el horario respete el siguiente formato: 13:20
    Retorna:
    True si el horario es valido
    False, si es invalido (Excepcion)
    """
    secuencia = "[0-9]{2}[:]{1}[0-9]{2}"
    patron = re.compile(secuencia)
    if patron.fullmatch(horario):
        return True
    try:
        raise ExcepcionValidacionHorario("Error Horario", "Formato correcto: 21:00")
    except ExcepcionValidacionHorario as error:
        error.mostrarError()
        window.m_ventana.horario_entrada.delete(0, "end")
        return False


def validar_turno(window, int_hora, int_minuto, fecha, micursor):

    """
    Se encarga de validar que el turno no se encuentre ocupado por otro paciente
    Retorna:
    True si el turno esta libre
    False, turno ocupado (Excepcion)
    """

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
                if isinstance(fecha, datetime):
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
                try:
                    raise Excepcion("Error", "Turno ya asignado anteriormente")
                except Excepcion as error:
                    error.mostrarError()
                    window.m_ventana.horario_entrada.delete(0, "end")
                    return False
            n_dato += 1
        n_dato = 0
    return True


def dni_existente(micursor, dni, condicion):

    """
    Se encarga de validar si el dni se encuentra registrado en sistema
    Retorna:
    True si el paciente ya esta inscripto
    False, si no se encuentra el paciente
    (Excepcion en caso de que el parametro condicion sea False utilizado para dar una nueva alta)
    """

    dato = (dni,)
    sentencia = "select dni from paciente where dni = %s"
    micursor.execute(sentencia, dato)
    for x in micursor:
        if condicion == False:
            try:
                raise Excepcion(
                    "Error",
                    "El paciente ya se encuentra en el sistema, debe modificar el turno",
                )
            except Excepcion as error:
                error.mostrarError()
                return True
        return True
    return False
