# pylint: disable=missing-function-docstring
"""les tests pour les fonctions des exercices 1 et 2 du TP10"""
import ecosysteme

def test_extinction_immediate():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    assert ecosysteme.extinction_immediate(ecosysteme_1, 'Lapin')
    assert ecosysteme.extinction_immediate(ecosysteme_1, 'Requin')
    assert not ecosysteme.extinction_immediate(ecosysteme_1, 'Mouton')
    assert not ecosysteme.extinction_immediate(ecosysteme_1, 'Dragon')
    assert not ecosysteme.extinction_immediate(ecosysteme_2, 'Poule')


def test_en_voie_disparition():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    ecosysteme_3 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard' }
    assert ecosysteme.en_voie_disparition(ecosysteme_1, 'Lapin')
    assert ecosysteme.en_voie_disparition(ecosysteme_1, 'Requin')
    assert ecosysteme.en_voie_disparition(ecosysteme_1, 'Dragon')
    assert not ecosysteme.en_voie_disparition(ecosysteme_1, 'Loup')
    assert not ecosysteme.en_voie_disparition(ecosysteme_1, 'Mouton')
    assert not ecosysteme.en_voie_disparition(ecosysteme_1, 'Herbe')
    assert not ecosysteme.en_voie_disparition(ecosysteme_2, 'Poule')
    assert not ecosysteme.en_voie_disparition(ecosysteme_2, 'Ours')
    assert not ecosysteme.en_voie_disparition(ecosysteme_3, 'Poule')


def test_animaux_en_danger():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    eco = {1:2, 2:3, 3:4, 4:5, 5:17, 6:4, 7:6, 8:9, 9:10, 10:11, 11:8}
    assert ecosysteme.animaux_en_danger(ecosysteme_1) =={'Lapin', 'Requin'}
    assert ecosysteme.animaux_en_danger(ecosysteme_2) == set()
    assert ecosysteme.animaux_en_danger(eco) == {5}


def test_especes_en_voie_disparition():
    ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
    ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
    eco = {1:2, 2:3, 3:4, 4:5, 5:17, 6:4, 7:6, 8:9, 9:10, 10:11, 11:8}
    assert ecosysteme.especes_en_voie_disparition(ecosysteme_1) == {'Lapin', 'Requin', 'Lion', 'Dragon'}
    assert ecosysteme.especes_en_voie_disparition(ecosysteme_2) == set()
    assert ecosysteme.especes_en_voie_disparition(eco) == {1, 2, 3, 4, 5, 6, 7}

