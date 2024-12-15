import bilan_carbone as bc

# Ici vos fonctions dédiées aux interactions

#liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Quitter"]
#liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "retour"]

def charger_csv(message):
    """
    Charge un fichier csv et le converti en liste

    Args:
        message (str): le message à afficher

    Returns:
        list: le fichier csv chargé converti en liste
    """
    fichierchargé = False
    liste_fichier = []
    while fichierchargé == False:
        try: 
            liste_fichier = bc.charger_activites(input("Entrez le nom du " + message + " csv que vous voulez charger (n'oubliez pas de mettre le .csv)" + "\n"))
        except:
            print("Fichier introuvable, veuillez réessayer")
        else:
            fichierchargé = True
            print("Fichier chargé")
    return liste_fichier

def sauver_liste(rep, list):
    """Sauvegarde une liste dans un fichier csv si l'utilisateur l'a demandé

    Args:
        rep (str): réponse de l'utilisateur (o ou n) à la question : voulez vous sauvegarder ces données ?
        list (list): La liste à sauvegarder en fichier csv
    """
    repOn = True
    try:
        while repOn:
            if rep == 'o' or rep == "O":
                Nomfichier = input("Donnez un nom à votre fichier (sans oublier le .csv): ")
                print("sauvegarde en cours...")
                bc.sauver_activites(Nomfichier, list)
                print("Liste sauvegardée avec succès (le fichier ce trouve dans le dossier courant)")
                repOn = False
            if rep == 'n' or rep == "N":
                print("")
                repOn = False
    except:
        print("Erreur lors de la sauvegarde !")

def fusion(fichier1, fichier2):
    """fusionne deux fichier csv convertis en listes en une liste

    Args:
        fichier1 (list): Un fichier csv converti en liste d'activité 
        fichier2 (list): Un deuxième fichier csv converti en liste d'activité

    Returns:
        fichier_fusionné(list): La liste fusionnée
    """
    try:
        fichier_fusionné = bc.fusionner_activites(fichier1, fichier2)
        return fichier_fusionné
    except:
        print("Erreur lors de la fusion !")

def sauver_fusion(fichier_fusionné):
    """Sauvegarde La liste fusionné donnée en paramètre dans un fichier csv

    Args:
        fichier_fusionn (list): une liste résultat de la fusion de deux listes
    """
    try:
        Nomfichier = input("Donnez un nom au fichier fusionné (sans oublier le .csv): ")
        print("sauvegarde en cours...")
        bc.sauver_activites(Nomfichier, fichier_fusionné)
        print("Liste sauvegardée avec succès (le fichier ce trouve dans le dossier courant)")
    except:
        print("Erreur lors de la sauvegarde !")
        


def menu(titre, liste_options):
    """Affiche le menu principal de l'application et demande à l'utilisateur de choisir une option dans liste_options

    Args:
        titre (str): le titre de l'application
        liste_options (list): La liste d'options du menu

    Returns:
        str: le numéro de l'option choisie par l'utilisateur
    """
    try:
        affichage_menu_principal(titre, liste_options)
        rep = demander_nombre("Entrez votre choix [1-", len(liste_options))
        return rep
    except:
        return None

def affichage_menu_principal(titre, liste_option):
    """Affiche le menu princiâl de l'application

    Args:
        titre (str): le titre de l'application
        liste_option (list): la liste d'options du menu principal
    """
    try:
        print("+-----------------------------------------+")
        print("|Bienvenu sur l'application " + titre + "|")
        print("+-----------------------------------------+" + "\n")
        print("-----------------------+")
        print("Que voulez vous faire ?|")
        print("-----------------------+")
        choix_options(liste_option)
    except:
        print("Erreur lors de l'affichage du menu principal")

def choix_options(liste_options):
    """Affiche une liste d'options

    Args:
        liste_options (list): Une liste d'options
    """
    try:
        cpt = 1
        for i in range(len(liste_options)):
            print(cpt, " -> ", liste_options[cpt-1])
            cpt+=1
    except:
        print("Erreur lors du choix des options")

