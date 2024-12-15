# fichier de tests de la SAE 1.01 partie 1
# bilan carbone d'activités mystères en septembre 2024

# on importe toutes les fonctions et données définies dans le fichier bilan_carbone
# l'appel de ces fonctions et données doit être préfixé par bc. 
import bilan_carbone as bc  

# ---------------------------------------------------------------------------------------------
# Exemples de tests à compléter impérativement
# ---------------------------------------------------------------------------------------------

def test_est_avant():
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Erika', '2024-09-01', 67.2, 'type4')) == False
    assert bc.est_avant(('Erika', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-10', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type4')) == False
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-10', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    assert bc.est_avant((), ('Lucas', '2024-09-01', 67.2, 'type4')) == None
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ()) == None
    assert bc.est_avant((),()) == None


def test_annee():
    assert bc.annee(('Lucas', '2024-09-01', 67.2, 'type3')) == '2024'
    assert bc.annee(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999'
    assert bc.annee(()) == None
    assert bc.annee(('Lucas', '', 70.08, 'type3')) == None


def test_annee_mois():
    assert bc.annee_mois(('Lucas', '2024-10-01', 67.2, 'type3')) == '2024-10'
    assert bc.annee_mois(('Lucas', '2023-09-01', 67.2, 'type3')) == '2023-09'
    assert bc.annee_mois(()) == None
    assert bc.annee_mois(('Lucas', '', 70.08, 'type3')) == None


def test_max_emmission():
    assert bc.max_emmission([]) == None
    assert bc.max_emmission(bc.liste1) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste2) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste3) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste4) == ('David', '2024-09-27', 21, 'type2')
    assert bc.max_emmission(bc.liste5) == ('Erika', '2024-09-28', 240.5, 'type2')
    assert bc.max_emmission(bc.liste6) == ('Erika', '2024-09-28', 76.56, 'type1')
    assert bc.max_emmission([('Erika', '2024-09-28', 76.56, 'type1'), ('Erika', '2024-09-28', 76.56, 'type1')]) == ('Erika', '2024-09-28', 76.56, 'type1')
    assert bc.max_emmission([('Erika', '2024-09-28', 76.56, 'type1')]) == ('Erika', '2024-09-28', 76.56, 'type1')


