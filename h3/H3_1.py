q1,mid,q2,fin=input("점수를 입력하시오(예:퀴즈1/중간/퀴즈2/기말) : ").split('/')
q1=int(q1)
q2=int(q2)
mid=int(mid)
fin=int(fin)
total= 0.15*q1+0.3*mid+0.15*q2+0.4*fin
print("최종 점수 : %.2f" % total)
