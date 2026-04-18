import sys
from PySide6.QtWidgets import QApplication 
from ui.app import app
from gestionnaire.movie import movie
app = QApplication(sys.argv)

movie = movie()
win = app(movie)
win.show()
sys.exit(app.exec())