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

CA,qte = extraire_requetes(requete,ms)
#print(CA)
#print(qte)
plt.scatter(qte, CA, color='blue', marker='o', alpha=0.7)
plt.show()