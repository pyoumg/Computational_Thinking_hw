t = 20000
h = t // 3600
m = (t - h * 3600) // 60
s = t % 60
print(t, "초는", h, "시간", m, "분", s, "초입니다")
