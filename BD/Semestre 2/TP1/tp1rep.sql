



--Exo2
--a
select datenaissond
from SONDE
where nomsond = 'SITOURIN';

--+--------------+
--| datenaissond |
--+--------------+
--| 1995-12-21   |
--+--------------+

--b
select nompan
from SONDE natural join PANEL natural join CONSTITUER
where nomsond = 'SITOURIN';

--+-----------------+
--| nompan          |
--+-----------------+
--| France global 1 |
--| Moins de 50 ans |
--| France global 2 |
--+-----------------+

--c
select intitulecat
from CATEGORIE natural join CARACTERISTIQUE natural join SONDE
where nomsond = 'SITOURIN';

--+----------------------------------+
--| intitulecat                      |
--+----------------------------------+
--| Inactifs ayant déjà travaillé    |
--+----------------------------------+

--d
select valdebut, valfin
from TRANCHE natural join CARACTERISTIQUE natural join SONDE
where nomsond = 'SITOURIN';

--+----------+--------+
--| valdebut | valfin |
--+----------+--------+
--|       20 |     29 |
--+----------+--------+

--Exo3

--1
select nompan
from SONDE natural join PANEL natural join CONSTITUER
where nomsond = 'BOURIER';

select nompan 
from PANEL natural join CONSTITUER r
where EXISTS (select numsond from SONDE s where s.numsond = r.numsond and nomsond = 'BOURIER');

select nompan 
from PANEL natural join CONSTITUER r
where numsond in (select numsond from SONDE s where s.numsond = r.numsond and nomsond = 'BOURIER');

--2
select nompan
from SONDE natural join PANEL natural join CARACTERISTIQUE natural join TRANCHE
where idtr = 6;


--3
select distinct nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE natural join TRANCHE
where intituleCat = "Ouvriers" and idtr = 6;

select distinct nomsond, prenomsond
from SONDE 
where EXISTS (select intituleCat from CATEGORIE natural join TRANCHE where intituleCat = "Ouvriers" and idtr = 6);
