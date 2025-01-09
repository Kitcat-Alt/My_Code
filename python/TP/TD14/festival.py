

# Exemples de modélisation de spectacles :

s1 = {'nom': 'JL Aubert', 'debut': 8, 'fin': 10}
s2 = {'nom': '2Be3', 'debut': 11, 'fin': 15}
s3 = {'nom': 'Tyko Moon', 'debut': 5, 'fin': 11}

# Exemple de modélisation de programme :

nikopol = [
    {'nom': 'JL Aubert', 'debut': 8, 'fin': 10}, 
    {'nom': 'JL Aubert', 'debut': 13, 'fin': 17}, 
    {'nom': 'JL Aubert', 'debut': 21, 'fin': 24}, 
    {'nom': 'C Goya', 'debut': 6, 'fin': 9}, 
    {'nom': 'C Goya', 'debut': 10, 'fin': 14}, 
    {'nom': 'C Goya', 'debut': 17, 'fin': 18}, 
    {'nom': '2Be3', 'debut': 11, 'fin': 15}, 
    {'nom': '2Be3', 'debut': 18, 'fin': 21}, 
    {'nom': 'Warhole', 'debut': 8, 'fin': 13}, 
    {'nom': 'Warhole', 'debut': 20, 'fin': 22}, 
    {'nom': 'Tyko Moon', 'debut': 5, 'fin': 11}, 
    {'nom': 'Tyko Moon', 'debut': 13, 'fin': 16}, 
    {'nom': 'Horus', 'debut': 7, 'fin': 18}, 
    {'nom': 'KKDZO', 'debut': 10, 'fin': 12}
    ]

exemple1 = [
    {'nom': 'A', 'debut': 10, 'fin': 14}, 
    {'nom': 'B', 'debut': 12, 'fin': 15}, 
    {'nom': 'C', 'debut': 11, 'fin': 16}, 
    {'nom': 'D', 'debut': 15, 'fin': 17}, 
    {'nom': 'E', 'debut': 13, 'fin': 21}, 
    {'nom': 'F', 'debut': 14, 'fin': 20}, 
    {'nom': 'G', 'debut': 16, 'fin': 16.5}, 
    {'nom': 'H', 'debut': 17, 'fin': 24}, 
]


###########################################
# QUELQUES FONCTIONS UTILES
###########################################


def compatibles(spectacle1, spectacle2):
    """ détermine si les deux spectacles sont compatibles """
    if spectacle1["debut"] < spectacle2["fin"] or spectacle2["debut"] < spectacle1["fin"]:
        if spectacle1["fin"] <= spectacle2["debut"] or spectacle2["fin"] <= spectacle1["debut"]:
            return True
        else:
            return False
    return False
#print(compatibles(s1,s2))

def tous_compatibles(selection, spectacle):
    """ détermine si spectacle est compatible avec tous les spectacles de la sélection """
    for pestacle in selection:
        if not compatibles(spectacle, pestacle):
            return False
    return True
#print(tous_compatibles(exemple1, s1))

###########################################
# LES FONCTIONS DE TRI
###########################################

# TRI SELON HEURE DE DEBUT

def tri_selon_debut(programme):
    """ trie les spectacles du programme selon leur heure de début """
    def critère (dico):
        return dico["debut"]
    return sorted(programme, key = critère)

# TRI SELON LA DUREE

def tri_selon_duree(programme):
    """ trie les spectacles du programme selon leur heure de début """
    def critère (dico):
        return dico["fin"] - dico["debut"]
    return sorted(programme, key = critère)

# TRI SELON HEURE DE FIN

def tri_selon_fin(programme):
    """ trie les spectacles du programme selon leur heure de début """
    def critère (dico):
        return dico["fin"]
    return sorted(programme, key = critère)
       

###########################################
# ALGORITHMES PROPOSES
###########################################


# Algo glouton (heure debut)

def prochain_spectacle1(programme, heure = 5):
    """ 
    'programme' est un programme dont les spectacles sont triés par heure de début croissante
    Cette fonction renvoie le premier spectacle qui commence après l'heure indiquée. 
    """
    for pestacle in programme:
        if pestacle["debut"] >= heure:
            return pestacle
    return None



def selection1(programme):
    """
    propose la sélection de spectacles donnée par l’algorithme 1 vu en TD
    """
    prog_trie = tri_selon_debut(programme)
    selection = []
    heure_actuelle = prog_trie[0]["debut"]
    selection_en_cours = True
    while selection_en_cours:
        pestacle = prochain_spectacle1(prog_trie, heure_actuelle)
        if pestacle is None:
            selection_en_cours = False
        else:
            selection.append(pestacle)
            heure_actuelle = pestacle["fin"]
    return selection        
    

proposition1 = selection1(nikopol)
print("Proposition 1 : ", proposition1)

# Algo glouton (durée)

def prochain_spectacle(programme, selection):
    """ 
    'programme' est un programme dont les spectacles sont triés (selon un certain critère)
    Cette fonction renvoie le premier spectacle compatible avec tous les autres spactacles de la sélection
    """
    

def selection2(programme):
    """
    propose la sélection de spectacles donnée par l’algorithme 2 vu en TD
    """
    ...

proposition2 = selection2(nikopol)
#print("Proposition 2 : ", proposition2)


# Algo glouton (heure de fin)

def selection3(programme):
    """
    propose la sélection de spectacles donnée par l’algorithme 3 vu en TD
    """
    ...

proposition3 = selection3(nikopol)
#print("Proposition 3 : ", proposition3)


# Algo glouton (forme plus générale)

def selection(programme, fonction_de_tri):
    ...


#print("Proposition 1 : ", selection(nikopol, tri_selon_debut))
#print("Proposition 2 : ", selection(nikopol, tri_selon_duree))
#print("Proposition 3 : ", selection(nikopol, tri_selon_fin))
