import random
import csv

import random
import csv

def creer_matrice(nombre_lignes, nombre_colonnes):
    matrice = []
    for _ in range(nombre_lignes):
        ligne_matrice = []
        for _ in range(nombre_colonnes):
            ligne_matrice.append(random.randint(0, 100))
        matrice.append(ligne_matrice)
    return matrice

def get_valeur(matrice, ligne, colonne):
    return matrice[ligne][colonne]

def set_valeur(matrice, ligne, colonne, valeur):
    matrice[ligne][colonne] = valeur

def get_ligne(matrice, num_ligne):
    return matrice[num_ligne]

def get_colonne(matrice, num_colonne):
    return [matrice[i][num_colonne] for i in range(len(matrice))]

def get_nombre_de_colonnes(matrice):
    return len(matrice[0]) if matrice else 0

def get_nombre_de_lignes(matrice):
    return len(matrice)

def enregistre_matrice(matrice, nom_fichier):
    with open(nom_fichier, 'w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        for ligne in matrice:
            writer.writerow(ligne)

def charge_matrice(nom_fichier):
    matrice_chargee = []
    with open(nom_fichier, 'r') as fichier_csv:
        reader = csv.reader(fichier_csv)
        for ligne in reader:
            ligne_entiers = [int(valeur) for valeur in ligne]
            matrice_chargee.append(ligne_entiers)
    return matrice_chargee
