"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================
mon_pokedex = [('Bulbizarre', 'Plante'), ('Aeromite', 'Poison'), ('Abo', 'Poison')]

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    #complexité O(N)
    familles = set()
    for pokemon in pokedex:
        familles.add(pokemon[1])
    return familles
#print(toutes_les_familles(mon_pokedex))

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    #complexité O(N)
    nb_pokemon_famille = 0
    for i in range(len(pokedex)):
        if pokedex[i][1] == famille:
            nb_pokemon_famille += 1
    return nb_pokemon_famille

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    #complexité O(N)
    famille = dict()
    for pokemon in pokedex:
        if pokemon[1] in famille.keys():
            famille[pokemon[1]] += 1
        else:
            famille[pokemon[1]] = 1
    return famille
#print(frequences_famille(mon_pokedex))

def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    #complexité O(N)
    dict_famille = dict()
    nom_pokemon = set()
    for i in range(len(pokedex)):
        if pokedex[i][1] in dict_famille.keys():
            dict_famille[pokedex[i][1]].add(pokedex[i][0])
        else:
            nom_pokemon.add(pokedex[i][0])
            dict_famille[pokedex[i][1]] = nom_pokemon
            nom_pokemon = set()
    return dict_famille
#print(dico_par_famille(mon_pokedex))


def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    famille_plus_representee = ''
    dico_pokedex = dico_par_famille(pokedex)
    longueur_max = 0
    for pokemon in dico_pokedex.keys():
        if len(dico_pokedex[pokemon]) >= longueur_max:
            famille_plus_representee = pokemon
    return famille_plus_representee
#print(famille_la_plus_representee(mon_pokedex))       
        
        



# ==========================
# Petites bêtes (la suite)
# ==========================
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
