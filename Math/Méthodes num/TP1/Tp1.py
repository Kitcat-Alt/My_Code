import matplotlib.pyplot as plt

def a(n):
    res = 0.25
    for i in range(n):
        res = 2*res+1
        #print(res)
    return res

xn = range(10)
yn = [a(n) for n in xn]

#plt.plot(xn,yn,'yp--')

# --------------------------------------------------
def b(n):
    res = 0.2
    for i in range(n):
        res = 1/(2*res+1)
        #print(res)
    return res

def Q5b (ib):
    while (abs(b(ib)-0.5) > 0.0001):
        ib+=1
     

xb = range(10)
yb = [b(n) for n in xb]
#plt.plot(xb,yb,'yp--')

# --------------------------------------------------

def c(n):
    res = 0
    for i in range(n):
        res = 1/(res+1)
        print(res)
    return res

xc = range(10)
yc = [c(n) for n in xc]
plt.plot(xc,yc,'yp--')


def Q5c(ic):
    while (abs(c(ic)-0.6) > 0.0001):
        ic+=1
