import random


class Carte:

    def __init__(self, valeur, couleur):
        self._valeur = valeur
        self._couleur = couleur

    def getNom(self):
        return str(self._valeur)+" de "+self._couleur

    def getPoints(self):
        return self._valeur

    def getCouleur(self):
        return self._couleur


class CarteFigure(Carte):

    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)

    def getNom(self):
        nom = str(self._valeur)
        # attribut un nom à la carte
        if self._valeur == 11:
            nom = "Valet"
        elif self._valeur == 12:
            nom = "Reine"
        elif self._valeur == 13:
            nom = "Roi"
        return nom +" de "+self._couleur

    def getPoints(self):
        return 10


class CarteAs(Carte):

    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)

    def getNom(self):
        return "As de " + self._couleur


class Jeu:

    def __init__(self, valeur_as):
        self.__valeur_as = valeur_as
        self.__paquet: list[Carte] = []
        self.remplirPaquet()
        self.lancerJeu()

    def remplirPaquet(self):
        for valeur in range(13):
            for couleur in ["Pique", "Trèfle", "Coeur", "Carreau"]:
                # si la carte est un as
                if valeur+1 == 1:
                    self.__paquet.append(CarteAs(self.__valeur_as, couleur))
                # si la carte est une figure
                elif valeur+1 > 10:
                    self.__paquet.append(CarteFigure(valeur+1, couleur))
                # si la carte est un nombre
                else:
                    self.__paquet.append(Carte(valeur+1, couleur))

    def lancerJeu(self):
        main_joueur: list[Carte] = []
        self.piocherCarte(main_joueur)
        self.piocherCarte(main_joueur)
        main_croupier: list[Carte] = []
        self.piocherCarte(main_croupier)
        self.piocherCarte(main_croupier)
        passe = False
        # boucle de jeu
        print("Bienvenue au BLACKJACK !\n\nRappelons que pour ce jeu, un as vaut", self.__valeur_as, "point(s) !")
        while True:
            # affiche la main du joueur
            print("\nVotre main (" + str(self.calculerTotalMain(main_joueur)) + " points):")
            for carte in main_joueur:
                print("-", carte.getNom(), "(" + str(carte.getPoints()) + " points)")
            if not passe and self.calculerTotalMain(main_joueur) <= 21:
                # attend l'input de l'utilisateur
                input_valide = False
                while not input_valide:
                    print("\n-\t1: PIOCHER UNE CARTE\n-\t2: PASSER")
                    user_input = input("Quelle action choisissez-vous ?\n")
                    try:
                        user_input = int(user_input)
                        if 1 <= user_input <= 2:
                            input_valide = True
                            if user_input == 1:
                                self.piocherCarte(main_joueur)
                            else:
                                passe = True
                        else:
                            print("L'entrée n'est pas valide !")
                    except:
                        print("L'entrée n'est pas valide !")
            elif self.calculerTotalMain(main_joueur) > 21:
                print("\nPerdu ! Votre main fait plus de 21 points !\nLe Croupier gagne !")
                break
            # si le joueur a passé, le croupier pioche des cartes
            if passe:
                if self.calculerTotalMain(main_croupier) < 17:
                    self.piocherCarte(main_croupier)
                    # si la main du croupier dépasse 21 points, le joueur gagne
                    if self.calculerTotalMain(main_croupier) > 21:
                        print("\nGagné ! La main du Croupier fait plus de 21 points !")
                        break
                else:
                    # si la main du joueur est plus petite que le croupier, il perd, sinon il gagne
                    if self.calculerTotalMain(main_joueur) < self.calculerTotalMain(main_croupier):
                        print("\nVotre main (" + str(self.calculerTotalMain(main_joueur)) + " points) est plus petite que celle du Croupier (" + str(self.calculerTotalMain(main_croupier)) + " points).\nVous avez perdu !")
                        break
                    else:
                        print("\nVotre main (" + str(self.calculerTotalMain(main_joueur)) + " points) est plus élevée que celle du Croupier (" + str(self.calculerTotalMain(main_croupier)) + " points).\nVous avez gagné !")
                        break

    # enlève une carte du paquet et la met dans la main passée en argument
    def piocherCarte(self, main: list[Carte]):
        # index de la carte à piocher
        index = random.randint(0, len(self.__paquet)-1)
        main.append(self.__paquet[index])
        self.__paquet.pop(index)

    def calculerTotalMain(self, main: list[Carte]):
        total = 0
        for carte in main:
            total += carte.getPoints()
        return total


# boucle principale (choix valeur as, rejouer)
running = True
while running:
    input_valide = False
    while not input_valide:
        user_input = input("Quel valeur les as devront avoir lors de cette partie ? 1: 1 POINT, 2: 11 POINTS.\n")
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 2:
                input_valide = True
                if user_input == 1:
                    jeu = Jeu(1)
                else:
                    jeu = Jeu(11)
            else:
                print("L'entrée n'est pas valide !")
        except:
            print("L'entrée n'est pas valide !")

    user_input = input("Voulez-vous rejouer ? (y/n)\n")
    if not (user_input == "y" or user_input == "Y"):
        running = False