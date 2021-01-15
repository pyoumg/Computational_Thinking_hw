def isValid(passwd):
    """input : password

    return value : 0~5

    """
    valid_1 = "abcdefghijklmnopqrstuvwxyz"
    valid_2 = "0123456789"
    valid_3 = "_!?$&"
    if len(passwd) < 12:
        return 1
    num_bi = 0
    num_nu = 0
    num_el = 0
    for item in passwd:
        if item in valid_2:
            num_nu += 1
        elif item.lower() in valid_1:
            if item not in valid_1:
                num_bi += 1
        elif item in valid_3:
            num_el += 1
        else:
            return 5

    if num_nu == 0:
        return 2
    elif num_bi < 2:
        return 3
    elif num_el == 0:
        return 4
    else:
        return 0


# main

password = input("Enter your password: ")
result = isValid(password)
if result == 0:
    print("Valid password. You can use it.")
elif result == 1:
    print("Invalid Password! Password must be at least 12 characters.")
elif result == 2:
    print("Invalid Password! Include at least one digit in your password.")
elif result == 3:
    print("Invalid Password! Include at least two capital characters in your password.")
elif result == 4:
    print("Invalid Password! Include at least one special character in your password.")
else:
    print("Invalid Password! Invalid character is included.")
