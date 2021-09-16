from tkinter import *
from frame1 import Hola


class HolaApp(Frame):
    def __init__(self, parent=None, **configs):
        self.myParent = parent
        self.myParent.geometry("500x300")
        button3 = Button(self.myParent, text="Boton3")
        button3.pack()

        parent = Frame(self.myParent, bg="yellow", width=300, height=100)
        parent.pack(expand=YES, fill=X)

        Hola(parent).pack(side=RIGHT)
        button4 = Button(parent, text="salir", command=exit)
        button4.pack(side=LEFT)


if __name__ == "__main__":
    root = Tk()
    miaplicacion = HolaApp(root, text="Hola subclass world")
    root.mainloop()
