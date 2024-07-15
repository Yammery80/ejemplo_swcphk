import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/usuarios')
def usuarios():
    # Conectar con DB(DataBase)
    conexion = psycopg2.connect(
        database="swcphk-faby-2024",
        user="postgres",
        password="Lindel2005",
        host="localhost",
        port="5432"
    )
    # Crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    # Ejecutar una consulta en PostgreSQL
    cursor.execute('''SELECT * FROM usuarios''')
    # Recuperar información
    datos = cursor.fetchall()
    # Cerrar cursor y conexión a la base de datos
    cursor.close()
    conexion.close()
    return render_template('usuarios.html', datos=datos)

