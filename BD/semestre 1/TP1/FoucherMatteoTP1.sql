--sqlplus foucher@ora12
--select * from tab;
--drop table BIN$IW6GqmstT2fgY/YNqMD/NQ==$0;
--purge recyclebin;
--rlwrap sqlplus foucher@ora12

drop table CONTENIR;
drop table EXPEDIER;
drop table COLIS;
drop table COMMANDE;
drop table ARTICLE;
drop table CLIENT;
drop table POINTDEDISTRIBUTION;
purge recyclebin;

create table POINTDEDISTRIBUTION(
    refPointDist number(5),
    adressePointDist varchar(30),
    constraint ClePOINTDEDISTRIBUTION PRIMARY KEY (refPointDist)
);

create table CLIENT(
    codeCl number(10),
    nomCl varchar2(40),
    prenom varchar2(30),
    adresse varchar(50),
    email varchar(50),
    constraint CleCLIENT PRIMARY KEY (codeCl),
    constraint PDISTEXISTE FOREIGN KEY (refPointDist) REFERENCES POINTDEDISTRIBUTION (refPointDist)
);


insert into CLIENT values(12, 'Foucher', 'Matteo', '194 Avenue de lArgonne', 'matteofoucher@gmail.com');

create table ARTICLE(
    RefArt number(5),
    designation varchar2(20),
    prix number(5,2),
    TVA number(4,2),
    qteStock number(5,2),
    constraint CleARTICLE PRIMARY KEY (RefArt)
);

create table COMMANDE(
    NumCom number(5),
    DateCom date,
    codeCl number(5),
    constraint CleCOMMANDE PRIMARY KEY (NumCom),
    constraint CLIENTEXIST FOREIGN KEY (CodeCl) REFERENCES CLIENT (codeCl)
);

create table COLIS(
    Numcom number(5),
    NumColis number(5),
    indiceRetrait varchar2(20),
    constraint CleCOLIS PRIMARY KEY (NumCom,NumColis),
    constraint COMEXIST FOREIGN KEY(Numcom) REFERENCES COMMANDE(NumCom)
);

create table EXPEDIER(
    NumCom number(5),
    NumColis number(5),
    RefArt number(5),
    qteExp number(5),
    qteAcc number(5),
    constraint CleEXPEDIER PRIMARY KEY (NumCom,NumColis,RefArt),
    constraint COLISEXIST FOREIGN KEY(NumColis,NumCom) REFERENCES COLIS(NumCom,NumColis),
    constraint  ARTICLEEXIST FOREIGN KEY(RefArt) REFERENCES ARTICLE(RefArt)
);

create table CONTENIR(
    numCom number(5),
    RefArt number(5),
    qteCom number(5),
    constraint CleCONTENIR PRIMARY KEY (NumCom,RefArt),
    constraint CONTENIRCOMEXIST FOREIGN KEY(NumCom) REFERENCES COMMANDE(NumCom),
    constraint ARTICLEEXIST FOREIGN KEY(RefArt) REFERENCES ARTICLE(RefArt)

);
