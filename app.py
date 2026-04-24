from PySide6 import QtWidgets
from movie import Movie
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
        self.add_btn.clicked.connect(self.remove_movie)
        self.search_input.textChanged.connect(self.filter_movies)

        self.refresh_list()

    def add_movie(self):
        title = self.title_input.text()
        year = self.year_input.text()
        genre = self.genre_input.text()
        if not title or not year or not genre:
            QtWidgets.QMessageBox.warninf(self, "Erreur", "tous les champs sont requis")
            return
        movie = Movie(title, year, genre)
        Movie.add_to_movies(movie)
        QtWidgets.QMessageBox.information(self, "Succes", f"{title} ajoute !")
        self.clear_fields()
        self.refresh_list()
    def remove_movie(self):
        selected_item = self.list_widget.currentItem()
        if not selected_item:
            QtWidgets.QMessageBox.warning(self, "Erreur", "selectionne un film")
            return
        text = selected_item.text()
        title = text.split("(")[0]
        Movie.remove_from_movies(title)
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
    def refresh_list(self):
        self.filter_movies()

    def clear_fields(self):
        self.title_input.clear()
        self.year_input.clear()
        self.genre_input.clear()
if __name__ == "__main__":

 app = QtWidgets.QApplication([])
 window = App()
 window.show()
 app.exec()

        




        
    
    