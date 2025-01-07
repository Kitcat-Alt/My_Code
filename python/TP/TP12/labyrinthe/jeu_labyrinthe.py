"""Permet de jouer au jeu du labyrinthe"""
import os
import plateau
import getch
import matrice
import matrice_graphique

def affiche_menu1():
    """Affiche le premier menu en sortie standart"""
    print(' ===== MON SUPER JEU =====')
    print(' (J)ouer ?')
    print(' (Q)uitter ?')


def affiche_menu2():
    """Affiche le deuxième menu (pour jouer) sur la sortie standart"""
    print(' ===== MON SUPER JEU =====')
    print('Choisissez une direction')
    print(plateau.NORD+":NORD\n "+
          plateau.EST+":EST\n "+
          plateau.SUD+":SUD\n "+
          plateau.OUEST+":OUEST\n")


def affiche_jeu(le_plateau, affichage_graphique=None):
    """Permet à l'utilisateur d'interagir avec le jeu
    Sur la sortie standart :
        - le terminal est clear
        - on affiche le deuxième menu
        - on affiche le plateau de jeu
    En mode graphique (si affiche_graphique n'est pas à None)
        - on met à jour l'affichage de la matrice dans une fenêtre pygame
    """
    os.system('clear')
    affiche_menu2()
    matrice.affiche(le_plateau)
    if affichage_graphique is not None:
        affichage_graphique.affiche_matrice()


def saisie_un_seul_caractere():
    """
    Attend que l'utilisateur tape un caractère au clavier et
    renvoie ce caractère sans avoir besoin d'appuyer sur la touche Entrée
    """
    return getch.getch()


def lance_menu():
    """
    Permet à l'utilisateur d'interagir avec le premier menu :
    lancer le jeu ou quitter l'application
    """
    affiche_menu1()
    quitte = False
    while not quitte:
        caractere = saisie_un_seul_caractere()
        if caractere.upper() == 'Q':
            quitte = True
        elif caractere.upper() == 'J':
            joue()


def affiche_message(message, affichage_graphique=None):
    """Affiche un message
    Sur la sortie standart :
        -  affiche le message sur la sortie standart
    En mode graphique (si affiche_graphique n'est pas à None)
        - affiche le message dans la fenêtre pygame
    """
    print(message)
    if affichage_graphique is not None:
        affichage_graphique.affiche_message(message)


def fin_du_jeu(gagne, affichage_graphique=None):
    """Gère les affichage en fin de partie"""
    if gagne:
        message = 'Bravo ! vous avez gagné !'
    else:
        message = 'Oh non ! Le fantome vous a attrapé !?'
    affiche_message(message, affichage_graphique)
    lance_menu()


def joue():
    """Permet de lancer le jeu du labyrinthe et y jouer"""
    mon_plateau = plateau.init()
    personnage = (0, 0)
    fantome = (matrice.get_nb_lignes(mon_plateau) - 1, matrice.get_nb_colonnes(mon_plateau) - 1)
    sortie = (matrice.get_nb_lignes(mon_plateau) - 1, matrice.get_nb_colonnes(mon_plateau) - 1)
    affichage_graphique = None
    affiche_jeu(mon_plateau, affichage_graphique)
    quitte = False
    while not quitte:
        direction = saisie_un_seul_caractere()
        personnage = plateau.deplace_personnage(mon_plateau, personnage, direction)
        fantome = plateau.deplace_fantome(mon_plateau, fantome, personnage)
        affiche_jeu(mon_plateau, affichage_graphique)
        if personnage == fantome:
            fin_du_jeu(False, affichage_graphique)
            quitte = True
        elif personnage == sortie:
            fin_du_jeu(True, affichage_graphique)
            quitte = True


joue()
