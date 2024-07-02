import os
import mysql.connector
from flask import g
from dotenv import load_dotenv

# Cargamos las variables de entorno del archivo .env
load_dotenv()

# Configuración de la BBDD
DATABASE_CONFIG = {
    "user": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", 3306),
    "database": os.getenv("DB_NAME")
}

# Función para obtener la conexión a la base de datos
def get_db():
    # Si db no está en el contexto global de g, entonces...
    if "db" not in g:
         # Creo nueva conexión a la base de datos
        g.db = mysql.connector.connect(**DATABASE_CONFIG) # Desempaquetado
    return g.db

# Función para cerrar la base de datos
def close_db(e=None):
    db = g.pop("db", None) # Extraigo la conexión a la base de datos y la elimino
    if db is not None: # Si la base de datos ya existe, entonces la cierro
        db.close()

# Funció para inicializar la app con el manejo de la base de datos
def init_app(app):
    # Registrar close_db para que se ejecute al final del contexto de la app
    app.teardown_appcontext(close_db)
