import motdepasse

# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_longueur_ok():
    assert motdepasse.longueur_ok("choubouilli") # longueur ok
    assert not motdepasse.longueur_ok("chou") # longueur pas ok
    assert not motdepasse.longueur_ok("") # chaine vide


def test_chiffre_ok():
    assert motdepasse.chiffre_ok("chou9bouilli")  # chiffre au milieu
    assert motdepasse.chiffre_ok("7choubouilli")  # chiffre au début
    assert motdepasse.chiffre_ok("choubouilli5")  # chiffre à la fin
    assert motdepasse.chiffre_ok("chou3boui8lli")  # deux chiffres    
    assert not motdepasse.chiffre_ok("chou")       # pas de chiffres
    assert not motdepasse.chiffre_ok("un deux trois") # pas de chiffres



def test_sans_espace():
    assert motdepasse.sans_espace("choubouilli") # sans espace ok
    assert not motdepasse.sans_espace("chou bouilli") # espace au milieu
    assert not motdepasse.sans_espace(" choubouilli") # espace au début
    assert not motdepasse.sans_espace("choubouilli ") # espace à la fin
    assert motdepasse.sans_espace("") # chaine vide


