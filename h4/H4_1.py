water=int(input("수도 사용량은? : "))

if water<=30:
    money=360*water
elif water<=50:
    money=550*(water-30)+360*30
else:
    money=790*(water-50)+20*550+30*360

print('상수도요금 : {:,}원'.format(money))
