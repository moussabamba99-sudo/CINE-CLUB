def ajouter(self, film):
    self.films.append(film)
    self.sauvegarder()
    return self.films

def retirer(self, film):
    self.films.remove(film)
    self.sauvegarder()
    return self.films

def creer(self, titre, annee, genre):
    film = {"titre": titre, "annee": annee, "genre": genre}
    return film
