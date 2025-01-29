import matplotlib.pyplot as plt
from random import *

def A(n):
    res = 0
    cpt = 0
    for k in range(n):
        if (n%2==0):
            for i in range(n):
                res=res+i
                cpt += 1
        else :
            res =3* res +1
        cpt += 1
    return (res,cpt)

def T(n):
    return A(n)[1]



#xn=range(1,51)
#qn=[T(n)/n**2 for n in xn]
#plt.plot(xn,qn,'db-')
#plt.show()

#---------------------------------


def tab(n):
    cpt = 0
    return [randint(1 ,1000) for i in range(n)]

# renvoie True si x est dans tab, False sinon

def Recherche (x,tab):
    start = 0
    end = len(tab) -1
    tab = sorted(tab)
    cpt = 0
    while start < end:
        cpt += 1 
        mid = (start+end)//2
        if tab[mid] < x:
            start = mid + 1
        elif tab[mid] > x:
            end = mid - 1
        else: 
            return True
    return False
print(Recherche(randint(1,1000),tab(500)))



from random import *
import numpy as np

def tab(n):
    cpt = 0
    return [randint(1 ,1000) for i in range(n)]

# renvoie True si x est dans tab, False sinon

def Recherche (x,tab):
    start = 0
    end = len(tab) -1
    tab = sorted(tab)
    mid = 0
    while start < end:
        mid = (start+end)//2
        if tab[mid] < x:
            start = mid + 1
        elif tab[mid] > x:
            end = mid - 1
        else: 
            return (mid,cpt)
        return (mid,cpt)
        
n_values = np.arrange(10, 10000, 50)
T_n = []

for n in n_values:
    tab = list(range(n))
    x = random.randint(0, n-1)
    _,nbiter = Recherche(x,tab)
    T_n.append(nbiter)

print(Recherche(randint(1,1000),tab(500)))