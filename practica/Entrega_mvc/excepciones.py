from tkinter.messagebox import showerror


class Excepcion(Exception):
    def __init__(self, titulo, descripcion):
        self.error = titulo
        self.mensaje = descripcion

    def mostrarError(self):
        showerror(self.error, self.mensaje)


class ExcepcionValidacionNombre(Excepcion):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)


class ExcepcionValidacionApellido(Excepcion):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)


class ExcepcionValidacionDni(Excepcion):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)


class ExcepcionValidacionDia(Excepcion):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)


class ExcepcionValidacionHorario(Excepcion):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)
