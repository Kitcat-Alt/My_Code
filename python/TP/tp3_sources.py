# exercice 1
def NbPairsMajo_exo2(liste_nb):
    """[summary] Permet de savoir si il y autant ou plus de nombres pairs que d'impairs dans un liste de nombres

    Args:
        entree ([type]): list int

    Returns:
        [type]: booléen
    """
    nb_Pair = 0 
    nb_Impair = 0
    # au début de chaque tour de boucle
    #  A COMPLETER
    for nb in liste_nb:
        if nb % 2 == 0:
            nb_Pair += 1
        else:
            nb_Impair += 1
    return nb_Pair >= nb_Impair

#print(NbPairsMajo_exo2([1,4,6,-2,-5,3,10]))
#print(NbPairsMajo_exo2([-4,5,-11,-56,5,-11]))

# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = liste_nombres[0]
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur
    for n in liste_nombres:
        if n > valeur:
            Ok = True
        else: 
            Ok = False
    if Ok == True:
        for elem in liste_nombres:
            if valeur < elem < res:
                res = elem
    else: 
        res = None  
    return res

print(min_sup([5, 7, 6, 5, 7, 3], 10))

def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None


# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = ''
    # au début de chaque tour de boucle
    # c1 vaut c2
    # c2 vaut un caractère de la phrase
    # resultat vaut
    for c2 in phrase:
        if c1 == ' ' and c2 != ' ':
            resultat = resultat + 1
            c1 = c2
    if phrase == "" or phrase[0] == ' ':
        return resultat
    else:
        return resultat+1

print(nb_mots("bonjour, il fait beau"))

def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    .") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

def test_Pairs_Majo():
    assert NbPairsMajo_exo2([8, 12, 7, 3, 9, 2, 1, 4, 9]) == False
    assert NbPairsMajo_exo2([-2, -5, 2, 9.8, -8.1, 7]) == False
    assert NbPairsMajo_exo2([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 5]) == True
    assert NbPairsMajo_exo2([-2, -5, 2, 9.8, -8.1, 7]) == False


