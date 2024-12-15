# Codé par Papy Force X, jeune padawan de l'informatique

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        # je vérifie la longueur
        if len(mot_de_passe) < 8:
            longueur_ok = False
        else:
            longueur_ok = True
        # je vérifie s'il y a un chiffre
        chiffre_ok = False
        for lettre in mot_de_passe:
            if lettre.isdigit():
                chiffre_ok = True
        # je vérifie qu'il n'y a pas d'espace
        sans_espace = True
        for lettre in mot_de_passe:
            if lettre == " ":
                sans_espace = False
        # Je gère l'affichage
        if not longueur_ok:
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok:
            print("Votre mot de passe doit comporter au moins un chiffre")
        elif not sans_espace:
            print("Votre mot de passe ne doit pas comporter d'espace")	   
        else:
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe

dialogue_mot_de_passe()
