def find_LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    L = [[0] * (n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    result = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            result = s1[i-1] + result
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return result


s1 = input("Nhập xâu s1: ")
s2 = input("Nhập xâu s2: ")
 

result = find_LCS(s1, s2)
##serendipitous
##precipitation 

print("Xâu con chung dài nhất của s1 và s2 là:", result)