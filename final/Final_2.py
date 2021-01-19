string = input("Enter any string to compress : ")

now_index = 0
num = 0
ans = ""
while now_index < len(string):
    if now_index == 0:
        ans += string[0]
        num = 1
    elif string[now_index] != string[now_index - 1]:
        ans += str(num)
        ans += string[now_index]
        num = 1
    else:
        num += 1
    now_index += 1
ans += str(num)

print("Compressed string :", ans)
