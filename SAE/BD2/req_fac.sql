select nommag as Magasin, nomcli as Nom, prenomcli as Prenom, adressecli as adresse, codepostal as CodePostal, villecli as Ville, numcom, datecom as date, numlig, isbn, titre, qte, prixvente 
from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join MAGASIN 
where MONTH(datecom) = ? and YEAR(datecom) = ? order by idmag, numcom, numlig