def demander_nombre(message, borne_max):
    """demande à l'utilisateur d'entrer un nombre dans le terminal

    Args:
        message (str): le message à afficher dans le terminal
        borne_max (int): le nombre maximum que l'utilisateur peut entrer

    Returns:
        int: le numéro entré par l'utilisateur
    """
    try:
        rep = int(input(message + str(borne_max) + "]" + "\n"))

        if rep <= borne_max:
            return rep
    except:
        return None

def demander_oui_non(message):
    """Demande à l'utilisateur d'entrer oui ou non selon le message affiché

    Args:
        message (str): le message à afficher

    Returns:
        str: la réponse de l'utilisateur
    """
    repexist = True
    while repexist:
        try:
            rep = input((message))
            if rep == "o" or rep == "O":
                repexist = False
                return rep
            elif rep == "n" or rep == "N":
                repexist = False
                return rep
            else:
                print("réponse inconnue, veuillez réessayer")
        except:
            print("réponse inconnue, veuillez réessayer")
    
def rechercher_une_personne(csv_to_list):
    """Demande à l'utilisateur d'entrer un prénom présent dans le fichier csv chargé

    Args:
        csv_to_list (list)): la liste d'activité chargée
    Returns:
        str: le prénom entré par l'utilisateur
    """
    Prenomexist = False
    while Prenomexist == False:
        try:
            Prenom = input("Entrez le prénom de la personne que vous recherchez : ")
            if Prenom in bc.liste_des_personnes(csv_to_list):
                Prenomexist = True
                return Prenom
            elif Prenom == "None" or Prenom == "none":
                Prenomexist = True
                return None
            else: 
                print("je ne connais pas la personne que vous cherchez, veuillez réessayer")
        except:
            print("je ne connais pas la personne que vous cherchez, veuillez réessayer")

def affichage_menu_recherche_personne(Prenom, liste_options):
    """affiche le menu de la recherche d'une personne et ses options

    Args:
        Prenom (str): Le prenom de la personne recherché
        liste_options (list): la liste d'options du menu rechercher une personne
    """
    try:
        print("---------------------------------------+") 
        print("Que voulez vous savoir sur " + Prenom + " ?    |")
        print("---------------------------------------+")
        choix_options(liste_options)
    except:
        print("Erreur lors de l'affichage du menu recherche personne")

def bilan_carbonne_personne(Prenom, Prenom_csv_to_list):
    """Calcule et affiche le bilan carbonne d'une personne

    Args:
        Prenom (str): Le prénom de la personne 
        Prenom_csv_to_list (list): la liste d'activité de la personne
    """
    try:
        print("-------------------------------------")
        print(Prenom + " a émit au total " + str(bc.cumul_emmissions(Prenom_csv_to_list)) + " grammes de Co2" )
        print("-------------------------------------")
    except:
        print("Erreur lors du calcul du bilan carbonne")

def plus_polluante_personne(Prenom, Prenom_csv_to_list):
    """Affiche l'activité la plus polluante d'une personne 

    Args:
        Prenom (str): Le prénom de la personne
        Prenom_csv_to_list (list): la liste d'activité de la personne 
    """
    try:
        act_plus_polluante = bc.max_emmission(Prenom_csv_to_list)
        print("-------------------------------------")
        print("l'acivité la plus polluante de " + Prenom + " a émise " + str(act_plus_polluante[2]) + " grammes de Co2 le " + act_plus_polluante[1] + ", c'était une activité de " + act_plus_polluante[3]) 
        print("-------------------------------------")
    except:
        print("Erreur lors du calcul de l'activité la plus polluante")

def afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom):
    """Affiche les activités pratiqué par une personne

    Args:
        Prenom_csv_to_list (list): la liste d'activités de la personne
        Prenom (str): Le prénom de la personne
    """
    try:
        liste_types = bc.liste_des_types(Prenom_csv_to_list)
        print("------------------------------------------")
        print(Prenom + " pratique les activités de type :" + str(liste_types))
        print("------------------------------------------")
    except:
        print("Erreur lors de l'affichage des activités")


def rechercher_date(csv_to_list):
    """Demande à l'utilisateur d'entrer une date présente dans la liste d'activités chargée

    Args:
        csv_to_list (list): La liste d'activités chargée

    Returns:
        str: la date entrée par l'utilisateur 
    """
    Dateexist = False
    Liste_act_date = []
    while Dateexist == False:
        try:
            date = input("Entrez la date que vous recherchez (format AAAA-MM-JJ) : ")
            if date != "None":
                Liste_act_date = bc.filtre(csv_to_list, 1, date)
            if Liste_act_date != []:
                Dateexist = True
                return date
            elif date == "None" or date == "none":
                Dateexist = True
                return None
            else:
                print("je ne trouve pas la date que vous cherchez, veuillez réessayer")
        except:
            print("je ne trouve pas la date que vous cherchez, veuillez réessayer")

def affichage_liste_personne(csv_to_list):
    """Affiche la liste des personnes présente dans la liste chargée

    Args:
        csv_to_list (list): la liste d'activités chargée

    Returns:
        list: La liste des personnes présente dans la liste d'activités chargée
    """
    try:
        print("Voici la liste des personnes :")
        liste_personne = bc.liste_des_personnes(csv_to_list)
        print(liste_personne)
        return liste_personne
    except:
        print("Erreur lors de l'affichage des personnes")

def moyenne_act_personne(Prenom, Prenom_csv_to_list):
    """Calcule et affiche la moyenne des émissions de CO2 d'une personne

    Args:
        Prenom (str): Le prénom de la personne
        Prenom_csv_to_list (list): la liste d'activité de la personne 
    """
    try:
        print("----------------------------------------")
        print(Prenom + " a émis quotidiennement en moyenne " + str(bc.cumul_emmissions(Prenom_csv_to_list)/len(Prenom_csv_to_list)+1) + " grammes de Co2 en septembre")
        print("----------------------------------------")
    except:
        print("Erreur lors du calcul de la moyenne")

def affichage_menu_date(date, list_opt_date):
    """Affiche le menu de la recherche par date et ses options

    Args:
        date (str): la date recherchée
        list_opt_date (list): la liste d'options du menu
    """
    try:
        print("----------------------------------+")
        print("Que c'est t-il passé le " + date + " ?|")
        print("----------------------------------+")
        choix_options(list_opt_date)
    except:
        print("Erreur lors de l'affichage du menu de la date")

def bilan_caronne_date(date, date_csv_to_list):
    """Calcule et affiche le bilan carbonne d'une date

    Args:
        date (str): une date présente dans la liste d'activités chargée
        date_csv_to_list (list): la liste d'activités de cette date
    """
    try:
        print("\n")
        print("-------------------------------------")
        print(str(bc.cumul_emmissions(date_csv_to_list)) + " grammes de Co2 ont été émis le " + date)
        print("-------------------------------------")
        print("\n")
    except:
        print("Erreur lors du calcul du bilan carbonne")

def liste_des_personne_date(date, date_csv_to_list):
    """Affiche la liste des personnes ayant émise du CO2 à une date donnée

    Args:
        date (str): Une date présente dans la liste d'activités chargée
        date_csv_to_list (list): la liste d'activités de cette date

    Returns:
        list: la liste des personnes ayant émise du CO2 à cette date
    """
    try:
        print("voici la liste des personnes ayant émi du Co2 le " + date)
        print("-----------------------------------------------")
        liste_pers_date = bc.liste_des_personnes(date_csv_to_list)
        print(liste_pers_date)
        print("---------------------------------------")
        return liste_pers_date
    except:
        print("Erreur lors de l'affichage des personnes")

