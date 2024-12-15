drop table BDHABITANTVOITURE;

create table BdHabitantVoiture(
    Prenom varchar2(20),
    Nom varchar2(20),
    sexe varchar2(20),
    Rue varchar2(20),
    Num Number(2),
    Ville varchar2(10),
    MarqueV varchar2(10),
    NomV varchar2(10),
    AnneeV Number(4),
    CouleurV varchar2(10),
    TypeMoteurV varchar2(10),
    ImmV varchar2(10)
);

insert into BdHabitantVoiture values ('Arlette', 'Fort', 'F', 'des Allouettes', 15, 'Olivet', 'Renault', 'Zoe', 2016, 'blanche', 'electrique', 'AD-123-EF');
insert into BdHabitantVoiture values ('Jean', 'Duprack', 'M', 'des Allouettes', 12, 'Olivet', 'Peugeot', '2008', 2015, 'noire', 'essence', 'AD-234-EF');
insert into BdHabitantVoiture values ('Arlette', 'Fort', 'F', 'Alesia', 4, 'Paris', 'Renault', 'Clio', 2017, 'rouge', 'essence', 'AD-567-EF');
insert into BdHabitantVoiture values ('Arlette', 'Fort', 'F', 'des Allouettes', 15, 'Olivet', 'Renault', 'Clio', 2017, 'rouge', 'essence', 'AD-567-EF');
insert into BdHabitantVoiture values ('Jean', 'Dubois', 'M', 'Rivoli', 12, 'Paris', 'Peugeot', '2008', 2015, 'noire', 'essence', 'AD-333-EF');
insert into BdHabitantVoiture values ('Jean', 'Dubois', 'M', 'Rivoli', 12, 'Paris', 'Renault', 'Clio', 2017, 'noire', 'essence', 'AD-444-EF');
insert into BdHabitantVoiture values ('Jean', 'Dubois', 'M', 'Rivoli', 12, 'Paris', 'Toyota', 'Verso', 2015, 'Bleu', 'diesel', 'AA-333-BB');
insert into BdHabitantVoiture values ('Jean', 'Dubois', 'M', 'Rivoli', 12, 'Paris', 'Toyota', 'Yaris', 2017, 'rouge', 'hybrid', 'AA-333-BB');










select Prenom, Nom, Ville, MarqueV, NomV from BdHabitantVoiture where Nom = 'Fort';
select Prenom, Nom, Ville, MarqueV, NomV from BdHabitantVoiture;