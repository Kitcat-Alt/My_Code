drop table RESERVATIONS;
drop table CLIENTS;
drop table VOYAGES;

create table CLIENTS 
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table VOYAGES
(Code Varchar2(6) primary key,
VilleDepart VarChar2(30),
VilleArrivee VarChar2(30),
Depart Date,
Retour Date,
Prix Number(8,2));


create table RESERVATIONS (
Id Number(4) , 
Code Varchar2(6),
DateReserv Date,
foreign key (Id) references CLIENTS(Id) on delete cascade,
foreign key (Code) references VOYAGES (Code) on delete cascade);

--CLIENTS [Id, Nom, Prenom, Ville]
--VOYAGES [Code, VilleDepart, VilleArrivee, Depart, Retour, Prix]
--RESERVATIONS [Id, Code, DateReserv]

--1. Trouver les clients n’ayant r´eserv´e aucun voyage.
select Nom, Prenom
from CLIENTS
where Id not in (select Id from RESERVATIONS);
--2. Trouver les voyages n’ayant ´et´e r´eserv´es par aucun client.
select Code, VilleDepart
from VOYAGES
where Code not in (select Code from RESERVATIONS);
--3. Trouver les noms des clients ayant r´eserv´e seulement un voyage (une seule r´eservation).
select Nom, Prenom
from CLIENTS natural join RESERVATIONS
where Id not in (
    select R1.Id
    from RESERVATIONS R1, RESERVATIONS R2
    where R1.Id = R2.Id and R1.code != R2.code
    );
--4. Codes des voyages les plus chers.
select Code
from VOYAGES
where Prix >= ALL(select prix from VOYAGES);
--5. Codes des voyages les moins chers.
select Code
from VOYAGES
where Prix <= ALL(select prix from VOYAGES);
--6. Code, trajet et prix des voyages pour lesquels il existe au moins un autre voyage pour
--le mˆeme parcours, c’est-`a-dire, ayant les mˆemes villes d’arriv´ee et de d´epart.
select R1.Code, R1.VilleDepart, R1.VilleArrivee, R1.prix
from VOYAGES R1, VOYAGES R2
where R1.VilleDepart = R2.VilleDepart and R1.VilleArrivee = R2.VilleArrivee and R1.Code != R2.Code;
--7. Code, trajet et prix des voyages pour lesquels il existe une unique option. Autrement
--dit, les voyages pour lesquels il n’existe pas un autre voyage pour le mˆeme parcours,
--c’est-`a-dire, ayant les mˆemes villes d’arriv´ee et de d´epart.
select Code, VilleDepart, VilleArrivee, prix
from VOYAGES
where Code not in(
    select R1.Code
    from VOYAGES R1, VOYAGES R2
    where R1.VilleDepart = R2.VilleDepart and R1.VilleArrivee = R2.VilleArrivee and R1.Code != R2.Code
    );

--8. ? Trouver les clients qui ont r´eserv´e tous les voyages `a Amsterdam. Autrement dit :
--trouvez les clients (id) pour lesquels il n’existe pas un voyage `a Amsterdam qu’ils
--n’ont pas r´eserv´e.
select Nom
from CLIENTS
where not exists(
    select Code 
    from VOYAGES where VilleArrivee = 'Amsterdam'
    minus
    select code
    from RESERVATIONS where RESERVATIONS.id = CLIENTS.id
);

--9. ? Trouver les voyages qui ont ´et´e r´eserv´es par tous les clients parisiens.
select Code
from CLIENTS natural join RESERVATIONS
where 