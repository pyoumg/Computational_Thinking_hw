print("두 점의 좌표를 입력하시오.")
x1, y1, z1 = input("X1,Y1,Z1 : ").split()
x2, y2, z2 = input("X2,Y2,Z2 : ").split()
x1 = float(x1)
y1 = float(y1)
z1 = float(z1)
x2 = float(x2)
y2 = float(y2)
z2 = float(z2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
print(
    "두 점 ({}, {}, {}) ({}, -{}, {})의 거리는 {:.2f}이다.".format(
        x1, y1, z1, x2, y2, z2, distance
    )
)
