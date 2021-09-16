from vista import VistaApp
from tkinter import Tk


class MiApp:
    def __init__(self, window):
        self.ventana = window
        VistaApp(self.ventana)


if __name__ == "__main__":
    root = Tk()
    obj = MiApp(root)
    root.mainloop()
