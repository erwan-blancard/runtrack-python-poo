STATUTS = ["En cours", "Terminée", "Annulée"]


class Commande:

    def __init__(self, numero_commande, liste_plats: dict = dict()):
        self.__numero_commande = numero_commande
        self.__liste_plats = liste_plats
        self.__statut = 0

    def ajouter_plat(self, plat: str, prix):
        self.__liste_plats[plat] = prix

    def annuler(self):
        self.__statut = 2

    def __calculer_prix(self):
        prix_total = 0
        for plat in self.__liste_plats:
            prix_total += self.__liste_plats[plat]
        return prix_total

    # calcule la TVA pour un taux de 20%
    def calculer_TVA(self):
        return self.__calculer_prix()*0.2

    def afficher_commande(self):
        for plat in self.__liste_plats:
            print(plat + ":", self.__liste_plats[plat])
        print("Total:", round(self.__calculer_prix(), 2), "\nTVA:", round(self.calculer_TVA(), 2), "\nStatut:", STATUTS[self.__statut])


commande = Commande(5465635, {"Couscous": 20.99})
commande.afficher_commande()

commande.ajouter_plat("Pizza Fromage", 9.99)
commande.afficher_commande()
