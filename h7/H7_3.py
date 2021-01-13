n, b, x, y=input('n, b, x, y : ').split()
n=int(n)
b=int(b)
x=int(x)
y=int(y)
li=[]
if n<=0 or x<=0 or y<=0:
    print('Invalid input')
    exit()
if b<=0:
    temp=0#temp: 시작해야하는 x의 몫
else:    
    temp=(b//x+1)

while len(li)<n:
    if temp*x%y==0:
        li.append(temp*x)
    temp+=1
i=0
while i<len(li):
    print(str(li[i])+' ',end='')
    i+=1



    

    
    