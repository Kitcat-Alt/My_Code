# TP8 B - Manipuler des listes, ensembles et dictionnaires
mon_troupeau = {"moutons":20, "poules":15, "vache":30, "âne":2}
troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    somme_troupeau = 0
    for animal in troupeau.values():
        somme_troupeau+= animal
    return somme_troupeau
#print(total_animaux(troupeau))



def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:print()
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    liste_animaux = [] 
    for clés in troupeau.keys():
        liste_animaux.append(clés)
    return set(liste_animaux)
#print(tous_les_animaux(troupeau))


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    res = None
    for animal in troupeau.values():
        if animal >= 30:
            res = True
            return True
        else: 
            res = False
    return res
        


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    max = 0
    get_clé = None
    
    for clés, animal in troupeau.items():
        if animal >= max:
            max = animal
            get_clé = clés
    return get_clé
#print(le_plus_represente(troupeau))

print()
def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    res = None
    for animal in troupeau.values():
        if animal >= 5:
            res = True
        else:
            return False
    return res
#print(quantite_suffisante())


def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    troupeau3 = {}
    get_value = None
    for clé, animal in troupeau2.items():
        if clé in troupeau1.keys():
            get_value = troupeau1[clé]
            animal += get_value
            troupeau1[clé] = animal
        else:
            troupeau1[clé] = animal    
    return troupeau1
print(reunion_troupeaux(mon_troupeau, troupeau_de_jean))