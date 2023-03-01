import random


class Personnage:

    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def getNom(self):
        return self.__nom

    def getVie(self):
        return self.__vie

    def enleverVie(self, nbre):
        self.__vie -= nbre
        print(self.__nom, "reçoit", nbre,"dégats !")

    def attaquer(self, personnage):
        print(self.__nom, "attaque", personnage.getNom(), "!")
        personnage.enleverVie(random.randint(1, 6))

    def soigner(self):
        nbre = random.randint(2, 6)
        if nbre > 3:
            self.__vie += nbre
            print("\nSoin de", nbre, "PV pour", self.__nom, "!")
        else:
            print("\nLe pouvoir SOINS de", self.__nom, "a raté !")


class Jeu:

    def __init__(self):
        self.__niveau = 0

    def choisirNiveau(self):
        user_input = input("Choisir le niveau de difficulté 1: FACILE, 2: NORMAL, 3: DIFFICILE :\n")
        try:
            user_input = int(user_input)
            if 1 <= user_input <= 3:
                self.__niveau = user_input
                self.lancerJeu(self.__niveau)
            else:
                print("L'entrée n'est pas valide !")
        except:
            print("L'entrée n'est pas valide !")

    def lancerJeu(self, niveau):
        running = True
        joueur: Personnage
        ennemi: Personnage
        # NORMAL
        if niveau == 2:
            joueur = Personnage("Joueur", 25)
            ennemi = Personnage("Ennemi", 25)
        # DIFFICILE
        elif niveau == 3:
            joueur = Personnage("Joueur", 20)
            ennemi = Personnage("Ennemi", 30)
        # FACILE
        else:
            joueur = Personnage("Joueur", 20)
            ennemi = Personnage("Ennemi", 15)
        while running:
            self.afficher_stats(joueur, ennemi)
            # attend l'input de l'utilisateur
            input_valide = False
            while not input_valide:
                print("-\t1: ATTAQUER\n-\t2: SOINS")
                user_input = input("Quelle action choisissez-vous ?\n")
                try:
                    user_input = int(user_input)
                    if 1 <= user_input <= 2:
                        input_valide = True
                        print()
                        self.action(joueur, ennemi, user_input)
                    else:
                        print("L'entrée n'est pas valide !")
                except:
                    print("L'entrée n'est pas valide !")
            if ennemi.getVie() > 0:
                self.action(ennemi, joueur, random.randint(1, 2))
            running = self.check_stats(joueur, ennemi)

    def action(self, personnage, adversaire, index):
        if index == 2:
            personnage.soigner()
        else:
            personnage.attaquer(adversaire)

    def afficher_stats(self, joueur, ennemi):
        print()
        print(joueur.getNom(), ":", joueur.getVie())
        print(ennemi.getNom(), ":", ennemi.getVie())

    def check_stats(self, joueur, ennemi):
        if ennemi.getVie() <= 0:
            print("\nGame Over! Vous avez triomphé !")
            return False
        elif joueur.getVie() <= 0:
            print("\nGame Over! Vous avez succombé !")
            return False
        return True


jeu = Jeu()
jeu.choisirNiveau()
