-- TP 4
-- Nom:  , Prenom: 

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Créer une vue Produit10 qui permet de retrouver la liste des produits valant plus de 10 Euros.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+-----------------+--------+
-- | refProd | nomProd         | puProd |
-- +---------+-----------------+--------+
-- | 38      | Téléphone       | 78.00  |
-- | 58      | Alcool          | 10.30  |
-- | 64      | Linge de maison | 10.30  |
-- | 65      | Lessive liquide | 11.60  |
-- +---------+-----------------+--------+
-- = Reponse question 1.

with Produit10 as (select * from PRODUIT where puProd > 10)
select * from Produit10;

-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Créer une vue DixMars2024 permettant de retrouver la liste des produits facturés le 10 mars 2024.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+-------------------+--------+
-- | refProd | nomProd           | puProd |
-- +---------+-------------------+--------+
-- | 30      | Pâtes en conserve | 1.30   |
-- | 37      | Oeuf              | 2.80   |
-- | 55      | Sirop             | 2.40   |
-- | 82      | Savon             | 0.90   |
-- | 84      | Rasage            | 6.40   |
-- | etc...
-- = Reponse question 2.

with DixMars2024 as (select * from PRODUIT natural join DETAIL natural join FACTURE where dateFac = "2024-03-10")
select refProd, nomProd, puProd from DixMars2024;


-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Créer une vue NbClientsParVille qui indique combien l'entreprise a de clients dans  chaque ville.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------+-------+
-- | ville       | nbCli |
-- +-------------+-------+
-- | Marseille   | 50    |
-- | Metz        | 52    |
-- | Montpellier | 45    |
-- +-------------+-------+
-- = Reponse question 3.

with NbClientsParVille as (select adresseCli as Ville, count(numCli) as nbCli from CLIENT group by Ville)
select Ville, nbCli from NbClientsParVille where Ville like "M%";


-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Créer une vue CAParMois qui calcule le chiffre d'affaire par mois de l'entreprise. Le résultat doit être trié par ordre chronologique.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------+-------+---------+
-- | mois | annee | CA      |
-- +------+-------+---------+
-- | 1    | 2024  | 3500.92 |
-- | 2    | 2024  | 3724.64 |
-- | 3    | 2024  | 2826.72 |
-- | 4    | 2024  | 2749.72 |
-- | 5    | 2024  | 3156.85 |
-- | etc...
-- = Reponse question 4.

with CAParMois as(select MONTH(dateFac) as mois, YEAR(dateFac) as annee, sum(qte*puProd) as CA 
                    from FACTURE natural join DETAIL natural join PRODUIT
                    where YEAR(dateFac) = "2024"
                    group by mois)
select * from CAParMois;

-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait retrouver les produits jamais facturés en utilisant une jointure externe.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------+
-- | nomProd           |
-- +-------------------+
-- | Thé               |
-- | Mayonnaise        |
-- | Pois secs         |
-- | Beurre            |
-- | Steack haché      |
-- | etc...
-- = Reponse question 5.

select distinct nomProd
from PRODUIT natural left join DETAIL
where numFac is Null;


-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque produit dont le nom commence par un M, on voudrait le nombre de factures qui le concerne (on veut aussi les 0).

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+-------+
-- | nomProd    | nbFac |
-- +------------+-------+
-- | Mayonnaise | 0     |
-- | Miel       | 85    |
-- | Moutarde   | 182   |
-- +------------+-------+
-- = Reponse question 6.

select nomProd, IFNULL(count(numFac),0) as nbFac
from PRODUIT natural left join DETAIL
where nomProd like "M%"
group by nomProd;



-- +------------------+--
-- * Question 7 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque produit dont le nom commence par un M, on voudrait la quantité totale facturée (on veut aussi les 0).

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+-----------+
-- | nomProd    | qteTotale |
-- +------------+-----------+
-- | Mayonnaise | 0         |
-- | Miel       | 500       |
-- | Moutarde   | 993       |
-- +------------+-----------+
-- = Reponse question 7.

select nomProd, IFNULL(sum(qte), 0) as qteTotale
from PRODUIT natural left join DETAIL
where nomProd like "M%"
group by nomProd;
-- +------------------+--
-- * Question 8 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait le montant total des factures par année et par client en comptant les 0.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+--------+-----------+-------+--------+
-- | numCli | nomCli | prenomCli | annee | CA     |
-- +--------+--------+-----------+-------+--------+
-- | 848    | ZET    | Mathieu   | 2021  | 29.25  |
-- | 848    | ZET    | Mathieu   | 2022  | 159.40 |
-- | 848    | ZET    | Mathieu   | 2023  | 6.90   |
-- | 848    | ZET    | Mathieu   | 2024  | 0.00   |
-- +--------+--------+-----------+-------+--------+
-- = Reponse question 8.

with Annee as (select nomCli, prenomCli, distinct YEAR(dateFac) as annee from FACTURE natural join CLIENT
group by nomCli, prenomCli)
select * from Annee;



--select numCli, nomCli, prenomCli, YEAR(dateFac) as annee, IFNULL(sum(qte*puProd), 0) as CA
--from PRODUIT 

-- +------------------+--
-- * Question 9 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait obtenir le chiffre d'affaire par an de chaque produit.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+-----------+-------+----------+
-- | refProd | nomProd   | annee | CA       |
-- +---------+-----------+-------+----------+
-- | 6       | Thé       | 2021  | 0.00     |
-- | 38      | Téléphone | 2021  | 9594.00  |
-- | 77      | Torchons  | 2021  | 404.80   |
-- | 6       | Thé       | 2022  | 0.00     |
-- | 38      | Téléphone | 2023  | 8658.00  |
-- | etc...
-- = Reponse question 9.



