class Personne:

    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.prenom, self.nom)


# création d'une liste d'objets Personne ayant chacun un nom et un prénom
personnes = [
    Personne("John", "Delarue"),
    Personne("Marc", "Legrand"),
    Personne("Théo", "Dizos")
]

# affiche le nom de chaque personne dans la liste
for personne in personnes:
    personne.SePresenter()
