multiple2 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
multiple5 = [5,10,15,20,25,30]

num=int(input('Enter the number :'))
if num in multiple2 and num in multiple5:
    print('2,5,10의 배수')
elif num in multiple2:
    print('2의 배수')
elif num in multiple5:
    print('5의 배수')
else:
    print('배수가 아님')
