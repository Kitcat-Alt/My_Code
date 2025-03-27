-- Devoir 127
-- Nom: , Prenom: 

-- Feuille SAE2.05 Exploitation d'une base de données: Livre Express
-- 
-- Veillez à bien répondre aux emplacements indiqués.
-- Seule la première requête est prise en compte.

-- +-----------------------+--
-- * Question 127156 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les livres qui ont été commandés le 1er décembre 2024 ?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------------+--------------------------------------------+---------+-----------+-------+
-- | isbn          | titre                                      | nbpages | datepubli | prix  |
-- +---------------+--------------------------------------------+---------+-----------+-------+
-- | etc...
-- = Reponse question 127156.

select distinct isbn, titre, nbpages, datepubli, prix
from LIVRE natural join POSSEDER natural join MAGASIN natural join COMMANDE
where datecom = DATE('2024-12-1');

select  isbn, titre, nbpages, datepubli, prix
from LIVRE natural join COMMANDE natural join DETAILCOMMANDE
WHERE DAY(datecom) = 1 and month(datecom) =12 and year(datecom) = 2024;
--requete gwen

-- +-----------------------+--
-- * Question 127202 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels clients ont commandé des livres de René Goscinny en 2021 ?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+---------+-----------+-----------------------------+------------+-------------+
-- | idcli | nomcli  | prenomcli | adressecli                  | codepostal | villecli    |
-- +-------+---------+-----------+-----------------------------+------------+-------------+
-- | etc...
-- = Reponse question 127202.

select distinct idcli, nomcli, prenomcli, adressecli, codepostal, villecli
from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join AUTEUR
where nomauteur = "René Goscinny" and  YEAR(datecom) = 2021;

select distinct idcli, nomcli, prenomcli, adressecli, codepostal, villecli
from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join AUTEUR natural join ECRIRE
where nomauteur='René Goscinny' and year(datecom) = 2021
order by idcli;
--requete gwen

-- +-----------------------+--
-- * Question 127235 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les livres sans auteur et étant en stock dans au moins un magasin en quantité strictement supérieure à 8 ?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------------+-----------------------------------+-------------------------+-----+
-- | isbn          | titre                             | nommag                  | qte |
-- +---------------+-----------------------------------+-------------------------+-----+
-- | etc...
-- = Reponse question 127235.



-- +-----------------------+--
-- * Question 127279 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque magasin, on veut le nombre de clients qui habitent dans la ville de ce magasin (en affichant les 0)

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-------------------------+-------+
-- | idmag | nommag                  | nbcli |
-- +-------+-------------------------+-------+
-- | etc...
-- = Reponse question 127279.

select idmag, nommag, IFNULL(count(distinct idcli),0) as nbCli
from CLIENT right join MAGASIN on villecli = villemag
group by idmag, nommag; 

select idmag, nommag, IFNULL(count(distinct idcli),0) as nbCli
from CLIENT natural left join COMMANDE natural join MAGASIN
where villecli = villemag
group by idmag, nommag;

-- +-----------------------+--
-- * Question 127291 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque magasin, on veut la quantité de livres achetés le 15/09/2022 en affichant les 0.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+------+
-- | nommag                  | nbex |
-- +-------------------------+------+
-- | etc...
-- = Reponse question 127291.

select nommag, IFNULL(sum(qte), 0) as nbex
from MAGASIN m left join COMMANDE c on m.idmag = c.idmag and datecom = DATE('2022-09-15') natural left join DETAILCOMMANDE 
group by nommag;

-- +-----------------------+--
-- * Question 127314 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Instructions d'insertion dans la base de données

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+
-- | insertions |
-- +------------+
-- | etc...
-- = Reponse question 127314.

insert into LIVRE(isbn, titre, nbpages, datepubli, prix) values
    ('9782844273765', 'SQL pour les nuls', 292, 2002, 33.5);

insert into ECRIRE(isbn, idauteur) values
    ('9782844273765', 'OL246259A'),
    ('9782844273765', 'OL7670824A');

insert into AUTEUR(idauteur, nomauteur,anneenais,anneedeces) values
    ('OL246259A', 'Allen G. Taylor', NULL, NULL),
    ('OL7670824A', 'Reinhard Engel', NULL, NULL);

insert into EDITEUR(nomedit, idedit) values
    ('First Interactive', 240);

insert into EDITER(isbn, idedit) values
    ('9782844273765', 240);

insert into POSSEDER(idmag, isbn, qte) values
    (7, '9782844273765', 3);

-- +-----------------------+--
-- * Question 127369 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 1 Nombre de livres vendus par magasin et par an

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+-------+-----+
-- | Magasin                 | Année | qte |
-- +-------------------------+-------+-----+
-- | etc...
-- = Reponse question 127369.

select distinct nommag as Magasin, YEAR(datecom) as annee, sum(qte) as qte
from MAGASIN natural join COMMANDE natural join DETAILCOMMANDE
group by Magasin, annee
order by annee;

