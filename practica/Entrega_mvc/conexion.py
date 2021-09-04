import mysql.connector


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

        return mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )

    except Exception:

        return mysql.connector.connect(
            host="localhost", user="root", passwd="", database="entrega"
        )


def tabla_inicializada(micursor):
    micursor.execute("select count(*) from paciente")
    cantidad_elementos = []
    for x in micursor:
        cantidad_elementos.append(x)
    if cantidad_elementos[0][0] != 0:
        return True
    return False


bd = creacion_conexion_db()
micursor = bd.cursor(buffered=True)