def test_filtre_par_prenom():
    assert bc.filtre_par_prenom([], 'Lucas') == []
    assert bc.filtre_par_prenom(bc.liste5, "Alix") == []
    assert bc.filtre_par_prenom([], '') == []
    assert bc.filtre_par_prenom([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')], 'Lucas') == [('Lucas', '2024-09-01', 67.2, 'type3')]
    assert bc.filtre_par_prenom(bc.liste1, 'David') == [('David', '2024-09-26', 18, 'type1'), ('David', '2024-09-27', 21, 'type2'), ('David', '2024-09-28', 17, 'type3'), ('David', '2024-09-29', 23, 'type4')]
    assert bc.filtre_par_prenom(bc.liste5, 'Matéo') == [('Matéo', '2024-09-01', 22.62, 'type1'), ('Matéo', '2024-09-02', 6.09, 'type1'), ('Matéo', '2024-09-03', 30.45, 'type1'), ('Matéo', '2024-09-04', 12.18, 'type1'), ('Matéo', '2024-09-05', 22.62, 'type1'), ('Matéo', '2024-09-06', 20.01, 'type1'), ('Matéo', '2024-09-07', 42.63, 'type1'), ('Matéo', '2024-09-08', 18.27, 'type1'), ('Matéo', '2024-09-09', 54.81, 'type1'), ('Matéo', '2024-09-10', 24.36, 'type1'), ('Matéo', '2024-09-11', 9.57, 'type1'), ('Matéo', '2024-09-12', 22.62, 'type1'), ('Matéo', '2024-09-13', 15.66, 'type1'), ('Matéo', '2024-09-14', 26.1, 'type1'), ('Matéo', '2024-09-15', 11.31, 'type1'), ('Matéo', '2024-09-16', 20.88, 'type1'), ('Matéo', '2024-09-17', 25.23, 'type1'), ('Matéo', '2024-09-18', 11.31, 'type1'), ('Matéo', '2024-09-19', 13.05, 'type1'), ('Matéo', '2024-09-20', 13.92, 'type1'), ('Matéo', '2024-09-21', 22.62, 'type1'), ('Matéo', '2024-09-22', 0.87, 'type1'), ('Matéo', '2024-09-23', 21.75, 'type1'), ('Matéo', '2024-09-24', 6.09, 'type1'), ('Matéo', '2024-09-25', 49.59, 'type1'), ('Matéo', '2024-09-26', 13.92, 'type1'), ('Matéo', '2024-09-27', 28.71, 'type1'), ('Matéo', '2024-09-28', 15.66, 'type1'), ('Matéo', '2024-09-29', 33.93, 'type1'), ('Matéo', '2024-09-30', 19.14, 'type1'), ('Matéo', '2024-09-01', 70.08, 'type3'), ('Matéo', '2024-09-02', 18.24, 'type3'), ('Matéo', '2024-09-03', 93.12, 'type3'), ('Matéo', '2024-09-04', 37.44, 'type3'), ('Matéo', '2024-09-05', 70.08, 'type3'), ('Matéo', '2024-09-06', 60.48, 'type3'), ('Matéo', '2024-09-07', 129.6, 'type3'), ('Matéo', '2024-09-08', 55.68, 'type3'), ('Matéo', '2024-09-09', 167.04, 'type3'), ('Matéo', '2024-09-10', 74.88, 'type3'), ('Matéo', '2024-09-11', 30.72, 'type3'), ('Matéo', '2024-09-12', 69.12, 'type3'), ('Matéo', '2024-09-13', 48.0, 'type3'), ('Matéo', '2024-09-14', 81.6, 'type3'), ('Matéo', '2024-09-15', 35.52, 'type3'), ('Matéo', '2024-09-16', 63.36, 'type3'), ('Matéo', '2024-09-17', 77.76, 'type3'), ('Matéo', '2024-09-18', 35.52, 'type3'), ('Matéo', '2024-09-19', 41.28, 'type3'), ('Matéo', '2024-09-20', 43.2, 'type3'), ('Matéo', '2024-09-21', 69.12, 'type3'), ('Matéo', '2024-09-22', 2.88, 'type3'), ('Matéo', '2024-09-23', 68.16, 'type3'), ('Matéo', '2024-09-24', 20.16, 'type3'), ('Matéo', '2024-09-25', 150.72, 'type3'), ('Matéo', '2024-09-26', 43.2, 'type3'), ('Matéo', '2024-09-27', 86.4, 'type3'), ('Matéo', '2024-09-28', 48.0, 'type3'), ('Matéo', '2024-09-29', 103.68, 'type3'), ('Matéo', '2024-09-30', 59.52, 'type3')]
    assert bc.filtre_par_prenom(bc.liste2, "Christophe") == [('Christophe', '2024-09-26', 15, 'type1'), ('Christophe', '2024-09-27', 19, 'type2'), ('Christophe', '2024-09-28', 14, 'type3'), ('Christophe', '2024-09-29', 20, 'type4')]


def test_filtre():
    assert bc.filtre([], 3, 'type1') == []
    assert bc.filtre(bc.liste6, 3, 'type4') == []
    assert bc.filtre(bc.liste6, 0, 'Alix') == []
    assert bc.filtre(bc.liste6, 1, '2025-09-19') == []
    assert bc.filtre(bc.liste3, 1, '2024-09-29') == [('David', '2024-09-29', 23, 'type4'), ('Guillaume', '2024-09-29', 22, 'type4')]
    assert bc.filtre(bc.liste5, 0, 'Hugo') == [('Hugo', '2024-09-01', 61.77, 'type1'), ('Hugo', '2024-09-02', 17.4, 'type1'), ('Hugo', '2024-09-03', 46.11, 'type1'), ('Hugo', '2024-09-04', 30.45, 'type1'), ('Hugo', '2024-09-05', 41.76, 'type1'), ('Hugo', '2024-09-06', 6.09, 'type1'), ('Hugo', '2024-09-07', 9.57, 'type1'), ('Hugo', '2024-09-08', 17.4, 'type1'), ('Hugo', '2024-09-09', 22.62, 'type1'), ('Hugo', '2024-09-10', 6.96, 'type1'), ('Hugo', '2024-09-11', 25.23, 'type1'), ('Hugo', '2024-09-12', 15.66, 'type1'), ('Hugo', '2024-09-13', 21.75, 'type1'), ('Hugo', '2024-09-14', 57.42, 'type1'), ('Hugo', '2024-09-15', 29.58, 'type1'), ('Hugo', '2024-09-16', 24.36, 'type1'), ('Hugo', '2024-09-17', 13.05, 'type1'), ('Hugo', '2024-09-18', 26.97, 'type1'), ('Hugo', '2024-09-19', 16.53, 'type1'), ('Hugo', '2024-09-20', 5.22, 'type1'), ('Hugo', '2024-09-21', 40.02, 'type1'), ('Hugo', '2024-09-22', 23.49, 'type1'), ('Hugo', '2024-09-23', 10.44, 'type1'), ('Hugo', '2024-09-24', 19.14, 'type1'), ('Hugo', '2024-09-25', 30.45, 'type1'), ('Hugo', '2024-09-26', 42.63, 'type1'), ('Hugo', '2024-09-27', 14.79, 'type1'), ('Hugo', '2024-09-28', 30.45, 'type1'), ('Hugo', '2024-09-29', 30.45, 'type1'), ('Hugo', '2024-09-30', 31.32, 'type1'), ('Hugo', '2024-09-01', 192.4, 'type2'), ('Hugo', '2024-09-02', 53.95, 'type2'), ('Hugo', '2024-09-03', 145.6, 'type2'), ('Hugo', '2024-09-04', 96.85, 'type2'), ('Hugo', '2024-09-05', 130.65, 'type2'), ('Hugo', '2024-09-06', 19.5, 'type2'), ('Hugo', '2024-09-07', 31.2, 'type2'), ('Hugo', '2024-09-08', 54.6, 'type2'), ('Hugo', '2024-09-09', 70.85, 'type2'), ('Hugo', '2024-09-10', 21.45, 'type2'), ('Hugo', '2024-09-11', 79.95, 'type2'), ('Hugo', '2024-09-12', 50.7, 'type2'), ('Hugo', '2024-09-13', 68.9, 'type2'), ('Hugo', '2024-09-14', 181.35, 'type2'), ('Hugo', '2024-09-15', 92.3, 'type2'), ('Hugo', '2024-09-16', 77.35, 'type2'), ('Hugo', '2024-09-17', 41.6, 'type2'), ('Hugo', '2024-09-18', 85.15, 'type2'), ('Hugo', '2024-09-19', 52.0, 'type2'), ('Hugo', '2024-09-20', 18.2, 'type2'), ('Hugo', '2024-09-21', 125.45, 'type2'), ('Hugo', '2024-09-22', 72.8, 'type2'), ('Hugo', '2024-09-23', 32.5, 'type2'), ('Hugo', '2024-09-24', 61.75, 'type2'), ('Hugo', '2024-09-25', 95.55, 'type2'), ('Hugo', '2024-09-26', 133.25, 'type2'), ('Hugo', '2024-09-27', 46.8, 'type2'), ('Hugo', '2024-09-28', 95.55, 'type2'), ('Hugo', '2024-09-29', 96.85, 'type2'), ('Hugo', '2024-09-30', 97.5, 'type2'), ('Hugo', '2024-09-01', 187.2, 'type3'), ('Hugo', '2024-09-02', 52.8, 'type3'), ('Hugo', '2024-09-03', 141.12, 'type3'), ('Hugo', '2024-09-04', 94.08, 'type3'), ('Hugo', '2024-09-05', 126.72, 'type3'), ('Hugo', '2024-09-06', 18.24, 'type3'), ('Hugo', '2024-09-07', 29.76, 'type3'), ('Hugo', '2024-09-08', 52.8, 'type3'), ('Hugo', '2024-09-09', 69.12, 'type3'), ('Hugo', '2024-09-10', 21.12, 'type3'), ('Hugo', '2024-09-11', 77.76, 'type3'), ('Hugo', '2024-09-12', 48.96, 'type3'), ('Hugo', '2024-09-13', 66.24, 'type3'), ('Hugo', '2024-09-14', 176.64, 'type3'), ('Hugo', '2024-09-15', 90.24, 'type3'), ('Hugo', '2024-09-16', 74.88, 'type3'), ('Hugo', '2024-09-17', 40.32, 'type3'), ('Hugo', '2024-09-18', 82.56, 'type3'), ('Hugo', '2024-09-19', 50.88, 'type3'), ('Hugo', '2024-09-20', 17.28, 'type3'), ('Hugo', '2024-09-21', 121.92, 'type3'), ('Hugo', '2024-09-22', 71.04, 'type3'), ('Hugo', '2024-09-23', 31.68, 'type3'), ('Hugo', '2024-09-24', 60.48, 'type3'), ('Hugo', '2024-09-25', 93.12, 'type3'), ('Hugo', '2024-09-26', 129.6, 'type3'), ('Hugo', '2024-09-27', 45.12, 'type3'), ('Hugo', '2024-09-28', 93.12, 'type3'), ('Hugo', '2024-09-29', 94.08, 'type3'), ('Hugo', '2024-09-30', 95.04, 'type3'), ('Hugo', '2024-09-01', 18.27, 'type4'), ('Hugo', '2024-09-02', 5.04, 'type4'), ('Hugo', '2024-09-03', 13.86, 'type4'), ('Hugo', '2024-09-04', 8.82, 'type4'), ('Hugo', '2024-09-05', 12.6, 'type4'), ('Hugo', '2024-09-06', 1.89, 'type4'), ('Hugo', '2024-09-07', 2.52, 'type4'), ('Hugo', '2024-09-08', 5.04, 'type4'), ('Hugo', '2024-09-09', 6.3, 'type4'), ('Hugo', '2024-09-10', 1.89, 'type4'), ('Hugo', '2024-09-11', 7.56, 'type4'), ('Hugo', '2024-09-12', 4.41, 'type4'), ('Hugo', '2024-09-13', 6.3, 'type4'), ('Hugo', '2024-09-14', 17.01, 'type4'), ('Hugo', '2024-09-15', 8.82, 'type4'), ('Hugo', '2024-09-16', 6.93, 'type4'), ('Hugo', '2024-09-17', 3.78, 'type4'), ('Hugo', '2024-09-18', 8.19, 'type4'), ('Hugo', '2024-09-19', 5.04, 'type4'), ('Hugo', '2024-09-20', 1.26, 'type4'), ('Hugo', '2024-09-21', 11.97, 'type4'), ('Hugo', '2024-09-22', 6.93, 'type4'), ('Hugo', '2024-09-23', 3.15, 'type4'), ('Hugo', '2024-09-24', 5.67, 'type4'), ('Hugo', '2024-09-25', 8.82, 'type4'), ('Hugo', '2024-09-26', 12.6, 'type4'), ('Hugo', '2024-09-27', 4.41, 'type4'), ('Hugo', '2024-09-28', 8.82, 'type4'), ('Hugo', '2024-09-29', 8.82, 'type4'), ('Hugo', '2024-09-30', 9.45, 'type4')]
    assert bc.filtre(bc.liste4, 3, 'type1') == [('David', '2024-09-26', 18, 'type1')]
    assert bc.filtre(bc.liste5, 5, 'Hugo') == None
    
def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78
    assert bc.cumul_emmissions(bc.liste5) == 33710.84000000004
    assert bc.cumul_emmissions(bc.liste6) == 960.4799999999998
    assert bc.cumul_emmissions(bc.liste1) == 222
    assert bc.cumul_emmissions(bc.liste2) == 222
    assert bc.cumul_emmissions(bc.liste3) == 144

def test_plus_longue_periode_emmissions_decroissantes():
    assert bc.plus_longue_periode_emmissions_decroissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste6) == 3
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste5) == 4
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste1) == 1
    assert bc.plus_longue_periode_emmissions_decroissantes([('Erika', '2024-09-28', 76.56, 'type1'), ('Erika', '2024-09-28', 60, 'type1'), ('Erika', '2024-09-28', 55, 'type1')]) == 2
    assert bc.plus_longue_periode_emmissions_decroissantes([('Erika', '2024-09-28', 76.56, 'type1')]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes([('Erika', '2024-09-28', 76.56, 'type1'), ('Erika', '2024-09-28', 70, 'type1')]) == 1
    
def test_est_bien_triee():
    assert bc.est_bien_triee([]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]) == False
    assert bc.est_bien_triee(bc.liste6) == True
    assert bc.est_bien_triee(bc.liste5) == True
    assert bc.est_bien_triee(bc.liste1) == False
    



