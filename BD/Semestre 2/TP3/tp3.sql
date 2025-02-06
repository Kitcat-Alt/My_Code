-- TP 3
-- Nom: Foucher  , Prenom: Mattéo

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Combien y a-t-il de personnes dans la table SONDE?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+
-- | nbSondes |
-- +----------+
-- | 1348     |
-- +----------+
-- = Reponse question 1.
select count(*) as nbSondes
from SONDE;


-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Combien y a-t-il de personnes qui s'appellent Jean?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+
-- | nbJean |
-- +--------+
-- | 9      |
-- +--------+
-- = Reponse question 2.
select count(*) as nbJean
from SONDE
where prenomSond = "Jean";



-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Combien de prénoms différents y a-t-il dans la base de données?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+
-- | nbPrenom |
-- +----------+
-- | 181      |
-- +----------+
-- = Reponse question 3.
select count(distinct prenomSond) nbPrenom
from SONDE;


-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quel est l'âge de la plus jeune femme du panel France global 2? Pour faire ce calcul on aura besoin de la date du jour retournée  par la fonction CURDATE() et de faire une différence entre deux dates grâce à la fonction DATEDIFF(date1,date2) qui retourne le nombre de jours qui sépare date1 et date2.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+
-- | minAge |
-- +--------+
-- | 21     |
-- +--------+
-- = Reponse question 4.
select round(min(DATEDIFF(CURDATE(), datenaissond)/365)) as minAge
from SONDE natural join CARACTERISTIQUE natural join PANEL
where sexe = 'F' and nomPan = "France global 2";


-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quel est l'age moyen du panel  Moins de 50 ans?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+
-- | ageMoyen |
-- +----------+
-- | 37       |
-- +----------+
-- = Reponse question 5.

select round(avg(DATEDIFF(CURDATE(), datenaissond)/365)) as ageMoyen
from PANEL natural join SONDE natural join CONSTITUER
where nomPan = "Moins de 50 ans";


-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner le nom du sondé le plus jeune de la base de données.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+------------+
-- | nomSond | prenomSond |
-- +---------+------------+
-- | PENCHE  | Elise      |
-- +---------+------------+
-- = Reponse question 6.

select nomSond, prenomSond
from SONDE
where datenaissond >=ALL(select datenaissond from SONDE);

-- +------------------+--
-- * Question 7 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait le nombre de sondés dans chaque panel.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+--------+
-- | nomPan          | nbSond |
-- +-----------------+--------+
-- | France global 1 | 800    |
-- | France global 2 | 800    |
-- | Moins de 50 ans | 665    |
-- +-----------------+--------+
-- = Reponse question 7.

select nomPan, count(numSond) as nbSond
from PANEL natural join CONSTITUER natural join SONDE
group by nomPan;

-- +------------------+--
-- * Question 8 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On voudrait l'âge moyen arroundi des sondés dans chaque catégorie.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------------------------------+--------+
-- | intituleCat                                     | ageMoy |
-- +-------------------------------------------------+--------+
-- | Agriculteurs exploitants                        | 41     |
-- | Artisans, commerçants, chefs d'entreprise       | 43     |
-- | Autres sans activité professionnelle            | 63     |
-- | Cadres, professions intellectuelles supérieures | 43     |
-- | Employés                                        | 47     |
-- | etc...
-- = Reponse question 8.

select intituleCat, round(avg(DATEDIFF(CURDATE(), datenaissond)/365)) as ageMoy
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE
group by intituleCat;


-- +------------------+--
-- * Question 9 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  On veut la même chose mais pour chaque panel.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+-------------------------------------------------+--------+
-- | nomPan          | intituleCat                                     | ageMoy |
-- +-----------------+-------------------------------------------------+--------+
-- | France global 1 | Agriculteurs exploitants                        | 42     |
-- | France global 1 | Artisans, commerçants, chefs d'entreprise       | 45     |
-- | France global 1 | Autres sans activité professionnelle            | 62     |
-- | France global 1 | Cadres, professions intellectuelles supérieures | 43     |
-- | France global 1 | Employés                                        | 46     |
-- | etc...
-- = Reponse question 9.

select nomPan, intituleCat, round(avg(DATEDIFF(CURDATE(), datenaissond)/365)) as ageMoy
from PANEL natural join CONSTITUER natural join SONDE natural join CARACTERISTIQUE natural join CATEGORIE
group by nomPan, intituleCat;

-- +-------------------+--
-- * Question 10 :     --
-- +-------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque catégorie, on veut le nombre de femmes.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------------------------------+-----+
-- | intituleCat                                     | nbF |
-- +-------------------------------------------------+-----+
-- | Agriculteurs exploitants                        | 6   |
-- | Artisans, commerçants, chefs d'entreprise       | 23  |
-- | Autres sans activité professionnelle            | 96  |
-- | Cadres, professions intellectuelles supérieures | 60  |
-- | Employés                                        | 108 |
-- | etc...
-- = Reponse question 10.

select intituleCat, count(sexe)
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE
where sexe = 'F'
group by intituleCat;

-- +-------------------+--
-- * Question 11 :     --
-- +-------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Donner la liste des prénoms portés par plus de 20 sondés.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+--------+
-- | prenomSond | nbPers |
-- +------------+--------+
-- | Camille    | 22     |
-- | Claire     | 24     |
-- | Lucie      | 20     |
-- | Mathieu    | 20     |
-- | Mathilde   | 25     |
-- | etc...
-- = Reponse question 11.

select prenomSond, count(*) as nbPers
from SONDE
group by prenomSond
having count(*) > 20;


-- +-------------------+--
-- * Question 12 :     --
-- +-------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour le panel France Global 1 on veut le nombre de personnes nées en 2001 pour chaque catégorie.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------------------------------+--------+
-- | intituleCat                                     | nbPers |
-- +-------------------------------------------------+--------+
-- | Cadres, professions intellectuelles supérieures | 2      |
-- | Employés                                        | 3      |
-- | Inactifs ayant déjà travaillé                   | 1      |
-- | Ouvriers                                        | 3      |
-- | Professions intermédiaires                      | 3      |
-- +-------------------------------------------------+--------+
-- = Reponse question 12.

select intituleCat, count(*) as nbPers
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE natural join CONSTITUER natural join PANEL
where YEAR(datenaissond) = 2001 and nomPan = "France Global 1"
group by intituleCat;

