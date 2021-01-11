num=1
smallest=0
while num<=10:
    temp=int(input('Enter number {} : '.format(num)))
    if num==1:
        smallest=temp
    elif smallest>temp:
        smallest=temp
    num+=1
print('The smallest number is {}.'.format(smallest))

