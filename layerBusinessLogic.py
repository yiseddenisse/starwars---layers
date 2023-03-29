import requests

movie_url = "https://swapi.dev/api/films/"

def movies_sorted():
    data = requests.get(movie_url).json()
    movies = []
    for movie in data["results"]:
        movies.append({
            "id": str(movie["episode_id"]),
            "name": movie["title"]
        })
    sorted_movies = sorted(movies, key=lambda k: k['id'])

    return sorted_movies

def list_characters(movie_id):
    movie_data = requests.get(movie_url + str(movie_id)).json()
    characters = []
    for character_url in movie_data["characters"]:
        character_data = requests.get(character_url).json()
        characters.append(character_data["name"])

    return characters
