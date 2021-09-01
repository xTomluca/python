import validaciones
import conexion
from tkinter.messagebox import showerror, showinfo
from datetime import datetime

min_hora = 0
max_hora = 23
min_min = 0
max_min = 59


class Abmc:
    def __init__(self, window):
        self.m_ventana = window

    def alta_paciente(
        self,
        nombre_entrada,
        apellido_entrada,
        dni_entrada,
        dia_entrada,
        horario_entrada,
    ):
        nombre = nombre_entrada
        apellido = apellido_entrada
        dni = dni_entrada
        dia = dia_entrada
        horario = horario_entrada
        hora = horario[0] + horario[1]
        minuto = horario[3] + horario[4]
        int_hora = int(hora)
        int_minuto = int(minuto)

        if (
            int_hora >= min_hora
            and int_hora <= max_hora
            and int_minuto >= min_min
            and int_minuto <= max_min
        ):
            if (
                len(nombre) != 0
                and len(apellido) != 0
                and len(dni) != 0
                and len(dia) != 0
            ):
                fecha = validaciones.validar_dia(self, dia)
                if (
                    validaciones.validar_dni(self, dni)
                    and validaciones.validar_horario(self, horario)
                    and fecha != False
                    and validaciones.validar_nombre(self, nombre)
                    and validaciones.validar_apellido(self, apellido)
                ):
                    bd = conexion.bd
                    micursor = conexion.micursor
                    if (
                        validaciones.validar_turno(
                            self, int_hora, int_minuto, fecha, micursor
                        )
                        and validaciones.dni_existente(micursor, dni) == False
                    ):

                        if conexion.tabla_inicializada(micursor):
                            sql = "INSERT INTO paciente (nombre, apellido, dni, dia, hora, minuto) VALUES (%s, %s, %s, %s,%s,%s)"
                            datos = (
                                nombre,
                                apellido,
                                dni,
                                fecha,
                                hora,
                                minuto,
                            )
                            micursor.execute(sql, datos)
                            bd.commit()
                            showinfo(
                                "Alta exitosa",
                                "Agendado correctamente",
                            )
                            self.m_ventana.nombre_entrada.delete(0, "end")
                            self.m_ventana.apellido_entrada.delete(0, "end")
                            self.m_ventana.dni_entrada.delete(0, "end")
                            self.m_ventana.dia_entrada.delete(0, "end")
                            self.m_ventana.horario_entrada.delete(0, "end")
                        else:
                            print("ELSE")
                            sql = "INSERT INTO paciente (nombre, apellido, dni, dia, hora, minuto) VALUES (%s, %s, %s, %s,%s,%s)"
                            datos = (
                                nombre,
                                apellido,
                                dni,
                                fecha,
                                hora,
                                minuto,
                            )
                            micursor.execute(sql, datos)
                            bd.commit()
                            showinfo("Alta exitosa", "Agendado correctamente")
                            self.m_ventana.nombre_entrada.delete(0, "end")
                            self.m_ventana.apellido_entrada.delete(0, "end")
                            self.m_ventana.dni_entrada.delete(0, "end")
                            self.m_ventana.dia_entrada.delete(0, "end")
                            self.m_ventana.horario_entrada.delete(0, "end")
                else:
                    print("algo fallo")
            else:
                showerror("Error", "Faltan datos")
                self.m_ventana.dni_entrada.delete(0, "end")
        else:
            showerror("Fuera de rango", "0:00 a 23:59")
