def checkPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


a = int(input("Enter a : "))

b = int(input("Enter b : "))
a = max(a, 2)
L = []
for i in range(a, b + 1):
    if checkPrime(i):
        L.append(i)
print("L :", L)
print("----------------------------------------")

print(f"number of primes between {a} and {b} : {len(L)}")