def plus_polluante_date(date, date_csv_to_list):
    """Affiche l'activité la plus polluante d'une date

    Args:
        date (str): une date présente dans la liste d'activités chargée
        date_csv_to_list (list): la liste d'activités de cette date
    """
    try:
        plus_polluante = bc.max_emmission(date_csv_to_list)
        print("---------------------------------")
        print("L'activité la plus polluante le " + date + " a émise " + str(plus_polluante[2]) + " grammes de Co2, c'était une activité de " + str(plus_polluante[3]))
        print("---------------------------------")
    except:
        print("Erreur lors de l'affichage")

def moyenne_act_date(date, date_csv_to_list):
    """Affiche et calcule la moyenne des émissions de CO2 à une date donnée

    Args:
        date (str): une date présente dans la liste d'activités chargée
        date_csv_to_list (list): la liste d'activités de cette date
    """
    try:
        print("----------------------------------------")
        print("Il y a eu en moyenne " + str(bc.cumul_emmissions(date_csv_to_list)/len(date_csv_to_list)) + " grammes de Co2 émis le " + date)
        print("----------------------------------------")
    except:
        print("Erreur lors du calcul de la moyenne")

def duree_moyenne(Prenom, prenom_csv_to_list):
    """Affiche et calcule la durée moyenne qu'une personne à consacré à toute ses activités

    Args:
        Prenom (str): Le prénom de la personne 
        prenom_csv_to_list (list): La liste d'activités de la personne 
    """
    try:
        temp_moyen = bc.cumul_temps_activite(prenom_csv_to_list, bc.co2_minute)/len(prenom_csv_to_list)
        temp_moyen = temp_moyen/60
        print("-----------------------------------")
        print(Prenom + " a consacré en moyenne " + str(temp_moyen) + " heures à ces activités")
        print("-----------------------------------")
    except:
        print("Erreur lors du calcul de la durée moyenne")

def rechercher_type(csv_to_list):
    """demande à l'utilisateur d'entrer le type d'activité qu'il recherche 

    Args:
        csv_to_list (list): La liste d'activités chargée

    Returns:
        str: le type entré par l'utilisateur 
    """
    typeexist = False
    Liste_act_date = []
    while typeexist == False:
        try:
            type = input("Entrez le type que vous recherchez : ")
            if type != "None":
                Liste_act_date = bc.filtre(csv_to_list, 3, type)
            if Liste_act_date != []:
                typeexist = True
                return type
            elif type == "None" or type == "none":
                typeexist = True
                return None
            else:
                print("je ne trouve pas le type que vous cherchez, veuillez réessayer")
        except:
            print("je ne trouve pas le type que vous cherchez, veuillez réessayer")

def affichage_menu_type(type, liste_options_type):
    """Affiche le menu de la recherche par type et ses options

    Args:
        type (str): le type recherché
        liste_options_type (list): la liste des options du menu
    """
    try:
        print("----------------------------------------------------+")
        print("Que voulez vous savoir sur les activités de " + type + " ? |")
        print("----------------------------------------------------+")
        choix_options(liste_options_type)
    except:
        print("Erreur lors de l'affichage du menu type")

def bilan_carbonne_type(type, type_csv_to_list):
    """Affiche et calcule le bilan crabonne d'un type d'activité

    Args:
        type (str): le type d'activité recherchée
        type_csv_to_list (list): La liste des activités de ce type
    """
    try:
        print("-----------------------------")
        print("Les activités de " + type + " on émise au total " + str(bc.cumul_emmissions(type_csv_to_list)) + " grammes de Co2")
        print("-----------------------------")
    except:
        print("Erreur lors du calcul du bilan carbonne")