def test_liste_des_types():
    assert bc.liste_des_types([]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type4', 'type3']
    assert bc.liste_des_types(bc.liste5) == ['type1', 'type2', 'type3', 'type4']
    assert bc.liste_des_types(bc.liste1) == ['type1', 'type2', 'type3', 'type4']
    assert bc.liste_des_types(bc.liste6) == ['type1']


def test_liste_des_personnes():
    assert bc.liste_des_personnes([]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')]) == ['Lucas', 'David']
    assert bc.liste_des_personnes(bc.liste6) == ['Erika']
    assert bc.liste_des_personnes(bc.liste5) == ['Anaëlle', 'Emrecan', 'Erika', 'Florian', 'Hugo', 'Ilan', 'Lucas', 'Matéo', 'Noah', 'Titouan', 'Anaëlle', 'Erika', 'Florian', 'Hugo', 'Lucas', 'Titouan', 'Hugo', 'Ilan', 'Lucas', 'Matéo', 'Titouan', 'Emrecan', 'Hugo', 'Lucas', 'Noah']


def test_fusionner_activites():
    assert bc.fusionner_activites([], []) == []
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-02', 70.08, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-03', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]
    assert bc.fusionner_activites(bc.liste3, bc.liste4) == bc.liste2
    assert bc.fusionner_activites(bc.liste3, []) == bc.liste3
    assert bc.fusionner_activites([], bc.liste3) == bc.liste3
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]
    


