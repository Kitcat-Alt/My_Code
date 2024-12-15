# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic-vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

#Exo1
#1.3
def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if liste_observations == []:
        return None
    oiseau_max = ("",0)
    for i in range(len(liste_observations)):
        if liste_observations[i][1] > oiseau_max[1]:
            oiseau_max = liste_observations[i]
    return oiseau_max[0]
#print(oiseau_le_plus_observe(observations1))

#Exo2
#2.1
def info_piaf(Nom_piaf, liste_oiseaux):
    for i in range(len(liste_oiseaux)):
        if liste_oiseaux[i][0] == Nom_piaf:
            return liste_oiseaux[i][1]
    return None
#print(info_piaf("Tourterelle", oiseaux))

#2.2
def oiseaux_in_observation(Famille, liste_oiseaux):
    oiseaux_famille = []
    for i in range(len(liste_oiseaux)):
        if liste_oiseaux[i][1] == Famille:
            oiseaux_famille.append(liste_oiseaux[i])
    return oiseaux_famille
#print(oiseaux_in_observation("Passereau", oiseaux))

#Exo3
#3.1
def est_bien_triee(liste_observation):
    res = None
    for i in range(len(liste_observation)-1):
        if liste_observation[i][0] < liste_observation[i+1][0] and liste_observation[i][1] != 0:
            res = True
        else:
            return False
    return res
#print(est_bien_triee(observations1))

#3.2
def plus_grande_observation(liste_observation):
    max_observation = 0
    for i in range(len(liste_observation)):
        if liste_observation[i][1] > max_observation:
            max_observation = liste_observation[i][1]
    return max_observation
#print(plus_grande_observation(observations2))

#3.3
def moyenne_piaf(liste_observation):
    somme_observation = 0
    nb_obs = 0
    moyenne_obersavtion = 0
    for i in range(len(liste_observation)):
        somme_observation += liste_observation[i][1]
        nb_obs += 1
    moyenne_obersavtion = somme_observation/nb_obs
    return moyenne_obersavtion
#print(moyenne_piaf(observations3))

#3.4
def nb_total_specimen(liste_observation, famille, oiseaux):
    cpt = 0
    liste_famille = []
    for i in range(len(oiseaux)):
        if oiseaux[i][1] == famille:
            liste_famille.append(oiseaux[i][0])
    for i in range(len(liste_observation)):
        if liste_observation[i][0] in liste_famille:
            cpt += liste_observation[i][1]
    return cpt
#print(nb_total_specimen(observations2, "Turtidé", oiseaux))

#Exo4
#4.1
def create_liste_observation(oiseaux, liste_comptage):
    liste_observation = []
    obersvation = ()
    for i in range(len(liste_comptage)):
        if liste_comptage[i] != 0:
            obersvation = (oiseaux[i][0], liste_comptage[i])
            liste_observation.append(obersvation)
            obersvation = ()
    return liste_observation
#print(create_liste_observation(oiseaux, comptage3))

#4.2
def utilisateur_observations(oiseaux):
    liste_observation = []
    observation = ()
    for i in range(len(oiseaux)):
        observation = (oiseaux[i][0], int(input("Entrez le nombre de " + oiseaux[i][0] + " observés : ")))
        if observation[1] != 0: 
            liste_observation.append(observation)
            observation = ()
    return liste_observation
print(utilisateur_observations(oiseaux))

#Exo5
#5.1
def joli_affichage(liste_oiseaux, liste_observation):
    for i in range(len(liste_oiseaux)):










# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)
