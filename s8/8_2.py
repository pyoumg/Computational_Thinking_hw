L = ["ICN", "KIX", "CDG", "LIS"]
s = L[0]
for item in L[1:]:
    s = s + "->" + item

print(s)
