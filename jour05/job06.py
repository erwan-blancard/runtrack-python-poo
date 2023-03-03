"""Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce
plateau n dames de jeu d'échecs, de manière à ce qu’aucune dame ne puisse se
“prendre”, quand cela est possible. La valeur de n'est renseignée par l’utilisateur. Quand
cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le
caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames."""


def creer_plateau(n, dames_pos):
    if n < 0:
        return []
    if n == 0:
        return dames_pos
    else:
        dames_pos.append(check_position(n, dames_pos))
        return creer_plateau(n-1, dames_pos)


def check_position(n, dames_pos):
    """next_pos = -1

    for col in range(n):
        i = 0
        while i < len(dames_pos):
            x = dames_pos[i]
            # diagonale en bas vers la droite
            if x + 1 + i < n and col != x + 1 + i and not (col in dames_pos and x + 1 + i in dames_pos):
                return x + 1 + i
            # diagonale en bas vers la gauche
            elif x - 1 - i >= 0 and col != x - 1 - i and not (col in dames_pos and x - 1 - i in dames_pos):
                return x - 1 - i
            i += 1

    return next_pos"""

    x_invalides = []

    i = 0
    while i < len(dames_pos):
        x = dames_pos[i]
        x_invalides.append(x)
        # diagonales en bas vers la droite
        if x + (len(dames_pos)-i) < n:
            x_invalides.append(x + (len(dames_pos)-i))
        # diagonales en bas vers la gauche
        if x - (len(dames_pos)-i) >= 0:
            x_invalides.append(x - (len(dames_pos)-i))
        i += 1

    for x in range(n):
        if (n-1-x) not in x_invalides:
            print("x:", (n-1-x))
            return n-1-x

    return -1


def dessiner_plateau(dames_pos: list):
    for col in range(len(dames_pos)):
        ligne_str = ""
        for row in range(len(dames_pos)):
            if row == dames_pos[col]:
                ligne_str += "X "
            else:
                ligne_str += "O "
        print(ligne_str)


print("Avertissement: le programme n'est pas fonctionnel.")
user_input = input("Saisir un entier (taille du plateau): ")
try:
    dessiner_plateau(creer_plateau(int(user_input)-1, [0]))
except Exception as e:
    print("Entrée invalide:", str(e))
