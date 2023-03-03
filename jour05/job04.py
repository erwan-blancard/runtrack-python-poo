def greater_in_list(num_list: list):
    # si la liste est vide, la fonction retourne None
    try:
        num_list[0]
    except:
        return None

    # on essaye de récupérer le deuxième nombre de la liste, si la liste n'a pas de deuxième nombre,
    # une exception est levée et on retourne le premier numéro comme résultat (supposé être le plus grand)
    try:
        num_list[1]
        if num_list[0] < num_list[1]:
            return greater_in_list(num_list[1:])
        else:
            return greater_in_list([num_list[0]]+num_list[2:])
    except:
        return num_list[0]


#                                                   résultats attendus
print(greater_in_list([1, 6, 5, 4]))                # 6
print(greater_in_list([6, 5, 4, 1]))                # 6
print(greater_in_list([1, 1, 1, 0]))                # 1
print(greater_in_list([-2, -71, -1, -88]))          # -1
print(greater_in_list([]))                          # None
print(greater_in_list([-1]))                        # -1
print(greater_in_list([-1, -2]))                    # -1
print(greater_in_list([-2, -1]))                    # -1
print(greater_in_list([-1, -1]))                    # -1
