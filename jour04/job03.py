class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def périmètre(self):
        return (self.__longueur + self.__largeur)*2

    def surface(self):
        return self.__longueur*self.__largeur

    def getLongueur(self):
        return self.__longueur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def getLargeur(self):
        return self.__largeur

    def setLargeur(self, largeur):
        self.__largeur = largeur


class Parallélépipède(Rectangle):

    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.getLongueur()*self.getLargeur()*self.__hauteur


rect = Rectangle(10, 6)
print("Longueur:", rect.getLongueur(), "Largeur:", rect.getLargeur(), "Périmètre:", rect.périmètre(), "Surface:", rect.surface())
rect.setLongueur(15)
rect.setLargeur(5)
print("Longueur:", rect.getLongueur(), "Largeur:", rect.getLargeur(), "Périmètre:", rect.périmètre(), "Surface:", rect.surface())

paral = Parallélépipède(15, 15, 6)
print("\nVolume:", paral.volume())

