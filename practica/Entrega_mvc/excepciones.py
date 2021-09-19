from tkinter.messagebox import showerror


class Excepcion(Exception):
    def __init__(self, titulo, descripcion):
        """
        Instancia de clase Excepcion(Hereda de Exception)
        """
        self.error = titulo
        self.mensaje = descripcion

    def mostrarError(self):
        """
        Muestra error por el cual se lanza la excepcion
        """
        showerror(self.error, self.mensaje)


class ExcepcionValidacionNombre(Excepcion):
    def __init__(self, titulo, descripcion):
        """
        Instancia de clase ExcepcionValidacionNombre(Hereda de Excepcion)
        """
        super().__init__(titulo, descripcion)


class ExcepcionValidacionApellido(Excepcion):
    def __init__(self, titulo, descripcion):
        """
        Instancia de clase ExcepcionValidacionApellido(Hereda de Excepcion)
        """
        super().__init__(titulo, descripcion)


class ExcepcionValidacionDni(Excepcion):
    def __init__(self, titulo, descripcion):
        """
        Instancia de clase ExcepcionValidacionDni(Hereda de Excepcion)
        """
        super().__init__(titulo, descripcion)


class ExcepcionValidacionDia(Excepcion):
    def __init__(self, titulo, descripcion):
        """
        Instancia de clase ExcepcionValidacionDia(Hereda de Excepcion)
        """
        super().__init__(titulo, descripcion)


class ExcepcionValidacionHorario(Excepcion):
    def __init__(self, titulo, descripcion):
        """
        Instancia de clase ExcepcionValidacionHorario(Hereda de Excepcion)
        """
        super().__init__(titulo, descripcion)
