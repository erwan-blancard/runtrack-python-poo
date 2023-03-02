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

    def __init__(self, age=14):
        super().__init__(age=age)

    def allerEnCours(self):
        print("Je vais en cours.")

    def affichageAge(self):
        print("J'ai", self._age, "ans.")


class Professeur(Personne):

    def __init__(self, matièreEnseignée: str, age=14):
        super().__init__(age=age)
        self.__matièreEnseignée = matièreEnseignée

    def enseigner(self):
        print("Le cours va commencer.")


personne = Personne(24)
eleve = Eleve()
professeur = Professeur("Maths", age=40)

eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.affichageAge()

professeur.bonjour()
professeur.enseigner()
