#Exo5
la_matrice2 = (3, 4,[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

def get_ligne(matrice, ligne):
    liste_ligne = []
    ind_debut = (ligne-1)*matrice[1]
    ind = 0
    while ind <= (matrice[1]-1):
        liste_ligne.append(matrice[2][ind_debut])
        ind += 1
        ind_debut += 1
    return liste_ligne
#print(get_ligne(la_matrice2,1))

def get_colonne(matrice, colonne):
    liste_colonne = []
    ind_debut = colonne-1
    ind = 0
    while ind <= (matrice[0]-1):
        liste_colonne.append(matrice[2][ind_debut])
        ind += 1
        ind_debut += colonne+1
    return liste_colonne
#print(get_colonne(la_matrice2, 3))

la_matrice_carree = (3, 3,[10, 11, 12, 13, 14, 15, 16, 17, 18])

def diag_principale(matrice):
    liste_diag_principale = []
    ind_diag = 0
    ind = 0
    while ind <= (matrice[1]-1):
        liste_diag_principale.append(matrice[2][ind_diag])
        ind += 1
        ind_diag += matrice[1]+1
    return liste_diag_principale
#print(diag_principale(la_matrice_carree))

def diag_second(matrice):
    liste_diag_second = []
    ind_diag = matrice[1]-1
    ind = 0 
    while ind <= (matrice[1]-1):
        liste_diag_second.append(matrice[2][ind_diag])
        ind += 1
        ind_diag += matrice[1]-1
    return liste_diag_second
#print(diag_second(la_matrice_carree))