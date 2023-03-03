def len_str(string):
    # on essaye de récupérer le premier caractère de la chaîne string (sans la passer dans une variable)
    # si la chaîne est vide, une exception est levée et on retourne 0 comme résultat de len_str()
    try:
        string[0]
        return 1 + len_str(string[1:])
    except:
        return 0


u_input = input("Donner une chaîne de caractères: ")
print(len_str(u_input))
