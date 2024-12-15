# pylint: disable=missing-function-docstring
"""les tests pour les foctions des exercices 1 et 4 du TP9"""
import petites_betes_Exo4

# ==================================
# TESTS pour l'exercice 4
# ==================================

def test_toutes_les_familles_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes_Exo4.toutes_les_familles_v2(mon_pokedex) == {'Plante', 'Insecte', 'Poison'}

def test_nombre_pokemons_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes_Exo4.nombre_pokemons_v2(mon_pokedex, 'Plante') == 1
    assert petites_betes_Exo4.nombre_pokemons_v2(mon_pokedex, 'Poison') == 3
    assert petites_betes_Exo4.nombre_pokemons_v2(mon_pokedex, 'Fée') == 0


def test_frequences_famille_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes_Exo4.frequences_famille_v2(mon_pokedex) == {'Plante': 1, 'Poison': 3, 'Insecte':1}


def test_dico_par_famille_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes_Exo4.dico_par_famille_v2(mon_pokedex) == {
        'Plante': {'Bulbizarre'},
        'Poison': {'Aeromite', 'Abo', 'Bulbizarre'},
        'Insecte':{'Aeromite'}}


def test_famille_la_plus_representee_v2():
    mon_pokedex = {"Bulbizarre":{"Plante", "Poison"},
                   "Aeromite":{"Poison", "Insecte"}, "Abo":{"Poison"}}
    assert petites_betes_Exo4.famille_la_plus_representee_v2(mon_pokedex) == 'Poison'
