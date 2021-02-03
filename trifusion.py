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

def tri_fusion(l):
    longueur = len(l)
    if longueur>1:
        milieu = longueur // 2
        return fusion(tri_fusion(l[:milieu]), tri_fusion(l[milieu:]))
    else:
        t = l
    return t


assert tri_fusion([38, 27, 43, 3, 9, 72, 10]) == [3, 9, 10, 27, 38, 43, 72]
assert tri_fusion([91, 4, 52, 14, 12, 1, 9, 66, 13]) == [1, 4, 9, 12, 13, 14, 52, 66, 91]
