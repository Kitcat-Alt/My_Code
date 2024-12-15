def mystere(liste, valeur):
    """[summary]
    la fonction compte le nombre d'itération qu'il faut faire pour trouver 4 fois la valeur donnée dans une liste.

    Args:
        liste ([list]): [liste de nombres]
        valeur ([int]): [un nombre]

    Returns:
        [int]: [le nombre d'ittération qu'il à fallu faire pour trouver 4 fois la valeur donnée en para]
        [Boleen]: [il y a moins de 4 fois la mm valeur dans la liste]
    """
    nb_itérations = 0
    nbvaleur = 0
    for elem in liste:
        if elem == valeur:
            nbvaleur += 1
            if nbvaleur > 3:
                return nb_itérations
        nb_itérations += 1
    return None

#print(mystere([12, 5, 8, 20, 12, 20, 185, 20, 5, 20], 20))

def test_nb_itérations():
    assert test_nb_itérations([12, 5, 8, 20, 12, 20, 185, 20, 5, 20]) == 9
    assert test_nb_itérations([12, 5, 8, 12, 20, 185, 20, 5, 20]) == 8
    assert test_nb_itérations([12, 5, 8, 20, 12, 20, 185]) == 7
    assert test_nb_itérations([12, 5, 8]) == None

#1.4
def nb_itérations(liste, valeur):
    nb_itérations = 0
    nbvaleur = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            nbvaleur += 1
            if nbvaleur > 3:
                return nb_itérations
            nb_itérations += 1
    return None


liste_villes1 = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux", "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population1 = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,  25725]
#Exo2
#2.1
def IndicePremierInt(phrase):
    chiffres = '0123456789'
    for i in range(len(phrase)):
        if phrase[i] in chiffres:
            return i
    return None
#print(IndicePremierInt("on est le 30/09/2021"))

#2.2
def PopulationVille(liste_villes, population, ville):
    res = None
    for i in range(len(liste_villes)):
        if liste_villes[i] == ville:
            res = population[i]
            return res
        elif liste_villes[i] != ville:
            res = None
    return res
        
#print(PopulationVille(liste_villes1, population1, "Vierzon"))

#Exo 3 
#3.1
def ordreCroissant(liste_val):
    for i in range(1, len(liste_val)-1):
        if liste_val[i-1] < liste_val[i+1]:
            res = True
        else:
            res = False
    return res
#print(ordreCroissant([1,2,3,4,5]))

#3.2
def DepasseSeuil(liste_val, seuil):
    somme_val = 0
    res = None
    for i in range(len(liste_val)):
        somme_val += liste_val[i]
    if somme_val > seuil:
        res = True
    else:
        res = False
    return res

#print(DepasseSeuil([1, 4], 6))

#3.3
def AdresseMail(mail):
    cptAt = 0
    res = True
    mail_split = []
    mailAT = []
    point = "."
    for i in range(len(mail)):
        if mail[0] == "@" or mail[-1] == "." or "@" not in mail:
            res = False
            return res
        
        if mail[i] == "@":
            cptAt += 1
            if cptAt > 1:
                res = False
                return res
    for i in range(len(mail)):
        if mail[i] != ' ':
            res = True
        if mail[i] == ' ':
            res = False
            return res
    mail_split = mail.split("@")
    mailAT = mail_split[1]
    for i in range(len(mailAT)):
        if mailAT[i] not in point:
            res = False
        elif mailAT[i] == ".":
            res = True
            return res
    return res

#print(AdresseMail("matteofouchergmail.com"))

#Exo4
#4.1
def Best_Score(scores, joueurs, Prenom):
    Score_max = 0
    get_Score = 0
    for i in range(len(joueurs)):
        if Prenom not in joueurs:
            return None
        if joueurs[i] == Prenom:
            get_Score = scores[i]
            if get_Score > Score_max:
                Score_max = 0
                Score_max += get_Score
    return Score_max

#print(Best_Score([352100, 325410, 312785, 220199, 127853], ['Batman', 'Robin', 'Batman', 'Joker', 'Batman'], "Batman"))

#4.2
def Score_décroissant(scores):
    res = None
    for i in range(len(scores)-1):
        if scores[i] > scores[i+1]:
            res = True
        else:
            return False
    return res
#print(Score_décroissant([352100, 325410, 312785, 220199, 127853]))

#4.3
def nb_Joueur_BS(joueurs, Prenom):
    cpt_Joueur = 0
    for i in range(len(joueurs)):
        if joueurs[i] == Prenom:
            cpt_Joueur+=1
    if cpt_Joueur == 0:
        return None
    return cpt_Joueur
#print(nb_Joueur_BS(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'], "Harley"))

#4.4
def Best_classement(joueurs, Prenom):
    if Prenom not in joueurs:
        return None
    for i in range(len(joueurs)):
        if joueurs[i] == Prenom:
            return i+1
#print(Best_classement(['Batman', 'Robin', 'Batman', 'Joker', 'Batman'], "Harley"))

#4.5
def ranger(score, liste_score):
    for i in range(1, len(liste_score)-1):
        if score > liste_score[i]:
            return i
    return len(liste_score)
#print(ranger(250000, [352100, 325410, 312785, 220199, 127853]))

#4.6
def ajouter(score, Prenom, liste_score, joueurs):            
        place = ranger(score, liste_score)
        liste_score.insert(place, score)
        joueurs.insert(place, Prenom)
print(ajouter(150000, "Harley", [352100, 325410, 312785, 220199, 127853], ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']))
        
                
        


    




# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
