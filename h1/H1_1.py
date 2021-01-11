won=1500000
dollar=won//1088.50
dollar_l=won-dollar*1088.5
print("달러 총액 :",int(dollar),", 거스름돈 :",int(dollar_l))
print("100달러 :",int(dollar//100))
dollar=dollar-dollar//100*100
print("50달러 :",int(dollar//50))
dollar=dollar-dollar//50*50
print("20달러 :",int(dollar//20))
dollar=dollar-dollar//20*20
print("10달러 :",int(dollar//10))
dollar=dollar-dollar//10*10

print("50달러 :",int(dollar//5))
dollar=dollar-dollar//5*5
print("1달러 :",int(dollar))
