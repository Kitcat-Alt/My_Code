drop table  EXPOSITIONTABLEAUX;
drop table GALERIES;
drop table TABLEAUX;
drop table PEINTRES;


create table PEINTRES (
nomP Varchar2(20) primary key,
dateN date,
ecole Varchar2(20));

create table TABLEAUX(
nomP Varchar2(20),
titreTab VarChar2(30) ,
valeurEstimee number (10,2),
type VarChar2(10),
constraint KTableaux primary key (nomP, titreTab),
constraint KFPeintreExisteInTableaux foreign key (nomP) references  PEINTRES (nomP) on delete cascade);


create table GALERIES
(IdSalle number(3) primary key,
nomSalle VarChar2(20),
superfice number(4),
ville VarChar2(15));

create table EXPOSITIONTABLEAUX
(IdSalle number(3),
nomP Varchar2(20),
titreTab VarChar2(30) ,
dateDebut date,
dateFin date,
constraint KEXPO primary key (IdSalle,nomP,titreTab),
constraint KFTableauxExisteInExpo foreign key (nomP,titreTab) references  TABLEAUX (nomP,titreTab) on delete cascade,
constraint KFSalleExisteInExpo foreign key (IdSalle) references GALERIES(IdSalle) on delete cascade);






--Peintres [ nomP, dateN, ecole ]
--Tableaux [ nomP, titre, annee, valeurEstimee, type ]
--Galeries [ idSalle, nomSalle, superficie, ville]
--ExpositionTableaux [ nomP, titre, idSalle, dateDebut, dateFin]

--1. Lister les peintres sans aucun tableaux enregistr´e dans la base.
select nomP, dateN, ecole
from PEINTRES
minus
select nomP, dateN, ecole
from TABLEAUX natural join PEINTRES;

select *
from PEINTRES
where nomP not in (select nomP from TABLEAUX);

select *
from PEINTRES
where not exists (
    select *
    from TABLEAUX
    where TABLEAUX.nomP = PEINTRES.nomP
);
--2. Lister les tableaux de Monet ou Renoir.
select titreTab
from TABLEAUX
where nomP='Monet' or nomP='Renoir';
--3. Lister les villes ayant expos´e des tableaux de Picasso et de Monet.
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Picasso'
intersect
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Monet';
--4. Lister les villes ayant expos´e des tableaux de Picasso ou de Monet.
select distinct ville 
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Picasso' or nomP='Monet';
--5. Lister les villes ayant expos´e des tableaux de Picasso mais pas de Monet.
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Picasso'
minus
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Monet';
--6. Lister les villes ayant expos´e seulement des tableaux de Toulouse-Lautrec (par rapport
--aux peintres dans la base).
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Toulouse-Lautrec'
minus
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP!='Toulouse-Lautrec';
--7. Lister les villes n’ayant jamais expos´e des tableaux de Picasso.
select ville
from GALERIES G1
where not exists(
    select *
    from EXPOSITIONTABLEAUX natural join GALERIES
    where nomP='Picasso' and ville = G1.ville
);

select ville 
from EXPOSITIONTABLEAUX natural join GALERIES
minus
select ville
from EXPOSITIONTABLEAUX natural join GALERIES
where nomP='Picasso';
--8. Lister les galeries n’ayant pas eu d’exposition.
select nomSalle
from GALERIES
where IdSalle not in (
    select IdSalle
    from EXPOSITIONTABLEAUX
);
--9. Lister les villes ayant au moins deux galeries.
select ville
from GALERIES
where ville
--10. Lister les villes ayant seulement une galerie.