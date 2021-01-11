num = 0
sum_integer = 0
while sum_integer <= 100:
    sum_integer += num
    num += 1
    if num + sum_integer > 100:
        break

print("The last number is {} and total is {}".format(num - 1, sum_integer))
