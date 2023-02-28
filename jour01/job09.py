class Produit:

    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def changerNom(self, nom):
        self.nom = nom

    def changerPrix(self, prix):
        self.prixHT = prix

    def changerTVA(self, TVA):
        self.TVA = TVA

    def Nom(self):
        return self.nom

    def PrixHT(self):
        return self.prixHT

    def tva(self):
        return self.TVA

    # retourne le prix du produit (toutes taxes comprises)
    def CalculerPrixTTC(self):
        return self.prixHT+self.TVA

    # affiche les informations relatives au produit
    def afficher(self):
        print("Nom:", self.nom, "\nPrix Hors Taxes:", self.prixHT, "\nTVA:", self.TVA, "\nPrix TTC:", self.CalculerPrixTTC())


lait = Produit("lait", 1.99, 0.99)
lait.afficher()
sel = Produit("Sel", 2.49, 0.49)
sel.afficher()

print(lait.CalculerPrixTTC())
print(sel.CalculerPrixTTC())

lait.changerPrix(2.99)
sel.changerPrix(1.99)

lait.afficher()
print(lait.Nom())
print(lait.PrixHT())
print(lait.tva())
print(lait.CalculerPrixTTC())

sel.afficher()
print(sel.CalculerPrixTTC())
