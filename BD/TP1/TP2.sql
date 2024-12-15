--sqlplus foucher@ora12
--select * from tab;
--drop table BIN$IW6GqmstT2fgY/YNqMD/NQ==$0;
--purge recyclebin;
--rlwrap sqlplus foucher@ora12
-- set linesize 500;


drop table TEMPS;
drop table ETAPES;
drop table COUREURS;
drop table EQUIPES;
drop table PAYS;

create table PAYS (
CodePays Varchar2(3) primary key,
NPays Varchar2(20));

create table EQUIPES
(NomEquipe VarChar2(30)  primary key, 
DirecteurSportif  VarChar2(20));

create table COUREURS
(NumCoureur Number (4) primary key,
NomCoureur VarChar2(30),
PrenomCoureur VarChar2(30),
NomEquipe VarChar2(20),
CodePays VarChar(3),
foreign key (CodePays) references PAYS(CodePays) on delete cascade,
foreign key (NomEquipe) references EQUIPES(NomEquipe) on delete cascade);

create table ETAPES(
NumEtape Number (3) primary key,
DateEtape DATE DEFAULT sysdate,
VilleDepart Varchar2(20),
VilleArrivee Varchar2(20),
NbKm Number (3));

create table TEMPS(
NumCoureur Number (3),
NumEtape Number (3),
TempsRealise Date,
constraint Temps_ok primary key (NumCoureur, NumEtape));


--1. Lister les noms des ´equipes.
select NomEquipe
from EQUIPES;

--2. Lister les noms des directeurs sportifs.
select DirecteurSportif
from EQUIPES;

--3. Lister les noms et les pr´enoms des coureurs.
select NomCoureur, PrenomCoureur
from COUREURS;

--4. Trouver l’´equipe du coureur ULLRICH
select NomEquipe 
from COUREURS 
where NomCoureur = 'ULLRICH';

--5. Donner les noms des coureurs de l’´equipe COFIDIS
select NomCoureur 
from COUREURS 
where NomEquipe = 'COFIDIS';

--6. Lister tous les coureurs fran¸cais.
select NomCoureur, PrenomCoureur 
from COUREURS natural join PAYS
where NPays = 'FRANCE';

--7. Quel temps le coureur ’JALABERT’ a fait dans l’´etape 3 ?

--8. Trouver le temps r´ealis´e par les coureurs sous l’encadrement de Manolo SAIZ dans
--les ´etapes dont la ville de d´epart est Rouen.
--9. Lister les pays ayant des coureurs dans l’´etape dont l’arriv´ee est Plumelec.
--10. Trouver des couples de coureurs du mˆeme pays.
--11. Lister tous les coureurs fran¸cais. Afficher (en concat´enant) pr´enom et nom. La colonne
--doit afficher Coureur.
--12. Afficher les coureurs dont les pr´enoms commence par J.
--13. Afficher les noms des coureurs en ordre alphab´etique.
--14. Afficher les r´esultats des ´etapes ordonn´es par le num´ero de l’´etape, le temps r´ealis´e et
--le nom du coureur.




insert into PAYS values ('ALL','ALLEMAGNE');
insert into PAYS values ('AUT','AUTRICHE');
insert into PAYS values ('BEL','BELGIQUE');
insert into PAYS values ('DAN','DANEMARK');
insert into PAYS values ('ESP','ESPAGNE');
insert into PAYS values ('FRA','FRANCE');
insert into PAYS values ('GB','GRANDE BRETAGNE');
insert into PAYS values ('ITA','ITALIE');
insert into PAYS values ('SUI','SUISSE');





insert into EQUIPES values ('BANESTO','Eusebio UNZUE');
insert into EQUIPES values ('COFIDIS','Cyrille GUIMARD');
insert into EQUIPES values ('LA FRANCAISE DES JEUX','Marc MADIOT');
insert into EQUIPES values ('FESTINA','Bruno ROUSSEL');
insert into EQUIPES values ('GAN','Roger LEGEAY');
insert into EQUIPES values ('TELEKOM','Walter GODEFROOT');
insert into EQUIPES values ('ONCE', 'Manolo SAIZ');




insert into COUREURS values (8,'ULLRICH','Jan','TELEKOM','ALL');
insert into COUREURS values (31,'JALABERT','Laurent','ONCE','FRA');
insert into COUREURS values (61,'ROMINGER','Tony','COFIDIS','SUI');
insert into COUREURS values (91 ,'BOARDMAN','Chris','GAN','GB');
insert into COUREURS values (151 ,'OLANO','Abraham ','BANESTO','ESP');
insert into COUREURS values (133,'COPPEL','Jerome','COFIDIS','FRA');
insert into COUREURS values (137,'MATE','Luis-Angel','COFIDIS','ESP');


insert into  ETAPES values (1, to_date('06-07-97', 'dd-MM-yy'),'Rouen','Forges-les-Eaux', 192);
insert into  ETAPES values (2, to_date('07-07-97', 'dd-MM-yy'),'St-Valery-en-Caux','Vire', 262);
insert into  ETAPES values (3, to_date('08-07-97', 'dd-MM-yy'),'Vire','Plumelec', 224);


insert into TEMPS values (8,3,to_date('04:54:33', 'hh24:mi:ss'));
insert into TEMPS values (8,1,to_date('04:48:21', 'hh24:mi:ss'));
insert into TEMPS values (8,2,to_date('06:27:47', 'hh24:mi:ss'));
insert into TEMPS values (31,3,to_date('04:54:33', 'hh24:mi:ss'));
insert into TEMPS values (31,1,to_date('04:48:33', 'hh24:mi:ss'));
insert into TEMPS values (31,2,to_date('06:27:27', 'hh24:mi:ss'));