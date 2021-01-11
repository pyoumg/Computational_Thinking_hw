word1 = input("Enter the first word : ")
word2 = input("Enter the second word : ")
if len(word1) > len(word2):
    l = len(word2)
else:
    l = len(word1)

for i in range(l):
    if word1[i] == word2[i]:
        print("{} is at {}".format(word1[i], i))
