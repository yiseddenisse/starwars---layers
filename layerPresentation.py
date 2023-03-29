import os
from flask import Flask, jsonify
import layerBusinessLogic

print("Application startup")
#port = int(os.environ['PORT'])
port = 3000
print("PORT::", port)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def list_movies():
    movies = layerBusinessLogic.movies_sorted()
    return jsonify(movies)

@app.route("/characters/<int:movie_id>", methods=['GET'])
def list_characters(movie_id):
    characters = layerBusinessLogic.list_characters(movie_id)
    return jsonify(characters)


if __name__ == "__main__":
    app.run()