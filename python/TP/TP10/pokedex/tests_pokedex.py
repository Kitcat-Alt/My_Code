# pylint: disable=missing-function-docstring
"""les tests pour les fonctions des exercices 1 et 2 du TP10"""
import pokedex

# ==================================
# TESTS pour l'exercice 1
# ==================================

def exemples_pokedex_v1():
    """renvoie un couple de deux exemples de pokedex en utilisant la modélisation 1"""
    pokedex_anakin = {
        ('Carmache', 'Dragon'), ('Carmache', 'Sol'),
        ('Colimucus', 'Dragon'), ('Palkia', 'Dragon'),
        ('Palkia', 'Eau')}
    pokedex_romain = ...      
    return (pokedex_anakin, pokedex_romain)

def exemples_pokedex_v2():
    """renvoie un couple de deux exemples de pokedex en utilisant la modélisation 2"""
    pokedex_anakin = {
        'Carmache': {'Dragon','Sol'},
        'Colimucus': {'Dragon'},
        'Palkia': {'Dragon', 'Eau'}}
    pokedex_romain = ...   
    return (pokedex_anakin, pokedex_romain)

def exemples_pokedex_v3():
    """renvoie un couple de deux exemples de pokedex en utilisant la modélisation 3"""
    pokedex_anakin = {
        'Dragon': {'Carmache','Colimucus', 'Palkia'},
        'Sol': {'Carmache'},
        'Eau': {'Palkia'}}
    pokedex_romain = ...
    return (pokedex_anakin, pokedex_romain)


# ==================================
# Exercice 1 : Modélisation n°1
# ==================================

def test_appartient_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert not pokedex.appartient_v1("Racaillou", pokedex_anakin)
    assert pokedex.appartient_v1("Racaillou", pokedex_romain)


def test_toutes_les_attaques_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert pokedex.toutes_les_attaques_v1("Palkia", pokedex_anakin) == {'Eau', 'Dragon'}
    assert pokedex.toutes_les_attaques_v1("Colimucus", pokedex_anakin) == {'Dragon'}


def test_nombre_de_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert pokedex.nombre_de_v1("Dragon", pokedex_anakin) == 3
    assert pokedex.nombre_de_v1("Dragon", pokedex_romain) == 0

def test_attaque_preferee_v1():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v1()
    assert pokedex.attaque_preferee_v1(pokedex_anakin) == "Dragon"
    assert pokedex.attaque_preferee_v1(pokedex_romain) == "Sol"

# ==================================
# Exercice 1 : Modélisation n°2
# ==================================

def test_appartient_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert not pokedex.appartient_v2("Racaillou", pokedex_anakin)
    assert pokedex.appartient_v2("Racaillou", pokedex_romain)


def test_toutes_les_attaques_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert pokedex.toutes_les_attaques_v2("Palkia", pokedex_anakin) == {'Eau', 'Dragon'}
    assert pokedex.toutes_les_attaques_v2("Colimucus", pokedex_anakin) == {'Dragon'}


def test_nombre_de_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert pokedex.nombre_de_v2("Dragon", pokedex_anakin) == 3
    assert pokedex.nombre_de_v2("Dragon", pokedex_romain) == 0

def test_attaque_preferee_v2():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v2()
    assert pokedex.attaque_preferee_v2(pokedex_anakin) == "Dragon"
    assert pokedex.attaque_preferee_v2(pokedex_romain) == "Sol"


# ==================================
# Exercice 1 : Modélisation n°3
# ==================================


def test_appartient_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert not pokedex.appartient_v3("Racaillou", pokedex_anakin)
    assert pokedex.appartient_v3("Racaillou", pokedex_romain)


def test_toutes_les_attaques_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert pokedex.toutes_les_attaques_v3("Palkia", pokedex_anakin) == {'Eau', 'Dragon'}
    assert pokedex.toutes_les_attaques_v3("Colimucus", pokedex_anakin) == {'Dragon'}


def test_nombre_de_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert pokedex.nombre_de_v3("Dragon", pokedex_anakin) == 3
    assert pokedex.nombre_de_v3("Dragon", pokedex_romain) == 0

def test_attaque_preferee_v3():
    (pokedex_anakin, pokedex_romain) = exemples_pokedex_v3()
    assert pokedex.attaque_preferee_v3(pokedex_anakin) == "Dragon"
    assert pokedex.attaque_preferee_v3(pokedex_romain) == "Sol"

# ==================================
# Exercice 1 : Transformations
# ==================================

def test_v1_to_v2():
    (pokedex_anakin_v1, pokedex_romain_v1) = exemples_pokedex_v1()
    (pokedex_anakin_v2, pokedex_romain_v2) = exemples_pokedex_v2()    
    assert pokedex.v1_to_v2(pokedex_anakin_v1) == pokedex_anakin_v2
    assert pokedex.v1_to_v2(pokedex_romain_v1) == pokedex_romain_v2

def test_v2_to_v3():
    (pokedex_anakin_v3, pokedex_romain_v3) = exemples_pokedex_v3()
    (pokedex_anakin_v2, pokedex_romain_v2) = exemples_pokedex_v2()    
    assert pokedex.v2_to_v3(pokedex_anakin_v2) == pokedex_anakin_v3
    assert pokedex.v2_to_v3(pokedex_romain_v2) == pokedex_romain_v3
