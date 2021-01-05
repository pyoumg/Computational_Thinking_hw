first=input("First Name : ")
last=input("Last Name : ")
l_id=first[0].lower()+last[::-1].upper()
print("Login ID : "+l_id)
