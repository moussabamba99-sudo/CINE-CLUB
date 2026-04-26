import json
class Movie:
    fichier = "C:/Users/Panasonic/Documents/PROJET_CINE_CLUB/gestionnaire/movies.json"
    def __init__(self, title, year, genre):
        
        self.title = title
        self.year = year
        self.genre = genre
    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre
            }
    @classmethod
    def _get_movies(cls):
        try:
            with open(cls.fichier, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    @classmethod
    def _write_movies(cls, movies):
        with open(cls.fichier, "w", encoding="utf-8") as f:
         json.dump(movies, f, indent=4)
    @classmethod
    def add_to_movies(cls, movie):
        movies = cls._get_movies()
        movies.append(movie.to_dict())
        cls._write_movies(movies)
    @classmethod
    def get_movies(cls):
        movies_data = cls._get_movies()
        return [cls(m["title"], m["year"], m["genre"]) for m in movies_data]
    @classmethod
    def remove_from_movies(cls, title):
        movies = cls._get_movies()
        print ("Titre a supprimer:", title)
        print ("Avant: ", movies)
        movies = [m for m in movies if m["title"].strip().lower() != title.strip().lower()]
        print ("Apres : ", movies)
        cls._write_movies(movies)
    


        