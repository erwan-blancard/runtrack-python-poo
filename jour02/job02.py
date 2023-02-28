class Livre:

    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def getTitre(self):
        return self.__titre

    def getAuteur(self):
        return self.__auteur

    def getPages(self):
        return self.__pages

    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setPages(self, pages):
        # nombres entiers positifs --> N {0, INF}
        if pages >= 0:
            self.__pages = pages
        else:
            print("Le nombre de pages saisies est invalide ("+str(pages)+")")


harrypotter = Livre("Harry Potter", "JK Rolling", 555)
print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages())

harrypotter.setTitre("Pas Harry Potter")
harrypotter.setAuteur("JK Bro")

harrypotter.setPages(1111)

print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages())

harrypotter.setPages(0)

print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages())

harrypotter.setPages(-22)

print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages())
