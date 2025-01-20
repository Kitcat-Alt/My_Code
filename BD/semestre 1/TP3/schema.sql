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

--1. Lister les destinations proposées à partir de Paris.
select VilleArrivee
from VOYAGES
where VilleDepart = 'Paris';   
--2. Lister tous les voyages pour Amsterdam.
select *
from VOYAGES
where VilleArrivee = 'Amsterdam';
--3. Lister les villes de d´epart, les dates et les heures de d´epart pour tous les voyages pour
--Amsterdam.
select VilleDepart, Depart, Retour
from VOYAGES
where VilleArrivee = 'Amsterdam';
--4. Lister des noms des clients ayant une r´eservation en informant leur destination et le
--prix du voyage. La r´eponse est en ordre alphab´etique du nom et un ordre d´ecroissante
--de prix.
select Nom, Prix, VilleArrivee
from CLIENTS natural join VOYAGES natural join RESERVATIONS
order by Nom, Prix desc;
--5. Donner les clients qui habitent dans la ville de d´epart de leur voyage. Indiquer le nom
--du client, la ville de d´epart et le code du voyage.
select VilleDepart, Nom, code
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where Ville=VilleDepart;  
--6. Ins´erer dans la base au moins un nouveau voyage qui devra avoir lieu dans un an.
--insert into Voyages values ('V333', 'Paris', 'Tokyo',  to_date('29-11-2024-8:30','DD-MM-YYYY-HH24:MI'), to_date('29-11-2025-15:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V333', 'Paris', 'NeoTokyo3',  to_date('29-11-2024-8:30','DD-MM-YYYY-HH24:MI'), to_date('29-11-2025-15:30','DD-MM-YYYY-HH24:MI'),1200.00);
--7. Pour tous les vols dont le d´epart est dans plus de 3 mois, lister les villes de d´epart et
--arriv´ee, les dates et les heures de d´epart. Pr´esenter la liste dans l’ordre chronologique
--de d´epart.
select VilleDepart, VilleArrivee, to_char(Depart, 'DD-MM-YYYY-HH24:MI') as Depart
from VOYAGES
where Depart > to_date('29-11-2019-8:30','DD-MM-YYYY-HH24:MI');
-- where months_sysdate(sysdate, depart) > 3
--8. Quelles sont les villes concern´ees par les voyages. Pr´esenter le r´esultat dans une rela-
--tion avec un seul attribut : Villes.
select VilleDepart as Ville
from VOYAGES
union
select VilleArrivee as Ville
from VOYAGES;

--9. Lister les clients qui n’habitent pas Paris.
select Nom
from CLIENTS
where Ville != 'Paris';
--10. Lister les clients qui partent de Paris, mais qui n’habitent pas Paris.
select distinct Nom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleDepart = 'Paris' and Ville != VilleDepart;
--11. Trouver les clients qui n’ont aucune r´eservation.
select Nom, Prenom
from Clients
minus
select Nom, Prenom
from CLIENTS natural join RESERVATIONS;
--12. Voyages qui ne font pas objet d’une r´eservation.
select Code, VilleDepart, VilleArrivee
from VOYAGES
minus
select Code, VilleDepart, VilleArrivee
from VOYAGES natural join RESERVATIONS;
--13. Clients qui partent de Paris, mais qui vont uniquement a Amsterdam (´eventuellement
--plusieurs fois). Aucun voyage vers une autre destination.
select distinct Nom, Prenom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleDepart = 'Paris' and VilleArrivee = 'Amsterdam'
minus
select distinct Nom, Prenom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleDepart = 'Paris' and VilleArrivee != 'Amsterdam';

--14. Clients qui vont `a Amsterdam et `a Rio de Janeiro.
select Nom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleArrivee = 'Rio de Janeiro'
intersect
select Nom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleArrivee = 'Amsterdam'; 
--15. Clients qui vont `a Amsterdam ou `a Rio de Janeiro.
select Nom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleArrivee = 'Rio de Janeiro'
union
select Nom
from CLIENTS natural join VOYAGES natural join RESERVATIONS
where VilleArrivee = 'Amsterdam';
--16. Couples de clients habitant la mˆeme ville. Indiquer la ville en question.
select c1.Nom, c2.Nom
from CLIENTS c1, CLIENTS c2
where c1.Ville = c2.Ville and c1.Nom < c2.Nom;
--17. Couples de (code) voyages ayant le mˆeme prix. Indiquer le prix en question.
select c1.Prix, c2.Prix
from VOYAGES c1, VOYAGES c2
where c1.Prix = c2.Prix and c1.Prix < c2.Prix;
--18. Clients ayant au moins deux r´eservations.
select distinct c1.Nom
from CLIENTS c1, RESERVATIONS R1, RESERVATIONS R2
where R1.id = C1.id and R2.id = C1.id and R1.Code != R2.Code;
--19. Clients ayant une seule r´eservation.
select Nom
from CLIENTS natural join RESERVATIONS
minus
select distinct c1.Nom
from CLIENTS c1, RESERVATIONS R1, RESERVATIONS R2
where R1.id = C1.id and R2.id = C1.id and R1.Code != R2.Code;
--20. Couples de clients ayant fait des r´eservations le mˆeme jour. Informer aussi les codes
--des voyages en question et la date de r´eservation.
select 
--21. Couples de clients ayant r´eserv´e le mˆeme voyage le mˆeme jour.