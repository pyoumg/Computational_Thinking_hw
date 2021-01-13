word = input("Enter a word : ")
alpha = input("Enter alphabet character : ")
li = []
if alpha not in word:
    print("{} is not in '{}'".format(alpha, word))
else:
    for i in range(len(word)):
        if alpha == word[i]:
            li.append(i)
    print("{} is at".format(alpha), li)
