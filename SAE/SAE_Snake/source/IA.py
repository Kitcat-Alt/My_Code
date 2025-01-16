# coding: utf-8
"""
            SAE1.02 SERPIUT'O
         BUT1 Informatique 2024-2025

    Module IA.py
    Ce module implémente toutes les fonctions ainsi que l'IA de votre serpent
"""

import partie
import argparse
import client
import random
import arene
import serpent
import case

import matrice

direction_prec='X' # variable indiquant la décision précédente prise par le joueur. A mettre à jour soi-même
DIRECTIONS={"N":(-1,0),"E":(0,1),"S":(1,0),"O":(0,-1)}

####################################################################
### A partir d'ici, implémenter toutes les fonctions qui vous seront 
### utiles pour prendre vos décisions
### Toutes vos fonctions devront être documentées
####################################################################

def get_next_pos(ligne: int,col: int,direction: str) -> int:
    """Indique les coordonnées d'une position après mouvement
    
    Args:
        ligne,col (int): les  coordonnées de positions actuelles
        direction (str): la direction

    Returns:
        int: ligne et col après déplacement   
    """
    ligne += arene.DIRECTIONS[direction][0]
    col += arene.DIRECTIONS[direction][1]

    return ligne,col

def going_back(dir: str):
    """Revoie la direction pour faire marche arrière

    Args:
        dir(str): la direction précédente

    Returns:    
        str: direction opposée de la direction précédente
    """
    backward_dir = ""

    match dir:
        case "N":
            backward_dir = "S"
        case "S":
            backward_dir = "N"
        case "O":
            backward_dir = "E"
        case "E":
            backward_dir = "O"

    return backward_dir
            


def direction_possibles_coords(l_arene: dict,ligne: int,col: int,num_joueur: int) -> str:
    """Indique les directions possible pour le joueur num_joueur
        c'est à dire les directions qu'il peut prendre sans se cogner dans
        un mur, sortir de l'arène ou se cogner sur une boîte trop grosse pour sa tête

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur

    Returns:
        str: une chaine composée de NOSE qui indique les directions
            pouvant être prise par le joueur. Attention il est possible
            qu'aucune direction ne soit possible donc la fonction peut retourner la chaine vide
    """ 
    res=''
    mat=l_arene["matrice"]
    nb_lig=matrice.get_nb_lignes(mat)
    nb_col=matrice.get_nb_colonnes(mat)
    copy_arena = arene.copy_arene(l_arene)

    player_head_ligne,player_head_col = arene.get_serpent(copy_arena,num_joueur)[0]
    player_head_val = arene.get_val_boite(l_arene,player_head_ligne,player_head_col)

    for dir in 'NOSE':
        delta_lig,delta_col=DIRECTIONS[dir]
        lig_arr=ligne+delta_lig
        col_arr=col+delta_col
        if lig_arr<0 or lig_arr>=nb_lig or col_arr<0 or col_arr>=nb_col:
            continue
        if case.est_mur(matrice.get_val(mat,lig_arr,col_arr)):
            continue
        if case.get_proprietaire(matrice.get_val(mat,lig_arr,col_arr))==num_joueur:
            continue
        if player_head_val < case.get_val_boite (matrice.get_val(mat,lig_arr,col_arr)):
            continue
        res+=dir
    return res

def directions_possibles(l_arene:dict,num_joueur:int)->str:
    res=''
    mat=l_arene["matrice"]
    nb_lig=matrice.get_nb_lignes(mat)
    nb_col=matrice.get_nb_colonnes(mat)
    lig_dep,col_dep=serpent.get_liste_pos(l_arene["serpents"][num_joueur-1])[0]
    copy_arena = arene.copy_arene(l_arene)

    player_head_ligne,player_head_col = arene.get_serpent(copy_arena,num_joueur)[0]
    player_head_val = arene.get_val_boite(l_arene,player_head_ligne,player_head_col)

    for dir in 'NOSE':
        delta_lig,delta_col=DIRECTIONS[dir]
        lig_arr=lig_dep+delta_lig
        col_arr=col_dep+delta_col
        if lig_arr<0 or lig_arr>=nb_lig or col_arr<0 or col_arr>=nb_col:
            continue
        if case.est_mur(matrice.get_val(mat,lig_arr,col_arr)):
            continue
        if case.get_proprietaire(matrice.get_val(mat,lig_arr,col_arr))==num_joueur:
            continue
        if player_head_val < case.get_val_boite (matrice.get_val(mat,lig_arr,col_arr)):
            continue
        res+=dir
    return res

def est_impasse(l_arene:dict,ligne:int,col:int,num_joueur:int,dir:str):
    
    next_ligne,next_col = get_next_pos(ligne,col,dir)
    next_possibilities = direction_possibles_coords(l_arene,next_ligne,next_col,num_joueur)

    if len(next_possibilities) > 1:
        return False
    
    if len(next_possibilities) == 0:
        return True
    
    while len(next_possibilities) == 1:
        next_ligne,next_col = get_next_pos(next_ligne,next_col,next_possibilities[0])
        next_possibilities = direction_possibles_coords(l_arene,next_ligne,next_col,num_joueur)

        if len(next_possibilities) > 1:
            return False
    
        if len(next_possibilities) == 0:
            return True

    return True

