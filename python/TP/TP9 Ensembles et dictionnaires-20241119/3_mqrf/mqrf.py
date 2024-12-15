
# ==========================
# La maison qui rend fou
# ==========================

mqrf1 = {"Abribus": "Astus" ,"Jeancloddus": "Abribus", "Plexus": "Gugus", "Astus": None , "Gugus": "Plexus" ,"Saudepus" : None}
mqrf2 = {"Abribus": "Astus", "Jeancloddus": None, "Plexus": "Saudepus", "Astus": "Gugus" ,"Gugus": "Plexus", "Saudepus": None}
mqrf3 = {"Abribus": "Astus" ,"Jeancloddus": "Astus", "Plexus": "Jeancloddus" ,"Astus": "Gugus", "Gugus": "Plexus" ,"Saudepus": "Bielorus"}

def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    cpt = 0 
    while mqrf[guichet] != None:
        guichet = mqrf[guichet]
        cpt += 1
        if cpt >= len(mqrf):
            return None
    return guichet
#print(quel_guichet(mqrf1, "Gugus"))
            





def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    cpt = 0 
    while mqrf[guichet] != None:
        guichet = mqrf[guichet]
        cpt += 1
        if cpt >= len(mqrf):
            return None
    return (guichet, cpt+1)
#print(quel_guichet_v2(mqrf2, "Abribus"))


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    cpt = 0 
    while mqrf[guichet] != None:
        guichet = mqrf[guichet]
        cpt += 1
        if cpt >= len(mqrf):
            return None
    return (guichet, cpt+1)
print(quel_guichet_v3(mqrf3, "Abribus"))