def test_premiere_apparition_type():
    assert bc.premiere_apparition_type([], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], 'type3') == '2024-09-01'
    assert bc.premiere_apparition_type(bc.liste5, "type1") == "2024-09-01"
    assert bc.premiere_apparition_type(bc.liste5, "type2") == '2024-09-01'
    assert bc.premiere_apparition_type(bc.liste5, "type3") == '2024-09-01'
    assert bc.premiere_apparition_type(bc.liste5, "type4") == '2024-09-01'
    assert bc.premiere_apparition_type(bc.liste5, '') == None

    
def test_recherche_activite_dichotomique():
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', []) == None
    assert bc.recherche_activite_dichotomique('', '', '', bc.liste5) == None
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ('Lucas', '2024-09-01', 67.2, 'type3')
    assert bc.recherche_activite_dichotomique("Matéo", "2024-09-01", "type3", bc.liste5) == ('Matéo', '2024-09-01', 70.08, 'type3')
    assert bc.recherche_activite_dichotomique('Erika', '2024-09-10', 'type1', bc.liste6) == ('Erika', '2024-09-10', 28.71, 'type1')
    assert bc.recherche_activite_dichotomique('David', '2024-09-19', 'type3', bc.liste1) == None


def test_charger_sauver():
    assert bc.charger_activites("liste5.csv") == bc.liste5

def test_temps_activite():
    assert bc.temps_activite(('Lucas', '2024-09-01', 67.2, 'type3'), bc.co2_minute) == 67.2/0.96
    assert bc.temps_activite(('Lucas', '2024-09-02', 70.08, 'type5'), bc.co2_minute) is None
    assert bc.temps_activite(('Lucas', '2024-09-02', 0, 'type3'), bc.co2_minute) == 0.0
    assert bc.temps_activite(('Lucas', '2024-09-02', 80, 'type2'), bc.co2_minute) == 80/0.65

def test_cumul_temps_activite():
    assert bc.cumul_temps_activite([], bc.co2_minute) == 0
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 67.2/0.96
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 140
    
# ---------------------------------------------------------------------------------------------
# Ajoutez ici les tests manquants (vos propres fonctions le cas échéant)
# ---------------------------------------------------------------------------------------------

