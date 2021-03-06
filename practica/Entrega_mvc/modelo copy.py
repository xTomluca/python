from logging import exception
from excepciones import Excepcion
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
        """
        Instancia objeto de la clase ABMC
        """
        self.m_ventana = window

    def alta_paciente(
        self,
        nombre_entrada,
        apellido_entrada,
        dni_entrada,
        dia_entrada,
        horario_entrada,
    ):

        """
        Se encarga de realizar el alta de nuevos paciente
        En caso de encontrarse registrado el mismo dni lanza una excepcion
        """

        nombre = nombre_entrada
        apellido = apellido_entrada
        dni = dni_entrada
        dia = dia_entrada
        if (
            nombre_entrada
            and apellido_entrada
            and dni_entrada
            and dia_entrada
            and horario_entrada
        ):
            if (
                validaciones.validar_nombre(self, nombre)
                and validaciones.validar_apellido(self, apellido)
                and validaciones.validar_dia(self, dia)
                and validaciones.validar_dni(self, dni)
                and validaciones.validar_horario(self, horario_entrada)
            ):
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
                    fecha = validaciones.validar_dia(self, dia)
                    if fecha:
                        bd = conexion.bd
                        micursor = conexion.micursor
                        if validaciones.dni_existente(
                            micursor, dni, False
                        ) == False and validaciones.validar_turno(
                            self, int_hora, int_minuto, fecha, micursor
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
                    try:
                        horario_laboral = ""
                        if min_hora < 10:
                            horario_laboral += "0" + str(min_hora) + ":"
                        else:
                            horario_laboral += str(min_hora) + ":"
                        if min_min < 10:
                            horario_laboral += "0" + str(min_min) + " - "
                        else:
                            horario_laboral += str(min_min) + " - "
                        if max_hora < 10:
                            horario_laboral += "0" + str(max_hora) + ":"
                        else:
                            horario_laboral += str(max_hora) + ":"
                        if max_min < 10:
                            horario_laboral += "0" + str(max_min)
                        else:
                            horario_laboral += str(max_min)
                        mensaje = "Fuera del horario: " + horario_laboral
                        raise Excepcion("Error", mensaje)
                    except Excepcion as error:
                        error.mostrarError()
        else:
            try:
                raise Excepcion("Error", "Varios datos se encuentran vacios")
            except Excepcion as error:
                error.mostrarError()

    def modificar_paciente(
        self,
        nombre_entrada,
        apellido_entrada,
        dni_entrada,
        dia_entrada,
        horario_entrada,
    ):

        """
        Se utiliza para realizar actualizacion de los datos de un paciente inscripto
        Se pueden modificar todos los campos a excepcion de el DNI
        En caso de querer modificar turno, debe completar campos de dia y horario
        """

        nombre = nombre_entrada
        apellido = apellido_entrada
        dni = dni_entrada
        dia = dia_entrada
        horario = horario_entrada

        flag_sentencia = False
        bd = conexion.bd
        micursor = conexion.micursor
        sentencia = "UPDATE paciente SET "
        datos_correctos = True
        if conexion.tabla_inicializada(micursor):
            if (
                dni
                and validaciones.validar_dni(self, dni)
                and validaciones.dni_existente(micursor, dni, True)
            ):
                if (
                    (nombre and validaciones.validar_nombre(self, nombre))
                    or (apellido and validaciones.validar_apellido(self, apellido))
                    or (
                        horario
                        and validaciones.validar_horario(self, horario)
                        or dia
                        and validaciones.validar_dia(self, dia)
                    )
                    and dni
                ):
                    if nombre:
                        """and validaciones.validar_nombre(self, nombre)"""
                        sentencia += "nombre = '{0}'".format(nombre)
                        flag_sentencia = True
                    elif nombre:
                        datos_correctos = False
                    if apellido and validaciones.validar_apellido(self, apellido):
                        if flag_sentencia:
                            sentencia += ", apellido = '{0}' ".format(apellido)
                        else:
                            sentencia += "apellido = '{0}' ".format(apellido)
                            flag_sentencia = True
                    elif apellido:
                        datos_correctos = False
                    if dia and horario:
                        hora = horario[0] + horario[1]
                        minuto = horario[3] + horario[4]
                        int_hora = int(hora)
                        int_minuto = int(minuto)
                        fecha = validaciones.validar_dia(self, dia)
                        if (
                            int_hora >= min_hora
                            and int_hora <= max_hora
                            and int_minuto >= min_min
                            and int_minuto <= max_min
                        ):
                            if validaciones.validar_turno(
                                self, int_hora, int_minuto, fecha, micursor
                            ):
                                if flag_sentencia:
                                    sentencia += ", dia = '{0}', hora = {1}, minuto = {2} ".format(
                                        fecha, hora, minuto
                                    )
                                else:
                                    sentencia += (
                                        "dia = '{0}', hora = {1}, minuto = {2} ".format(
                                            fecha, hora, minuto
                                        )
                                    )
                                    flag_sentencia = True
                            else:
                                datos_correctos = False
                        else:
                            try:
                                horario_laboral = ""
                                if min_hora < 10:
                                    horario_laboral += "0" + str(min_hora) + ":"
                                else:
                                    horario_laboral += str(min_hora) + ":"
                                if min_min < 10:
                                    horario_laboral += "0" + str(min_min) + " - "
                                else:
                                    horario_laboral += str(min_min) + " - "
                                if max_hora < 10:
                                    horario_laboral += "0" + str(max_hora) + ":"
                                else:
                                    horario_laboral += str(max_hora) + ":"
                                if max_min < 10:
                                    horario_laboral += "0" + str(max_min)
                                else:
                                    horario_laboral += str(max_min)
                                mensaje = "Fuera del horario: " + horario_laboral
                                raise Excepcion("Error", mensaje)
                            except Excepcion as error:
                                error.mostrarError()
                                self.m_ventana.horario_entrada.delete(0, "end")
                                datos_correctos = False
                    elif dia or horario:
                        try:
                            raise Excepcion(
                                "Completar campos", "Completar d??a y horario"
                            )
                        except Excepcion as error:
                            error.mostrarError()
                            datos_correctos = False
                    if flag_sentencia and datos_correctos:
                        sentencia += "WHERE dni = '{0}'".format(dni)
                        micursor.execute(sentencia)
                        bd.commit()
                        self.m_ventana.nombre_entrada.delete(0, "end")
                        self.m_ventana.apellido_entrada.delete(0, "end")
                        self.m_ventana.dni_entrada.delete(0, "end")
                        self.m_ventana.dia_entrada.delete(0, "end")
                        self.m_ventana.horario_entrada.delete(0, "end")
                        showinfo("OK!", "Actualizacion efectuada con exito")
                else:
                    try:
                        raise Excepcion("Datos erroneos", "Unico campo no mutable DNI")
                    except Excepcion as error:
                        error.mostrarError()
            else:
                try:
                    raise Excepcion("Error", "Verifique que el DNI sea correcto")
                except Excepcion as error:
                    error.mostrarError()

    def baja_paciente(self, dni):

        """
        Se utiliza para realizar la baja de un paciente mediante el DNI
        """

        dato = (dni,)
        sentencia = "DELETE FROM paciente where dni = %s"
        bd = conexion.bd
        micursor = conexion.micursor

        if conexion.tabla_inicializada(micursor):
            if dni and validaciones.validar_dni(self, dni):
                if validaciones.dni_existente(micursor, dni, True):
                    micursor.execute(sentencia, dato)
                    bd.commit()
                    showinfo("Eliminado", "Se elimino el paciente con exito")
                    self.m_ventana.nombre_entrada.delete(0, "end")
                    self.m_ventana.apellido_entrada.delete(0, "end")
                    self.m_ventana.dni_entrada.delete(0, "end")
                    self.m_ventana.dia_entrada.delete(0, "end")
                    self.m_ventana.horario_entrada.delete(0, "end")
                else:
                    try:
                        raise Excepcion(
                            "Error",
                            "El DNI ingresado no se encuentra en la base de datos",
                        )
                    except Excepcion as error:
                        error.mostrarError()
            # else:
            #    showerror("Error", "Verique DNI ingresado")
        else:
            try:
                raise Excepcion("Error", "No hay pacientes cargados")
            except Excepcion as error:
                error.mostrarError()

    def listar_pacientes(self):

        """
        Se encarga de listar los pacientes inscriptos en la caja de texto
        """
        self.m_ventana.caja_texto.delete(1.0, "end")
        str_lista_pacientes = "No hay pacientes cargados"
        cantidad_de_pacientes = []
        micursor = conexion.micursor
        micursor.execute("select count(*) from paciente")

        for cantidad in micursor:
            cantidad_de_pacientes.append(cantidad)
        if cantidad_de_pacientes[0][0] != 0:
            str_lista_pacientes = ""
            n_dato = 0
            lista_pacientes = []
            micursor.execute("select * from paciente")
            for paciente in micursor:
                lista_pacientes.append(paciente)
            for paciente in lista_pacientes:
                for dato in paciente:
                    if n_dato == 0:
                        str_lista_pacientes += str(dato) + ") "
                    elif n_dato <= 4:
                        str_lista_pacientes += str(dato) + " | "
                    elif n_dato == 5:
                        if dato < 10:
                            str_lista_pacientes += "0" + str(dato) + ":"
                        else:
                            str_lista_pacientes += str(dato) + ":"
                    else:
                        if dato < 10:
                            str_lista_pacientes += "0" + str(dato) + "\n"
                        else:
                            str_lista_pacientes += str(dato) + "\n"
                    n_dato += 1
                n_dato = 0
            self.m_ventana.caja_texto.insert("end", str_lista_pacientes)

    def mostrar_paciente(self, dni):

        """
        Se encarga de completar/mostrar los datos del paciente en los entrys buscando mediante el DNI
        """

        dato = (dni,)
        n_dato = 0
        dia_armada = ""
        hora_armada = ""
        datos_paciente = []

        sentencia = "select * from paciente where dni = %s"
        micursor = conexion.micursor

        if conexion.tabla_inicializada(micursor):
            self.m_ventana.nombre_entrada.delete(0, "end")
            self.m_ventana.apellido_entrada.delete(0, "end")
            self.m_ventana.dia_entrada.delete(0, "end")
            self.m_ventana.horario_entrada.delete(0, "end")
            micursor.execute(sentencia, dato)

            global paciente_existe
            paciente_existe = False
            if validaciones.validar_dni(self, dni):
                for x in micursor:
                    paciente_existe = True
                    datos_paciente.append(x)
                for campos in datos_paciente:
                    for dato in campos:
                        if n_dato == 1:
                            self.m_ventana.nombre_entrada.insert("end", dato)
                        elif n_dato == 2:
                            self.m_ventana.apellido_entrada.insert("end", dato)
                        elif n_dato == 4:
                            if dato.day < 10:
                                dia_armada += "0" + str(dato.day) + "/"
                            else:
                                dia_armada += str(dato.day) + "/"
                            if dato.month < 10:
                                dia_armada += "0" + str(dato.month) + "/"
                            else:
                                dia_armada += str(dato.month) + "/"
                            dia_armada += str(dato.year)
                            self.m_ventana.dia_entrada.insert("end", dia_armada)
                        elif n_dato == 5:
                            if dato < 10:
                                hora_armada += "0" + str(dato) + ":"
                            else:
                                hora_armada += str(dato) + ":"
                        elif n_dato == 6:
                            if dato < 10:
                                hora_armada += "0" + str(dato)
                            else:
                                hora_armada += str(dato)
                            self.m_ventana.horario_entrada.insert("end", hora_armada)
                        n_dato += 1
                if paciente_existe == True:
                    self.m_ventana.caja_texto.delete(1.0, "end")
                else:
                    try:
                        raise Excepcion(
                            "Error paciente",
                            "El numero de DNI no coincide con ningun paciente",
                        )
                    except Excepcion as error:
                        error.mostrarError()

    def limpiar_campos(self):

        """
        Se encarga de limpiar todos los entrys
        """
        self.m_ventana.nombre_entrada.delete(0, "end")
        self.m_ventana.apellido_entrada.delete(0, "end")
        self.m_ventana.dni_entrada.delete(0, "end")
        self.m_ventana.dia_entrada.delete(0, "end")
        self.m_ventana.horario_entrada.delete(0, "end")
