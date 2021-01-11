month,time=input("경력(개월수)과 1주일 동안 일한 시간을 입력하시오(예:25,40) : ").split(',')
month=int(month)
time=int(time)


if month<24:
    phour=11000
elif month<48:
    phour=14000
elif month<72:
    phour=17000
else:
    phour=20000



if month<12*6:
    if 52>=time>40:
        money=40*phour+(time-40)*phour*1.17
    elif time>52:
        money=40*phour+12*phour*1.17
    else:
        money=time*phour
    money=money*(1-0.014)
else:
    if time<=52:
        money=phour*time
    else:
        money=phour*52
    money=money*(1-0.016)

print("주급은 {:.2f}입니다".format(money))
