select  sum(qte*prixvente) as CA, sum(qte) as qte 
from MAGASIN natural join COMMANDE natural join DETAILCOMMANDE 
group by YEAR(datecom), MONTH(datecom);