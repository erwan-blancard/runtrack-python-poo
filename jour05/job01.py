"""def factorielle(n, total=1):
    if n > 1:
        factorielle(n-1, total=total*n)
    else:
        print(total)


factorielle(5)
factorielle(0)"""


def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


user_input = input("Donner un nombre (n!): ")
try:
    print(factorielle(int(user_input)))
except:
    print("Entrée invalide")
