avengers = {'Spiderman': (5 , 5 , 'araignée a quatre pattes') , 'Hulk': (7, 4, "Grand homme vert") ,'Agent 13': (2, 3, 'agent 13') , 'M Melin': (2, 6, 'expert en archi')}

def intelligence_moyenne(avengers):
    somme = 0
    cpt = 0
    for hero in avengers.values():
        somme += hero[1]
        cpt += 1
    return somme/cpt

#print(intelligence_moyenne(avengers))

def plus_fort(avengers):
    nom_plus_fort = None
    puissance_max  = 0
    for hero in avengers.keys():
        if avengers[hero][0] >= puissance_max:
            puissance_max = avengers[hero][0]
            nom_plus_fort = avengers[hero][2]
    return nom_plus_fort

#print(plus_fort(avengers))

def les_plus_débiles(avengers):
    moyenne = intelligence_moyenne(avengers)
    cpt = 0
    for hero in avengers.values():
        if hero[1] < moyenne:
            cpt += 1
    return cpt

#print(les_plus_débiles(avengers))
