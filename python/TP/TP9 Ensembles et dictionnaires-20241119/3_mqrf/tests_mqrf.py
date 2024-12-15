import mqrf

# ==================================
# TESTS pour l'exercice 3
# ==================================

def test_quel_guichet():
    mqrf1 = {"Abribus":"Astus", "Jeancloddus":"Abribus", "Plexus":"Gugus",
             "Astus":None, "Gugus":"Plexus", "Saudepus":None}
    mqrf2 = {"Abribus":"Astus", "Jeancloddus":None, "Plexus":"Saudepus",
             "Astus":"Gugus", "Gugus":"Plexus", "Saudepus":None}
    assert mqrf.quel_guichet(mqrf1, "Saudepus") == "Saudepus"
    assert mqrf.quel_guichet(mqrf1, "Abribus") == "Astus"
    assert mqrf.quel_guichet(mqrf2, "Abribus") == "Saudepus"

def test_quel_guichet_v2():
    mqrf1 = {"Abribus":"Astus", "Jeancloddus":"Abribus", "Plexus":"Gugus",
             "Astus":None, "Gugus":"Plexus", "Saudepus":None}
    mqrf2 = {"Abribus":"Astus", "Jeancloddus":None, "Plexus":"Saudepus",
             "Astus":"Gugus", "Gugus":"Plexus", "Saudepus":None}
    assert mqrf.quel_guichet_v2(mqrf1, "Saudepus") == ("Saudepus", 1)
    assert mqrf.quel_guichet_v2(mqrf2, "Abribus") == ("Saudepus", 5)


def test_quel_guichet_v3():
    mqrf1 = {"Abribus":"Astus", "Jeancloddus":"Abribus", "Plexus":"Gugus",
             "Astus":None, "Gugus":"Plexus", "Saudepus":None}
    assert mqrf.quel_guichet_v3(mqrf1, "Abribus") == ("Astus", 2)
    assert mqrf.quel_guichet_v3(mqrf1, "Plexus") is None
    mqrf3 = {"Abribus":"Astus", "Jeancloddus":"Astus",
            "Plexus":"Jeancloddus", "Astus":"Gugus",
            "Gugus":"Plexus", "Saudepus":"Bielorus"}
    assert mqrf.quel_guichet_v3(mqrf3, "Abribus") is None