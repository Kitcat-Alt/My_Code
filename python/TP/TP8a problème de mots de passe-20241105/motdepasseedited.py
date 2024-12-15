def longueur_ok(mot_de_passe):
    if len(mot_de_passe) < 8:
        longueur_ok = False
    else:
        longueur_ok = True
    return longueur_ok

def chiffre_ok(mot_de_passe):
    chiffre_ok = False
    cpt_chiffre = 0
    for lettre in mot_de_passe:
        if lettre.isdigit():
            cpt_chiffre += 1
    if cpt_chiffre >= 3:
        chiffre_ok = True
        return chiffre_ok
    else:
        return chiffre_ok

def sans_chiffre_consecutif(mot_de_passe):
    chiffre_consec = True
    for i in range(1, len(mot_de_passe)):
        if mot_de_passe[i-1].isdigit() and mot_de_passe[i].isdigit():
            chiffre_consec = False
            return chiffre_consec
    return chiffre_consec

def chiffre_plus_petit_1_fois(mot_de_passe):
    ...

    
    
def sans_espace(mot_de_passe):
    sans_espace = True
    for lettre in mot_de_passe:
        if lettre == " ":
            sans_espace = False  
    return sans_espace  


def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    res = None
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok(mot_de_passe) and not sans_chiffre_consecutif(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 3 chiffre et ne doit pas comporter deux chiffres consécutifs")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")	   
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe

dialogue_mot_de_passe()
