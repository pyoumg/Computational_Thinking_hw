str = input("문자열을 입력하시오 :\n")
str = str.lower()
al = 0
num = 0
for item in str:
    if item <= "z" and item >= "a":
        al += 1
    elif item >= "0" and item <= "9":
        num += 1
print("알파벳의 개수 :", al)
print("숫자의 개수 :", num)
