def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel
    prec = ''  # caractère précédent dans la chaine
    for lettre in chaine:
        if lettre == prec:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
        prec = lettre
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    return lg_max


# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]

#exo 4
def Premiere_lettre(liste_mots, lettre):
    res = []
    for i in range(len(liste_mots)):
        for l in liste_mots[i]:
            if lettre != l[0]:
                break
            else:
                res.append(liste_mots[i])
    return res

#print(Premiere_lettre(["salut","hello","hallo","ciao","hola"],"c"))

#exo 5
def mots_phrase(phrase):
    liste_mots =[]
    mots = ''
    res = None
    for i in range(len(phrase)):
        res = phrase[i].isalpha()
        if res == True:
            mots = mots + phrase[i]
        elif mots:
            liste_mots.append(mots)
            mots = ''
    if mots != '':
        liste_mots.append(mots)
    return liste_mots

#print(mots_phrase("Cela fait déjà 28 jours! 28 jours à l'IUT'O! Cool"))

#exo 6
def same_first_letter(phrase, lettre):
    liste1_mots =[]
    liste2_mots = []
    mots = ''
    res = None
    res2 = []
    for i in range(len(phrase)):
        res = phrase[i].isalpha()
        if res == True:
            mots = mots + phrase[i]
        elif mots:
            liste1_mots.append(mots)
            mots = ''
    if mots != '':
        liste1_mots.append(mots)
    
    liste2_mots = liste1_mots
    for i in range(len(liste2_mots)):
        for l in liste2_mots[i]:
            if lettre != l[0]:
                break
            else:
                res2.append(liste2_mots[i])
    return res2

#print(same_first_letter("Cela fait déjà 28 jours! 28 jours à l'IUT'O! Cool!!", "j"))

#exo7.1
def list_bool(N):
    liste_N = [False,False]
    for i in range(2,N+1):
        liste_N.append(True)
    return liste_N
#print(list_bool(5))

#exo7.2
def False_multiple(N,x):
    list_bool2 = list_bool(N)
    for i in range(2,len(list_bool2),x):
        list_bool2[i] = False
        if i == 2:
            list_bool2[i] = True
    return list_bool2

#print(False_multiple(6,3))

#exo 7.3
def Nombres_Premier(N,x):
    n_cpt = 0
    list_bool2 = list_bool(N)
    liste_nombres_premiers =[]
    for i in range(2,len(list_bool2),x):
        list_bool2[i] = False
        if i == x:
            list_bool2[i] = True
    print(list_bool2)
    
    for i in range(len(list_bool2)):
        if list_bool2[i] == True:
            liste_nombres_premiers.append(i)    
    return liste_nombres_premiers
print(Nombres_Premier(10,2))





    




