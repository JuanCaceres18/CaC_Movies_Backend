from flask import jsonify, request

def index():
    return jsonify({"message": "Hola desde API Python"})

# Obtener todas las películas
def get_all_movies():
    movies = [
        {
            "id_movie": 1,
            "title": "The Office",
            "director": "Greg Daniels",
            "release_date": "2005-01-01",
            "banner": "imagen.jpg"
        },
        {
            "id_movie": 2,
            "title": "Pulp Fiction",
            "director": "Quentin Tarantino",
            "release_date": "1995-01-01",
            "banner": "imagen.jpg"
        }
    ]
    return jsonify(movies)

# Obtener una sola película
def get_movie(id_movie):
    movie = {
        "id_movie":id_movie
    }
    return jsonify(movie)

# Agregar una película
def create_movie():
    data = request.json 
    return jsonify({"message":"Movie created successfully!", "data": data}), 201

# Actualizar película
def update_movie(id_movie):
    data = request.json
    return jsonify({"message":"Movie updated successfully","data":data,"id_movie":id_movie})

# Eliminar película
def delete_movie(id_movie):
    return jsonify({"message":"Movie deleted successfully!", "id_movie":id_movie})