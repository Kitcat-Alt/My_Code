def sante(taille,poids):
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
print(sante(1.78,60))