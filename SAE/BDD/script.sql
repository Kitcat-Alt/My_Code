create table ReserveBotanique(
    IDReservebota number(5),
    Nomreserv varchar2(20),
    Ville varchar2(20),
    Pays varchar2(20),
    Tel number(5),
    Email varchar2(20),
    NomRep varchar2(20),
    TypeReserv varchar2(20),
);

create table Plante(
    IDPlante number(5),
    Dateplantation varchar2(20),
    Couleur varchar2(20),
    Hauteur number(5),
    Emplacement number(5),
);

create table Espece(
    IDEspeces number(5),
    NomScientifique varchar(20),
    NomVulgaire varchar(20),
    Description varchar2(20),
    ZoneGeoOrigine varchar2(20),
    IDFiche number(20),
);

create table FamilleEspece(
    NomFamille varchar2(20),
    Description varchar2(20),
    Caractéristiques varchar2(20)
);

create table FichesArrosage(
    IDFiche number(5),
    QuantitéEauWeek number(5),
    ModeArrosage varchar2(20),
    AjustSaisonsCondiClimatiques varchar2(20),
);

create table Nutriments(
    IDNutriments number(5),
    NomNutriments varchar2(20),
    FormuleChimique varchar2(20),
    Type varchar2(20),
    TauxRemplacement number(5),
);

create table Forêts(
    Superficie number(5),
);

create table Jardins(
    NomOrga varchar2(20),
    Adresse varchar2(20),
    Contact varchar2(20),
);