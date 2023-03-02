class Vehicule:

    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def informationsVehicule(self):
        print("Marque:", self.__marque, "\nModèle:", self.__modele, "\nAnnée:", self.__annee, "\nPrix:", self.__prix)

    def demarrer(self):
        print("Attention, je roule")
        

class Voiture(Vehicule):
    
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Portes:", self.__portes)

    def demarrer(self):
        print("Attention, la voiture démarre")


class Moto(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Roues:", self.__roues)

    def demarrer(self):
        print("Attention, la moto démarre")


voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()
voiture.demarrer()

moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
moto.demarrer()