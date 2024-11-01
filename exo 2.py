def tableau_surveille(LG,T):
    assert True ,"PE"
    i=0
    while i<len(LG) and abs(LG[i]-T)>2:
        i+=1
    return i<len(LG)

assert tableau_surveille([0,1],0)
assert tableau_surveille([0,2,1],4)
assert tableau_surveille([2],5)==False
assert tableau_surveille([3,0],2)
assert tableau_surveille([],2)==False


def dicho (l, ele):

    n = len(l)

    if n == 0:
        return False

    pos = n // 2
    milieu = l[pos]

    if milieu - 2 < ele < milieu + 2:
        return True

    elif n == 1:
        return False

    elif ele < milieu:
        return dicho (l[: pos], ele)

    else:
        return dicho (l[pos :], ele)


def bs_ite (lg, lt):

    lg.sort ()

    surveille = True
    for tableau in lt:
        surveille = surveille and dicho (lg, tableau)

    return surveille


def bs_rec (lg, lt):

    if lt == []:
        return True
        
    elif lg == []:
        return False

    else:
        gardien = lg[0]
        tableau = lt[0]
        return (gardien - 2 < tableau < gardien + 2 or bs_rec (lg[1 :], [tableau])) and bs_rec (lg, lt[1 :])


def musee (lt):

    assert len(LT)>0 and LT==sorted(LT) , '' PB PE''
    N=len(LT)
    i = lt[0] #indice du dernier tableau traité
    lg = [i + 2] #choix glouton
    j = lg[0] #indice du dernier gendarme placé
    #INV : les gendarmes de lg[:j+1] déjà placés surveillent les tableaux de LT[:i+1]
    assert bs(lg[:j+1], LT[:i+1]) , '' PB init''
    while .... :
    #INV et CC : les gendarmes de lg[:j+1] déjà placés surveillent les tableaux de LT[:i+1] et CC
    if ... :
    lg.append(...) #placer un nouveau gendarme (choix glouton)
    j+=1
    i+=1 #passer au tableau suivant
    #INV : les gendarmes de lg[:j+1] déjà placés surveillent les tableaux de LT[:i+1]
    assert bs(lg[:j+1], LT[:i+1] ) , '' PB fin d'itération''
    #INV et non(CC)
    assert bs(lg[:j+1], LT[:i+1]) and i==N-1 , '' PB sortie de boucle''
    #PS
    assert bs(lg,LT) , '' PB PS''
    return lg




assert bs_ite ([0], [0]), "Test 1 itératif"
assert not (bs_ite ([4], [6])), "Test 2 itératif"
assert bs_ite ([3.5], []), "Test 3 itératif"
assert not (bs_ite ([], [8.7])), "Test 4 itératif"
assert bs_ite ([], []), "Test 5 itératif"
assert bs_ite ([1, 3, 6.5, 13.32], [0.5, 2, 13.1]), "Test 6 itératif"

assert bs_rec ([0], [0]), "Test 1 récursif"
assert not (bs_rec ([4], [6])), "Test 2 récursif"
assert bs_rec ([3.5], []), "Test 3 récursif"
assert not (bs_rec ([], [8.7])), "Test 4 récursif"
assert bs_rec ([], []), "Test 5 récursif"
assert bs_rec ([1, 3, 6.5, 13.32], [0.5, 2, 13.1]), "Test 6 récursif"