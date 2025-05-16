from Settings.sql_serve import get_connection,get_sqlalchemy_uri
from Models.modelo import Prueba
from flask_sqlalchemy import SQLAlchemy

def obtener_pruebas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, dni, fecha FROM prueba")
    rows = cursor.fetchall()
    conn.close()
    
    pruebas = []
    for row in rows:
        prueba = Prueba(id=row[0], nombre=row[1], dni=row[2], fecha=row[3])
        pruebas.append(prueba)
        print(prueba.id)
    
    return pruebas