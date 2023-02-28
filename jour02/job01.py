class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

rect = Rectangle(10, 5)
print(rect.getLongueur(), rect.getLargeur())

rect.setLongueur(55)
rect.setLargeur(40)

print(rect.getLongueur(), rect.getLargeur())
