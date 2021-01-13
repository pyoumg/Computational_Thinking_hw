scores = [90, 85, 77, 80, 74, 83, 93, 85, 77, 80, 85, 77]

S = set(scores)  # 중복제거
S = sorted(S, reverse=True)
for i in S:
    print("{}점 : {}명".format(i, scores.count(i)))
