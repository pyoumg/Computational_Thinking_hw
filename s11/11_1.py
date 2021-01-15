def center(sentence, width):
    for i in range((width - len(sentence)) // 2):
        print(" ", end="")
    print(sentence)


def right(sentence, width):
    for i in range(width - len(sentence)):
        print(" ", end="")
    print(sentence)


# main

sentence = input("문장을 입력하시오 : ")

width = int(input("폭을 입력하시오 : "))

align = int(input("정렬방식을 선택하시오(center:1, left:2, right:3) : "))

if align == 2:
    print(sentence)
elif align == 1:
    center(sentence, width)
elif align == 3:
    right(sentence, width)
else:
    print("지원되지 않는 정렬방식입니다")
