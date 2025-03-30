import numpy as np
import matplotlib.pyplot as plt

import sqlalchemy
import argparse
import getpass

class MySQL(object):
    def __init__(self, user, passwd, host, database,timeout=20):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.database = database
        #try:
        self.engine = sqlalchemy.create_engine(
                'mysql+mysqlconnector://' + self.user + ':' + self.passwd + '@' + self.host + '/' + self.database,
                )
        self.cnx = self.engine.connect()
        print("connexion réussie")

    def close(self):
        self.cnx.close()

    def execute(self, requete):
        #for param in liste_parametres:
        #    if type(param)==str:
        #        requete=requete.replace('?',"'"+param+"'",1)
        #    else:
        #        requete=requete.replace('?',str(param),1)
        requete = sqlalchemy.text(requete)
        return self.cnx.execute(requete)

def extraire_requetes(requete:str, bd:MySQL):
    CA = []
    qte = []
    curseur=bd.execute(requete)
    # Initialisations du traitement
    for ligne in curseur:
        # parcours du résultat de la requête. 
        CA.append(ligne[0])
        qte.append(ligne[1])
    #ici fin du traitement
    # fermeture de la requête
    curseur.close()
    return (CA,qte)
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--serveur",dest="nomServeur", help="Nom ou adresse du serveur de base de données", type=str, default="127.0.0.1")
    parser.add_argument("--bd",dest="nomBaseDeDonnees", help="Nom de la base de données", type=str,default='Librairie')
    parser.add_argument("--login",dest="nomLogin", help="Nom de login sur le serveur de base de donnée", type=str, default='limet')
    parser.add_argument("--requete", dest="fichierRequete", help="Fichier contenant la requete des commandes", type=str)    
    args = parser.parse_args()
    #passwd = getpass.getpass("mot de passe SQL:")
    passwd = "Maria_K|DB_2109"
    try:
        ms = MySQL(args.nomLogin, passwd, args.nomServeur, args.nomBaseDeDonnees)
    except Exception as e:
        print("La connection a échoué avec l'erreur suivante:", e)
        exit(0)
    with open(args.fichierRequete) as fic_req:
        requete=fic_req.read()

#extraction des données de la requetes dans des listes
CA,qte = extraire_requetes(requete,ms)

#calcul des moyenne du CA et du nombre de livres vendus
moyCa = sum(CA)/len(CA)
moyQte = sum(qte)/len(qte)


def regression_lineaire(qte, CA):
    """_summary_
        calcule les coefficient a et b de l'equetion de la droite de régression
    Args:
        qte (List): la liste de nombre de livres vendu par mois
        CA (List): la liste des chiffres d'affaire réalisés
    """
    # Etape 1 : Calcul des moyennes
    mean_qte = sum(qte) / len(qte)
    mean_CA = sum(CA) / len(CA)

    # Etape 2 : Calcul de la difference qte - moyenne
    qte_diff = [qte - mean_qte for qte in qte]
    CA_diff = [ca - mean_CA for ca in CA]

    # Etape 3 : Calcul du numerateur (somme des produits des ecarts quadratiques)
    moyCa
    return(a,b)

def coefficient_correlation(moyCa, moyQte):
    """_summary_
        Calcule le coefficient de corrélation
    Args:
        moyCa (float): la moyenne des chiffre d'affaire
        moyQte (float): la moyenne des livres vendus par mois
    """
    # Etape 2 : Calcul de la difference X - moyenne
    X_diff = [x - moyCa for x in CA]
    Y_diff = [y - moyQte for y in qte]

    # Etape 3 : Calcul du numerateur (somme des produits des ecarts quadratiques)
    num = sum(xd * yd for xd, yd in zip(X_diff, Y_diff))

    # Etape 4 : Calcul du denominateur (les variances de X et Y)
    denom_X = sum(xd ** 2 for xd in X_diff)
    #print(denom_X)
    denom_Y = sum(yd ** 2 for yd in Y_diff)
    #print(denom_Y)

    # Etape 5 : Calcul du coefficient de correlation
    correlation = num / (np.sqrt(denom_X) * np.sqrt(denom_Y))
    print("Coefficient de correlation de Pearson :", correlation)


print(f' moyenne CA : {moyCa}')
print(f' moyenne qte : {moyQte}')
coefficient_correlation(moyCa,moyQte)

#coeficients a et b de la droite de régression
Qte,Ca = regression_lineaire(qte,CA)


x_vals1 = np.linspace(min(qte), max(qte))
y_vals1 = Qte * x_vals1 + Ca

plt.xlabel("Nombre de vente de livre")
plt.ylabel("Chiffre d'affaire")
plt.title("Evolution CA en fontion du nombre de ventes")
plt.scatter(qte, CA, color='blue', marker='o', alpha=0.7)
plt.plot(x_vals1, y_vals1, color='red')
plt.show()



