import os
# from flask import Flask
# import requests
import layerPresentation

#from flask import jsonify

print("Application startup")
#port = int(os.environ['PORT'])
port = 3000
print("PORT::", port)

"""
app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"


@app.route("/", methods=['GET'])
def list_movies():
    data = requests.get(movie_url).json()
    # movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    movies = []
    for movie in data["results"]:
        movies.append({
            "id": movie["episode_id"],
            "name": movie["title"]
        })

    return jsonify(movies)
"""

if __name__ == "__main__":
    layerPresentation.app.run(host="0.0.0.0", debug=True, port=port)
