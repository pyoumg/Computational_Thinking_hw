students = [20190001, 20190002, 20190003, 20190004, 20190005]
kor_scores = [59, 79, 60, 100, 80]
math_scores = [73, 69, 85, 50, 90]
eng_scores = [55, 79, 48, 68, 100]
scores = [students, kor_scores, math_scores, eng_scores]

for i in range(len(students)):
    total = 0
    for j in range(1, len(scores)):
        total += scores[j][i]
    print(
        "{} 총점 : {} 평균 : {:.2f}".format(
            scores[0][i],
            total,
            total / 3,
        )
    )
