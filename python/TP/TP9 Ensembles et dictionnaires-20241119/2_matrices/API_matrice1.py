""" Matrices : API n 1 """
la_matrice = (3, 4,[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])


def matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    matrice = (nb_lignes, nb_colonnes, [])
    for i in range(nb_lignes*nb_colonnes):
        matrice[2].append(valeur_par_defaut)
    return matrice
#print(matrice(6,3,4))

    



def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    indice = (ligne*la_matrice[1]+colonne)
    la_matrice[2][indice] = nouvelle_valeur
    return la_matrice
#print(set_val(la_matrice, 2, 1, 58))


def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    if la_matrice == ():
        return None
    else:
        return la_matrice[0]
#print(get_nb_lignes(()))

def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    if la_matrice == ():
        return None
    else:
        return la_matrice[1]
#print(get_nb_colonnes((6, 3, [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])))


def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    indice = (ligne*get_nb_colonnes(la_matrice)+colonne)
    return la_matrice[2][indice]
#print(get_val(la_matrice, 2, 1))
# Fonctions pour l'affichage

def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(la_matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def charge_matrice_str(nom_fichier):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    matrice = []
    fic = open(nom_fichier, "r")
    nb_ligne = 0
    nb_colonne = 0
    for ligne in fic:
        carac = ligne.split(",")
        carac.pop()
        matrice.append(carac)
        nb_ligne +=1
    fic.close()
    nb_colonne = len(matrice[0])
    matrice_finale = (nb_ligne, nb_colonne, matrice)
    return matrice_finale
#print(charge_matrice_str("python/TP/TP9 Ensembles et dictionnaires-20241119/2_matrices/matrice.csv"))


def sauve_matrice(la_matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    fic = open(nom_fichier, "w")
    for i in range(len(la_matrice)):
        fic.write(ligne)
    fic.close
#print(sauve_matrice(la_matrice, "bleh.csv"))

#-------------------------------------------------------
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
print(diag_second(la_matrice_carree))