-- +-----------------------+--
-- * Question 127370 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 2  Chiffre d'affaire par thème en 2024

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------------+---------+
-- | Theme                                | Montant |
-- +--------------------------------------+---------+
-- | etc...
-- = Reponse question 127370.
with CA2024 as (
    select sum(qte*prixvente) Total
    from DETAILCOMMANDE natural join COMMANDE 
    where YEAR(datecom)=2025
)

select nomclass Theme, ROUND((sum(qte*prixvente)/Total)*100) total
from CA2024 natural join DETAILCOMMANDE natural join COMMANDE natural join LIVRE natural join THEMES natural join CLASSIFICATION
where YEAR(datecom) = 202------× 5
group by LEFT(LPAD(iddewey,3,'0'),1)
order by nomclass; 
--requete gwen

-- +-----------------------+--
-- * Question 127381 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 3 Evolution chiffre d'affaire par magasin et par mois en 2024

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------+-------------------------+---------+
-- | mois | Magasin                 | CA      |
-- +------+-------------------------+---------+
-- | etc...
-- = Reponse question 127381.

select MONTH(datecom) as mois, nommag as Magasin, sum(qte*prix) as CA 
from MAGASIN natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE 
where YEAR(datecom) = 2024 
group by nommag, MONTH(datecom);

-- +-----------------------+--
-- * Question 127437 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 4 Comparaison ventes en ligne et ventes en magasin

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+------------+---------+
-- | annee | typevente  | montant |
-- +-------+------------+---------+
-- | etc...
-- = Reponse question 127437.

select YEAR(datecom) as annee, enligne as typevente, sum(qte*prix) as montant
from COMMANDE natural join DETAILCOMMANDE natural join LIVRE
where YEAR(datecom)<>2025
group by annee, typevente;

-- +-----------------------+--
-- * Question 127471 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 5 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------+-----------+
-- | Editeur           | nbauteurs |
-- +-------------------+-----------+
-- | etc...
-- = Reponse question 127471.


select nomedit as Editeur, count(idauteur) as nbauteurs
from EDITEUR natural join EDITER natural join LIVRE natural join ECRIRE natural join AUTEUR
group by nomedit
order by nbauteurs desc
limit 10;

-- +-----------------------+--
-- * Question 127516 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 6 Qté de livres de R. Goscinny achetés en fonction de l'orgine des clients

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------+-----+
-- | ville       | qte |
-- +-------------+-----+
-- | etc...
-- = Reponse question 127516.

select villecli as ville, sum(qte) as qte
from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join ECRIRE natural join AUTEUR
where nomauteur = 'René Goscinny'
group by villecli;

-- +-----------------------+--
-- * Question 127527 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 7 Valeur du stock par magasin
-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+---------+
-- | Magasin                 | total   |
-- +-------------------------+---------+
-- | etc...
-- = Reponse question 127527.

select nommag as Magasin, sum(qte*prix) as total
from MAGASIN natural join POSSEDER natural join LIVRE
group by nommag;

-- +-----------------------+--
-- * Question 127538 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
-- Requête Graphique 8 Statistiques sur l'évolution du chiffre d'affaire total par client 
-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+---------+---------+---------+
-- | annee | maximum | minimum | moyenne |
-- +-------+---------+---------+---------+
-- | etc...
-- = Reponse question 127538.

with MaxCAParClient as (select idcli, YEAR(datecom) as annee, sum(qte*prixvente) as CA
    from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE
    group by YEAR(datecom), idcli)
select annee, max(CA) as maximum, min(CA) as minimum, avg(CA) as moyenne
from MaxCAParClient 
group by annee;

-- +-----------------------+--
-- * Question 127572 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Palmarès

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-----------------------+-------+
-- | annee | nomauteur             | total |
-- +-------+-----------------------+-------+
-- | etc...
-- = Reponse question 127572.
with QteAuteurAnnee as (select YEAR(datecom) as annee, idauteur, nomauteur, sum(qte) as total
                        from COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join ECRIRE natural join AUTEUR 
                        where YEAR(datecom) <> 2025
                        group by annee, idauteur, nomauteur
                        order by annee)
select annee, nomauteur, total
from QteAuteurAnnee
where total >= ALL(select total from QteAuteurAnnee q2 where q2.annee = QteAuteurAnnee.annee)
group by annee;
-- +-----------------------+--
-- * Question 127574 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête imprimer les commandes en considérant que l'on veut celles de février 2020
-- = Reponse question 127574
--
select nommag as Magasin, nomcli as Nom, prenomcli as Prenom, adressecli as adresse, codepostal as CodePostal, villecli as Ville, numcom, datecom as date, numlig, isbn, titre, qte, prixvente from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join MAGASIN where MONTH(datecom) = 2 and YEAR(datecom) = 2020 order by idmag, nomcli, prenomcli;




select sum(qte*prixvente) as CA, sum(qte) as qte
from MAGASIN natural join COMMANDE natural join DETAILCOMMANDE
group by YEAR(datecom), MONTH(datecom);
