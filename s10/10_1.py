T = ("m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i")
alpha = input("Enter alphabet character : ")
li = []
for i in range(len(T)):
    if T[i] == alpha:
        li.append(i)
if len(li) == 0:
    print("{} is not in T".format(alpha))
else:
    li = tuple(li)
    print("{} is at".format(alpha), li)
