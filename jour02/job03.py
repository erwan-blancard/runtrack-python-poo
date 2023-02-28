class Livre:

    def __init__(self, titre, auteur, pages, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = disponible

    def getTitre(self):
        return self.__titre

    def getAuteur(self):
        return self.__auteur

    def getPages(self):
        return self.__pages

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.vérification():
            self.__disponible = False

    def rendre(self):
        if not self.vérification():
            self.__disponible = True

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
print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages(), harrypotter.vérification())

harrypotter.rendre()
print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages(), harrypotter.vérification())

harrypotter.emprunter()
print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages(), harrypotter.vérification())

harrypotter.emprunter()
print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages(), harrypotter.vérification())

harrypotter.rendre()
print(harrypotter.getTitre(), harrypotter.getAuteur(), harrypotter.getPages(), harrypotter.vérification())
