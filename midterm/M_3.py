
s_num=input('학번을입력하시오(예:20201234) : ').split()
scores=input('점수를입력하시오(예:70 80 90) : ').split()
scores[0]=int(scores[0])
scores[1]=int(scores[1])
scores[2]=int(scores[2])
scores=s_num+scores

scores.append([sum(scores[1:]),sum(scores[1:])/len(scores[1:])])

print(scores)
