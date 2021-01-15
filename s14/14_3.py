li = []
name = input("Enter filename : ")
for i in range(3):
    li.append(input("Enter score : ") + "\n")
f = open(name, "w")
f.writelines(li)
f.close()