import math

b = int(input("변 b의 길이는? : "))
c = int(input("변 c의 길이는? : "))
a = int(input("두 변 사이의 각도(A)는? : "))

area = 0.5 * b * c * math.sin(math.radians(a))
print("삼각형의 넓이 : {:.2f}".format(area))
