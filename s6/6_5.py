str_a = input("영문자를 하나 입력하시오 : ")
str_a = str_a.upper()
if "A" in str_a or "E" in str_a or "I" in str_a or "O" in str_a or "U" in str_a:
    print(str_a + "은(는) 모음입니다.")
else:
    print(str_a + "은(는) 자음입니다.")
