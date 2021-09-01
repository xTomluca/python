from tkinter import *
from parametrostema import bcolor, bfont, bsize
from boton1 import HolaButton


class TemaDeBoton:
    def __init__(self, parent=None, **configs):
        self.myParent = parent
        self.myParent.geometry("300x300")
        button = Button(self.myParent, **configs)
        button.pack()
        button.config(bg=bcolor, font=(bfont, bsize))


def callback1():
    print("callback1")


def callback2():
    print("callback2")


class MiButton(TemaDeBoton):
    def __init__(self, parent=None, **configs):
        TemaDeBoton.__init__(self, parent, **configs)


if __name__ == "__main__":
    root = Tk()
    b1 = MiButton(root, text="Boton que herada de TemaDeButton", command=callback2)
    b2 = TemaDeBoton(root, text="Boton con tema y callback1", command=callback1)
    b3 = TemaDeBoton(root, text="Boton con tema y con callback2", command=callback2)
    b4 = HolaButton(root, text="Boton sin tema y con callback")
    root.mainloop()
