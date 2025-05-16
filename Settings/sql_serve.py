# Settings/sql_server.py
import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=DESKTOP-0JUDDFN\\SQLEXPRESS;DATABASE=GESTORTAREAS;UID=;PWD='
        )
        print("Conexión exitosa.")
        return connection
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
        return None
    
def get_sqlalchemy_uri():
    return (
        "mssql+pyodbc://@DESKTOP-0JUDDFN\\SQLEXPRESS/GESTORTAREAS"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )