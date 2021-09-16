from tkinter import *
from modelo import Abmc


class VistaApp:
    def __init__(self, parent=None, **configs):
        self.my_parent = parent
        self.my_parent.geometry("820x600")
        self.my_parent.title("Agenda de consultorio")

        ##CONTENEDOR PRINCIPAL
        self.contenedor = Frame(self.my_parent, bg="#444")
        self.contenedor.pack(expand=YES, fill=BOTH)

        ### TITULO
        self.seccion_titulo = Frame(
            self.contenedor, bg="gray", borderwidth=1, relief=RAISED
        )
        self.seccion_titulo.pack(side=TOP, expand=NO, fill=BOTH)
        Label(
            self.seccion_titulo,
            text="Agenda de consultorio por Tomas Luca Suarez",
            bg="gray",
            height=2,
            font=24,
            fg="white",
        ).pack(
            side=TOP,
            expand=NO,
        )

        ### SECCION ENTRY - LABELS - CONTROLES - TEXT
        self.seccion_entrys = Frame(
            self.contenedor, bg="gray", borderwidth=2, relief=RAISED
        )
        self.seccion_entrys.pack(side=TOP, expand=NO, fill=BOTH, ipady=5)
        self.seccion_botones = Frame(
            self.contenedor, bg="gray", borderwidth=2, relief=RAISED
        )
        self.seccion_botones.pack(side=TOP, expand=NO, fill=BOTH)

        self.seccion_cajatexto = Frame(self.contenedor, bg="yellow")
        self.seccion_cajatexto.pack(side=TOP, expand=YES)

        ### ENTRYS Y LABELS
        Label(self.seccion_entrys, text="Nombre").pack(side=LEFT, expand=NO, fill=Y)
        self.nombre_entrada = Entry(self.seccion_entrys, bg="white", justify=CENTER)
        self.nombre_entrada.pack(side=LEFT, expand=NO, fill=Y)
        Label(self.seccion_entrys, text="Apellido").pack(side=LEFT, expand=NO, fill=Y)
        self.apellido_entrada = Entry(self.seccion_entrys, bg="white", justify=CENTER)
        self.apellido_entrada.pack(side=LEFT, expand=NO, fill=Y)
        Label(self.seccion_entrys, text="DNI").pack(side=LEFT, expand=NO, fill=Y)
        self.dni_entrada = Entry(self.seccion_entrys, bg="white", justify=CENTER)
        self.dni_entrada.pack(side=LEFT, expand=NO, fill=Y)
        Label(self.seccion_entrys, text="Día").pack(side=LEFT, expand=NO, fill=Y)
        self.dia_entrada = Entry(self.seccion_entrys, bg="white", justify=CENTER)
        self.dia_entrada.pack(side=LEFT, expand=NO, fill=Y)
        Label(self.seccion_entrys, text="Horario").pack(side=LEFT, expand=NO, fill=Y)
        self.horario_entrada = Entry(self.seccion_entrys, bg="white", justify=CENTER)
        self.horario_entrada.pack(side=LEFT, expand=NO, fill=Y)
        #### BOTONES

        self.boton_alta = Button(
            self.seccion_botones,
            text="Alta",
            width=10,
            height=1,
            activebackground="Green",
            activeforeground="White",
            command=lambda: self.alta_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        ).pack(side=LEFT, expand=NO, fill=Y, padx=30)

        self.boton_modificar = Button(
            self.seccion_botones,
            text="Modificar",
            width=10,
            height=1,
            activebackground="Yellow",
            activeforeground="White",
            command=lambda: self.modificar_paciente(
                self.nombre_entrada.get(),
                self.apellido_entrada.get(),
                self.dni_entrada.get(),
                self.dia_entrada.get(),
                self.horario_entrada.get(),
            ),
        ).pack(side=LEFT, expand=NO, fill=Y, padx=30)

        self.boton_baja = Button(
            self.seccion_botones,
            text="Baja",
            width=10,
            height=1,
            activebackground="Red",
            activeforeground="White",
            command=lambda: self.baja_paciente(self.dni_entrada.get()),
        ).pack(side=LEFT, expand=NO, fill=Y, padx=30)

        self.boton_listar = Button(
            self.seccion_botones,
            text="Listar",
            width=10,
            height=1,
            activebackground="OrangeRed",
            activeforeground="White",
            command=self.listar_pacientes,
        ).pack(side=LEFT, expand=NO, fill=Y, padx=30)

        self.boton_mostrar = Button(
            self.seccion_botones,
            text="Mostrar",
            width=10,
            height=1,
            activebackground="Purple",
            activeforeground="White",
            command=lambda: self.mostrar_paciente(self.dni_entrada.get()),
        ).pack(side=LEFT, expand=NO, fill=Y, padx=30)

        self.boton_limpiar = Button(
            self.seccion_botones,
            text="Limpiar",
            width=10,
            height=1,
            command=self.limpiar_campos,
        ).pack(side=LEFT, expand=NO, fill=Y, padx=30)

        self.caja_texto = Text(self.seccion_cajatexto)
        self.caja_texto.pack(expand=YES, fill=BOTH)

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

    def modificar_paciente(
        self,
        nombre_entrada,
        apellido_entrada,
        dni_entrada,
        dia_entrada,
        horario_entrada,
    ):
        self.m_abcm = Abmc(self)
        self.m_abcm.modificar_paciente(
            nombre_entrada, apellido_entrada, dni_entrada, dia_entrada, horario_entrada
        )

    def baja_paciente(self, dni):
        self.m_abcm = Abmc(self)
        self.m_abcm.baja_paciente(dni)

    def listar_pacientes(self):
        self.m_abcm = Abmc(self)
        self.m_abcm.listar_pacientes()

    def mostrar_paciente(self, dni):
        self.m_abcm = Abmc(self)
        self.m_abcm.mostrar_paciente(dni)

    def limpiar_campos(self):
        self.m_abcm = Abmc(self)
        self.m_abcm.limpiar_campos()
