# El primero de alta de datos, debe permitir tomar los valores de los campos de entrada y presentarlos en la consola.
# El segundo debe permitir cambiar el color de fondo de la aplicación.
from tkinter import *

master = Tk()
master.geometry("300x120")
Label(master,text="Ingrese sus datos", bg="violet").grid(row=0, column=1)
Label(master,text="Titulo").grid(row=1, column=0,sticky=W)
Label(master,text="Ruta").grid(row=2, column=0,sticky=W)
Label(master,text="Descripcion").grid(row=3, column=0,sticky=W)

titulo = Entry(master)
ruta = Entry(master)
descripcion = Entry(master)

titulo.grid(row=1, column=1)
ruta.grid(row=2, column=1)
descripcion.grid(row=3, column=1)


def mensajeConsola():
    if len(titulo.get()) == 0 or len(ruta.get()) == 0 or len(descripcion.get()) == 0:
        print("\nFavor de ingresar todos los campos", end="\n\n")
    else:
        print("\n" + titulo.get(), ruta.get(), descripcion.get(), sep=" ",end="\n\n")


alta = Button(master, text="Alta", command=mensajeConsola)

def cambioFondo():
    master.configure(bg="Salmon")

sorpresa = Button(master, text="Sorpresa", command=cambioFondo)

alta.grid(row=4,column=1)
sorpresa.grid(row=4, column=2)

mainloop()