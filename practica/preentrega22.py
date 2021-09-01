from os import stat_result
from re import A
from time import time
import tkinter as tk
from tkinter.constants import END, TRUE
from tkinter.messagebox import showerror, showinfo
from typing import Text
from datetime import date, datetime
from tkinter.constants import FALSE, TRUE
import mysql.connector
from mysql.connector import cursor

app = tk.Tk()
app.geometry("580x400")
app.title("Agenda Consultorio Medico")
pacientes = {}
contador = 0
flag_dia = FALSE
flag_hora = FALSE
flag_minuto = FALSE
flag_turno_repetido = FALSE
min_hora = 0
max_hora = 23
min_min = 0
max_min = 59


def validar_dni(dni):
    if len(dni) == 10 or len(dni) == 9:
        if(dni[2] == "." and dni[6] == "." and dni[0].isdigit() and dni[1].isdigit() and dni[3].isdigit() and dni[4].isdigit() and dni[5].isdigit() and dni[7].isdigit() and dni[8].isdigit() and dni[9].isdigit()) or (dni[1] == "." and dni[5] == "." and dni[0].isdigit() and dni[2].isdigit() and dni[3].isdigit() and dni[4].isdigit() and dni[6].isdigit() and dni[7].isdigit() and dni[8].isdigit()):
            return TRUE
    return FALSE


def validar_turno(int_hora, int_minuto, fecha, micursor):
    micursor.execute("select dia, hora, minuto from paciente")
    n_dato = 0
    global flag_dia
    global flag_hora
    global flag_minuto
    global flag_turno_repetido
    for paciente in micursor:
        for dato in paciente:
            if n_dato == 0:
                if dato == fecha.date():
                    flag_dia = TRUE
                    showinfo("DIA","asdasd")
                else:
                    flag_dia = FALSE
            elif n_dato == 1:
                if dato == int_hora:
                    flag_hora = TRUE
                    showinfo("HORA","asdasd")
                else:
                    flag_hora = FALSE
            else:
                if dato == int_minuto:
                    flag_minuto = TRUE
                    showinfo("Minuto","asdasd")
                else:
                    flag_minuto = FALSE
            if (flag_dia == TRUE and flag_hora == TRUE and flag_minuto == TRUE):
                
                return FALSE
            n_dato += 1
        n_dato = 0
    return TRUE


def validar_horario(horario):
    if (len(horario) == 5 and horario[2] == ":" and horario[0].isdigit() and horario[1].isdigit() and horario[3].isdigit() and horario[4].isdigit()):
        return TRUE
    return FALSE


def validar_dia(dia):
    if (len(dia) == 10 and dia[2] == "/" and dia[5] == "/" and dia[0].isdigit() and dia[1].isdigit() and dia[3].isdigit() and dia[4].isdigit() and dia[6].isdigit() and dia[7].isdigit() and dia[8].isdigit() and dia[9].isdigit()):
        return TRUE
    return FALSE                        


def dni_existente(micursor, dni):
    dato = (dni,)
    sentencia = "select dni from paciente where dni = %s"                                     
    micursor.execute(sentencia, dato)
    for x in micursor:
        return FALSE
    return TRUE


def alta_paciente():
    nombre = nombre_entrada.get()
    apellido = apellido_entrada.get()
    dni = dni_entrada.get()
    dia = dia_entrada.get()
    horario = horario_entrada.get()
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
            if (validar_dni(dni)):
                if (validar_horario(horario)):
                    if (validar_dia(dia)):
                        bd = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="",
                            database="entrega",
                            )
                        micursor = bd.cursor(buffered=True)
                        micursor.execute("select count(*) from paciente")
                        cantidad_elementos = []
                        for x in micursor:
                            cantidad_elementos.append(x)
                        str_dia = dia[0] + dia[1]
                        str_mes = dia[3] + dia[4]
                        str_an = dia[6] + dia[7] + dia[8] + dia[9]
                        int_dia = int(str_dia)
                        int_mes = int(str_mes)
                        int_an = int(str_an)
                        fecha = datetime(int_an, int_mes, int_dia)
                        if cantidad_elementos[0][0] != 0:
                            if validar_turno(int_hora, int_minuto, fecha, micursor):
                                if dni_existente(micursor, dni):
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
                            showinfo(
                                "Alta exitosa", "Agendado correctamente"
                            )
                            nombre_entrada.delete(0, END)
                            apellido_entrada.delete(0, END)
                            dni_entrada.delete(0, END)
                            dia_entrada.delete(0, END)
                            horario_entrada.delete(0, END)
                    else:
                        showerror(
                            "Error formato",
                            "Fomato correcto DIA= 20/06/2021",
                        )
                        dia_entrada.delete(0, END)
                else:
                    showerror(
                        "Error formato", "Fomato correcto HORARIO= 12:20"
                     )
                    horario_entrada.delete(0, END)
            else:
                showerror(
                    "Error formato", "Fomato correcto DNI= 31.540.089"
                )
                dni_entrada.delete(0, END)
        else:
            showerror("Error", "Faltan datos")
            dni_entrada.delete(0, END)
    else:
        showerror("Fuera de rango", "0:00 a 23:59")


caja_texto = tk.Text(app, height=4, width=33)


def listar_pacientes():
    caja_texto.delete(1.0, END)
    str_lista_pacientes = "No hay pacientes cargados"
    cantidad_de_pacientes = []
    bd = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="entrega",
    )
    micursor = bd.cursor(buffered=True)
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
                    str_lista_pacientes += str(dato) + ":"
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
    app, text="Modificar paciente", activebackground="Yellow", activeforeground="Black"
)
boton_listar = tk.Button(
    app,
    text="Listar pacientes",
    activebackground="Light blue",
    activeforeground="White",
    command=listar_pacientes,
)
boton_baja = tk.Button(
    app, text="Baja paciente", activebackground="Red", activeforeground="White"
)


boton_listar.place(x=20, y=100, width=120, height=20)
boton_alta.place(x=160, y=100, width=120, height=20)
boton_modificacion.place(x=300, y=100, width=120, height=20)
boton_baja.place(x=440, y=100, width=120, height=20)
# contador += 1
# caja_texto.insert(END, contador)
app.mainloop()
