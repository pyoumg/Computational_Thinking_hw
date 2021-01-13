weekdays = ["월", "화", "수", "목", "금", "토", "일"]
month, day = input("날짜를 입력하시오(예:10/1) : ").split("/")
# 10월 중 하루니까 day만 필요함
day = int(day)
month = int(month)
print("{}월 {}일은 {}요일이다".format(month, day, weekdays[(day % 7 + 2) % 7]))
