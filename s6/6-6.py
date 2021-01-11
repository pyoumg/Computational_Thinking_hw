first=input("Enter your first name : ")
last=input("Enter your last name : ")
Id=first.lower()+last[0].upper()
print("Your Id is \"{}\"".format(Id))
password=input("Input password : ")
flag=True
if len(password)<12:
    print('Must be at least 12 letters')
else:
    for item in password:
        if item>='0' and item<='9' or item>='A' and item<='Z' or item>='a' and item<='z':
            pass
        else:
            flag=False
    if flag==False:
        print("Alphabet and numbers only")
    else:
        print("Valid password")
