word1 = input("enter word 1 : ")
word2 = input("enter word 2 : ")

flag = False
num = 0
if len(word1) == len(word2):
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            num = num + 1
            if num > 2:
                break
        if i == len(word1) - 1 and num == 1:
            flag = True

if flag:
    print("('{}', '{}') : differ by one character".format(word1, word2))
else:
    print("('{}', '{}') : not differ by one character".format(word1, word2))
