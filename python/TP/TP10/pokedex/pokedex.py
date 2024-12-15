"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

pokedex_anakin_v1 = {('Carmache', 'Dragon'), ('Carmache', 'Sol'), ('Colimucus', 'Dragon'), ('Palkia', 'Dragon'), ('Palkia', 'Eau')}

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke in pokedex:
        if poke[0] == pokemon:
            return True
    return False
#print(appartient_v1("Carmache", pokedex_anakin_v1))


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    attaques = set()
    for poke in pokedex:
        if poke[0] == pokemon:
            attaques.add(poke[1])
    return attaques
#print(toutes_les_attaques_v1("Carmache", pokedex_anakin_v1))



def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt_poke = 0
    for poke in pokedex:
        if poke[1] == attaque:
            cpt_poke += 1
    return cpt_poke
#print(nombre_de_v1("Dragon", pokedex_anakin_v1))

def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    max = 0
    attaque_max = ""
    attaque = dict()
    for poke in pokedex:
        if poke[1] in attaque.keys():
            attaque[poke[1]] += 1
        else:
            attaque[poke[1]] = 1
    for attaques, nombre in attaque.items():
        if nombre >= max:
            max = nombre
            attaques_max = attaques
    return attaques_max
#print(attaque_preferee_v1(pokedex_anakin_v1))
    


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests
pokedex_anakin_v2 = {'Carmache': {'Dragon', 'Sol'}, 'Colimucus': {'Dragon'}, 'Palkia': {'Dragon', 'Eau'}}

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke in pokedex.keys():
        if poke == pokemon:
            return True
    return False
#print(appartient_v2("bleh", pokedex_anakin_v2))
    


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    attaques = set()
    for poke in pokedex.keys():
        if poke == pokemon:
            for attaque in pokedex[poke]:
                attaques.add(attaque)
    return attaques
#print(toutes_les_attaques_v2("Carmache", pokedex_anakin_v2))

def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt_poke = 0
    for poke in pokedex.values():
        if attaque in poke:
            cpt_poke += 1 
    return cpt_poke
#print(nombre_de_v2('Dragon', pokedex_anakin_v2))



def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dict_attaque = dict()
    attaque_max = 0
    for attaque in pokedex.values():
        for type in attaque:
            if type in dict_attaque.keys():
                dict_attaque[type] += 1
            else:
                dict_attaque[type] = 1
    for attaque, nb_attaques in dict_attaque.items():
        if nb_attaques >= attaque_max:
            attaque_max = nb_attaques
            nom_attaque_max = attaque
    return nom_attaque_max
#print(attaque_preferee_v2(pokedex_anakin_v2))         
    

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests

pokedex_anakin_v3 = {'Dragon': {'Carmache', 'Colimucus', 'Palkia'}, 'Sol': {'Carmache'}, 'Eau': {'Palkia'}}

def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke in pokedex.values():
        if pokemon in poke:
            return True
    return False
#print(appartient_v3('evoli', pokedex_anakin_v3))


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    attaques_pokemon = set()
    for attaque, poke in pokedex.items():
        if pokemon in poke:
            attaques_pokemon.add(attaque)
    return attaques_pokemon
#print(toutes_les_attaques_v3('Palkia', pokedex_anakin_v3))


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt_pokemon = 0
    for type in pokedex.keys():
        if type == attaque:
            cpt_pokemon += len(pokedex[type])
    return cpt_pokemon
#print(nombre_de_v3('Sol', pokedex_anakin_v3))
        


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    nom_attaque_max = ''
    attaque_max = 0
 
    for attaque, pokemon in pokedex.items():
        if len(pokemon) >= attaque_max:
            attaque_max = len(pokemon)
            nom_attaque_max = attaque
    return nom_attaque_max
#print(attaque_preferee_v3(pokedex_anakin_v3))

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    
    


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    ...

