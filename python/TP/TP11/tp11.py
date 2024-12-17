apero_mai = {'Pierre': [12,70,10], 'Paul': [100], 'Marie': [15], 'Anna': [0]}
apero_juin = {'Pierre': [15,12,8,3], 'Marie': [34,20], 'Anna': [52], 'Beatrice': [8], 'sasha': [0]}

def montant_apero(apero):
    somme_apero = 0
    for argent in apero.values():
        for euro in argent:
            somme_apero += euro
    return somme_apero

def dette_apero(ami, apero):
    somme_ami = 0
    for argent in apero[ami]:
        somme_ami += argent
    return somme_ami

def afficher_dettes_apero(apero):
    dette = 0
    somme_apero = montant_apero(apero)/4
    for personne in apero:
        dette = somme_apero - dette_apero(personne, apero)
        if dette > 0:
            print(f"{personne} doit verser {abs(dette)}")
        if dette < 0:
            print(f"{personne} doit recevoir {abs(dette)}")
        if dette == 0:
            print(f"{personne} ne doit rien payer")
    return "merci d'utiliser l'app"
print(afficher_dettes_apero(apero_juin))
        

