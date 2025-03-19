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
from MAGASIN natural left join COMMANDE natural join DETAILCOMMANDE
where datecom = DATE('2022-09-15')
group by nommag;

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

select nomclass as Theme, sum(qte*prix) as Montant
from CLASSIFICATION natural join THEMES natural join LIVRE natural join COMMANDE natural join DETAILCOMMANDE natural join MAGASIN
where YEAR(datecom) = 2025
group by Theme;

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

select nommag, MONTH(datecom) as mois, sum(qte*prix) as CA 
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


select nomedit, count(idauteur) as nbauteurs
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

select villecli, sum(qte) as nbCli
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

select nommag, sum(qte*prix) as stock
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

with MaxCAParClient as (select idcli, YEAR(datecom) as annee, sum(qte*prix) as CA
from CLIENT natural join COMMANDE natural join DETAILCOMMANDE natural join LIVRE
group by annee, idcli)
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

select YEAR(datecom) as annee, nomauteur, sum(qte)
from COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join ECRIRE natural join AUTEUR
where YEAR(datecom) <> 2025
group by annee;

with MaxVenteAuteur as (select YEAR(datecom) as annee, nomauteur, sum(qte) as total
from COMMANDE natural join DETAILCOMMANDE natural join LIVRE natural join ECRIRE natural join AUTEUR
group by annee)
select annee, nomauteur, max(total)
from MaxVenteAuteur
where annee <> 2025
group by annee;


-- +-----------------------+--
-- * Question 127574 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête imprimer les commandes en considérant que l'on veut celles de février 2020
-- = Reponse question 127574
--