def plus_polluante_type(type, type_csv_to_list):
    """Affiche l'activité la plus polluante d'un type d'activité

    Args:
        type (str): le type d'activité recherché
        type_csv_to_list (list): La liste des activités de ce type
    """
    try:
        plus_polluante = bc.max_emmission(type_csv_to_list)
        print("-----------------------------")
        print("L'activité la plus polluante de " + type + " a émise " + str(plus_polluante[2]) + " grammes de Co2")
        print("-----------------------------")
    except:
        print("Erreur lors du calcul de l'activité la plus polluante")

def pourcentage_type(type, type_csv_to_list, csv_to_list):
    """Affiche et calcule le pourcentage de personnes pratiquant un type d'activité

    Args:
        type (str): le type d'activité recherché
        type_csv_to_list (list): La liste des activités de ce type
        csv_to_list (list): la liste d'activité chargée
    """
    try:
        pourcentage = (len(type_csv_to_list)/len(csv_to_list))*100
        print("-----------------------------")
        print("Il y a " + str(pourcentage) + " % " + " de personne pratiquant des activités de " + type)
        print("-----------------------------")
    except:
        print("Erreur lors du calcul de pourcentage")

def affichage_liste_personnes_type(type, type_csv_to_list):
    """Affiche la liste des personnes présente dans la liste d'activité par type

    Args:
        type (str): le type d'activité recherché
        type_csv_to_list (list): La liste des activités de ce type
    """
    try:
        print("Voici la liste des personnes pratiquant des activités de " + type)
        print("---------------------------------------")
        print(str(bc.liste_des_personnes(type_csv_to_list)))
        print("---------------------------------------")
    except:
        print("Erreur lors de l'affichage des personnes")

def affichage_dichotomique(Prenom, date, type, csv_to_list):
    """Recherche une activité dans une liste d'activité triée puis l'affiche.

    Args:
        Prenom (str): le prenomr recherché
        date (str): la date recherchée
        type (str): le type recherché
        csv_to_list (list): la liste d'activités chargée
    """
    try:
        activite_precise = bc.recherche_activite_dichotomique(Prenom, date, type, csv_to_list)
        print("-------------------------------")
        print(Prenom + " a émis " + str(activite_precise[2]) + " grammes de Co2 le " + date + " c'était une activité de " + type)
        print("-------------------------------")
    except:
        print("Désolé mais cette activité n'existe pas !")

def affichage_recherche_precise(Liste_options_menu_recherche_precise):
    """Affiche le menu de la recherche précise ainsi que ses options

    Args:
        Liste_options_menu_recherche_precise (list): la liste d'options du menu recherche précise
    """
    try:
        print("---------------------------------------------+")
        print("Que voulez vous savoir sur cette recherche ? |")
        print("---------------------------------------------+")
        choix_options(Liste_options_menu_recherche_precise)
    except:
        print("Erreur lors de l'affichage du menu recherche précise")

def bilan_carbonne_precis(precis_csv_to_list):
    """Calcule et affiche le bilan carbonne d'une recherche précise

    Args:
        precis_csv_to_list (list): la liste d'activités en fonction des critères de la recherche
    """
    try:
        print("--------------------------------")
        print("Ces activités ont émise au total " + str(bc.cumul_emmissions(precis_csv_to_list)) + " grammes de Co2")
        print("--------------------------------")
    except:
        print("Erreur lors du bilan carbonne !")

def plus_polluante_precis(precis_csv_to_list):
    """Affiche l'activité la plus polluante d'une recherche précise 

    Args:
        precis_csv_to_list (list): la liste d'activités en fonction des critères de la recherche
    """
    try:
        act_plus_polluante = bc.max_emmission(precis_csv_to_list)
        print("--------------------------------")
        print("L'activité la plus polluante de cette liste à émise " + str(act_plus_polluante[2]) + " grammes de Co2")
        print("--------------------------------")
    except:
        print("Erreur lors de l'affichage precis !")

