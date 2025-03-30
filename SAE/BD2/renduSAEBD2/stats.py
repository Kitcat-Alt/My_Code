import numpy as np
import matplotlib.pyplot as plt



CA = [
    833.17, 1025.44, 1591.98, 840.95, 693.90, 1659.02, 1551.63, 1558.55,
    3712.36, 3226.70, 3687.84, 3711.98, 1069.89, 797.59, 825.50, 980.68,
    1083.62, 1169.57, 2258.52, 2363.32, 3566.82, 3172.77, 3651.71, 3648.87,
    1280.37, 560.63, 1040.61, 908.52, 1434.43, 1697.37, 2402.41, 2295.32,
    4028.01, 3152.43, 3732.31, 4021.45, 1352.44, 834.27, 916.02, 1229.69,
    1453.42, 2224.74, 2439.95, 2548.73, 5559.79, 3104.95, 4364.57, 5313.24,
    1674.16, 1992.89, 1619.45, 843.17, 1409.86, 1985.20, 2453.13, 2864.73,
    5857.81, 4274.50, 5285.04, 5779.58, 1598.62, 1467.22
]

qte = [
    64, 49, 63, 54, 42, 85, 102, 106,
    232, 179, 200, 235, 68, 49, 56, 58,
    68, 76, 112, 119, 237, 171, 213, 246,
    76, 46, 60, 61, 72, 97, 134, 150,
    288, 202, 227, 251, 85, 49, 77, 70,
    72, 107, 148, 159, 319, 200, 264, 293,
    90, 80, 106, 66, 82, 111, 159, 172,
    338, 240, 291, 349, 112, 78
]

#calcul des moyenne du CA et du nombre de livres vendus
moyCa = sum(CA)/len(CA)
moyQte = sum(qte)/len(qte)


def regression_lineaire(qte, CA):
    """_summary_
        calcule les coefficient a et b de l'equetion de la droite de régression
    Args:
        qte (List): la liste de nombre de livres vendu par mois
        CA (List): la liste des chiffres d'affaire réalisés
    """
    # Etape 1 : Calcul des moyennes
    mean_qte = sum(qte) / len(qte)
    mean_CA = sum(CA) / len(CA)

    # Etape 2 : Calcul de la difference qte - moyenne
    qte_diff = [qte - mean_qte for qte in qte]
    CA_diff = [ca - mean_CA for ca in CA]

    # Etape 3 : Calcul du numerateur (somme des produits des ecarts quadratiques)
    
    num = sum(qted * CAd for qted, CAd in zip(qte_diff, CA_diff)) 
    print(f'covariance(CA, Qte) : {num}')
    # Etape 4 : Calcul du denominateur (les variances de qte et Y)
    denom_qte = sum(qted ** 2 for qted in qte_diff) #variance de qte

    a = num/denom_qte
    b = mean_CA - a*mean_qte

    return(a,b)

    

def coefficient_correlation(moyCa, moyQte):
    """_summary_
        Calcule le coefficient de corrélation
    Args:
        moyCa (float): la moyenne des chiffre d'affaire
        moyQte (float): la moyenne des livres vendus par mois
    """
    # Etape 2 : Calcul de la difference X - moyenne
    X_diff = [x - moyCa for x in CA]
    Y_diff = [y - moyQte for y in qte]

    # Etape 3 : Calcul du numerateur (somme des produits des ecarts quadratiques)
    num = sum(xd * yd for xd, yd in zip(X_diff, Y_diff))

    # Etape 4 : Calcul du denominateur (les variances de X et Y)
    denom_X = sum(xd ** 2 for xd in X_diff)
    #print(denom_X)
    denom_Y = sum(yd ** 2 for yd in Y_diff)
    #print(denom_Y)

    # Etape 5 : Calcul du coefficient de correlation
    correlation = num / (np.sqrt(denom_X) * np.sqrt(denom_Y))
    print("Coefficient de correlation de Pearson :", correlation)


print(f'moyenne CA : {moyCa}')
print(f'moyenne qte : {moyQte}')
coefficient_correlation(moyCa,moyQte)

#coeficients a et b de la droite de régression
Qte,Ca = regression_lineaire(qte,CA)


x_vals1 = np.linspace(min(qte), max(qte))
y_vals1 = Qte * x_vals1 + Ca

plt.xlabel("Nombre de vente de livre")
plt.ylabel("Chiffre d'affaire")
plt.title("Evolution CA en fontion du nombre de ventes")
plt.scatter(qte, CA, color='blue', marker='o', alpha=0.7)
plt.plot(x_vals1, y_vals1, color='red')
plt.show()



