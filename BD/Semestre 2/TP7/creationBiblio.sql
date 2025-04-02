DROP TABLE ECRIRE;
DROP TABLE LIVRE;
DROP TABLE GENRE;
DROP TABLE AUTEUR;




CREATE TABLE AUTEUR(
    idaut int NOT NULL,
    PRIMARY KEY(idaut),
    nom varchar(20),
    prenom varchar(20)
);

CREATE TABLE GENRE(
    idgen int NOT NULL,
    PRIMARY KEY(idgen),
    nomgen varchar(20)
);

CREATE TABLE LIVRE(
    idliv int NOT NULL,
    idgen int,
    PRIMARY KEY(idliv),
    titre varchar(50)
);

CREATE TABLE ECRIRE(
    idaut int,
    idliv int,
    PRIMARY KEY(idaut,idliv)
);

ALTER TABLE ECRIRE ADD FOREIGN KEY (idaut) REFERENCES AUTEUR (idaut);
ALTER TABLE ECRIRE ADD FOREIGN KEY (idliv) REFERENCES LIVRE (idliv);
ALTER TABLE LIVRE ADD FOREIGN KEY (idgen) REFERENCES GENRE (idgen);