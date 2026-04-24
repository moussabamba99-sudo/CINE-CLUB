from movie import Movie
def menu():
    print ("\n === CINE CLUB ===")
    print ("1. Ajouter un film")
    print ("2. Supprimer un film")
    print ("3. Voir tous les films")
    print ("4. Quitter")
def add_movie():
    title = input("Titre du film : ")
    year = input("Annee du film : ")
    genre = input("Genre du film : ")
    movie = Movie(title, year, genre)
    Movie.add_to_movies(movie)
    print (f" '{title}' ajoute avec succes!")

def remove_movie():
        title = input("Titre du film a supprimer : ")
        Movie.remove_from_movies(title)
        print (f" '{title}' supprime (si present).")

def show_movies():
        movies = Movie.get_movies()
        if not movies:
            print ("aucun film dans la liste")
            return
        print ("\n Liste des films: ")
        for i, movie in enumerate(movies, 1):
            print (f"{i}. {movie.title} {movie.year} {movie.genre}")
def main():
        while True:
            menu()
            choice = input("Choix : ")

            if choice == "1":
                add_movie()
            elif choice == "2":
                remove_movie()
            elif choice == "3":
                show_movies()
            elif choice == "4":
                print ("Fin de seance.... A bientot !")
                break
            else:
                print (" choix invalide. ")
if __name__ == "__main__":
     main()
    
        


