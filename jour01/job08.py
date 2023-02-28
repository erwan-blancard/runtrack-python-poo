import math


class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    # affiche les informations relatives au cercle
    def afficherInfos(self):
        print("rayon:", self.rayon, "circonférence:", self.circonférence(), ", aire:", self.aire(), ", diametre:", self.diametre())

    def circonférence(self):
        return 2*math.pi*self.rayon

    def aire(self):
        return (self.rayon**2)*math.pi

    def diametre(self):
        return self.rayon*2


cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
cercle2.afficherInfos()
