-- TP 2
-- Nom:  , Prenom: 

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont ne fait pas partie Louane DJARA?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 1.

select nomPan
from PANEL
where nomPan not in (select nomPan from PANEL natural join CONSTITUER natural join SONDE where nomsond = 'DJARA' and prenomsond = 'Louane');

select nomPan
from PANEL
except
select nomPan
from PANEL natural join CONSTITUER natural join SONDE
where nomsond = 'DJARA' and prenomsond = 'Louane';
-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les prénoms de sondé commençant par un A qui n'apparaissent pas dans la tranche d'age 20-29 ans? Classez ces noms par ordre alphabétique.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+
-- | prenomSond |
-- +------------+
-- | Alice      |
-- | Allan      |
-- | Amaury     |
-- | Ambre      |
-- | Anaïs      |
-- | etc...
-- = Reponse question 2.

select prenomsond 
from SONDE natural join CARACTERISTIQUE natural join TRANCHE
where prenomsond like "A%" 
except
select prenomsond 
from SONDE natural join CARACTERISTIQUE natural join TRANCHE
where prenomsond like "A%" and valdebut = 20 and valfin = 29
ORDER BY prenomsond;

-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les panels dont tous les sondés ont moins de 60 ans? Rappel: CURDATE() donne la date du jour et DATEDIFF(d1,d2) donne le nombre de jours entre d1 et d2.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 3.

select nomPan
from PANEL natural join CONSTITUER natural join SONDE 
except
select nomPan
from PANEL natural join CONSTITUER natural join SONDE 
where DATEDIFF(CURDATE(), dateNaisSond)/365 > 60; 

-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les catégories qui comportent des personnes nées en 1979? On rappelle que YEAR(d) donne l'année de la date d sous la forme d'un entier.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------------------------------+
-- | intituleCat                                     |
-- +-------------------------------------------------+
-- | Cadres, professions intellectuelles supérieures |
-- | Professions intermédiaires                      |
-- | Employés                                        |
-- | Ouvriers                                        |
-- | Inactifs ayant déjà travaillé                   |
-- +-------------------------------------------------+
-- = Reponse question 4.

select distinct intituleCat
from CATEGORIE natural join CARACTERISTIQUE natural join SONDE
where YEAR(dateNaisSond) = 1979;

-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les sondés nés en 2001 qui appartiennent aux panels France global 1 et France global 2?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+------------+
-- | nomSond    | prenomSond |
-- +------------+------------+
-- | TRISAULOLU | Elise      |
-- | MAMIAT     | Mathieu    |
-- | NEUSIL     | Theo       |
-- +------------+------------+
-- = Reponse question 5.

select nomsond, prenomsond
from SONDE natural join CONSTITUER natural join PANEL p1
where (nomsond, prenomsond) in (select nomsond, prenomsond from PANEL p2 natural join SONDE natural join CONSTITUER where YEAR(dateNaisSond) = 2001 and p1.nomPan = "France global 1" and p2.nomPan = "France global 2");


-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés nés en 1979 qui ont la même date de naissance?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+------------+----------+------------+
-- | nomSond | prenomSond | nomSond  | prenomSond |
-- +---------+------------+----------+------------+
-- | DASA    | Maxime     | PEKARDAC | Bilal      |
-- +---------+------------+----------+------------+
-- = Reponse question 6.

select distinct s1.nomsond, s1.prenomsond, s1.dateNaisSond, s2.nomsond, s2.prenomsond, s2.dateNaisSond
from SONDE natural join SONDE s1 natural join SONDE s2
where YEAR(dateNaisSond) = 1979 and s1.dateNaisSond = s2.dateNaisSond;

select distinct s1.nomsond, s1.prenomsond, s1.dateNaisSond, s2.nomsond, s2.prenomsond, s2.dateNaisSond
from SONDE s1, SONDE s2 
where YEAR(s1.dateNaisSond) = 1979 and (s1.nomsond, s1.prenomsond) in (select s2.nomsond, s2.prenomsond where s1.dateNaisSond = s2.dateNaisSond);

select nomsond, prenomsond
from SONDE
where YEAR(dateNaisSond) = 1979 and (nomsond, prenomsond) in (select s1.nomsond, s1.prenomsond from SONDE s1, SONDE s2 where s1.dateNaisSond = s2.dateNaisSond);