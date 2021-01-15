def replace(L, D):
    for i in range(len(L)):
        if D.get(L[i]) is None:
            pass
        else:
            L[i] = D[L[i]]


L = [2, 4, 5, 2]
D = {1: 5, 2: 7, 3: 3, 5: 20}
replace(L, D)
print(L)
