months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

first=input('First Name : ')
last=input('Last Name : ')

bday=input('Birthday(yyyy/mm/dd) : ').split('/')
month=int(bday[1])
year=int(bday[0])
day=int(bday[2])
ID=first[-3:].lower()+last.upper()+months[month-1][0].upper()+months[month-1][1:].lower()+str(day)+str(year)[2:]

print('Login ID :'+ID)
pass # 코드를 완성하시오.
