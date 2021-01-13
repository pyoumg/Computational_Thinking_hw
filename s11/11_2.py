def checkPrime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


# main

num = int(input("소수인지 확인할 숫자를 입력하시오 : "))
if checkPrime(num):
    print("{}은(는) 소수입니다".format(num))
else:
    print("{}은(는) 소수가 아닙니다".format(num))
