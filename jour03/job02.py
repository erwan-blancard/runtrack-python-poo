class CompteBancaire:

    def __init__(self, numero_compte, prenom, nom, solde, decouvert=True):
        self.__numero_compte = numero_compte
        self.__prenom = prenom
        self.__nom = nom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Numéro de compte:", self.__numero_compte, "\nTitulaire:", self.__prenom, self.__nom, "\nSolde:", self.__solde)

    def afficherSolde(self):
        print(self.__solde)

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
        else:
            print("Impossible de retirer le montant demandé ("+str(montant)+")")

    def agios(self):
        if self.__decouvert and self.__solde < 0:
            self.__solde = 0

    # permet de faire un virement entre deux comptes
    def virement(self, compte, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte.versement(montant)
        else:
            print("Impossible d'effectuer le versement demandé")


compteA = CompteBancaire(546465416351, "John", "Doe", 512)
compteA.afficher()
compteA.retrait(500)
compteA.retrait(50)
compteA.versement(250)
compteA.afficherSolde()

compteB = CompteBancaire(3513213, "Homer", "Simpson", -23)
compteA.virement(compteB, 23)
compteA.afficher()
compteB.afficher()

