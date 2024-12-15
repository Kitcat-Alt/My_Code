def nombres(a,b,c,d):
    """Permet de connaitre l'ordre de grandeur de différents nombre

    Args:
        a (int): nombre a
        b (int): nombre b
        c (int): nombre c
        d (int): nombre d

    Returns:
        int: le nombre le plus petit entre a b c et d
    """

    if a < b:
        res = a
    else:
        res = b

    if c < res:
        res = c
    if d < res:
        res = d
    return res
print(nombres(67,55,20,30))