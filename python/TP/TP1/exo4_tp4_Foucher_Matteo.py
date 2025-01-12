def Premiere_lettre(liste_mots, lettre):
    res = []
    for i in range(len(liste_mots)):
        for l in liste_mots[i]:
            if lettre != l[0]:
                break
            else:
                res.append(liste_mots[i])
    return res