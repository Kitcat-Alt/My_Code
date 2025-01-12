#question 1
def Somme_nb_pairs(liste_nb):
    """Fait la somme des nombres pairs dans une liste donnée

    Args:
        liste_nb (int): liste de nombres entiers (positifs ou négatifs)

    Returns:
        _type_: int 
    """
    somme = 0
    # au début de chaque tour de boucle
    # nb vaut une valeur de liste_nb
    # somme vaut somme + nb 
    for nb in liste_nb:
        if nb%2 == 0:
            somme+=nb
    return somme
#print(Somme_nb_pairs([12,13,6,5,7]))

def test_Somme_nb_pairs():
    assert Somme_nb_pairs([12,13,6,5,7]) == 18
    assert Somme_nb_pairs([2,4,6,8,10]) == 30
    assert Somme_nb_pairs([1,3,5,7,9]) == 0
    assert Somme_nb_pairs([1,56,48,-102,115,1099]) == 2


#question 2
def Derniere_voyelle(chaine):
    """Donne la dernière voyelle de la chaine de caractère donnée

    Args:
        chaine (str): chaine de caractères

    Returns:
        _type_: str
    """
    cpt_voyelle = 0
    # au début de chaque tour de boucle
    # carac vaut un caractère de chaine
    # voyelle vaut la dernière voyelle rencontré dans chaine
    # cpt_voyelle vaut le nombre de voyelle rencontrée dans chaine
    for carac in chaine:
        if carac in "aeiouy":
            voyelle = carac
            cpt_voyelle+=1
    if cpt_voyelle != 0:
        return voyelle
    else :
        return None
#print(Dernière_voyelle("salut les amis"))

def test_Derniere_voyelle():
    assert Derniere_voyelle("ctrl") == None 
    assert Derniere_voyelle("salut les amis !") == "i"
    assert Derniere_voyelle("") == None 
    assert Derniere_voyelle("aeiuuoy") == "y" 


#question 3
def ProportionNegatifs (liste_nb):
    """Donne la proportion de nombres négatifs dans une liste de nombre donnée 

    Args:
        liste_nb (int): liste de nombres négatifs ou positifs

    Returns:
        _type_: float
    """
    cpt_negatifs = 0
    # au début de chaque tour de boucle
    # nb vaut une valeur de liste_nb
    # cpt_negatifs vaut le nombre de nombre négatifs rencontrés dans liste_nb
    for nb in liste_nb:
        if nb < 0:
            cpt_negatifs+=1
    if len(liste_nb) == 0:
        return None
    else:
        return cpt_negatifs/len(liste_nb)
#print(ProportionNegatifs([4,-2,8,2,-2,-7]))

def test_ProportionNegatifs():
    assert ProportionNegatifs([1,2,3,4,5]) == 0.0
    assert ProportionNegatifs([-9,-4,-8,5]) == 0.75
    assert ProportionNegatifs([-9,-10,-50,-78])  == 1.0
    assert ProportionNegatifs([-1000,50,-987,52,4]) == 0.4