import bilan_carbone as bc

def afficher_menu():
    print('\n'"Que voulez-vous faire ? \n(Pensez a CHARGER une ACTIVITE avant de commencer)"'\n')
    print("[1] Charger des activités à partir d'un fichier")
    print("[2] Sauvegarder des activités dans un fichier")
    print("[3] Afficher la liste des personnes")
    print("[4] Rechercher une activité")
    print("[5] Filtrer les activités par prénom")
    print("[6] Fusionner deux listes d'activités")
    print("[7] Afficher la première apparition d'un type d'activité")
    print("[8] Afficher le cumul des émissions")
    print("[9] Afficher le temps d'une activité")
    print("[10] Afficher la liste des types d'activités")
    print("[11] Afficher la plus longue période d'émissions décroissantes")
    print("[12] Afficher l'activité avec les émissions maximales")
    print("[13] Quitter")

def charger_activites():
    nom_fichier = input("Entrez le nom du fichier à charger : ")
    activites = bc.charger_activites(nom_fichier)

    print('\n'"Activités chargées :")
    print(activites)

    return activites

def sauvegarder_activites(activites):
    nom_fichier = input("Entrez le nom du fichier où sauvegarder les activités : ")

    bc.sauver_activites(nom_fichier, activites)
    print('\n'"Activités sauvegardées.")

def afficher_liste_personnes(activites):
    personnes = bc.liste_des_personnes(activites)

    print('\n'"Liste des personnes :")
    print(personnes)

def rechercher_activite(activites):
    prenom = input("Entrez le prénom : ")
    jour = input("Entrez le jour (YYYY-MM-DD) : ")
    type_activite = input("Entrez le type d'activité : ")
    activite = bc.recherche_activite_dichotomique(prenom, jour, type_activite, activites)

    print('\n'"Activité trouvée :")
    print(activite)

def filtrer_par_prenom(activites):
    prenom = input("Entrez le prénom : ")
    activites_filtrees = bc.filtre_par_prenom(activites, prenom)

    print('\n'"Activités filtrées :")
    print(activites_filtrees)

def fusionner_listes():
    print("Charger la première liste d'activités :")
    activites1 = charger_activites()

    print("Charger la deuxième liste d'activités :")
    activites2 = charger_activites()

    activites_fusionnees = bc.fusionner_activites(activites1, activites2)

    print('\n'"Activités fusionnées :")
    print(activites_fusionnees)

    sauvegarder = input("Voulez-vous sauvegarder la liste fusionnée dans un fichier ? (oui/non) : ")
    if sauvegarder.lower() == 'oui':
        sauvegarder_activites(activites_fusionnees)
    return activites_fusionnees

def afficher_premiere_apparition_type(activites):
    type_act = input("Entrez le type d'activité : ")
    apparition = bc.premiere_apparition_type(activites, type_act)

    print("Première apparition du type d'activité :")
    print(apparition)

def afficher_cumul_emissions(activites):
    cumul = bc.cumul_emmissions(activites)

    print("Cumul des émissions :")
    print(cumul)

def afficher_temps_activite(activites):
    prenom = input("Entrez le prénom : ")
    jour = input("Entrez le jour (YYYY-MM-DD) : ")
    type_activite = input("Entrez le type d'activité : ")
    activite = bc.recherche_activite_dichotomique(prenom, jour, type_activite, activites)
    temps = bc.temps_activite(activite, bc.co2_minute)

    print("Temps de l'activité :")
    print(temps)

def afficher_liste_types(activites):
    types = bc.liste_des_types(activites)

    print("Liste des types d'activités :")
    print(types)

def afficher_plus_longue_periode_emissions_decroissantes(activites):
    periode = bc.plus_longue_periode_emmissions_decroissantes(activites)

    print("Plus longue période d'émissions décroissantes :")
    print(periode, 'jours')

def afficher_max_emission(activites):
    max_em = bc.max_emmission(activites)
    
    print("Activité avec les émissions maximales :")
    print(max_em)

def programme_principal():
    activites = []
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")
        if choix == "1":
            activites = charger_activites()
        elif choix == "2":
            sauvegarder_activites(activites)
        elif choix == "3":
            afficher_liste_personnes(activites)
        elif choix == "4":
            rechercher_activite(activites)
        elif choix == "5":
            filtrer_par_prenom(activites)
        elif choix == "6":
            activites = fusionner_listes()
        elif choix == "7":
            afficher_premiere_apparition_type(activites)
        elif choix == "8":
            afficher_cumul_emissions(activites)
        elif choix == "9":
            afficher_temps_activite(activites)
        elif choix == "10":
            afficher_liste_types(activites)
        elif choix == "11":
            afficher_plus_longue_periode_emissions_decroissantes(activites)
        elif choix == "12":
            afficher_max_emission(activites)
        elif choix == "13":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    print('\n''Bienvenue !')
    programme_principal()
