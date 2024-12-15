def sante(taille,poids):
    """Permet de détecter un problème de santé en fonction de l'imc

    Args:
        taille (_type_): la taille de la personne en mètre
        poids (_type_): le pid de la personne en kg

    Returns:
        str: le problème éventuellement détecté
    """
    imc = poids/(taille*taille)
    if imc < 16.5:
        res = "famine"
    elif imc < 18.5:
        res = "maigreur"
    elif imc < 25:
        res = "normal"
    elif imc > 30:
        res = "surpoids"
    else: 
        res = "obésité"
    return res
def test_sante():
    assert sante(1.8,80) == "normal"
    assert sante(1.6, 67) == "obésité"