def moyenne_emission_precis(precis_csv_to_list):
    """Calcule et affiche la moyenne des émissions d'une recherche précise

    Args:
        precis_csv_to_list (list): la liste d'activités en fonction des critères de la recherche
    """
    try:
        print("--------------------------------")
        print("Ces activités ont emises en moyenne " + str(bc.cumul_emmissions(precis_csv_to_list)/len(precis_csv_to_list)) + " grammes de Co2")
        print("--------------------------------")
    except:
        print("Erreur lors du calcul de la moyenne des émissions !")

def affichage_liste_act_precis(precis_csv_to_list):
    """Affiche la liste d'activités selon les critère de la recherche

    Args:
        precis_csv_to_list (list): la liste d'activités en fonction des critères de la recherche
    """
    try:
        print("Voici la liste des activités selon vos critères :")
        print("-------------------------------------------------------")
        print(precis_csv_to_list)
        print("-------------------------------------------------------")
    except:
        print("Erreur lors de l'affichage de la liste !")

def affichage_menu_autres_informations(options_autres_informations):
    """Affiche le menu des autres informations ainsi que ses options

    Args:
        options_autres_informations (list): la liste d'option du menu
    """
    try:
        print("-------------------------+")
        print("Que voulez vous savoir ? |")
        print("-------------------------+")
        choix_options(options_autres_informations)
    except:
        print("Erreur lors de l'affichage du menu autres nformations")

def plus_longue_emission_decroissante(csv_to_list):
    """Affiche la plus longue période d'émissions décroissantes d'une liste d'activités

    Args:
        csv_to_list (list): Une liste d'activités
    """
    try:
        print("--------------------------------------------------")
        print("Il y a eu au maximum au cours du mois de septembre, " + str(bc.plus_longue_periode_emmissions_decroissantes(csv_to_list)) + " diminutions consécutives des émissions de Co2")
        print("--------------------------------------------------")
    except:
        print("Erreur lors du calcul d'émissions décroiossantes")

def duree_moyenne_act(csv_to_list):
    """Calcule et affiche la durée moyenne d'une activité dans une liste d'activités

    Args:
        csv_to_list (list): une liste d'activités
    """
    try:
        temp_moyen = bc.cumul_temps_activite(csv_to_list, bc.co2_minute)/len(csv_to_list)
        temp_moyen = temp_moyen/60
        print("-------------------------------------")
        print("La duree moyenne d'une activité est de " + str(temp_moyen) + " heures")
        print("-------------------------------------")
    except:
        print("Erreur lors du calcul de la duree moyenne")




# ici votre programme principal

