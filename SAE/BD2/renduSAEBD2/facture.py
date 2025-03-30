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
        requete = sqlalchemy.text(requete)
        return self.cnx.execute(requete)

def faire_factures(requete:str, mois:int, annee:int, bd:MySQL):
    curseur=bd.execute(requete,(mois,annee))
    magasins = ["La librairie parisienne", "Cap au Sud", "Ty Li-Breizh-rie", "L'européenne", "Le Ch'ti livre", "Rhône à lire", "Loire et livres"]
    client_prec = ()
    magasin_prec = None
    totalCommande = 0
    totalQteMagasin = 0
    totalPrixGlobal = 0
    totalQteGlobal = 0
    nbFactureMag = 0
    premierTour = True
    writeMag = True
    print(f'Factures du {mois}/{annee}')

    for ligne in curseur:
        if magasin_prec == ligne[0]:
            writeMag = False
            
        if writeMag == False and client_prec != ({ligne[1]},{ligne[2]}):
            totalPrixGlobal += totalCommande
            print(f'                                                                                     --------')
            print(f'                                                                               Total    {totalCommande}')
            totalCommande = 0
            nbFactureMag += 1

        if magasin_prec != ligne[0] and premierTour == False:
            print("---------------------------------------------------------------------------------------------")
            print(f'{nbFactureMag} factures éditées')
            print(f'{totalQteMagasin} livres vendus')
            print('*********************************************************************************************' + "\n")
            totalQteGlobal += totalQteMagasin
            nbFactureMag = 0

        if ligne[0] in magasins:
            if premierTour == True:
                print(f'Edition des factures du magasin {ligne[0]}')
                magasins.remove(ligne[0])
            else:
                print(f'Edition des factures du magasin {ligne[0]}')
                magasins.remove(ligne[0])
                totalQteMagasin = 0
                writeMag = True
                    
        if client_prec != ({ligne[1]},{ligne[2]}) or client_prec == ():
            print("---------------------------------------------------------------------------------------------")
            print(f'{ligne[1]} {ligne[2]}')
            print(f'{ligne[3]}')
            print(f'{ligne[4]} {ligne[5]}')
            print(f'                                        commande n°{ligne[6]} du {ligne[7]}')
            print(f'                    ISBN                           Titre                     qte  prix  total')
            print(f'              {ligne[8]} {ligne[9]} {ligne[10]}', end = ' ')
            print(f'{ligne[11]}  {ligne[12]} {ligne[11]*ligne[12]}')
            totalQteMagasin += ligne[11]
            totalCommande += ligne[11]*ligne[12]
            
        else:
            print(f'              {ligne[8]} {ligne[9]} {ligne[10]}', end= ' ')
            print(f'{ligne[11]} {ligne[12]} {ligne[11]*ligne[12]}')
            totalCommande += ligne[11]*ligne[12]
            totalQteMagasin += ligne[11]
        premierTour = False
        client_prec = ({ligne[1]},{ligne[2]})
        magasin_prec = ligne[0]

    totalPrixGlobal += totalCommande
    print(f'                                                                                     --------')
    print(f'                                                                               Total    {totalCommande}')
    totalCommande = 0
    nbFactureMag += 1
    print("---------------------------------------------------------------------------------------------")
    print(f'{nbFactureMag} factures éditées')
    print(f'{totalQteMagasin} livres vendus')
    print('*********************************************************************************************')
    totalQteGlobal += totalQteMagasin
    print(f"Chiffre d'affaire global: {totalPrixGlobal}")
    print(f'Nombre de livres vendus: {totalQteGlobal}')
    curseur.close()
        


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
    faire_factures(requete,mois,annee,ms)