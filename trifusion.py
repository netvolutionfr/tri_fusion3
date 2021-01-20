def tri_fusion(l):
    longueur = len(l)
    if longueur>1:
        return tri_fusion(l[])
    t = l
    return t


# assert tri_fusion([38, 27, 43, 3, 9, 72, 10]) == [3, 9, 10, 27, 38, 43, 82]

def fusion(l1, l2):
    i1 = 0
    i2 = 0
    f = []
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] <= l2[i2]:
            f.append(l1[i1])
            i1 = i1 + 1
        else:
            f.append(l2[i2])
            i2 = i2 + 1
    while i1 < len(l1):
        f.append(l1[i1])
        i1 = i1 + 1
    while i2 < len(l2):
        f.append(l2[i2])
        i2 = i2 + 1
    return f


assert fusion([35, 56], [32, 42]) == [32, 35, 42, 56]
assert fusion([35, 56, 68, 89], [1, 32, 42]) == [1, 32, 35, 42, 56, 68, 89]

