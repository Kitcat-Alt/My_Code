-- create database NOTES;
-- use NOTES;
drop table if exists OBTENIR;
drop table if exists SUIVRE;
drop table if exists EVALUATION;
drop table if exists COURS;
drop table if exists ETUDIANT;
create table ETUDIANT (numetu int, nometu varchar(15), prenometu varchar(15),
  primary key (numetu));
create table SUIVRE (numetu int, numco int, primary key (numetu, numco));
create table COURS (numco int, nomco Varchar(15), primary key (numco));
create table EVALUATION (numev int, nomev varchar(15), dateev date, coefev int,
  numco int, primary key (numev));
create table OBTENIR ( numetu int, numev int, note int, 
 primary key (numetu, numev));

alter table SUIVRE add foreign key (numco) references COURS (numco);
alter table SUIVRE add foreign key (numetu) references ETUDIANT (numetu);
alter table EVALUATION add foreign key (numco) references COURS (numco);
alter table OBTENIR add foreign key (numev) references EVALUATION (numev);
alter table OBTENIR add foreign key (numetu) references ETUDIANT (numetu);


insert into ETUDIANT(numetu, nometu, prenometu) values
       	    		     (1,'Martin','Pierre'),
			     (2,'Dubois','Julie'),
			     (3,'Dupont','Marie'),
			     (4,'Valin','Patrick'),
			     (5,'Deschamps','Hector');

insert into COURS(numco, nomco) values (10,'Informatique'), (20,'Mathematiques'), (30,'Anglais'), (40,'Espagnol');
insert into SUIVRE(numetu,numco) values (1,10), (1,20),
       	    			 	(2,20), (2,30),
					(3,10), (3,20), (3,30), (3,40),
       	    			 	(4,10), (4,20), (4,30);
					
insert into EVALUATION(numev,nomev,dateev,coefev,numco) values
       	    				(101,'Algo-Prog',STR_TO_DATE('10/09/2024','%d/%m/%Y'),2,10),
					(102,'BD',STR_TO_DATE('25/10/2024','%d/%m/%Y'),1,10),
					(103,'Analyse',STR_TO_DATE('08/12/2024','%d/%m/%Y'),1,20),
					(104,'Algèbre',STR_TO_DATE('17/01/2025','%d/%m/%Y'),1,20),
					(105,'Proba',STR_TO_DATE('28/02/2025','%d/%m/%Y'),2,20),
					(106,'Vocabular',STR_TO_DATE('23/09/2024','%d/%m/%Y'),1,30),
					(107,'Translation',STR_TO_DATE('10/01/2025','%d/%m/%Y'),1,30);
					
insert into OBTENIR(numetu,numev,note) values (1,101,12), (1,102,11), (1,103,8), (1,104,7), (1,105,9),
       	    			       	      (2,106,18), (2,107,16), (2,103,18), (2,104,14), (2,105,8),
					      (3,106,14), (3,101,8), (3,103,14), (3,104,8),
					      (4,101,10), (4,103,13), (4,104,11), (4,105,10);
					      
