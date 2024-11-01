from copy import deepcopy
from random import randrange


def inv (j, K, t, T, x):

    l = t[j : K + 1]
    return 0 <= j <= K and x == T[K] and t[: j] == T[: j] and l == sorted (l)


def insertion (t, K):

    # Initialisation
    n = len(t)
    T = t[:]
    j = K
    x = t[K]

    # Précondition
    assert n > 1 and 0 < K < n and T[: K] == sorted (T[: K]), ""

    # Invariant
    assert inv (j, K, t, T, x), ""

    while j != 0 and t[j - 1] > x:

        # Invariant et condition d'arrêt
        assert inv (j, K, t, T, x), ""
        assert j != 0 and t[j - 1] > x, ""

        j -= 1
        t[j + 1] = t[j]

        # Invariant
        assert inv (j, K, t, T, x), ""

    # Invariant et non condition d'arrêt
    assert inv (j, K, t, T, x), ""

    t[j] = x

    # Postcondition
    assert t[: K + 1] == sorted (t[: K + 1]) and sorted (t[: K + 1]) == sorted (T[: K + 1])


def tri_insertion (t):

    for i in range (1, len(t)):
        insertion (t, i)
    return t


l = [1, 2]
insertion (l, 1)
assert l == [1, 2], ""

l = [2, 1]
insertion (l, 1)
assert l == [1, 2], ""

l = [-5, 3, 4, 1, -8]
insertion (l, 3)
assert l == [-5, 1, 3, 4, -8], ""

def test_tri (tri_a_tester):

    pb=False
    for i in range(1000) : #nombre de tris
        nb=randrange(100) #longueur de la liste a trier
        #génération d'une liste aléatoire de nb nombres de [-10,10]
        T=[randrange(21)-10 for p in range(nb)]
        t=deepcopy(T)
        if sorted(T)!=tri_a_tester(t): #liste triée avec la fonction à tester
            pb=True
            print('Pb :')
            print(T)
            print(t)
    if pb==False :
        print("Ok")

test_tri (tri_insertion)


