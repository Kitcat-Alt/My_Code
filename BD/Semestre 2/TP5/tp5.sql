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

select fil_lib_voe_acc as specialité, fili as filière, nb_voe_pp_bg as nb_gene, nb_voe_pp_bt as nb_techno
from STATS natural join VOEUX natural join FORMATION natural join FILIERE natural join ETABLISSEMENT natural join DEPARTEMENT natural join REGION
where fili = 'BUT' and session = 2023 and reg_etab_aff = 'Centre-Val de Loire';

select reg_etab_aff as region, contrat_etab as contrat, count(cod_uai) as nbEtablissements
from ETABLISSEMENT natural join DEPARTEMENT natural join REGION
group by region, contrat;

select g_ea_lib_vx as Etablissement, voe_tot as VoeuxTotal, nb_cla_pp as nbPrincipal
from STATS natural join VOEUX natural join ETABLISSEMENT natural join DEPARTEMENT
where session = 2023 and dep_lib = 'Indre';

