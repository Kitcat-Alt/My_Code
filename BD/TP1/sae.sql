drop table REMPLACER;
drop table NOURRIR;
drop table STOCKER;
drop table Nutriment;
drop table Plante;
drop table Espece;
drop table FicheArrosage;
drop table FamilleEspece;
drop table Emplacement;
drop table Jardins;
drop table Forets;
drop table ReserveBotanique;
purge recyclebin;

create table ReserveBotanique (
	IDReserveBota number(10) PRIMARY KEY,
	NomReserve varchar2(30),
	Ville varchar2(30),
	Pays varchar2(30),
	Telephone number(20),
	Email varchar2(40),
	NomRepresentant varchar2(30),
	TypeReserve varchar2(10),
	CHECK (TypeReserve IN ('Forets', 'Jardins'))
);

create table Forets (
	IDReserveBota number(10) NOT NULL,
	Superficie number(20),
	constraint foreignkey_Forets_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table Jardins (
	IDReserveBota number(10) NOT NULL,
	NomOrganisation varchar2(30),
	AdresseContact varchar2(50),
	InformationContact varchar2(80),
	constraint foreignkey_Jardins_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table Emplacement (
	CodeEmplacement number(10),
	IDReserveBota number(10) NOT NULL,
	SituationEmplacement varchar2(10),
	PRIMARY KEY (CodeEmplacement, IDReserveBota),
	constraint foreignkey_Emplacement_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table FamilleEspece(
	NomFamille varchar2(20) PRIMARY KEY,
	DescriptionFamille varchar2(300),
	Catateristiques varchar2(50)
);

create table FicheArrosage (
	IDFicheArrosage number(10) PRIMARY KEY,
	QteEauSemaine number(10),
	ModeArrosage varchar2(20),
	AjustementsSaison varchar2(60)
);

create table Espece (
	IDEspece number(10) PRIMARY KEY,
	NomScientifique varchar2(30),
	NomVulgaire varchar2(30),
	DescriptionEspeces varchar2(50),
	NomFamille varchar2(20) NOT NULL,
	IDFicheArrosage number(10) NOT NULL,
	constraint foreignkey_Espece_NomFamille FOREIGN KEY (NomFamille) REFERENCES FamilleEspece (NomFamille),
	constraint foreignkey_Espece_IDFicheArrosage FOREIGN KEY (IDFicheArrosage) REFERENCES FicheArrosage (IDFicheArrosage)
);

create table Plante (
	IDPlante number(10) PRIMARY KEY,
	DatePlantation date,
	Couleur varchar2(20),
	Hauteur number(5),
	IDEspece number(10) NOT NULL,
	CodeEmplacement number(10) NOT NULL,
	IDReserveBota number(10) NOT NULL,
	constraint foreignkey_Plante_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece),
	constraint foreignkey_Plante_IDReserveBotaCodeEmplacement FOREIGN KEY (CodeEmplacement, IDReserveBota) REFERENCES Emplacement (CodeEmplacement, IDReserveBota)
);

create table Nutriment (
	IDNutriment number(10) PRIMARY KEY,
	NomNutriment varchar2(50),
	FormuleChimique varchar2(50),
	TypeNutriment varchar2(50)
);

create table STOCKER (
	IDNutriment number(10),
	IDReserveBota number(10),
	QteNutriment number(10),
	PRIMARY KEY (IDReserveBota, IDNutriment),
	constraint foreignkey_STOCKER_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment),
	constraint foreignkey_STOCKER_IDReserveBota FOREIGN KEY (IDReserveBota) REFERENCES ReserveBotanique (IDReserveBota)
);

create table NOURRIR (
	IDEspece number(10) NOT NULL,
	IDNutriment number(10) NOT NULL,
	QteParJour number(10,5),
	PRIMARY KEY (IDEspece, IDNutriment),
	constraint foreignkey_NOURRIR_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece),
	constraint foreignkey_NOURRIR_IDNutriment FOREIGN KEY (IDNutriment) REFERENCES Nutriment (IDNutriment)
);

create table REMPLACER (
	IDNutrimentPrincipal number(10) NOT NULL,
	IDNutrimentSubstitut number(10) NOT NULL,
	TauxRemplacement number(4,2),
	PRIMARY KEY (IDNutrimentPrincipal, IDNutrimentSubstitut),
	constraint foreignkey_REMPLACER_IDNutrimentPrincipal FOREIGN KEY (IDNutrimentPrincipal) REFERENCES Nutriment (IDNutriment),
	constraint foreignkey_REMPLACER_IDNutrimentSubstitut FOREIGN KEY (IDNutrimentSubstitut) REFERENCES Nutriment (IDNutriment)
);

create table ORIGINAIRE (
  IDEspece number(10),
  ZoneGeoOrigine varchar2(50),
  PRIMARY KEY (IDEspece, ZoneGeoOrigine),
  constraint foreignkey_ORIGINAIRE_IDEspece FOREIGN KEY (IDEspece) REFERENCES Espece (IDEspece)
);



insert into ReserveBotanique values (1, 'Neo-Tokyo Forest Reserve', 'Neo-Tokyo', 'Japon', 0312345678, 'contact@neo-tokyo.jp', 'Gendo Ikari', 'Forets');
insert into ReserveBotanique values (2, 'Jardin de la NERV', 'Hakone', 'Japan', 0312345076, 'contact@nerv-garden.jp', 'Misato Katsuragi', 'Jardins');
insert into ReserveBotanique values (3, 'LCL Reserve Amazonienne', 'Manaus', 'Brasil', 5647382910, 'contact@lcl-reserve.br', 'Ryoji Kaji', 'Forets');
insert into ReserveBotanique values (4, 'Geofront Jardin Botanique', 'Tokyo-3', 'Japon', 0312345698, 'contact@geofront.jp', 'Ritsuko Akagi', 'Jardins');

insert into Forets values (1, 50000);
insert into Forets values (3, 150000);
-- Ne fonctionne pas car les identifiants (IDReserveBota) n'existe pas dans la table ReserveBotanique
insert into Forets values (5, 100000);
insert into Forets values (6, 75000);

insert into Jardins values (2, 'NERV HQ', 'GeoFront Level 3', 'contact@nerv-hq.jp');
insert into Jardins values (4, 'SEELE Organization', 'Hakone District', 'info@seele.org');
-- Ne fonctionne pas car les identifiants (IDReserveBota) n'existe pas dans la table ReserveBotanique
insert into Jardins values (7, 'Shinji Community', 'GeoFront Aile Sud', 'shinji@community.jp');
insert into Jardins values (8, 'Tokyo-3 Residents', 'Secteur A4', 'tokyo3@gardens.jp');

insert into Emplacement values (101, 1, 'Fleurie');
insert into Emplacement values (102, 1, 'Vide');
insert into Emplacement values (103, 1, 'Pousse');
insert into Emplacement values (101, 2, 'Fleurie');
insert into Emplacement values (102, 2, 'Pousse');
insert into Emplacement values (103, 2, 'Vide');
insert into Emplacement values (101, 3, 'Pousse');
insert into Emplacement values (102, 3, 'Vide');
insert into Emplacement values (103, 3, 'Fleurie');
insert into Emplacement values (101, 4, 'Pousse');
insert into Emplacement values (102, 4, 'Fleurie');
insert into Emplacement values (103, 4, 'Vide');
