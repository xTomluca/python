from os import stat_result
import re
from time import time
import tkinter as tk
from tkinter.constants import END, TRUE
from tkinter.messagebox import showerror, showinfo
from typing import Text, final
from datetime import date, datetime
from tkinter.constants import FALSE, TRUE
from weakref import finalize
import mysql.connector
from mysql.connector import cursor
import conexion
import validaciones

app = tk.Tk()
app.geometry("580x400")
app.title("Agenda Consultorio Medico")
pacientes = {}
contador = 0
min_hora = 0
max_hora = 23
min_min = 0
max_min = 59


def mostrar_paciente():
    dni = dni_entrada.get()
    dato = (dni,)
    n_dato = 0
    dia_armada = ""
    hora_armada = ""
    str_lista_pacientes = ""
    datos_paciente = []

    sentencia = "select * from paciente where dni = %s"
    micursor = conexion.micursor

    if conexion.tabla_inicializada(micursor):
        nombre_entrada.delete(0, END)
        apellido_entrada.delete(0, END)
        dia_entrada.delete(0, END)
        horario_entrada.delete(0, END)
        micursor.execute(sentencia, dato)

        global paciente_existe
        paciente_existe = 0

        for x in micursor:
            paciente_existe = 1
            datos_paciente.append(x)
        for campos in datos_paciente:
            for dato in campos:
                if n_dato == 1:
                    nombre_entrada.insert(END, dato)
                elif n_dato == 2:
                    apellido_entrada.insert(END, dato)
                elif n_dato == 4:
                    if dato.day < 10:
                        dia_armada += "0" + str(dato.day) + "/"
                    else:
                        dia_armada += str(dato.day) + "/"
                    if dato.month < 10:
                        dia_armada += "0" + str(dato.month) + "/"
                    else:
                        dia_armada += str(dato.month) + "/"
                    dia_armada += str(dato.year)
                    dia_entrada.insert(END, dia_armada)
                elif n_dato == 5:
                    if dato < 10:
                        hora_armada += "0" + str(dato) + ":"
                    else:
                        hora_armada += str(dato) + ":"
                elif n_dato == 6:
                    if dato < 10:
                        hora_armada += "0" + str(dato)
                    else:
                        hora_armada += str(dato)
                    horario_entrada.insert(END, hora_armada)
                n_dato += 1
        if paciente_existe == 1:
            caja_texto.insert(END, str_lista_pacientes)
        else:
            showerror(
                "Error paciente", "El numero de DNI no coincide con ningun paciente"
            )


def baja_paciente():
    dni = dni_entrada.get()
    dato = (dni,)
    sentencia = "DELETE FROM paciente where dni = %s"
    bd = conexion.bd
    micursor = conexion.micursor

    if conexion.tabla_inicializada(micursor):
        if dni and validaciones.validar_dni(dni):
            if validaciones.dni_existente(micursor, dni):
                micursor.execute(sentencia, dato)
                bd.commit()
                showinfo("Eliminado", "Se elimino el paciente con exito")
            else:
                showerror(
                    "Error", "El DNI ingresado no se encuentra en la base de datos"
                )
        else:
            showerror("Error", "Verique DNI ingresado")
    else:
        showerror("Error", "No hay pacientes cargados")


