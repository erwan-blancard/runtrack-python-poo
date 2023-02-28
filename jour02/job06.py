STATUTS = ["En cours", "Terminée", "Annulée"]


class Commande:

    def __init__(self, numero_commande, liste_plats: dict = dict()):
        self.__numero_commande = numero_commande
        self.__liste_plats = liste_plats
        self.__statut = 0

    def ajouter_plat(self, plat: str, prix: int):
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
        print("Total:", self.__calculer_prix(), "\nTVA:", self.calculer_TVA(), "\nStatut:", STATUTS[self.__statut])

commande = Commande(5465635, {"jlkj": 55})
commande.afficher_commande()

commande.ajouter_plat("gk", 65)
commande.afficher_commande()
