"""
TD 14 : Fichier de tests
"""

import festival
def exemple_programme():
    return [
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

def exemple_programme2():
    return [
        {'nom': 'A', 'debut': 10, 'fin': 14}, 
        {'nom': 'B', 'debut': 12, 'fin': 15}, 
        {'nom': 'C', 'debut': 11, 'fin': 16}, 
        {'nom': 'D', 'debut': 15, 'fin': 17}, 
        {'nom': 'E', 'debut': 13, 'fin': 21}, 
        {'nom': 'F', 'debut': 14, 'fin': 20}, 
        {'nom': 'G', 'debut': 16, 'fin': 16.5}, 
        {'nom': 'H', 'debut': 17, 'fin': 24}, 
        ]


def test_compatibles():
    s1 = {'nom': 'JL Aubert', 'debut': 8, 'fin': 10}
    s2 = {'nom': '2Be3', 'debut': 11, 'fin': 15}
    s3 = {'nom': 'Tyko Moon', 'debut': 5, 'fin': 11}
    s4 = {'nom': 'C Goya', 'debut': 10, 'fin': 14}
    s5 = {'nom': 'mini', 'debut': 12, 'fin': 13}
    assert festival.compatibles(s1, s2)
    assert festival.compatibles(s2, s1)
    assert not festival.compatibles(s1, s3)
    assert not festival.compatibles(s3, s1)
    assert festival.compatibles(s1, s4)
    assert festival.compatibles(s4, s1)
    assert not festival.compatibles(s5, s2)
    assert not festival.compatibles(s2, s5)


def test_tous_compatibles():
    nikopol = exemple_programme()
    assert not festival.tous_compatibles(nikopol, {'nom': '', 'debut': 17, 'fin': 19})
    assert festival.tous_compatibles(nikopol, {'nom': '', 'debut': 4, 'fin': 5})


def test_tri_delon_debut():
    exemple = exemple_programme2()
    assert festival.tri_selon_debut(exemple) == [{'nom': 'A', 'debut': 10, 'fin': 14}, {'nom': 'C', 'debut': 11, 'fin': 16}, {'nom': 'B', 'debut': 12, 'fin': 15}, {'nom': 'E', 'debut': 13, 'fin': 21}, {'nom': 'F', 'debut': 14, 'fin': 20}, {'nom': 'D', 'debut': 15, 'fin': 17}, {'nom': 'G', 'debut': 16, 'fin': 16.5}, {'nom': 'H', 'debut': 17, 'fin': 24}]


def test_tri_selon_duree():
    exemple = exemple_programme2()
    assert festival.tri_selon_duree(exemple) == [{'nom': 'G', 'debut': 16, 'fin': 16.5}, {'nom': 'D', 'debut': 15, 'fin': 17}, {'nom': 'B', 'debut': 12, 'fin': 15}, {'nom': 'A', 'debut': 10, 'fin': 14}, {'nom': 'C', 'debut': 11, 'fin': 16}, {'nom': 'F', 'debut': 14, 'fin': 20}, {'nom': 'H', 'debut': 17, 'fin': 24}, {'nom': 'E', 'debut': 13, 'fin': 21}]


def test_tri_selon_fin():
    exemple = exemple_programme2()
    assert festival.tri_selon_fin(exemple) == [{'nom': 'A', 'debut': 10, 'fin': 14}, {'nom': 'B', 'debut': 12, 'fin': 15}, {'nom': 'C', 'debut': 11, 'fin': 16}, {'nom': 'G', 'debut': 16, 'fin': 16.5}, {'nom': 'D', 'debut': 15, 'fin': 17}, {'nom': 'F', 'debut': 14, 'fin': 20}, {'nom': 'E', 'debut': 13, 'fin': 21}, {'nom': 'H', 'debut': 17, 'fin': 24}]


def test_prochain_spectacle1():
    exemple = exemple_programme2()
    exemple_trié = festival.tri_selon_debut(exemple)
    assert festival.prochain_spectacle1(exemple_trié, 5) == {'nom': 'A', 'debut': 10, 'fin': 14}
    assert festival.prochain_spectacle1(exemple_trié, 12.4) == {'nom': 'E', 'debut': 13, 'fin': 21}
    assert festival.prochain_spectacle1(exemple_trié, 18) is None


