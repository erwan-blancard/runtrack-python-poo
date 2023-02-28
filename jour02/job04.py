class Student:

    def __init__(self, prenom, nom, numero_etudiant, credits=0):
        self.__prenom = prenom
        self.__nom = nom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    def get_name(self):
        return self.__prenom

    def get_lastname(self):
        return self.__nom

    def get_credits(self):
        return self.__credits

    def __studentEval(self):
        message = "Insuffisant"
        if self.get_credits() >= 90:
            message = "Excellent"
        elif self.get_credits() >= 80:
            message = "Très bien"
        elif self.get_credits() >= 70:
            message = "Bien"
        elif self.get_credits() >= 60:
            message = "Passable"
        return message

    def studentInfo(self):
        print("Prénom:", self.__prenom)
        print("Nom:", self.__nom)
        print("ID:", self.__numero_etudiant)
        self.__level = self.__studentEval()
        print("Niveau:", self.__level)

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits


john = Student("John", "Doe", 145)
john.add_credits(55)
john.add_credits(-85)
john.add_credits(1)

print("Le nombre de crédits de", john.get_name(), john.get_lastname(), "est de", john.get_credits(), "points")

john.studentInfo()
