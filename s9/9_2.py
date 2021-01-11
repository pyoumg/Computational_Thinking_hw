num = 0
score = []

print("종료하려면 음수를 입력하시오")
while num >= 0 and num <= 100:
    num = int(input("성적을 입력하시오 : "))
    if num >= 0 and num <= 100:
        score.append(num)
if len(score) > 0:
    print("성적의 평균은 {:.6f}입니다".format(sum(score) / len(score)))
