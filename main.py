"""
Programme principal.
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    premier = True
    if p < 2:
        premier = False
        print(str(p) + " inférieur à 2 donc pas premier")
    limit = int(sqrt(p))
    for i in range(2, limit + 1):
        if p % i == 0:
            premier = False
            print(str(p) + " = " + str(i) + " x " + str(p//i))
            break
    print(premier)
    return premier

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print(isprime(4))
    print()


if __name__ == "__main__":
    main()
