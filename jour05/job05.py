def nombre_Fibonacci(n):
    return suite_Fibonacci(n, 0, 1)


def suite_Fibonacci(n, a, b):
    # si le nombre entré est 3, la fonction retourne a+b (l'addition des 2 derniers termes)
    if n == 3:
        return a+b
    # si le nombre entré est 2, la fonction retourne b (donc 1)
    elif n == 2:
        return b
    # si le nombre entré est 1, la fonction retourne a (donc 0)
    elif n == 1:
        return a
    # si le nombre entré est 0, la fonction retourne None (invalide)
    elif n == 0:
        return None
    else:
        # a devient b et b devient a+b
        return suite_Fibonacci(n-1, b, a+b)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
user_input = input("Donner un nombre (n-ième nombre de la suite de Fibonacci): ")
try:
    print(nombre_Fibonacci(int(user_input)))
except Exception as e:
    print("Entrée invalide:", str(e))
