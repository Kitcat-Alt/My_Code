insert into AUTEUR(idaut, nom, prenom)values
        (1,'Zola', 'Emile');
insert into GENRE(idgen, nomgen)values
        (4, 'roman');
insert into LIVRE(idliv, titre)values
        (3,'Germinal');
insert into ECRIRE(idaut, idliv)values
        (1,3);

insert into AUTEUR(idaut, nom, prenom)values
        (2,'Uderzo', 'Albert');
insert into GENRE(idgen, nomgen)values
        (5, 'bande dessinée');
insert into LIVRE(idliv, titre)values
        (4,'Asterix chez les Bretons');
insert into ECRIRE(idaut, idliv)values
        (2,4);

insert into AUTEUR(idaut, nom, prenom)values
        (3,'Moliere', NULL);
insert into GENRE(idgen, nomgen)values
        (6, 'piece de theatre');
insert into LIVRE(idliv, titre)values
        (5,'Le bourgeois gentilhomme');
insert into ECRIRE(idaut, idliv)values
        (3,5);