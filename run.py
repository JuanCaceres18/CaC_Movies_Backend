from flask import Flask
from app.views import *
from app.database import init_app

app = Flask(__name__)

# Inicializo conexión con la base de datos en la app Flask
init_app(app)

# Ruta - Primera interacción con Flask
app.route("/", methods=["GET"])(index)
# Ruta - Consultar películas
app.route("/api/movies/", methods=["GET"])(get_all_movies)
# Ruta - Consultar una sola película con ID pasado como argumento
app.route("/api/movies/<int:id_movie>", methods=["GET"])(get_movie)
# Ruta - Agregar película a base de datos
app.route("/api/movies/", methods=["POST"])(create_movie)
# Ruta - Editar película
app.route("/api/movies/<int:id_movie>", methods=["PUT"])(update_movie)
# Ruta - Eliminar película
app.route("/api/movies/<int:id_movie>", methods=["DELETE"])(delete_movie)


if __name__ == "__main__":
    app.run(debug=True)