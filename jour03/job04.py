class Joueur:

    def __init__(self, prenom, nom, position, nombre_buts, passes_decisives, cartons_jaunes, cartons_rouges):
        self.__nom = nom
        self.__prenom = prenom
        self.__position = position
        self.__nombre_buts = nombre_buts
        self.__passes_decisives = passes_decisives
        self.__cartons_jaunes = cartons_jaunes
        self.__cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.__nombre_buts += 1

    def effectuerUnePasseDecisive(self):
        self.__passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1

    def afficherStatistiques(self):
        print("Joueur:", self.__prenom, self.__nom,
              "\n- Position:", self.__position,
              "\n- Nombre de buts marqués:", self.__nombre_buts,
              "\n- Passes décisives:", self.__passes_decisives,
              "\n- Cartons Jaunes:", self.__cartons_jaunes,
              "\n- Cartons Rouges:", self.__cartons_rouges)


class Equipe:

    def __init__(self, nom, liste_joueurs: list[Joueur]):
        self.__nom = nom
        self.__liste_joueurs = liste_joueurs

    def ajouterJoueur(self, joueur):
        self.__liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        print("Joueurs de l'équipe " + self.__nom + ":")
        for joueur in self.__liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, but=False, passe_decisive=False, carton_jaune=False, carton_rouge=False):
        try:
            joueur_in = self.__liste_joueurs[self.__liste_joueurs.index(joueur)]
            if but:
                joueur_in.marquerUnBut()
            if passe_decisive:
                joueur_in.effectuerUnePasseDecisive()
            if carton_jaune:
                joueur_in.recevoirUnCartonJaune()
            if carton_rouge:
                joueur_in.recevoirUnCartonRouge()
        except:
            print("Le Joueur n'existe pas")


rene = Joueur("René", "LeGrand", "Défenseur", 0, 6, 1, 0)
richard = Joueur("Richard", "Mernier", "Attaquant", 6, 7, 2, 0)
pierre = Joueur("Pierre", "Pastis", "Attaquant", 8, 3, 1, 1)

pierrot = Joueur("Pierrot", "LeGrand", "Défenseur", 0, 6, 1, 0)
marc = Joueur("Marc", "Mernier", "Attaquant", 6, 7, 2, 0)
tristan = Joueur("Tristan", "Pastis", "Attaquant", 8, 3, 1, 1)

equipe1 = Equipe("Les Pastagas", [richard, rene, pierre])
equipe2 = Equipe("Les Ricards", [pierrot, marc, tristan])

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(rene, but=True, carton_jaune=True)
equipe2.mettreAJourStatistiquesJoueur(pierrot, passe_decisive=True, carton_rouge=True)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()
