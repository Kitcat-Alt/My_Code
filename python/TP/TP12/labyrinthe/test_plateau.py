""" tests pour le module plateau"""

import plateau
import matrice


def test_est_sur_le_le_plateau():
    le_plateau = plateau.init()
    assert plateau.est_sur_le_plateau(le_plateau, (0, 0))
    assert plateau.est_sur_le_plateau(le_plateau, (0, 8))
    assert plateau.est_sur_le_plateau(le_plateau, (8, 0))
    assert plateau.est_sur_le_plateau(le_plateau, (8, 8))
    assert plateau.est_sur_le_plateau(le_plateau, (3, 5))
    assert not plateau.est_sur_le_plateau(le_plateau, (3, 10))
    assert not plateau.est_sur_le_plateau(le_plateau, (15, 5))
    assert not plateau.est_sur_le_plateau(le_plateau, (13, 22))
    assert not plateau.est_sur_le_plateau(le_plateau, (-1, 6))
    assert not plateau.est_sur_le_plateau(le_plateau, (6, -3))

def test_get():
    le_plateau = plateau.init()
    assert plateau.get(le_plateau, (0, 0)) == plateau.PERSONNAGE
    assert plateau.get(le_plateau, (8, 8)) == plateau.FANTOME
    assert plateau.get(le_plateau, (2, 0)) == plateau.MUR
    assert plateau.get(le_plateau, (4, 5)) == plateau.COULOIR
    assert plateau.get(le_plateau, (5, 4)) == plateau.MUR    
    assert plateau.get(le_plateau, (1, 3)) == plateau.MUR
    assert plateau.get(le_plateau, (3, 1)) == plateau.MUR
    assert plateau.get(le_plateau, (10, 3)) is None

def test_est_un_mur():
    le_plateau = plateau.init()
    assert not plateau.est_un_mur(le_plateau, (0, 0))
    assert not plateau.est_un_mur(le_plateau, (8, 8))
    assert plateau.est_un_mur(le_plateau, (2, 0))
    assert not plateau.est_un_mur(le_plateau, (4, 5))
    assert plateau.est_un_mur(le_plateau, (5, 4))    
    assert plateau.est_un_mur(le_plateau, (1, 3))
    assert plateau.est_un_mur(le_plateau, (3, 1))


def test_contient_fantome():
    le_plateau = plateau.init()
    matrice.set_val(le_plateau, 4, 3, plateau.FANTOME)
    assert plateau.contient_fantome(le_plateau, (4, 3))
    assert not plateau.contient_fantome(le_plateau, (3, 4))
    assert not plateau.contient_fantome(le_plateau, (0, 0))
    assert plateau.contient_fantome(le_plateau, (8, 8))


def test_est_la_sortie():
    le_plateau = plateau.init()
    assert plateau.est_la_sortie(le_plateau, (8, 8))
    assert not plateau.est_la_sortie(le_plateau, (3, 4))
    assert not plateau.est_la_sortie(le_plateau, (0, 0))


def test_deplace_personnage():
    le_plateau = plateau.init()
    assert plateau.deplace_personnage(le_plateau, (0, 0), plateau.NORD) == (0, 0)
    assert plateau.get(le_plateau, (0, 0)) == plateau.PERSONNAGE
    assert plateau.deplace_personnage(le_plateau, (0, 0), plateau.EST) == (0, 0)
    assert plateau.deplace_personnage(le_plateau, (0, 0), plateau.OUEST) == (0, 0)
    assert plateau.deplace_personnage(le_plateau, (0, 0), plateau.SUD) == (1, 0)
    assert plateau.get(le_plateau, (0, 0)) == plateau.COULOIR    
    assert plateau.get(le_plateau, (1, 0)) == plateau.PERSONNAGE

    assert plateau.deplace_personnage(le_plateau, (4, 4), plateau.EST) == (4, 5)
    assert plateau.deplace_personnage(le_plateau, (4, 4), plateau.SUD) == (4, 4)
    assert plateau.deplace_personnage(le_plateau, (4, 4), plateau.OUEST) == (4, 3)
    assert plateau.deplace_personnage(le_plateau, (4, 4), plateau.NORD) == (3, 4)


def test_voisins():
    le_plateau = plateau.init()
    assert plateau.voisins(le_plateau, (0, 0)) == {(1, 0)}
    assert plateau.voisins(le_plateau, (4, 4)) == {(3, 4), (4, 3), (4, 5)}
    assert plateau.voisins(le_plateau, (1, 2)) == {(1, 1), (2, 2)}
    assert plateau.voisins(le_plateau, (8, 8)) == {(8, 7)}


def test_fabrique_le_calque():
    le_plateau = plateau.init()
    le_calque = plateau.fabrique_le_calque(le_plateau, (4, 2))
    assert le_calque == matrice.charge_matrice("./calque1_pour_test.csv")


def test_fabrique_chemin():
    le_plateau = plateau.init()
    assert plateau.fabrique_chemin(le_plateau, (4, 5), (8, 8)) == [(8, 8), (8, 7), (7, 7), (6, 7),
                                                                   (5, 7), (4, 7), (4, 6)]
    assert plateau.fabrique_chemin(le_plateau, (5, 3), (8, 8)) == [(8, 8), (8, 7), (7, 7), (7, 6), 
                                                                   (7, 5), (7, 4), (7, 3), (6, 3)]


def test_deplace_fantome():
    le_plateau = plateau.init()
    assert plateau.deplace_fantome(le_plateau, (8, 8), (0, 0)) == (8, 7)
    assert plateau.contient_fantome(le_plateau, (8, 7))
    assert not plateau.contient_fantome(le_plateau, (8, 8))
    le_plateau = plateau.init()
    assert plateau.deplace_fantome(le_plateau, (8, 8), (7, 4)) == (8, 7)
    assert plateau.deplace_fantome(le_plateau, (7, 4), (8, 8)) == (7, 5)
    assert plateau.deplace_fantome(le_plateau, (4, 4), (4, 4)) == (4, 4)
