from PySide6 import QtWidgets
from PySide6.QtWidgets import QListWidgetItem
from movie import Movie
import requests
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CINE CLUB")
        self.setGeometry(200, 200, 400, 500)
        self.setup_ui()
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.add_btn = QtWidgets.QPushButton("Ajouter")
        self.layout.addWidget(self.add_btn)
        
        self.remove_btn = QtWidgets.QPushButton("Supprimer")
        self.layout.addWidget(self.remove_btn)
        self.list_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        self.search_btn = QtWidgets.QPushButton("Rech_ligne")
        self.layout.addWidget(self.search_btn)
        self.search_btn.clicked.connect(self.search_movie_api)

        self.title_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.title_input)
        self.title_input.setPlaceholderText("Titre")

        self.year_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.year_input)
        self.year_input.setPlaceholderText("Annee")

        self.genre_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.genre_input)
        self.genre_input.setPlaceholderText("Genre")

        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setPlaceholderText("Rechercher un film...")
        self.layout.addWidget(self.search_input)

        self.add_btn.clicked.connect(self.add_movie)
        self.remove_btn.clicked.connect(self.remove_movie)
        self.search_input.textChanged.connect(self.filter_movies)
        self.list_widget.itemDoubleClicked.connect(self.load_movie)
        self.list_widget.itemDoubleClicked.connect(self.fill_fields_from_api)
        self.refresh_list()

    def add_movie(self):
        title = self.title_input.text()
        year = self.year_input.text()
        genre = self.genre_input.text()
        if not title or not year or not genre:
            QtWidgets.QMessageBox.warning(self, "Erreur", "tous les champs sont requis")
            return
        if hasattr(self, "current_movie_title"):
            Movie.remove_from_movies(self.current_movie_title)
            del self.current_movie_title

        movie = Movie(title, year, genre)
        Movie.add_to_movies(movie)
        QtWidgets.QMessageBox.information(self, "Succes", f"{title} enregistre !")
        self.clear_fields()
        self.refresh_list()
    def remove_movie(self):
        print ("bouton suppremer clique")
        selected_item = self.list_widget.currentItem()
        if not selected_item:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Selectionne un film")
            return
        
        
        text = selected_item.text()
        title = text.split("(")[0].strip()
        Movie.remove_from_movies(title)
        QtWidgets.QMessageBox.information(self, "Succes", f"{title} supprime !")
        self.clear_fields()
        self.refresh_list()
        
        
    def filter_movies(self):
        search_text = self.search_input.text().lower()
        self.list_widget.clear()
        movies = Movie.get_movies()
        for movie in movies:
            if (search_text in movie.title.lower() or 
                search_text in movie.year.lower() or
                search_text in movie.genre.lower()):
                self.list_widget.addItem(f"{movie.title} ({movie.year} - {movie.genre})")
    def load_movie(self, item):
        movie = item.data(0)
        if isinstance(movie, dict):
            title = movie.get("title", "")
            year = movie.get("release_date", "")
            genre = "Non Donne"
        else:
            text = item.text()
            title = text.split("(")[0]
            year = text.split("(")[1].split(")")[0]
            genre = text.split("- ")[1] if " - " in text else ""

        self.title_input.setText(title)
        self.year_input.setText(str(year) if year else "")
        self.genre_input.setText(genre)
        self.current_movie_title = title
    def refresh_list(self):
        self.filter_movies()

    def clear_fields(self):
        self.title_input.clear()
        self.year_input.clear()
        self.genre_input.clear()
    
    def search_movie_api(self):
        print ("Recherche lancee")
        print ("click ok")
        API_KEY = "3458f999c65a1db9d3e4fced2d7bf366"
        query = self.title_input.text()
        print ("Query:", query)
        if not query:
            return
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"
        print ("URL:", url)
        response = requests.get(url)
        print ("STATUS:", response.status_code)
        data = response.json()
        self.list_widget.clear()
        for movie in data.get("results", [])[:10]:
            title = movie.get("title", "")
            year = movie.get("release_date", "")[:4]

            self.list_widget.addItem(f"{title} ({year})")
    def fill_fields_from_api(self, item):
        
        movie = item.data(0)
        if not isinstance(movie, dict):
            return
        title = movie.get("title", "")
        year = movie.get("release_date", "")[4]
        

        self.title_input.setText(title)
        self.year_input.setText(year)
        self.genre_input.setText("")
        


            


            
            
if __name__ == "__main__":

 app = QtWidgets.QApplication([])
 window = App()
 window.show()
 app.exec()

        

        




        
    
    