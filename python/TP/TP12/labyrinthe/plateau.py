"""
Permet de modéliser un le_plateau de jeu avec :
    - une matrice qui contient des nombres entiers
    - chaque nombre entier correspond à un item :
      MUR, COULOIR, PERSONNAGE, FANTOME
"""
import matrice as mat

MUR = 1
COULOIR = 0
PERSONNAGE = 2
FANTOME = 3

NORD = 'z'
OUEST = 'q'
SUD = 's'
EST = 'd'


def init(nom_fichier="/home/Kitcat/MyCode/python/TP/TP12/labyrinthe/labyrinthe1.txt"):
    """Construit le plateau de jeu de la façon suivante :
        - crée une matrice à partir d'un fichier texte qui contient des COULOIR et MUR
        - met le PERSONNAGE en haut à gauche cad à la position (0, 0)
        - place un FANTOME en bas à droite
    Args:
        nom_fichier (str, optional): chemin vers un fichier csv qui contient COULOIR et MUR.
        Defaults to "./labyrinthe1.txt".

    Returns:
        le plateau de jeu avec les MUR, COULOIR, PERSONNAGE et FANTOME
    """
    matrice = mat.charge_matrice(nom_fichier)
    mat.set_val(matrice, 0, 0, PERSONNAGE)
    mat.set_val(matrice, mat.get_nb_lignes(matrice)-1, mat.get_nb_colonnes(matrice)-1, FANTOME)
    return matrice
#print(init("labyrinthe1.txt"))


def est_sur_le_plateau(le_plateau, position):
    """Indique si la position est bien sur le plateau

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        [boolean]: True si la position est bien sur le plateau
    """
    if position[0] <= mat.get_nb_lignes(le_plateau) and position[0] >= 0 and position[1] <= mat.get_nb_colonnes(le_plateau) and position[1] >= 0:
        return True
    return False



def get(le_plateau, position):
    """renvoie la valeur de la case qui se trouve à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        int: la valeur de la case qui se trouve à la position donnée ou
             None si la position n'est pas sur le plateau
    """
    value = mat.get_val(le_plateau, position[0], position[1])
    if est_sur_le_plateau(le_plateau, position) == True:
        return value
    else:
        return None


def est_un_mur(le_plateau, position):
    """détermine s'il y a un mur à la poistion donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        bool: True si la case à la position donnée est un MUR, False sinon
    """
    value = mat.get_val(le_plateau, position[0], position[1])
    if est_sur_le_plateau(le_plateau, position) == True and value == 1:
        return True
    else:
        return False


def contient_fantome(le_plateau, position):
    """Détermine s'il y a un fantôme à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est un FANTOME, False sinon
    """
    value = mat.get_val(le_plateau, position[0], position[1])
    if est_sur_le_plateau(le_plateau, position) == True and value == 3:
        return True
    else:
        return False

def est_la_sortie(le_plateau, position):
    """Détermine si la position donnée est la sortie
       cad la case en bas à droite du labyrinthe

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est la sortie, False sinon
    """
    mat.get_val(le_plateau, position[0], position[1])
    if est_sur_le_plateau(le_plateau, position) == True and position[0] == mat.get_nb_lignes(le_plateau)-1 and position[1] == mat.get_nb_colonnes(le_plateau)-1:
        return True
    else:
        return False


def deplace_personnage(le_plateau, personnage, direction):
    """déplace le PERSONNAGE sur le plateau si le déplacement est valide
       Le personnage ne peut pas sortir du plateau ni traverser les murs
       Si le déplacement n'est pas valide, le personnage reste sur place

    Args:
        le_plateau (plateau): un plateau de jeu
        personnage (tuple): la position du personnage sur le plateau
        direction (str): la direction de déplacement SUD, EST, NORD, OUEST

    Returns:
        [tuple]: la nouvelle position du personnage
    """
    
    if direction == SUD:
        if get(le_plateau, (personnage[0]+1, personnage[1])) == 0:
            mat.set_val(le_plateau, personnage[0], personnage[1], 0)
            personnage = (personnage[0]+1, personnage[1])
            mat.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)
            return personnage
        else:
            return personnage
        
        
    if direction == NORD:
        if get(le_plateau, (personnage[0]-1, personnage[1])) == 0:
            mat.set_val(le_plateau, personnage[0], personnage[1], 0)
            personnage = (personnage[0]-1, personnage[1])
            mat.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)
            return personnage
        else:
            return personnage
        
    if direction == EST:
        if get(le_plateau, (personnage[0], personnage[1]+1)) == 0:
            mat.set_val(le_plateau, personnage[0], personnage[1], 0)
            personnage = (personnage[0], personnage[1]+1)
            mat.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)
            return personnage
        else:
            return personnage
        
    if direction == OUEST:
        if get(le_plateau, (personnage[0], personnage[1]-1)) == 0:
            mat.set_val(le_plateau, personnage[0], personnage[1], 0)
            personnage = (personnage[0], personnage[1]-1)
            mat.set_val(le_plateau, personnage[0], personnage[1], PERSONNAGE)
            return personnage
        else:
            return personnage
        
le_plateau = init()
print(deplace_personnage(le_plateau, (0, 0), NORD))           


def voisins(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    ens_pos = set()
    if get(le_plateau, (position[0]+1, position[1])) == COULOIR and position[0]+1 < len(le_plateau):
        ens_pos.add((position[0]+1, position[1]))
    
    if get(le_plateau, (position[0]-1, position[1])) == COULOIR and position[0]-1 < len(le_plateau):
        ens_pos.add((position[0]-1, position[1]))
    
    if get(le_plateau, (position[0], position[1]+1)) == COULOIR and position[1]+1 < len(le_plateau):
        ens_pos.add((position[0], position[1]+1))
    
    if get(le_plateau, (position[0], position[1]-1)) == COULOIR and position[1]-1 < len(le_plateau):
        ens_pos.add((position[0], position[1]-1))
    return ens_pos
print(voisins(le_plateau,(8,8)))

def fabrique_le_calque(le_plateau, position_depart):
    """fabrique le calque d'un labyrinthe en utilisation le principe de l'inondation :
       
    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        matrice: une matrice qui a la taille du plateau dont la case qui se trouve à la
       position_de_depart est à 0 les autres cases contiennent la longueur du
       plus court chemin pour y arriver (les murs et les cases innaccessibles sont à None)
    """
    longueur_max = mat.get_nb_lignes(le_plateau) + mat.get_nb_colonnes(le_plateau)
    i2 = 0
    pos_apr_start = set()
    ens_pos = voisins(le_plateau, position_depart)
    while i2 <= longueur_max:
        for position in ens_pos:
            if get(le_plateau, position)!= COULOIR:
                mat.set_val(le_plateau, position[0], position[1], None)
            else:
                mat.set_val(le_plateau, position[0], position[1], i2+1)
        ens_pos = voisins(le_plateau,)
        



def fabrique_chemin(le_plateau, position_depart, position_arrivee):
    """Renvoie le plus court chemin entre position_depart position_arrivee

    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_arrivee (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_arrivee et position_depart
        qui représente un plus court chemin entre les deux positions
    """
    ...


def deplace_fantome(le_plateau, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        le_plateau (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    ...
