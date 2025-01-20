CREATE DATABASE IF NOT EXISTS Sondage DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE Sondage;

CREATE TABLE CARACTERISTIQUE (
  idc CHAR(3),
  sexe Char(1),
  idcat Char(1),
  idtr Char(1),
  PRIMARY KEY (idc)
);

CREATE TABLE SONDE (
  numsond decimal(6),
  nomsond Varchar(30),
  prenomsond Varchar(30),
  datenaissond Date,
  telephonesond Varchar(10),
  idc CHAR(3),
  PRIMARY KEY (numsond)
);

CREATE TABLE CONSTITUER (
  numsond decimal(6),
  idpan decimal(3),
  PRIMARY KEY (numsond, idpan)
);

CREATE TABLE PANEL (
  idpan decimal(3),
  nompan Varchar(30),
  PRIMARY KEY (idpan)
);

CREATE TABLE TRANCHE (
  idtr Char(1),
  valdebut Decimal(3),
  valfin Decimal(3),
  PRIMARY KEY (idtr)
);

CREATE TABLE CATEGORIE (
  idcat Char(1),
  intitulecat Varchar(50),
  PRIMARY KEY (idcat)
);

ALTER TABLE CARACTERISTIQUE ADD FOREIGN KEY (idtr) REFERENCES TRANCHE (idtr);
ALTER TABLE CARACTERISTIQUE ADD FOREIGN KEY (idcat) REFERENCES CATEGORIE (idcat);
ALTER TABLE SONDE ADD FOREIGN KEY (idc) REFERENCES CARACTERISTIQUE (idc);
ALTER TABLE CONSTITUER ADD FOREIGN KEY (idpan) REFERENCES PANEL (idpan);
ALTER TABLE CONSTITUER ADD FOREIGN KEY (numsond) REFERENCES SONDE (numsond);
