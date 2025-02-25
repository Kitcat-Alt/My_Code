-- Devoir 127
-- Nom: CHER , Prenom: Naick

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



-- +-----------------------+--
-- * Question 127516 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 6 Origine des clients ayant acheter des livres de R. Goscinny

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------+-----+
-- | ville       | qte |
-- +-------------+-----+
-- | etc...
-- = Reponse question 127516.



-- +-----------------------+--
-- * Question 127527 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 7 Valeur du stock par magasin
 Requête Graphique 8 Statistiques sur l'évolution du chiffre d'affaire total par client 

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+---------+
-- | Magasin                 | total   |
-- +-------------------------+---------+
-- | etc...
-- = Reponse question 127527.



-- +-----------------------+--
-- * Question 127538 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Palmarès

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+---------+---------+---------+
-- | annee | maximum | minimum | moyenne |
-- +-------+---------+---------+---------+
-- | etc...
-- = Reponse question 127538.



-- +-----------------------+--
-- * Question 127572 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête imprimer les commandes en considérant que l'on veut celles de février 2020

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-----------------------+-------+
-- | annee | nomauteur             | total |
-- +-------+-----------------------+-------+
-- | etc...
-- = Reponse question 127572.



