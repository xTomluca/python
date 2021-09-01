import mysql.connector

TRUE = 1
FALSE = 0


def creacion_conexion_db():
    global bd
    bd = mysql.connector.connect(host="localhost", user="root", passwd="")
    micursor = bd.cursor(buffered=True)
    try:
        micursor.execute("CREATE DATABASE entrega")
        bd = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )
        micursor = bd.cursor(buffered=True)
        micursor.execute(
            "CREATE TABLE paciente( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, apellido varchar(128) COLLATE utf8_spanish2_ci NOT NULL, dni VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, dia date NOT NULL, hora int(11) NOT NULL, minuto int(11) NOT NULL )"
        )
        """
        bd = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )
        micursor = bd.cursor(buffered=True)
        return micursor
        """
        return mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )

    except Exception:

        return mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )
        """
        bd = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )
        micursor = bd.cursor(buffered=True)
        return micursor"""


def tabla_inicializada(micursor):
    print("ENTRO")
    micursor.execute("select count(*) from paciente")
    cantidad_elementos = []
    print(cantidad_elementos)
    for x in micursor:
        print("FOR")
        cantidad_elementos.append(x)
        print(cantidad_elementos)
    if cantidad_elementos[0][0] != 0:
        print("cantidad elementos distinto 0")
        return TRUE
    return FALSE


bd = creacion_conexion_db()
micursor = bd.cursor(buffered=True)
print(bd)
