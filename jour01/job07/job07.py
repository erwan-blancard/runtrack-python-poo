# classe Personnage ayant des coordonnées x et y
# capable de bouger dans une matrice (qui s'étend de gauche à droite et du haut vers le bas)
class Personnage:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return self.x, self.y


joueur = Personnage(0, 0)

print(joueur.position())

joueur.droite()
print(joueur.position())
joueur.gauche()
print(joueur.position())
joueur.bas()
print(joueur.position())
joueur.haut()
print(joueur.position())