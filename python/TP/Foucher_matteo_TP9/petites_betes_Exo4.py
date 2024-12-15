mon_pokedex = {"Bulbizarre": {"Plante", "Poison"} ,"Aeromite" : {"Poison", "Insecte"} ,"Abo" : {"Poison"}}


def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    familles = set()
    for famille in pokedex.values():
        for types in famille:
            familles.add(types)
    return familles
#print(toutes_les_familles_v2(mon_pokedex))

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nombre_poke_famille = 0
    for type in pokedex.values():
        if famille in type:
            nombre_poke_famille += 1
    return nombre_poke_famille
#print(nombre_pokemons_v2(mon_pokedex, "Poison"))

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréquences des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    freq_famille = dict()
    for famille in pokedex.values():
        for type in famille:
            if type in freq_famille.keys():
                freq_famille[type] += 1
            else:
                freq_famille[type] = 1
    return freq_famille
#print(frequences_famille_v2(mon_pokedex))

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_famille = dict()
    poke_courant = set()
    for poke, famille in pokedex.items():
        for type in famille:
            if type in dico_famille.keys(): 
                dico_famille[type].add(poke)
            else:
                poke_courant.add(poke)
                dico_famille[type] = poke_courant
                poke_courant = set()
    return dico_famille
#print(dico_par_famille_v2(mon_pokedex))



def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    famille_plus_represente = frequences_famille_v2(pokedex)
    return max(famille_plus_represente)
#print(famille_la_plus_representee_v2(mon_pokedex))