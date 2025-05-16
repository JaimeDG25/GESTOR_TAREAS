from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from Settings.sql_serve import get_connection,get_sqlalchemy_uri
from Controllers.controle import obtener_pruebas
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = get_sqlalchemy_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    pruebas = obtener_pruebas()  # Aquí obtienes la lista desde SQL Server
    return render_template('index.html', pruebas=pruebas)

if __name__ == '__main__':
    app.run(debug=True)