def alta_paciente(
    nombre_entrada, apellido_entrada, dni_entrada, dia_entrada, horario_entrada
):
    nombre = nombre_entrada
    apellido = apellido_entrada
    dni = dni_entrada
    dia = dia_entrada
    horario = horario_entrada
    hora = horario[0] + horario[1]
    minuto = horario[3] + horario[4]
    int_hora = int(hora)
    int_minuto = int(minuto)

    if (
        int_hora >= min_hora
        and int_hora <= max_hora
        and int_minuto >= min_min
        and int_minuto <= max_min
    ):
        if len(nombre) != 0 and len(apellido) != 0 and len(dni) != 0 and len(dia) != 0:
            if validaciones.validar_dni(dni):
                if validaciones.validar_horario(horario):
                    if validaciones.validar_dia(dia):
                        bd = conexion.bd
                        micursor = conexion.micursor
                        str_dia = dia[0] + dia[1]
                        str_mes = dia[3] + dia[4]
                        str_an = dia[6] + dia[7] + dia[8] + dia[9]
                        int_dia = int(str_dia)
                        int_mes = int(str_mes)
                        int_an = int(str_an)
                        try:
                            fecha = datetime(int_an, int_mes, int_dia)
                            print("TRY")
                            if conexion.tabla_inicializada(micursor):
                                print("tabla inicializada")
                                if validaciones.validar_turno(
                                    int_hora, int_minuto, fecha, micursor
                                ):
                                    print("validar turno")
                                    if (
                                        validaciones.dni_existente(micursor, dni)
                                        == FALSE
                                    ):
                                        print("Inserto paciente")
                                        sql = "INSERT INTO paciente (nombre, apellido, dni, dia, hora, minuto) VALUES (%s, %s, %s, %s,%s,%s)"
                                        datos = (
                                            nombre,
                                            apellido,
                                            dni,
                                            fecha,
                                            hora,
                                            minuto,
                                        )
                                        print("antes execute")
                                        micursor.execute(sql, datos)
                                        bd.commit()
                                        showinfo(
                                            "Alta exitosa",
                                            "Agendado correctamente",
                                        )
                                        nombre_entrada.delete(0, END)
                                        apellido_entrada.delete(0, END)
                                        dni_entrada.delete(0, END)
                                        dia_entrada.delete(0, END)
                                        horario_entrada.delete(0, END)
                                    else:
                                        showerror(
                                            "Error",
                                            "El paciente ya se encuentra en el sistema, debe modificar el turno",
                                        )
                                else:
                                    showerror(
                                        "Error",
                                        "El turno se encuentra ocupado",
                                    )
                                    horario_entrada.delete(0, END)
                            else:
                                print("ELSE")
                                sql = "INSERT INTO paciente (nombre, apellido, dni, dia, hora, minuto) VALUES (%s, %s, %s, %s,%s,%s)"
                                datos = (
                                    nombre,
                                    apellido,
                                    dni,
                                    fecha,
                                    hora,
                                    minuto,
                                )
                                micursor.execute(sql, datos)
                                bd.commit()
                                showinfo("Alta exitosa", "Agendado correctamente")
                                nombre_entrada.delete(0, END)
                                apellido_entrada.delete(0, END)
                                dni_entrada.delete(0, END)
                                dia_entrada.delete(0, END)
                                horario_entrada.delete(0, END)
                        except Exception:
                            showerror("Error fecha", "Corregir fecha")
                            dia_entrada.delete(0, END)
                    else:
                        showerror(
                            "Error formato",
                            "Fomato correcto DIA= 20/06/2021",
                        )
                        dia_entrada.delete(0, END)
                else:
                    showerror("Error formato", "Fomato correcto HORARIO= 12:20")
                    horario_entrada.delete(0, END)
            else:
                showerror("Error formato", "Fomato correcto DNI= 31.540.089")
                dni_entrada.delete(0, END)
        else:
            showerror("Error", "Faltan datos")
            dni_entrada.delete(0, END)
    else:
        showerror("Fuera de rango", "0:00 a 23:59")


def modificar_paciente():
    nombre = nombre_entrada.get()
    apellido = apellido_entrada.get()
    dni = dni_entrada.get()
    dia = dia_entrada.get()
    horario = horario_entrada.get()
    flag_sentencia = FALSE
    bd = conexion.bd
    micursor = conexion.micursor
    sentencia = "UPDATE paciente SET "
    datos_correctos = TRUE
    if conexion.tabla_inicializada(micursor):
        if (
            dni
            and validaciones.validar_dni(dni)
            and validaciones.dni_existente(micursor, dni)
        ):
            if (
                (nombre and validaciones.validar_nombre_apellido(nombre))
                or (apellido and validaciones.validar_nombre_apellido(apellido))
                or (
                    horario
                    and validaciones.validar_horario(horario)
                    or dia
                    and validaciones.validar_dia(dia)
                )
                and dni
            ):
                if nombre and validaciones.validar_nombre_apellido(nombre):
                    sentencia += "nombre = '{0}'".format(nombre)
                    flag_sentencia = TRUE
                elif nombre:
                    showerror("Error nombre", "Nombre ingresado erroneo")
                    datos_correctos = FALSE
                if apellido and validaciones.validar_nombre_apellido(apellido):
                    if flag_sentencia:
                        sentencia += ", apellido = '{0}' ".format(apellido)
                    else:
                        sentencia += "apellido = '{0}' ".format(apellido)
                        flag_sentencia = TRUE
                elif apellido:
                    showerror("Error apellido", "Apellido ingresado erroneo")
                    datos_correctos = FALSE
                if dia and horario:
                    hora = horario[0] + horario[1]
                    minuto = horario[3] + horario[4]
                    int_hora = int(hora)
                    int_minuto = int(minuto)
                    str_dia = dia[0] + dia[1]
                    str_mes = dia[3] + dia[4]
                    str_an = dia[6] + dia[7] + dia[8] + dia[9]
                    int_dia = int(str_dia)
                    int_mes = int(str_mes)
                    int_an = int(str_an)
                    try:
                        fecha = datetime(int_an, int_mes, int_dia)
                        print("223232323")
                        if (
                            int_hora >= min_hora
                            and int_hora <= max_hora
                            and int_minuto >= min_min
                            and int_minuto <= max_min
                        ):
                            print("asdasdasdasdasd")
                            if validaciones.validar_turno(
                                int_hora, int_minuto, fecha, micursor
                            ):
                                if flag_sentencia:
                                    sentencia += ", dia = '{0}', hora = {1}, minuto = {2} ".format(
                                        fecha, hora, minuto
                                    )
                                    print("ENTRO VALIDAR TURNO")
                                else:
                                    sentencia += (
                                        "dia = '{0}', hora = {1}, minuto = {2} ".format(
                                            fecha, hora, minuto
                                        )
                                    )
                                    flag_sentencia = TRUE
                                    print("ENTRO VALIDAR TURNO2")
                            else:
                                showerror(
                                    "TURNO", "Error, turno ya asignado anteriormente"
                                )
                                datos_correctos = FALSE
                                dia_entrada.delete(0, END)
                                horario_entrada.delete(0, END)
                        else:
                            showerror(
                                "Horario incorrecto",
                                "Probar entre las {0}{0}:{1}{1} a {2}:{3}".format(
                                    min_hora, min_hora, max_hora, max_min
                                ),
                            )
                            horario_entrada.delete(0, END)
                            datos_correctos = FALSE
                    except Exception:
                        showerror("Fecha fecha", "Corregir día")
                elif dia or horario:
                    showerror("Completar campos", "Completar día y horario")
                    datos_correctos = FALSE
                if flag_sentencia and datos_correctos:
                    sentencia += "WHERE dni = '{0}'".format(dni)
                    micursor.execute(sentencia)
                    bd.commit()
                    nombre_entrada.delete(0, END)
                    apellido_entrada.delete(0, END)
                    dni_entrada.delete(0, END)
                    dia_entrada.delete(0, END)
                    horario_entrada.delete(0, END)
                    showinfo("OK!", "Actualizacion efectuada con exito")
            else:
                showerror("Datos erroneos", "Unico campo no mutable DNI")
        else:
            showerror("El DNI no es correcto", "Verifique que sea correcto")


def limpiar_campos():
    nombre_entrada.delete(0, END)
    apellido_entrada.delete(0, END)
    dni_entrada.delete(0, END)
    dia_entrada.delete(0, END)
    horario_entrada.delete(0, END)


caja_texto = tk.Text(app, height=4, width=33)


def listar_pacientes():
    caja_texto.delete(1.0, END)
    str_lista_pacientes = "No hay pacientes cargados"
    cantidad_de_pacientes = []
    micursor = conexion.micursor
    micursor.execute("select count(*) from paciente")

    for cantidad in micursor:
        cantidad_de_pacientes.append(cantidad)
    if cantidad_de_pacientes[0][0] != 0:
        str_lista_pacientes = ""
        n_dato = 0
        lista_pacientes = []
        micursor.execute("select * from paciente")
        for paciente in micursor:
            lista_pacientes.append(paciente)
        for paciente in lista_pacientes:
            for dato in paciente:
                if n_dato == 0:
                    str_lista_pacientes += str(dato) + ") "
                elif n_dato <= 4:
                    str_lista_pacientes += str(dato) + " | "
                elif n_dato == 5:
                    if dato < 10:
                        str_lista_pacientes += "0" + str(dato) + ":"
                    else:
                        str_lista_pacientes += str(dato) + ":"
                else:
                    if dato < 10:
                        str_lista_pacientes += "0" + str(dato) + "\n"
                    else:
                        str_lista_pacientes += str(dato) + "\n"
                n_dato += 1
            n_dato = 0
        caja_texto.insert(END, str_lista_pacientes)


nombre_entrada = tk.Entry(app)
apellido_entrada = tk.Entry(app)
dni_entrada = tk.Entry(app)
dia_entrada = tk.Entry(app)
horario_entrada = tk.Entry(app)
nombre_label = tk.Label(app, text="Nombre:")
apellido_label = tk.Label(app, text="Apellido:")
dni_label = tk.Label(app, text="DNI:")
dia_label = tk.Label(app, text="Dia:")
horario_label = tk.Label(app, text="Horario:")
nombre_label.place(x=20, y=20)
nombre_entrada.place(x=90, y=20, width=100, height=20)
apellido_label.place(x=210, y=20)
apellido_entrada.place(x=270, y=20, width=100, height=20)
dni_label.place(x=390, y=20)
dni_entrada.place(x=430, y=20, width=100, height=20)
dia_label.place(x=20, y=60)
dia_entrada.place(x=90, y=60, width=100, height=20)
horario_label.place(x=210, y=60)
horario_entrada.place(x=270, y=60, width=100, height=20)
caja_texto.place(x=20, y=130, width=550, height=240)
boton_alta = tk.Button(
    app,
    text="Alta paciente",
    activebackground="Green",
    activeforeground="White",
    command=alta_paciente,
)
boton_modificacion = tk.Button(
    app,
    text="Modificar paciente",
    activebackground="Yellow",
    activeforeground="Black",
    command=modificar_paciente,
)
boton_listar = tk.Button(
    app,
    text="Listar pacientes",
    activebackground="Light blue",
    activeforeground="White",
    command=listar_pacientes,
)
boton_baja = tk.Button(
    app,
    text="Baja paciente",
    activebackground="Red",
    activeforeground="White",
    command=baja_paciente,
)
boton_limpiar = tk.Button(
    app,
    text="Limpiar campos",
    activebackground="Red",
    activeforeground="White",
    command=limpiar_campos,
)
boton_mostrar = tk.Button(
    app,
    text="Mostrar paciente",
    activebackground="Red",
    activeforeground="White",
    command=mostrar_paciente,
)
boton_listar.place(x=20, y=100, width=120, height=20)
boton_alta.place(x=160, y=100, width=120, height=20)
boton_modificacion.place(x=300, y=100, width=120, height=20)
boton_baja.place(x=440, y=100, width=120, height=20)
boton_limpiar.place(x=440, y=75, width=120, height=20)
boton_mostrar.place(x=440, y=50, width=120, height=20)

# contador += 1
# caja_texto.insert(END, contador)
app.mainloop()
