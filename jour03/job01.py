class Ville:

    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def set_nombre_habitants(self, nombre_habitants):
        self.__nombre_habitants = nombre_habitants


class Personne:

    def __init__(self, nom, age, ville: Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.set_nombre_habitants(self.__ville.get_nombre_habitants()+1)


paris = Ville("Paris", 1000000)
print("Population de Paris:", paris.get_nombre_habitants())

marseille = Ville("Marseille", 861635)
print("Population de Marseille:", marseille.get_nombre_habitants())

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print("Population de Paris:", paris.get_nombre_habitants())
print("Population de Marseille:", marseille.get_nombre_habitants())
