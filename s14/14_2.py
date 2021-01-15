D = {}
with open("students.txt") as f:
    for line in f:
        temp = line.split()
        key = int(temp[0])
        val = temp[1:]
        D[int(key)] = val


print(D)
f.close()