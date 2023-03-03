def power(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)


x_input = input("Donner un nombre (x): ")
n_input = input("Donner un nombre (n): ")
try:
    x_input = int(x_input)
    n_input = int(n_input)
    print(power(x_input, n_input))
except:
    print("Entrée invalide")
