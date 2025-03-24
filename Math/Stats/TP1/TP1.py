import numpy as np
import matplotlib.pyplot as plt

def Exo1():
    X = np.random.randint(0, 10, 100)
    N = len(X)
    print(N)Y = 2 * X + np.random.normal(-1,0.2,50)

    print("Moyenne :",np.mean(X))

    print("Variance :",np.var(X))

    # Extraction des valeurs possibles et de leur effectif
    x, counts = np.unique(X, return_counts=True)
    # Les valeurs presentent dans la sequence
    print(x)
    # Le nombre d’apparition de chacune des valeurs dans la sequence
    print(counts)
    # Frequences pour chaque modalite
    f = counts / N
    print(f" fréquences : {f}")

    #Creation de la figure et des sous-graphiques
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    # Histogramme vertical
    ax[0].bar(x, f, color='blue')
    ax[0].set_title("Histogramme vertical")
    ax[0].set_xlabel("Valeurs")
    ax[0].set_ylabel("Effectifs")
    # Histogramme horizontal
    ax[1].barh(x, f, color='green')
    ax[1].set_title("Histogramme horizontal")
    ax[1].set_xlabel("Effectifs")
    ax[1].set_ylabel("Valeurs")
    # Ajustement des espacements
    plt.tight_layout()
    #plt.show()
    # Creation d’un histogramme en barres verticales
    plt.bar(x, f)
    # Creation d’un histogramme en barres horizontales
    plt.barh(x, f)

    plt.clf()

    # Frequences cumulees
    F = np.cumsum(f)
    # Creation du graphique en escalier
    #plt.step(x, F, where='mid', color='blue', linewidth=2, label="Graphe en escalier")
    ## Ajout des labels et du titre
    #plt.xlabel("Valeurs")
    #plt.ylabel("Frequence cumulee")
    #plt.title("Graphe en escalier de la frequence cumulee")
    #plt.legend()
    #plt.grid()
    #plt.show()

    Quartile = np.max(x[F <= 0.25])
    Quartile1 = np.max(x[F <= 0.5])
    Quartile2 = np.max(x[F <= 0.75])
    print(Quartile)
    print(Quartile1)
    print(Quartile2)
    #print(f"max de X : {max(X)}")
Exo1()

