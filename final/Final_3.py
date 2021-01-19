def whatIdo(M):
    """parameter : M – 변경할 리스트
    return value : result – 변경된 리스트
    새로운 리스트의 내용은 M의 원소를 규칙에 따라 변경하여 얻는다
    """
    # 함수를 완성하시오.
    l = len(M)
    ans = []
    for i in range(l):
        li = []
        for j in range(l):
            li.append(M[l - j - 1][i])
        ans.append(li)
    return ans


L = [
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"],
    ["M", "N", "O", "P"],
]
print(whatIdo(L))
