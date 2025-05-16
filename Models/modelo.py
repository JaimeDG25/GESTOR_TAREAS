from Settings.sql_serve import get_connection

class Prueba:
    def __init__(self, id, nombre, dni, fecha):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.fecha = fecha