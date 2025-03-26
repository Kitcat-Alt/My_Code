DROP TABLE EFFECTUER;
DROP TABLE COURSE;
DROP TABLE COUREUR;
DROP TABLE CATEGORIE; 
DROP TABLE CLUB;
DROP TABLE EVENEMENT;
DROP TABLE LIEU;







create table LIEU(
    PRIMARY KEY(idL),
    idL int NOT NULL,
    nomL varchar(20)
);

create table EVENEMENT(
    PRIMARY KEY(idEV, idL),
    idEV int NOT NULL,
    idL int,
    nomEv varchar(20),
    dateEv date
);

create table CLUB(
    PRIMARY KEY (idCl),
    idCl int  NOT NULL,
    sigleCl varchar(20),
    nomCL varchar(20)
);

create table CATEGORIE(
    PRIMARY KEY (idCat),
    idCat int NOT NULL,
    nomCate varchar(20)
);

create table COUREUR(
    PRIMARY KEY(idCo, idCl),
    idCo int NOT NULL,
    idCl int,
    idCat int,
    nomCo varchar(20),
    prenomCo varchar(20)
);

create table COURSE(
    PRIMARY KEY(idCourse, idEv),
    idEV int,
    idCat int,
    idCourse int NOT NULL,
    heure int
);

create table EFFECTUER(
    PRIMARY KEY(idCo, idEV, idCourse),
    temps int NOT NULL,
    idCo int,
    idEV int,
    idCourse int
);

ALTER TABLE EVENEMENT ADD FOREIGN KEY (idL) REFERENCES LIEU (idL);

ALTER TABLE COUREUR ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE (idCat);
ALTER TABLE COUREUR ADD FOREIGN KEY (idCl) REFERENCES CLUB (idCl);

ALTER TABLE COURSE ADD FOREIGN KEY (idEV) REFERENCES EVENEMENT (idEV);
ALTER TABLE COURSE ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE (idCat);

ALTER TABLE EFFECTUER ADD FOREIGN KEY (idCo) REFERENCES COUREUR (idCo);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idEV) REFERENCES EVENEMENT (idEv);
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idCourse) REFERENCES COURSE (idCourse);

