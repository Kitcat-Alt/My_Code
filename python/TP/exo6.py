def qualif_100m(genre,recordPerso100m,NbCoursesWin,ChampM):
    """Permet de savoir si une personne rempli les critères pour être qualifiée au 100m des JO

    Args:
        genre (_type_): str
        recordPerso100m (_type_): int
        NbCoursesWin (_type_): int
        ChampM (_type_): booléen

    Returns:
        _type_: booleen 
    """
    res = 0
    if genre == "H":
        if recordPerso100m < 12 and NbCoursesWin >=3 or ChampM == True: # res = recordPerso100m < 12 and NbCoursesWin >=3 or ChampM == True
            res = True
        else: 
            res = False
    
    if genre == "F":
        if recordPerso100m < 15 and NbCoursesWin >=3 or ChampM == True:
            res = True 
        else: 
            res = False
    return res

print(qualif_100m("H",16,1,True))

def test_qualif():
    assert qualif_100m("F",16,3,False) == True
    assert qualif_100m("H",15,2,True) == False