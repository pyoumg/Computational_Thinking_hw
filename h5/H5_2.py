data = [0,5,10,15,20,25,30]
average=sum(data)/len(data)
sum1=sum(data[::2])#짝
sum2=sum(data[1::2])
data.insert(0,average)
data.append(sum1)
data.append(sum2)
print(data)