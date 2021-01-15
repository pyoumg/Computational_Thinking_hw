def makeMatrix(file):
    temp_num = 0
    li = []
    with open(file) as f:
        for line in f:
            temp = line.split()
            if temp_num == 0:
                temp_num = len(temp)
            temp = temp[:temp_num]
            temp_num -= 1
            li.append(temp)
    f.close()
    return li


def trans(m):
    li2 = []
    for i in range(len(m)):
        li2.append([])
    temp = len(m)
    for i in range(temp):
        for j in range(len(m[i])):
            li2[i + j].append(m[i][j])
    return li2


def printToMatrix(m):

    for i in range(len(m)):

        row = m[i]

        for j in range(len(row)):
            print("%3s" % row[j], end=" ")

        print()


# main

L = makeMatrix("matrix.txt")

M = trans(L)

printToMatrix(M)
