firstName = "Younghee"

lastName = "Choi"

year = 2001

domain = "@sogang.ac.kr"

yearSlice=str(year)[2:]#슬라이싱
print("이름 : "+firstName+" "+lastName)
print("출생연도 :"+str(year)+"년")


firstName=firstName.lower()
lastName=lastName.lower()
email=firstName+"."+yearSlice+lastName+domain

print("Email ID : "+email)
