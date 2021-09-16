from tkinter import Tk as tk
from modelo import Abmc
from tkinter import Text
from tkinter import Label
from tkinter import Entry
from tkinter import Button


class VistaApp:
    def __init__(self, window):
        self.root = window
        self.root.geometry("580x400")
        self.root.title("Agenda Consultorio Medico")
        self.caja_texto = Text(self.root, height=4, width=33)
        self.nombre_entrada = Entry(self.root)
        self.apellido_entrada = Entry(self.root)
        self.dni_entrada = Entry(self.root)
        self.dia_entrada = Entry(self.root)
        self.horario_entrada = Entry(self.root)
        self.nombre_label = Label(self.root, text="Nombre:")
        self.apellido_label = Label(self.root, text="Apellido:")
        self.dni_label = Label(self.root, text="DNI:")
        self.dia_label = Label(self.root, text="Dia:")
        self.horario_label = Label(self.root, text="Horario:")
        self.nombre_label.place(x=20, y=20)
        self.nombre_entrada.place(x=90, y=20, width=100, height=20)
        self.apellido_label.place(x=210, y=20)
        self.apellido_entrada.place(x=270, y=20, width=100, height=20)
        self.dni_label.place(x=390, y=20)
        self.dni_entrada.place(x=430, y=20, width=100, height=20)
        self.dia_label.place(x=20, y=60)
        self.dia_entrada.place(x=90, y=60, width=100, height=20)
        self.horario_label.place(x=210, y=60)
        self.horario_entrada.place(x=270, y=60, width=100, height=20)
        self.caja_texto.place(x=20, y=130, width=550, height=240)
        self.boton_alta = Button(
            self.root,
            text="Alta paciente",
            activebackground="Green",
            activeforeground="White",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        )
        self.boton_modificacion = Button(
            self.root,
            text="Modificar paciente",
            activebackground="Yellow",
            activeforeground="Black",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        )
        self.boton_listar = Button(
            self.root,
            text="Listar pacientes",
            activebackground="Light blue",
            activeforeground="White",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        )
        self.boton_baja = Button(
            self.root,
            text="Baja paciente",
            activebackground="Red",
            activeforeground="White",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        )
        self.boton_limpiar = Button(
            self.root,
            text="Limpiar campos",
            activebackground="Red",
            activeforeground="White",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        )
        self.boton_mostrar = Button(
            self.root,
            text="Mostrar paciente",
            activebackground="Red",
            activeforeground="White",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        )
        self.boton_listar.place(x=20, y=100, width=120, height=20)
        self.boton_alta.place(x=160, y=100, width=120, height=20)
        self.boton_modificacion.place(x=300, y=100, width=120, height=20)
        self.boton_baja.place(x=440, y=100, width=120, height=20)
        self.boton_limpiar.place(x=440, y=75, width=120, height=20)
        self.boton_mostrar.place(x=440, y=50, width=120, height=20)

    def alta_paciente(
        self,
        nombre_entrada,
        apellido_entrada,
        dni_entrada,
        dia_entrada,
        horario_entrada,
    ):
        self.m_abcm = Abmc(self)
        self.m_abcm.alta_paciente(
            nombre_entrada, apellido_entrada, dni_entrada, dia_entrada, horario_entrada
        )
