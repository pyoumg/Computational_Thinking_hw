email=input('Enter email address : ')
if len(email)>=10 and email.count('@')==1 and email[0].lower()>='a' and email[0].lower()<='z':
    print("It's valid")
    
else:
    print("It's invalid")
