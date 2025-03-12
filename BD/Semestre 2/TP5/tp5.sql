select numsond, intitulecat
from SONDE natural join CONSTITUER natural join CARACTERISTIQUE natural join CATEGORIE natural join PANEL
where nompan = 'France Global 1';

select numsond, sexe, concat('Tranche ',valdebut,'-',valfin)
from SONDE natural join CONSTITUER natural join PANEL natural join CARACTERISTIQUE natural join TRANCHE
where nompan = 'France Global 2';

select numsond, concat('Tranche ',valdebut,'-',valfin) as Tranche, intitulecat
from SONDE natural join CATEGORIE natural join CARACTERISTIQUE natural join TRANCHE;

select intituleCat, YEAR(CURDATE())-YEAR(dateNaisSond)
from CATEGORIE natural join CARACTERISTIQUE natural join TRANCHE;

select fil_lib_voe_acc, fili, nb_voe_pp_bg as nb_gene, nb_voe_pp_bt as nb_techno
from STATS natural join VOEUX natural join FORMATION natural join FILIERE
where fili = 'BUT' and session = 2023;