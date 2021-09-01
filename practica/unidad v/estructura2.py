from tkinter import *


class MiApp:
    def __init__(self, parent=None, **configs):
        ############## Ventana principal ############
        self.my_parent = parent
        self.my_parent.geometry("700x600")

        ############## Agrego contenedor ############
        self.contenedor = Frame(self.my_parent, bg="#444")
        self.contenedor.pack(expand=YES, fill=BOTH)

        ############# Agrego secciones principales ####
        self.seccion_cerrar = Frame(
            self.contenedor, bg="#FF7F50", height=22, borderwidth=2, relief=RAISED
        )
        self.seccion_cerrar.pack(side=TOP, expand=NO, fill=X, padx=7)
        self.cerrar = Frame(self.seccion_cerrar, bg="yellow", height=22)
        self.cerrar.pack(side=TOP, expand=NO, fill=X)

        # Seccion controles #######
        self.seccion_controles = Frame(
            self.contenedor, bg="red", borderwidth=2, relief=RAISED
        )
        self.seccion_controles.pack(side=TOP, expand=NO, fill=BOTH, padx=7, pady=7)
        titulo_controles = "Controles"
        Label(
            self.seccion_controles,
            text=titulo_controles,
            bg="#222",
            fg="OrangeRed",
            justify=LEFT,
        ).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.controles = Frame(self.seccion_controles, bg="#222")
        self.controles.pack(side=TOP, expand=NO, fill=X)

        # Seccion representacion####
        self.seccion_representacion = Frame(
            self.contenedor, bg="red", borderwidth=2, relief=RAISED
        )
        self.seccion_representacion.pack(
            side=BOTTOM, expand=YES, fill=BOTH, padx=7, pady=7
        )
        titulo_grafico = "Representacion Grafica"
        Label(
            self.seccion_representacion,
            text=titulo_grafico,
            bg="#222",
            fg="OrangeRed",
            justify=LEFT,
        ).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.representacion = Frame(self.seccion_representacion, bg="OrangeRed")
        self.representacion.pack(side=TOP, expand=YES, fill=BOTH)
        self.temas_opciones = Frame(self.controles, borderwidth=5, bg="#222")
        self.nombres_opciones = Frame(self.controles, borderwidth=5, bg="#222")
        self.side_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.fill_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.expand_contenedor = Frame(self.controles, borderwidth=5, bg="#222")
        self.anchor_contenedor = Frame(self.controles, borderwidth=5, bg="#222")

        self.temas_opciones.pack(side=LEFT, expand=NO, fill=Y, anchor=N)
        self.nombres_opciones.pack(side=LEFT, expand=YES, fill=Y, anchor=N)
        self.side_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.fill_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.expand_contenedor.pack(side=LEFT, expand=YES, anchor=N)
        self.anchor_contenedor.pack(side=LEFT, expand=YES, anchor=N)

        Label(
            self.temas_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Temas",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.nombres_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Opciones",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.side_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Side",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.fill_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Fill",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.expand_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Expand",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        Label(
            self.anchor_contenedor,
            borderwidth=4,
            relief=RAISED,
            text="Anchor",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)

        ###### REPRESENTACION

        self.representacion_superior = Frame(self.representacion, bg="yellow")
        self.representacion_superior.pack(side=TOP, expand=YES, fill=BOTH)

        self.deslizador_central = Frame(
            self.representacion_superior,
            bg="black",
            borderwidth=7,
            relief=SUNKEN,
            width=250,
        )
        self.deslizador_central.pack(side=LEFT, expand=NO, fill=BOTH)

        self.deslizador_vertical = Frame(
            self.representacion_superior,
            bg="#FF7F50",
            borderwidth=5,
            relief=SUNKEN,
            width=50,
        )
        self.deslizador_vertical.pack(side=RIGHT, expand=NO, fill=Y)

        self.deslizador_horizontal = Frame(
            self.representacion,
            borderwidth=5,
            relief=SUNKEN,
            height=50,
            bg="OrangeRed",
        )
        self.deslizador_horizontal.pack(side=TOP, fill=X)

        self.botonVyH = Button(self.deslizador_central, text="VyH")
        self.botonVyH.pack()
        self.botonV = Button(self.deslizador_vertical, text="V")
        self.botonV.pack()
        self.botonH = Button(self.deslizador_horizontal, text="H")
        self.botonH.pack()
        self.elegir_nombre_botones = {
            "VyH": self.botonVyH,
            "V": self.botonV,
            "H": self.botonH,
        }
        self.deslizador_horizontal.pack(side=TOP, fill=X)

        self.temas = StringVar()
        self.temas.set("tema1")

        self.nombres = StringVar()
        self.nombres.set("VyH")

        self.side_option = StringVar()
        self.side_option.set(LEFT)

        self.fill_option = StringVar()
        self.fill_option.set(NONE)

        self.expand_option = StringVar()
        self.expand_option.set(YES)

        self.anchor_option = StringVar()
        self.anchor_option.set(N)

        ##### Nombres en controles

        temas = ["tema1", "tema2", "tema3"]
        nombre = ["VyH", "V", "H"]
        side_options = [LEFT, TOP, RIGHT, BOTTOM]
        fill_options = [X, Y, BOTH, NONE]
        expand_options = [YES, NO]
        anchor_options = [NW, N, NE, E, SE, S, SW, W, CENTER]
        ancho_boton = 10
        for opcion in temas:
            boton = Radiobutton(
                self.temas_opciones,
                text=str(opcion),
                indicatoron=1,
                value=opcion,
                bg="#222",
                fg="OrangeRed",
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in nombre:
            boton = Radiobutton(
                self.nombres_opciones,
                text=str(opcion),
                indicatoron=1,
                value=opcion,
                command=self.reseteo,
                variable=self.nombres,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in side_options:
            boton = Radiobutton(
                self.side_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.side_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in fill_options:
            boton = Radiobutton(
                self.fill_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.fill_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in expand_options:
            boton = Radiobutton(
                self.expand_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.expand_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        for opcion in anchor_options:
            boton = Radiobutton(
                self.anchor_contenedor,
                text=str(opcion),
                indicatoron=0,
                value=opcion,
                command=self.actualizar,
                variable=self.anchor_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

        ### DEFINO PARAMETROS
        ancho_boton = 10

        ##### BOTON CANCELAR
        self.cancelar = Button(self.cerrar, text="Cancelar", background="red")
        self.cancelar.pack(side=BOTTOM, anchor=S)
        self.cancelar.bind("<Button-1>", self.cerrarApp)

        ###FUNCIONES$$$$$$$$$$$$$$$$

    def reseteo(self):
        button = self.elegir_nombre_botones[self.nombres.get()]
        properties = button.pack_info()
        self.fill_option.set(properties["fill"])
        self.side_option.set(properties["side"])
        self.expand_option.set(properties["expand"])
        self.anchor_option.set(properties["anchor"])

    # $$$$ DESTRUIR
    def cerrarApp(self, event):
        self.my_parent.destroy()

    def actualizar(self):
        button = self.elegir_nombre_botones[self.nombres.get()]
        button.pack(
            fill=self.fill_option.get(),
            side=self.side_option.get(),
            expand=self.expand_option.get(),
            anchor=self.anchor_option.get(),
        )


"""
        for opcion in temas:
            boton = Radiobutton(
                self.temas_opciones,
                text=str(opcion),
                indicator=1,
                value=opcion,
                bg="#222",
                fg="OrangeRed",
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)
"""

if __name__ == "__main__":
    root = Tk()
    MiApp(root)
    root.mainloop()
