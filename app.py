import sys
from PySide6 import QtWidgets

class app(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CINE CLUB")
        self.setMinimumSize(400, 200)
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("Bienvenue au CINE CLUB")
        self.input_film = QtWidgets.QLineEdit()
        self.buttun = QtWidgets.QPushButton("Ajouter")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_film)
        self.layout.addWidget(self.buttun)
    
    def set_default_values(self):
        self.input_film.setPlaceholderText("Entrez le nom du film")
    def setup_connections(self):
        self.buttun.clicked.connect(self.compute)
    def compute(self):
        film = self.input_film.text()
        if film:
            self.label.setText(f"Film ajoute : {film}")
            self.input_film.clear()
        else:
            self.label.setText("Veuillez entrer un film")

        
    
        





      
app_instance = QtWidgets.QApplication(sys.argv)
win = app() # Instantiate your custom app class
win.show()
sys.exit(app_instance.exec())


        



        
    
    