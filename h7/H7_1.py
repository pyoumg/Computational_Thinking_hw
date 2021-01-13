a, b = input("Enter two numbers : ").split()
a = int(a)
b = int(b)
li_a = []
li_b = []
li_c = []
for i in range(1, a + 1):  # 문제에서는 while()사용
    if a % i == 0:
        li_a.append(i)
for i in range(1, b + 1):
    if b % i == 0:
        li_b.append(i)
print("{} :".format(a), li_a)
print("{} :".format(b), li_b)
for item in li_a:
    if item in li_b:
        li_c.append(item)
print("공약수 : ", end="")
for item in li_c:
    print(str(item) + " ", end="")
