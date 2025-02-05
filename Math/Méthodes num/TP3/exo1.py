def f(x):
    return (x**3)-(3*x**2)+1 

def dichotomie(f,a,b,E):
    n = 0
    an = a
    bn = b
    while (bn-an) > E:
        Cn = (an+bn)/2
        if f(Cn) == 0:
            return Cn
        elif f(Cn)*f(bn) < 0:
            an = Cn
        else:
            bn = Cn
        n+=1
    return (an+bn)/2

print(dichotomie(f,0,2,0.1))
