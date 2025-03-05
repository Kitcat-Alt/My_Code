-- TP 4bis
-- Nom:  , Prenom: 

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Ecrire une requête qui permet de connaitre le nombre de cours suivis par chaque étudiant en affichant les 0

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+-----------+-----------+----------+
-- | numetu | nometu    | prenometu | nb_cours |
-- +--------+-----------+-----------+----------+
-- | 1      | Martin    | Pierre    | 2        |
-- | 2      | Dubois    | Julie     | 2        |
-- | 3      | Dupont    | Marie     | 4        |
-- | 4      | Valin     | Patrick   | 3        |
-- | 5      | Deschamps | Hector    | 0        |
-- +--------+-----------+-----------+----------+
-- = Reponse question 1.

select numetu, nometu, prenometu, IFNULL(count(numCo),0) as nb_cours
from ETUDIANT natural left join SUIVRE 
group by numetu;

-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner le total des coefficients pour chaque cours en affichant les 0

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------------+----------+
-- | nomco         | coef_tot |
-- +---------------+----------+
-- | Anglais       | 2        |
-- | Espagnol      | 0        |
-- | Informatique  | 3        |
-- | Mathematiques | 4        |
-- +---------------+----------+
-- = Reponse question 2.

select nomco, IFNULL(sum(coefEv),0) as coef_tot
from COURS natural left join EVALUATION
group by nomco;

-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner les étudiants qui ont plus de 10 de moyenne en tenant compte des coefficients.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------+--------+-----------+---------+
-- | numetu | nometu | prenometu | moyenne |
-- +--------+--------+-----------+---------+
-- | 2      | Dubois | Julie     | 13.6667 |
-- | 3      | Dupont | Marie     | 10.4000 |
-- | 4      | Valin  | Patrick   | 10.6667 |
-- +--------+--------+-----------+---------+
-- = Reponse question 3.



-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner le nombre d'évaluations ayant eu lieu en 2025 par matière en comptant les 0 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------------+--------+
-- | nomco         | nb_dev |
-- +---------------+--------+
-- | Anglais       | 1      |
-- | Espagnol      | 0      |
-- | Informatique  | 0      |
-- | Mathematiques | 2      |
-- +---------------+--------+
-- = Reponse question 4.



-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner les évaluations ayant eu lieu en 2024 qui ont des moyennes supérieures à 12.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-----------+---------+
-- | numev | nomev     | moyenne |
-- +-------+-----------+---------+
-- | 103   | Analyse   | 13.2500 |
-- | 106   | Vocabular | 16.0000 |
-- +-------+-----------+---------+
-- = Reponse question 5.