def fabrique_calque(l_arene, num_joueur):
    calque = arene.copy_arene(l_arene)
    distance = 1 
    lig,col = arene.get_serpent(l_arene, num_joueur)[0]
    possibilities = directions_possibles(calque, num_joueur)
    new_possibilities = set()
    while len(possibilities.difference(seen_case)) != 0:
        for pos in possibilities:
            if pos not in seen_case:
                if pos == "N":
                    if not arene.est_mur(l_arene, lig-1, col):
                        matrice.set_val(calque, lig-1, col, distance)
                if pos == "S":
                    if not arene.est_mur(l_arene, lig+1, col):
                        matrice.set_val(calque, lig+1, col, distance)
                if pos == "E":
                    if not arene.est_mur(l_arene, lig, col+1):
                        matrice.set_val(calque, lig, col+1, distance)
                if pos == "O":
                    if not arene.est_mur(l_arene, lig, col-1):
                        matrice.set_val(calque, lig, col-1, distance)

                for possible in voisins(le_plateau,pos):
                    new_possibilities.add(possible)

            seen_case.add(pos)

        distance += 1
        possibilities = new_possibilities
        new_possibilities = set()

    matrice.set_val(calque,lig,col,0)
    print(calque)
    return calque

def mon_IA(num_joueur:int, la_partie:dict)->str:
    """Fonction qui va prendre la decision du prochain coup pour le joueur de numéro ma_couleur

    Args:
        num_joueur (int): un entier désignant le numero du joueur qui doit prendre la décision
        la_partie (dict): structure qui contient la partie en cours

    Returns:
        str: une des lettres 'N', 'S', 'E' ou 'O' indiquant la direction que prend la tête du serpent du joueur
    """
    arene = partie.get_arene(la_partie)
    meilleur_dir = meilleure_direction(arene, num_joueur)
    print()

    if meilleur_dir is None:
        meilleur_dir=random.choice("NSEO")

    return meilleur_dir
 


def meilleure_direction(l_arene:dict,num_joueur:int):
    position_joueur = arene.get_serpent(l_arene, num_joueur)[0]
    ligne = position_joueur[0]
    col = position_joueur[1]
    directions = directions_possibles(l_arene,num_joueur)
    points = {}
    for direction in directions:
        if direction == "N":
            points["N"] = [arene.get_val_boite(l_arene, ligne - 1, col),(ligne -1 ,col)]
        if direction == "S":
            points["S"] = [arene.get_val_boite(l_arene, ligne + 1, col),(ligne + 1,col)]
        if direction == "E":
            points["E"] = [arene.get_val_boite(l_arene, ligne, col + 1),(ligne,col + 1)]
        if direction == "O":
            points["O"] = [arene.get_val_boite(l_arene, ligne, col - 1),(ligne,col - 1)]
    
    #pas de directions possibles donc marche arrière
    if points == dict():
        return going_back(arene.get_derniere_direction(l_arene,num_joueur))
    
    for Dir, val in points.items():
        if val[0] == arene.MULTIPLIE and not est_impasse(l_arene,val[1][0],val[1][1],num_joueur,Dir):
            return Dir
    for Dir, val in points.items():
        if val[0] == arene.PROTECTION and not est_impasse(l_arene,val[1][0],val[1][1],num_joueur,Dir):
            return Dir
    for Dir, val in points.items():
        if val[0] == arene.AJOUTE and not est_impasse(l_arene,val[1][0],val[1][1],num_joueur,Dir):
            return Dir
        
    return max(points, key=points.get)
                                                                                                                                                                                                                    
def mon_IA_bete(num_joueur:int, la_partie:dict)->str:
    """Fonction qui va prendre la decision du prochain coup pour le joueur de numéro ma_couleur

    Args:
        num_joueur (int): un entier désignant le numero du joueur qui doit prendre la décision
        la_partie (dict): structure qui contient la partie en cours

    Returns:
        str: une des lettres 'N', 'S', 'E' ou 'O' indiquant la direction que prend la tête du serpent du joueur
    """
    direction=random.choice("NSEO")
    direction_prec=direction #La décision prise sera la direction précédente le prochain tour
    dir_pos=arene.directions_possibles(partie.get_arene(la_partie),num_joueur)
    if dir_pos=='':
        direction=random.choice('NOSE')
    else:
        direction=random.choice(dir_pos)
    return direction


if __name__=="__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--equipe", dest="nom_equipe", help="nom de l'équipe", type=str, default='Non fournie')
    parser.add_argument("--serveur", dest="serveur", help="serveur de jeu", type=str, default='localhost')
    parser.add_argument("--port", dest="port", help="port de connexion", type=int, default=1111)
    
    args = parser.parse_args()
    le_client=client.ClientCyber()
    le_client.creer_socket(args.serveur,args.port)
    le_client.enregistrement(args.nom_equipe,"joueur")
    ok=True
    while ok:
        ok,id_joueur,le_jeu,_=le_client.prochaine_commande()
        if ok:
            la_partie=partie.partie_from_str(le_jeu)
            actions_joueur=mon_IA(int(id_joueur),la_partie)
            le_client.envoyer_commande_client(actions_joueur)
    le_client.afficher_msg("terminé")
