input_file = open("nov_attend.txt", "r")
ans = {}
for line in input_file:
    row = line.split(":")
    day = int(row[0])
    temp = row[1].split(",")
    for name in temp:
        name = name.strip()
        if ans.get(name, 0) == 0:
            ans[name] = [day]
        else:
            ans[name].append(day)


input_file.close()
print(ans)
