#Exo1
liste = [1,2,3,4,5,6,7,8,9]
def trouver_dans_liste(liste, cible):
    ind = 0
    trouve = False
    while ind < len(liste) and not trouve:
        if liste[ind] == cible:
            trouve = True
        ind += 1
    return trouve

#print(trouver_dans_liste(liste, 16))

dico = {'a':10, 'b':6 ,'c':2}

def cumuler_jusqu_a_seuil(dico, seuil):
    total = 0
    ind_dico = 0
    liste_cles = []
    for elem in dico.keys():
        liste_cles.append(elem)
    while total <= seuil and ind_dico < len(liste_cles):
        total += dico[liste_cles[ind_dico]]
        ind_dico += 1
    return total
#print(cumuler_jusqu_a_seuil(dico, 20))

#Exo2
courses = {"lait": 2.30, "pomme": 1, "yaourt": 5}

def ajouter_article():
    article = input("Entrez le nom de l'article que vous voulez ajouter: ")
    prix = input("Entrez le prix de l'article: ")
    courses[article] = float(prix)
    print(courses)
    return courses

#ajouter_article()

def suppr_article():
    article = input("Entrez le nom de l'article que vous voulez supprimer: ")
    courses.pop(article)
    print(courses)
    return courses
#suppr_article()

def modifier_article():
    article = input("Entrez le nom de l'article que vous voulez modifier: ")
    prix = input("Entrez le nouveau prix de l'article: ")
    courses[article] = prix
    print(courses)
    return courses
#modifier_article()

def prix_total_courses(courses):
    prix_total = 0
    for prix in courses.values():
        prix_total += prix
    return prix_total
#print(prix_total_courses(courses))

def plus_cher(courses):
    plus_cher = ""
    prix_max = 0
    for article in courses.keys():
        if courses[article] >= prix_max:
            prix_max = courses[article]
            plus_cher = article
    return plus_cher
#print(plus_cher(courses))

#Exo3

def affichage_menu(titre):
    print("+----------------------------+")
    print("|Bienvenu sur" + titre + "|")
    print("+----------------------------+")

def programme_principal(courses):
    running = True
    affichage_menu("")

