class Personne:

    def __init__(self, age=14):
        self._age = age

    def afficherAge(self):
        print("Age:", self._age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self._age = age
    

class Eleve(Personne):
    
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print("Je vais en cours.")

    def affichageAge(self):
        print("J'ai", self._age, "ans.")


class Professeur(Personne):

    def __init__(self, matièreEnseignée: str):
        super().__init__()
        self.__matièreEnseignée = matièreEnseignée

    def enseigner(self):
        print("Le cours va commencer.")


personne = Personne(24)
eleve = Eleve()
professeur = Professeur("Maths")

personne.bonjour()
personne.afficherAge()
personne.modifierAge(28)
personne.afficherAge()

eleve.affichageAge()
eleve.modifierAge(18)
eleve.affichageAge()

professeur.enseigner()
