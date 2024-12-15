def Nb_voyelle_mot (mot):
    """Permet de savoir si un mot contient plus de voyelle que de consonnes

    Args:
        mot (_type_): str
    """    
    res = 0
    for lettre in mot:
        if lettre in 'aeiouy':
            res +=1
        else:
            res -=1
    return res>0

print(Nb_voyelle_mot("eia"))

def test_AlgoVoyelle():
    assert Nb_voyelle_mot("trad") == False
    assert Nb_voyelle_mot("aeiouy") == True


            
    