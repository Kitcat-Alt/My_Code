"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

ecosysteme_1 = {'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] in ecosysteme.keys():
        if ecosysteme[animal] == None:
            return False
        return False
    return True
#print(extinction_immediate(ecosysteme_1, 'Requin'))


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    cpt =0
    courant = animal
    while ecosysteme[animal] != None or cpt >= len(ecosysteme):
        if ecosysteme[courant] not in ecosysteme.keys():
            return False
        courant = ecosysteme[courant]
        cpt += 1
    if cpt > len(ecosysteme):
        return False
    return True
    

print(en_voie_disparition(ecosysteme_1, 'Dragon'))


def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    ...


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ...




