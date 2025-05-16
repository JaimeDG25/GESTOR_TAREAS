def get_sqlalchemy_uri():
    return (
        "mssql+pyodbc://@DESKTOP-0JUDDFN\\SQLEXPRESS/GESTORTAREAS"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )