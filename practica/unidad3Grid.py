from tkinter import *
root = Tk()
Label(root, text="id").grid(row=0, column=0)
Label(root, text="nombre").grid(row=1, column=0)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()

# Sticky para posicionar
"""
from tkinter import *
root = Tk()
Label(root, text="id").grid(row=0,column=0,sticky=W)
Label(root,text="nombre").grid(row=1, column=0, sticky=W)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1,column=1)
mainloop()
"""
# Botones y parametros Command = PASA FUNCION  State = Disable deshabilita boton
# Pading espacio interno del boton padx= pady=

"""
from tkinter import *
master = Tk()
def callback():
    print("Click!")
#b = Button(master,text="OK", command=callback, padx=20, pady=10)
#b.pack()
# ANCHO Y ALTO
b = Button(master,text="Sure!", anchor=N, justify=LEFT,padx=22,height=3,width=12)
b.pack(fill=BOTH, expand=1)
mainloop()
"""

# Boton con imagen gif
"""
from tkinter import *
master = Tk()

photo = PhotoImage(file="download.gif")
c = Button(master,text="Sure!",anchor=W,justify=LEFT,image=photo)
c.pack(fill=BOTH,expand=1)
mainloop()
"""

# Color

# Fondo: background="black" o bg="black"
# Letra: foreground="red" o fg="red"
# Fondo activo = activatebackground="green"
# Letra activa: activateforeground="yellow"
# Letra deshabilitado: disabledforeground="blue"

"""
from tkinter import *
master = Tk()
def callback():
    print("Click!")
b = Button(master, text="OK", command=callback, padx=132, pady=132,
activebackground="green", activeforeground="yellow",
background="black", fg="red"
)
b.pack()
a = Button(master, text="OK", command=callback, padx=132, pady=132,
state=DISABLED, background="black", disabledforeground="blue"
)
a.pack()
mainloop() 
"""

# Posicion de texto/imagen y boton
# Posicion de texto e imagen
# anchor = SW
# Opciones: N, NE, E, SE, S, SW, W, NW, o CENTER
# Por default es CENTER(anchor,Anchor)

# Posicion de boton
# pack()
# Side = LEFT / TOP / RIGHT / BOTTOM
"""
from tkinter import *

master = Tk()
master.geometry("300x300")
def callback():
    print("Click!")
b = Button(master, text="OK", command=callback,
activebackground="green", activeforeground="yellow",
background="black",foreground="red",height=7,width=12, anchor=SW
)
b.pack(side=TOP)
mainloop()
"""

# TIPO DE TEXTO
# font=('tipo',tamaño,'peso')
"""
from tkinter import *

master = Tk()

b = Button(master, text="Ok!", anchor=W, justify=LEFT, padx=22,
height=3, width=12, font=('courier',22,'bold'))
b.pack(fill=BOTH,expand=1)
mainloop()
"""