-- TP 1
-- Nom: Foucher , Prenom: Mattéo

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner la liste des panels dont fait partie Caroline BOURIER.




-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- +-----------------+
-- = Reponse question 1.

select nompan
from SONDE natural join PANEL natural join CONSTITUER
where nomsond = 'BOURIER';

select nompan 
from PANEL natural join CONSTITUER r
where EXISTS (select numsond from SONDE s where s.numsond = r.numsond and nomsond = 'BOURIER');

select nompan 
from PANEL natural join CONSTITUER r
where numsond in (select numsond from SONDE s where s.numsond = r.numsond and nomsond = 'BOURIER');


-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont un des sondés est de la tranche d'âge 70 à 120 ans?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | France global 2 |
-- +-----------------+
-- = Reponse question 2.

select nompan
from SONDE natural join PANEL natural join CARACTERISTIQUE natural join TRANCHE
where idtr = 6;


-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés de la tranche d'age 70-120 ans qui sont ouvriers?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | ERYS      | Imane      |
-- | BERRGAIES | Claire     |
-- | JABAT     | Rose       |
-- | WALLOCHE  | Marion     |
-- | LENUJA    | Pauline    |
-- | etc...
-- = Reponse question 3.

select distinct nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE natural join TRANCHE
where intituleCat = "Ouvriers" and idtr = 6;

select distinct nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE natural join TRANCHE
where (nomsond, prenomsond) in (select nomsond, prenomsond from CATEGORIE natural join SONDE natural join CARACTERISTIQUE where intituleCat = "Ouvriers") and idtr = 6;


-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les ouvriers qui portent le prénom Olivier?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | THALOUERD | Olivier    |
-- | POTRININ  | Olivier    |
-- +-----------+------------+
-- = Reponse question 4.

select nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE
where prenomsond = "Olivier" and intituleCat = "Ouvriers";

select nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE
where (nomsond,prenomSond) in (select nomsond, prenomsond from SONDE where prenomsond = "Olivier") and intituleCat = "Ouvriers";

select nomsond, prenomsond
from SONDE s natural join CARACTERISTIQUE natural join CATEGORIE
where EXISTS (select nomsond, prenomsond from SONDE where prenomsond = "Olivier" and s.prenomsond = prenomsond and s.nomsond = nomsond) and intituleCat = "Ouvriers";


-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les tranches d'âge qui comportent une ou plusieurs femmes nées un 25 avril?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+--------+
-- | valDebut | valFin |
-- +----------+--------+
-- | 40       | 49     |
-- +----------+--------+
-- = Reponse question 5.

select distinct valDebut, valFin 
from TRANCHE natural join SONDE natural join CARACTERISTIQUE 
where sexe='F' and month(dateNaisSond) = '04' and day(dateNaisSond) = '25';

select distinct valDebut, valFin 
from TRANCHE natural join SONDE natural join CARACTERISTIQUE 
where (valDebut, valFin) in (select valDebut, valFin from TRANCHE natural join SONDE natural join CARACTERISTIQUE where sexe='F' and month(dateNaisSond) = '04' and day(dateNaisSond) = '25');

select distinct nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE
where nomsond in (select nomsond from TRANCHE natural join CARACTERISTIQUE natural join CATEGORIE natural join SONDE where intituleCat = "Ouvriers" and idtr = 6);

--select distinct nomsond, prenomsond
--from SONDE natural join CARACTERISTIQUE
--where EXISTS (select nomsond from TRANCHE natural join CARACTERISTIQUE natural join CATEGORIE natural join SONDE where intituleCat = "Ouvriers" and idtr = 6);
-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés prénommés Jean qui appartiennent à au moins 2 panels différents? 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+----------+
-- | prenomSond | nomSond  |
-- +------------+----------+
-- | Jean       | DILY     |
-- | Jean       | JATECHU  |
-- | Jean       | PIETIENE |
-- | Jean       | FAL      |
-- | Jean       | BOYEGHE  |
-- +------------+----------+
-- = Reponse question 6.



