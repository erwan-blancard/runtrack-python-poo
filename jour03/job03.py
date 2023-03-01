STATUTS = ["À faire", "Terminée"]


class Tache:

    def __init__(self, titre, desc, statut: bool):
        self.__titre = titre
        self.__desc = desc
        self.__statut = statut

    def get_titre(self):
        return self.__titre

    def get_desc(self):
        return self.__desc

    def get_statut(self):
        return self.__statut

    def set_statut(self, statut: bool):
        self.__statut = statut


class ListeDeTaches:

    def __init__(self, taches: list[Tache] = []):
        self.__taches = taches

    def ajouterTache(self, tache: Tache):
        self.__taches.append(tache)

    def supprimerTache(self, tache):
        try:
            self.__taches.remove(tache)
        except:
            print("La tache n'existe pas")

    def marquerCommeFinie(self, tache):
        try:
            self.__taches[self.__taches.index(tache)].set_statut(True)
        except:
            print("La tache n'existe pas")

    def afficherListe(self):
        for tache in self.__taches:
            print("- ", tache.get_titre(), tache.get_desc(), STATUTS[tache.get_statut()])

    def filtrerListe(self, statut: bool):
        print("Affichage des taches avec le statut:", STATUTS[statut])
        for tache in self.__taches:
            if tache.get_statut() == statut:
                print("- ", tache.get_titre(), tache.get_desc())


tache1 = Tache("Finir POO", "Finir la runtrack poo", False)
tache2 = Tache("Jouer à Valorant", "Devenir un PGM sur Valorant", False)
tache3 = Tache("Créer une tache", "Créer une tache", False)
tache4 = Tache("Tache", "Une desc de Tache", False)

liste = ListeDeTaches([tache1, tache2, tache3])
liste.afficherListe()
liste.marquerCommeFinie(tache3)
liste.filtrerListe(True)
liste.ajouterTache(tache4)
liste.afficherListe()
liste.supprimerTache(tache4)
liste.afficherListe()