def programme_principal():
    appli_running = True
    liste_options_menu = ["Rechercher Une personne", "Rechercher une date", "Rechercher un type d'activité", "Effectuer une recherche précise", "Autres informations", "Afficher la liste des personnes", "Fusionner deux fichiers", "Charger un autre fichier", "Quitter"]
    liste_options_menu_Personne = ["Son bilan carbonne", "Ses activités", "Son activité la plus polluante", "La moyenne de ses émissions", "Le temps moyen consacré à ses activités", "Chercher une autre personne", "Retour"]
    Liste_options_menu_date = ["Bilan Carbonne de cette date", "Liste des Personnes à cette date", "Activité la plus polluante à cette date", "Moyenne des émissions", "Chercher une autre date", "Retour"]
    Liste_options_menu_type = ["Bilan carbonne de ces activité", "Activité la plus polluante de ce type", "Pourcentage des personnes pratiquant ce type d'activités", "Liste des personnes pratiquant ces activités", "Chercher un autre type", "Retour"]
    Liste_options_menu_recherche_precise = ["Bilan carbonne", "Activité la plus poulluante", "Moyenne des émissions", "Liste des activités", "Retour"]
    Liste_options_menu_autres_informations = ["Plus longue période d'émissions décroissantes", "Durée moyenne d'une activité", "Retour"]
    csv_to_list = charger_csv("fichier")
    fichier1 = None
    fichier2 = None
    while appli_running:
        rep_menu_principal = menu("Bilan carbonne", liste_options_menu)
        try:
            if rep_menu_principal is None:
                print("cette option n'existe pas !")
                    
            elif rep_menu_principal == 1:
                recherche_personne_en_cours = True
                Prenom = rechercher_une_personne(csv_to_list)
                Prenom_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom)
                while recherche_personne_en_cours:
                    affichage_menu_recherche_personne(Prenom, liste_options_menu_Personne)
                    rep_recherhe_personne = demander_nombre("Entrez un nombre [1-", len(liste_options_menu_Personne))
                    try:
                        if rep_recherhe_personne == 1:
                            bilan_carbonne_personne(Prenom, Prenom_csv_to_list)
                    
                        elif rep_recherhe_personne == 2:
                            afficher_activite_totale_prenom(Prenom_csv_to_list, Prenom)
                            rep_sauver_personne = demander_oui_non("Voulez vous sauvegarder la liste des activités de " + Prenom +  " dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_personne, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 3:
                            plus_polluante_personne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 4:
                            moyenne_act_personne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 5:
                            duree_moyenne(Prenom, Prenom_csv_to_list)

                        elif rep_recherhe_personne == 6:
                            Prenom = rechercher_une_personne(csv_to_list)
                            Prenom_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom)
                            
                        elif rep_recherhe_personne == 7:
                            recherche_personne_en_cours = False
                        
                        else:
                            print("cette option n'existe pas")
                    except:
                        print("erreur")
                    input("Appuyer sur Entrée pour continuer")

            elif rep_menu_principal == 2:
                recherche_date_en_cours = True
                date = rechercher_date(csv_to_list)
                date_csv_to_list = bc.filtre(csv_to_list, 1, date)
                while recherche_date_en_cours:
                    affichage_menu_date(date, Liste_options_menu_date)
                    rep_date = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_date))
                    try:
                        if rep_date == 1:
                            bilan_caronne_date(date, date_csv_to_list)
                        
                        elif rep_date == 2:
                            liste_des_personne_date(date, date_csv_to_list)
                            rep_sauver_date = demander_oui_non("Voulez vous sauvegarder ces données dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_date, date_csv_to_list)
                        
                        elif rep_date == 3:
                            plus_polluante_date(date, date_csv_to_list)

                        elif rep_date == 4:
                            moyenne_act_date(date, date_csv_to_list)                            
                    
                        elif rep_date == 5:
                            date = rechercher_date(csv_to_list)
                            date_csv_to_list = bc.filtre(csv_to_list, 1, date)

                        elif rep_date == 6:
                            recherche_date_en_cours = False
                        
                        else:
                            print("cette option n'existe pas")
                    except:
                        print("erreur")
                    input("Appuyer sur Entrée pour continuer")
            
            elif rep_menu_principal == 3:
                recherche_type_en_cours = True
                type = rechercher_type(csv_to_list)
                type_csv_to_list = bc.filtre(csv_to_list, 3, type)
                while recherche_type_en_cours:
                    affichage_menu_type(type, Liste_options_menu_type)
                    rep_type = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_type))
                    try:
                        if rep_type == 1:
                            bilan_carbonne_type(type, type_csv_to_list)

                        elif rep_type == 2:
                            plus_polluante_type(type, type_csv_to_list)
                       
                        elif rep_type == 3:
                            pourcentage_type(type, type_csv_to_list, csv_to_list)

                        elif rep_type == 4:
                            affichage_liste_personnes_type(type, type_csv_to_list)
                            rep_sauver_type = demander_oui_non("Voulez vous sauvegarder la liste des activités de " + type +  " dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_type, type_csv_to_list)
                        
                        elif rep_type == 5:
                            type = rechercher_type(csv_to_list)
                            type_csv_to_list = bc.filtre(csv_to_list, 3, type)

                        elif rep_type == 6:
                            recherche_type_en_cours = False
                        
                        else:
                            print("Cette option n'existe pas !")
                    except:
                        print("Erreur")
                    input("Appuyer sur Entrée pour continuer")


            elif rep_menu_principal == 4:
                recherche_precise_en_cours = True
                print("Veuillez renseigner au minimum 2 critères. (None si vous ne voulez pas renseigner un critère)")
                print("---------------------------------------------------------------------------------------------")
                Prenom_precis = rechercher_une_personne(csv_to_list)
                date_precise = rechercher_date(csv_to_list)
                type_precis = rechercher_type(csv_to_list)

                if Prenom_precis != None and date_precise != None and type_precis != None:
                    affichage_dichotomique(Prenom_precis, date_precise, type_precis, csv_to_list)
                    recherche_precise_en_cours = False
                
                if Prenom_precis == None:
                    precis_csv_to_list = bc.filtre(csv_to_list, 3, type_precis)
                    precis_csv_to_list = bc.filtre(precis_csv_to_list, 1, date_precise)                
                    if precis_csv_to_list == []:
                        print("Aucune des activités ne vérifie les critères données")
                if date_precise == None:
                    precis_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom_precis)
                    precis_csv_to_list = bc.filtre(precis_csv_to_list, 3, type_precis)
                    if precis_csv_to_list == []:
                        print("Aucune des activités ne vérifie les critères données")
                if type_precis == None:
                    precis_csv_to_list = bc.filtre_par_prenom(csv_to_list, Prenom_precis)
                    precis_csv_to_list = bc.filtre(precis_csv_to_list, 1, date_precise)
                    if precis_csv_to_list == []:
                        print("Aucune des activités ne vérifie les critères données")
                
                while recherche_precise_en_cours:
                    affichage_recherche_precise(Liste_options_menu_recherche_precise)
                    rep_precis = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_recherche_precise))
                    try:
                        if rep_precis == 1:
                            bilan_carbonne_precis(precis_csv_to_list)

                        elif rep_precis == 2:
                            plus_polluante_precis(precis_csv_to_list)

                        elif rep_precis == 3:
                            moyenne_emission_precis(precis_csv_to_list)

                        elif rep_precis == 4:
                            affichage_liste_act_precis(precis_csv_to_list)
                            rep_sauver_precis = demander_oui_non("Voulez vous sauvegarder cette liste d'activités dans un fichier ? (O/n)")
                            sauver_liste(rep_sauver_precis, precis_csv_to_list)

                        elif rep_precis == 5:
                            recherche_precise_en_cours = False
                        
                        else:
                            print("Cette option n'existe pas")
                    except:
                        print("Erreur lors de la recherche précise")
                    input("Appuyer sur Entrée pour continuer")


            elif rep_menu_principal == 5:
                autres_information_en_cours = True
                while autres_information_en_cours:
                    affichage_menu_autres_informations(Liste_options_menu_autres_informations)
                    rep_autre_info = demander_nombre("Entrez un nombre [1-", len(Liste_options_menu_autres_informations))
                    try:
                        if rep_autre_info == 1:
                            plus_longue_emission_decroissante(csv_to_list)
                        
                        elif rep_autre_info == 2:
                            duree_moyenne_act(csv_to_list)
                        
                        elif rep_autre_info == 3:
                            autres_information_en_cours = False
                        
                        else:
                            print("Cette option n'existe pas")
                    except:
                        print("Erreur lors de la recherche précise")
                    input("Appuyer sur Entrée pour continuer")
                        

                         
            elif rep_menu_principal == 6:
                affichage_liste_personne(csv_to_list) 

            elif rep_menu_principal == 7:
                fichier1 = charger_csv("premier fichier")
                fichier2 = charger_csv("deuxième fichier")
                sauver_fusion(fusion(fichier1, fichier2))

            elif rep_menu_principal == 8:
                csv_to_list = charger_csv("fichier")
                
            elif rep_menu_principal == 9:
                appli_running = False
            else:
                print("cette option n'existe pas !")
        except:
            print("erreur !")
        input("Appuyer sur Entrée pour continuer")
    print("Au revoir !")
programme_principal()


