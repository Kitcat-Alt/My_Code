import numpy as np
import matplotlib.pyplot as plt

# Genere 50 nombres aleatoires entre 0 et 1
X = np.random.rand(50)
# Ajoute un bruit gaussien de moyenne -1 et ecart-type 0.2
Y = 2 * X + np.random.normal(-1,0.2,50)
#plt.scatter(X, Y, color='blue', marker='o', alpha=0.7)
#plt.clf()


# Genere 50 nombres aleatoires entre 0 et 1
#X = np.random.rand(50)
# Ajoute un bruit gaussien de moyenne -1 et ecart-type 3
#Z =-3 * X**4 + np.random.normal(-1, 3,50)
#plt.scatter(X, Y, color='blue', marker='o', alpha=0.7)
#plt.show()

# Etape 1 : Calcul des moyennes
mean_X = sum(X) / len(X)
mean_Y = sum(Y) / len(Y)

print(mean_X)
print(mean_Y)


# Etape 2 : Calcul de la difference X - moyenne
X_diff = [x - mean_X for x in X]
Y_diff = [y - mean_Y for y in Y]

# Etape 3 : Calcul du numerateur (somme des produits des ecarts quadratiques)
num = sum(xd * yd for xd, yd in zip(X_diff, Y_diff))

# Etape 4 : Calcul du denominateur (les variances de X et Y)
denom_X = sum(xd ** 2 for xd in X_diff)
denom_Y = sum(yd ** 2 for yd in Y_diff)

# Etape 5 : Calcul du coefficient de correlation
correlation = num / (np.sqrt(denom_X) * np.sqrt(denom_Y))
print("Coefficient de correlation de Pearson :", correlation)

def regression_lineaire(X, Z):
    # Etape 1 : Calcul des moyennes
    mean_X = sum(X) / len(X)
    mean_Z = sum(Z) / len(Z)

    print(mean_X)
    print(mean_Z)


    # Etape 2 : Calcul de la difference X - moyenne
    X_diff = [x - mean_X for x in X]
    Z_diff = [y - mean_Z for y in Z]

    # Etape 3 : Calcul du numerateur (somme des produits des ecarts quadratiques)
    num = sum(xd * zd for xd, zd in zip(X_diff, Z_diff)) 

    # Etape 4 : Calcul du denominateur (les variances de X et Y)
    denom_X = sum(xd ** 2 for xd in X_diff) #variance de X

    a = num/denom_X
    b = mean_Z - a*mean_X

    return(a,b)

#a,b = regression_lineaire(X,Y)
#
#x_vals1 = np.linspace(min(X), max(X), 100)
#y_vals1 = a * x_vals1 + b
#plt.scatter(X, Y, color='blue', marker='o', alpha=0.7)
#plt.plot(x_vals1, y_vals1, color='red')
#plt.show()

Annees = np.array([1950, 1960, 1965, 1973, 1985, 1990, 2000, 2005, 2006, 2008, 2010, 2012])
W = np.array([63, 90, 115, 180, 202, 229, 269, 277, 276, 273, 263, 259])
G = np.array([30, 50, 66, 100, 132, 154, 188, 203, 208, 213, 210, 214])
P = np.array([41, 46, 49, 52, 55, 57, 59, 61, 61.4, 62.1, 62.8, 63.4])
#
#W1 = W[:7]
#G2 = G[:7]
#
#a,b = regression_lineaire(W1,G2)
#
#x_vals1 = np.linspace(min(W1), max(W1), 100)
#y_vals1 = a * x_vals1 + b
#
#plt.scatter(W1,G2, color='blue', marker='o', alpha=0.7)
#plt.plot(x_vals1, y_vals1, color='red')
#plt.show()

#W1 = W[7:12]
#G2 = G[7:12]
#
#a,b = regression_lineaire(W1,G2)
#
#x_vals1 = np.linspace(min(W1), max(W1))
#y_vals1 = a * x_vals1 + b
#
#plt.scatter(W1,G2, color='blue', marker='o', alpha=0.7)
#plt.plot(x_vals1, y_vals1, color='red')
#plt.show()

W1 = W[:12]
G2 = G[:12]

def WG(W1, G2):
    W1G2 = []
    i = 0
    for elem in W1:
        W1G2.append(G2[i]/elem)
        i += 1
    return W1G2
    

a,b = regression_lineaire(W1,G2)

x_vals1 = np.linspace(min(W1), max(W1))
y_vals1 = a * x_vals1 + b

Y = WG(W1, G2)
print(Y)

plt.scatter(Annees,Y, color='blue', marker='o', alpha=0.7)
plt.plot(x_vals1, y_vals1, color='red')
plt.show()

