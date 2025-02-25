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

    def execute(self, requete, liste_parametres):
        for param in liste_parametres:
            if type(param)==str:
                requete=requete.replace('?',"'"+param+"'",1)
            else:
                requete=requete.replace('?',str(param),1)
        return self.cnx.execute(requete)

def faire_factures(requete:str, mois:int, annee:int, bd:MySQL):
    # exécute la requête en remplaçant le premier ? par le numéro du mois 
    # et le deuxième ? par l'année
    curseur=bd.execute(requete,(mois,annee))
    # Initialisations du traitement
    res='pas encore implémentée'
    for ligne in curseur:
        # parcours du résultat de la requête. 
        # ligne peut être vu comme un dictionnaire dont les clés sont les noms des colonnes de votre requête
        # est les valeurs sont les valeurs de ces colonnes pour la ligne courante
        # par exemple ligne['numcom'] va donner le numéro de la commande de la ligne courante 
        ...

    #ici fin du traitement
    # fermeture de la requête
    curseur.close()
    return res
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--serveur",dest="nomServeur", help="Nom ou adresse du serveur de base de données", type=str, default="127.0.0.1")
    parser.add_argument("--bd",dest="nomBaseDeDonnees", help="Nom de la base de données", type=str,default='Librairie')
    parser.add_argument("--login",dest="nomLogin", help="Nom de login sur le serveur de base de donnée", type=str, default='limet')
    parser.add_argument("--requete", dest="fichierRequete", help="Fichier contenant la requete des commandes", type=str)    
    args = parser.parse_args()
    passwd = getpass.getpass("mot de passe SQL:")
    try:
        ms = MySQL(args.nomLogin, passwd, args.nomServeur, args.nomBaseDeDonnees)
    except Exception as e:
        print("La connection a échoué avec l'erreur suivante:", e)
        exit(0)
    rep=input("Entrez le mois et l'année sous la forme mm/aaaa ")
    mm,aaaa=rep.split('/')
    mois=int(mm)
    annee=int(aaaa)
    with open(args.fichierRequete) as fic_req:
        requete=fic_req.read()
    print(faire_factures(requete,mois,annee,ms))