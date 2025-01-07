""" tests pour le module matrice"""
import matrice

def matrice1():
    m1 = matrice.new_matrice(3, 4, None)
    matrice.set_val(m1, 0, 0, 10)
    matrice.set_val(m1, 0, 1, 11)    
    matrice.set_val(m1, 0, 2, 12)
    matrice.set_val(m1, 0, 3, 13)
    matrice.set_val(m1, 1, 0, 14)
    matrice.set_val(m1, 1, 1, 15)
    matrice.set_val(m1, 1, 2, 16)
    matrice.set_val(m1, 1, 3, 17)
    matrice.set_val(m1, 2, 0, 18)
    matrice.set_val(m1, 2, 1, 19)
    matrice.set_val(m1, 2, 2, 20)
    matrice.set_val(m1, 2, 3, 21)
    return m1

def matrice2():
    m2 = matrice.new_matrice(2, 3, None)
    matrice.set_val(m2, 0, 0, 'A')
    matrice.set_val(m2, 0, 1, 'B')    
    matrice.set_val(m2, 0, 2, 'C')
    matrice.set_val(m2, 1, 0, 'D')
    matrice.set_val(m2, 1, 1, 'E')
    matrice.set_val(m2, 1, 2, 'F')
    return m2

def matrice3():
    m3 = matrice.new_matrice(3, 3, None)
    matrice.set_val(m3, 0, 0, 2)
    matrice.set_val(m3, 0, 1, 7)    
    matrice.set_val(m3, 0, 2, 6)
    matrice.set_val(m3, 1, 0, 9)
    matrice.set_val(m3, 1, 1, 5)
    matrice.set_val(m3, 1, 2, 1)
    matrice.set_val(m3, 2, 0, 4)
    matrice.set_val(m3, 2, 1, 3)
    matrice.set_val(m3, 2, 2, 8)
    return m3

def test_get_nb_lignes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert matrice.get_nb_lignes(m1) == 3
    assert matrice.get_nb_lignes(m2) == 2
    assert matrice.get_nb_lignes(m3) == 3
        
def test_get_nb_colonnes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert matrice.get_nb_colonnes(m1) == 4
    assert matrice.get_nb_colonnes(m2) == 3
    assert matrice.get_nb_colonnes(m3) == 3

def test_get_val():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert matrice.get_val(m1, 0, 1) == 11
    assert matrice.get_val(m1, 2, 1) == 19
    assert matrice.get_val(m2, 1, 1) == 'E'
    assert matrice.get_val(m2, 0, 2) == 'C'
    assert matrice.get_val(m3, 2, 0) == 4
    assert matrice.get_val(m3, 1, 0) == 9

def test_sauve_charge_matrice():
    m1 = matrice1()
    matrice.sauve_matrice(m1, "matrice1.csv")
    m = matrice.charge_matrice("matrice1.csv")
    assert m1 == m
    m2 = matrice2()
    matrice.sauve_matrice(m2, "matrice2.csv")
    m = matrice.charge_matrice("matrice2.csv", type_valeur='str')
    assert m2 == m
    m3 = matrice3()
    matrice.sauve_matrice(m3, "matrice3.csv")
    m = matrice.charge_matrice("matrice3.csv")
    assert m3 == m     