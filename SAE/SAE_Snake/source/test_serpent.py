
import serpent

def test_Serpent():
    assert serpent.Serpent("Kitcat", 0, 5, [[5,2], [6,2], [7,2]], 10, 11, 0, "S") == {"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }
    assert serpent.Serpent("", 0, 5, [[0,0], [1,2], [3,2]], 0, 0, 0, "N") == {"nom_joueur": "", "num_joueur": 0, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }
    assert serpent.Serpent("Kit", 0, 5, [[5,2], [6,2], [7,2]], 5, 0, 0, "E") == {"nom_joueur": "Kit", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }
    assert serpent.Serpent("cat", 0, 5, [[5,2], [6,2], [7,2]], 10, 11, 0, "O") == {"nom_joueur": "cat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }

def test_get_nom():
    assert serpent.get_nom({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }) == "Kitcat"
    assert serpent.get_nom({"nom_joueur": "", "num_joueur": 0, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) == ""
    assert serpent.get_nom({"nom_joueur": "Kit", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == "Kit"
    assert serpent.get_nom({"nom_joueur": "cat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }) == "cat"


def test_get_num_joueur():
    assert serpent.get_num_joueur({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }) == 0
    assert serpent.get_num_joueur({"nom_joueur": "", "num_joueur": 3, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) == 3
    assert serpent.get_num_joueur({"nom_joueur": "Kit", "num_joueur": 2, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == 2
    assert serpent.get_num_joueur({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }) == 1

def test_get_points():
    assert serpent.get_points({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }) == 5
    assert serpent.get_points({"nom_joueur": "", "num_joueur": 3, "points": 6, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) == 6
    assert serpent.get_points({"nom_joueur": "Kit", "num_joueur": 2, "points": 10, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == 10
    assert serpent.get_points({"nom_joueur": "cat", "num_joueur": 1, "points": 0, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }) == 0

def test_get_liste_pos():
    assert serpent.get_liste_pos({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }) == [[5,2], [6,2], [7,2]]
    assert serpent.get_liste_pos({"nom_joueur": "", "num_joueur": 3, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) == [[0,0], [1,2], [3,2]]
    assert serpent.get_liste_pos({"nom_joueur": "Kit", "num_joueur": 2, "points": 5, "positions": [[5,2], [6,5], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == [[5,2], [6,5], [7,2]]
    assert serpent.get_liste_pos({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[], [], []], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }) == [[], [], []]

def test_get_queue():
    assert serpent.get_queue({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }) == [7,2]
    assert serpent.get_queue({"nom_joueur": "", "num_joueur": 3, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) == [3,2]
    assert serpent.get_queue({"nom_joueur": "Kit", "num_joueur": 2, "points": 5, "positions": [[5,2], [6,2], [4,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == [4,2]
    assert serpent.get_queue({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[5,2], [6,2], [10,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }) == [10,2]

def test_get_derniere_direction():
    assert serpent.get_derniere_direction({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S" }) == "S"
    assert serpent.get_derniere_direction({"nom_joueur": "", "num_joueur": 3, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) == "N"
    assert serpent.get_derniere_direction({"nom_joueur": "Kit", "num_joueur": 2, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == "E"
    assert serpent.get_derniere_direction({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "O" }) == "O"

def test_get_bonus():
    assert serpent.get_bonus({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 11, "tps_m": 0, "direction": "S"}) == ["Protection", "Surpuissance"]
    assert serpent.get_bonus({"nom_joueur": "", "num_joueur": 3, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_p": 0, "tps_m": 0, "direction": "N" }) ==  []
    assert serpent.get_bonus({"nom_joueur": "Kit", "num_joueur": 2, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_p": 0, "tps_m": 0, "direction": "E" }) == ["Surpuissance"]
    assert serpent.get_bonus({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 0, "tps_p": 0, "tps_m": 10, "direction": "O" }) == ["Mange-Mur"]
    assert serpent.get_bonus({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_p": 15, "tps_m": 20, "direction": "O" }) == ["Protection", "Surpuissance", "Mange-Mur"]


#def test_set_list_pos():
#    assert serpent.set_liste_pos()
#    assert serpent.set_liste_pos()
#    assert serpent.set_liste_pos()
#    assert serpent.set_liste_pos()
#
#def test_set_derniere_direction():
#    assert serpent.set_derniere_direction()
#    assert serpent.set_derniere_direction()
#    assert serpent.set_derniere_direction()
#    assert serpent.set_derniere_direction()
#
def test_to_str():
    assert serpent.to_str({"nom_joueur": "Kitcat", "num_joueur": 0, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 10, "tps_m": 11, "tps_p": 0, "direction": "S"}) == "Kitcat -> 5 s:10 m:11 p:0"
    #assert serpent.to_str({"nom_joueur": "", "num_joueur": 3, "points": 5, "positions": [[0,0], [1,2], [3,2]], "tps_s": 0, "tps_m": 0, "tps_p": 0, "direction": "N" }) == " -> 5 s:0 m:0 p:0"
    assert serpent.to_str({"nom_joueur": "Kit", "num_joueur": 2, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 5, "tps_m": 0, "tps_p": 0, "direction": "E" }) == "Kit -> 5 s:0 m:11 p:0"
    assert serpent.to_str({"nom_joueur": "cat", "num_joueur": 1, "points": 5, "positions": [[5,2], [6,2], [7,2]], "tps_s": 0, "tps_m": 0, "tps_p": 10, "direction": "O" }) == "cat -> 5 s:10 m:11 p:0"



def fabrique_calque(l_arene, num_joueur):
    """Fonction qui réalise l'innondation d'une arène par rapport à la 
       position du joueur. 


    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le joueur considéré

    Returns:
        dict: le calque de l'arène
    """
    calque = arene.copy_arene(l_arene)
    distance = 1 
    lig,col = arene.get_serpent(l_arene, num_joueur)[0]
    possibilities = directions_possibles(calque, num_joueur)
    new_possibilities = set()
    while len(possibilities.difference(seen_case)) != 0:
        for pos in possibilities:
            if pos not in seen_case:
                if pos == "N":
                    if not arene.est_mur(l_arene, lig-1, col):
                        matrice.set_val(calque, lig-1, col, distance)
                if pos == "S":
                    if not arene.est_mur(l_arene, lig+1, col):
                        matrice.set_val(calque, lig+1, col, distance)
                if pos == "E":
                    if not arene.est_mur(l_arene, lig, col+1):
                        matrice.set_val(calque, lig, col+1, distance)
                if pos == "O":
                    if not arene.est_mur(l_arene, lig, col-1):
                        matrice.set_val(calque, lig, col-1, distance)

                for possible in voisins(le_plateau,pos):
                    new_possibilities.add(possible)

            seen_case.add(pos)

        distance += 1
        possibilities = new_possibilities
        new_possibilities = set()

    matrice.set_val(calque,lig,col,0)
    print(calque)
    return calque