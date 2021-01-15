D = {}
with open("score.txt") as f:
    for line in f:
        temp = int(line)
        if D.get(temp, 0) == 0:
            D[temp] = 1
        else:
            D[temp] += 1


for k, v in D.items():
    print(f"{k} : {v}명")
f.close()