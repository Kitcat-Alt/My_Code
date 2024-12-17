import api_matrice as mat
ATM={'Armand':'Beatrice', 'Beatrice':'Cesar', 'Cesar':'Dalida', 'Dalida':'Cesar', 'Etienne':'Beatrice', 'Firmin':'Henri', 'Gaston':'Beatrice','Henri':'Firmin'}
#Exo2
#2.1
def couples(amoureux):
    liste_couples = []
    couple = ()
    for personne, amoureu in amoureux.items():
        if personne == amoureux[amoureu]:
            couple = (personne, amoureu)
            if (amoureu, personne) not in liste_couples:
                liste_couples.append(couple)
        couple = ()
    return liste_couples
#print(couples(ATM))

#2.2
def est_amoureux(ATM, personne):
    liste_amoureux = []
    for amoureux, pers in ATM.items():
        if pers == personne:
            liste_amoureux.append(amoureux)
    return liste_amoureux
print(est_amoureux(ATM, 'Beatrice'))

#Exo3
matrice = [[1,2,3],[4,5,6],[7,8,9]]
def sous_matrice(matrice, nb_lignes, nb_colonnes, position_haut, position_gauche):
    mat.get_ligne(matrice, position_haut)