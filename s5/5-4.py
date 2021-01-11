a_score=int(input("필기시험 점수는? "))
b_score=int(input("실기시험 점수는? "))

if a_score>=60 and b_score>=80:
    print("축하합니다. 2종 면허를 취득하셨습니다")
if a_score<60 or b_score<80:
    print("수고하셨습니다. 다음에 다시 시도해주세요.") #if-else 사용금지
