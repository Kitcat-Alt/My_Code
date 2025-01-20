create table Habitant(
    Id Number(2),
    Prenom varchar2(20),
    Nom varchar2(20),
    Sexe varchar2(1),
    Rue varchar2(20),
    num Number(2),
    Ville varchar2(10),
    constraint KeyHabitant PRIMARY KEY (Id)

);

create table Voiture(
    MarqueV Varchar2(20),
    NomV varchar2(20),
    AnneeV number(4),
    CouleurV varchar2(10),
    TypeMoteurV varchar2(10),
    ImmV varchar2(10),
    constraint KeyVoiture PRIMARY KEY (ImmV)

);

create table Posseder(
    Id Number(2),
    ImmV varchar2(10),
    constraint FKHabitant FOREIGN KEY (Id) REFERENCES Habitant (Id),
    constraint FKVoiture FOREIGN KEY (ImmV) REFERENCES Voiture (immv)

);